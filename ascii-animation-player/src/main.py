#!/usr/bin/env python3
"""Main CLI for video-to-ASCII converter."""
import click
import sys
from pathlib import Path
from config import ASCIIConfig
from video_processor import VideoToASCII
from storage import ASCIIStorage
from player import ASCIIPlayer
from terminal_utils import get_terminal_size
from colorama import Fore, Style


@click.group()
def cli():
    """Video to ASCII Animation Converter - Convert videos to ASCII art animations."""
    pass


@cli.command()
@click.argument('video_file', type=click.Path(exists=True))
@click.option('-o', '--output', default='ascii_animation.pkl', help='Output file path')
@click.option('-c', '--config', type=click.Path(exists=True), help='Config YAML file')
@click.option('--width', default=80, help='Terminal width in characters')
@click.option('--height', default=40, help='Terminal height in characters')
@click.option('--auto-terminal', is_flag=True, help='Auto-detect terminal size')
@click.option('--fps', default=30, help='Target FPS')
@click.option('--brightness', default=1.0, help='Brightness (0.5=darker, 2.0=brighter)')
@click.option('--contrast', default=1.0, help='Contrast (0.5=less, 2.0=more)')
@click.option('--chars', default=' .:-=+*#%@', help='ASCII characters from dark to light')
@click.option('--braille', is_flag=True, help='Use Unicode Braille characters')
@click.option('--dither', is_flag=True, help='Apply dithering')
@click.option('--edge', is_flag=True, help='Emphasize edges')
@click.option('--compression', type=click.Choice(['none', 'gzip', 'lzma', 'bz2']), default='gzip')
@click.option('--format', 'storage_format', type=click.Choice(['pickle', 'json', 'npz']), default='pickle')
@click.option('--preview', is_flag=True, help='Preview first frame before processing')
def convert(video_file, output, config, width, height, auto_terminal, fps, brightness, contrast, 
           chars, braille, dither, edge, compression, storage_format, preview):
    """Convert a video file to ASCII animation."""
    
    # Load or create config
    if config:
        cfg = ASCIIConfig.from_yaml(config)
        click.echo(f"Loaded config from {config}")
    else:
        cfg = ASCIIConfig()
        
    # Auto-detect terminal size if requested
    if auto_terminal:
        term_width, term_height = get_terminal_size()
        cfg.apply_terminal_size(term_width, term_height)
        click.echo(f"Auto-detected terminal size: {term_width}x{term_height}")
        click.echo(f"Using resolution: {cfg.width}x{cfg.height} (with margins)")
    else:
        # Override config with CLI options
        cfg.width = width
        cfg.height = height
        
    cfg.target_fps = fps
    cfg.brightness = brightness
    cfg.contrast = contrast
    cfg.ascii_chars = chars
    cfg.use_braille = braille
    cfg.dithering = dither
    cfg.edge_detection = edge
    cfg.compression = compression
    cfg.storage_format = storage_format
    
    # Show configuration
    click.echo(f"\n{Fore.GREEN}Configuration:{Style.RESET_ALL}")
    click.echo(f"  Resolution: {cfg.width}x{cfg.height}")
    click.echo(f"  Target FPS: {cfg.target_fps}")
    click.echo(f"  Brightness: {cfg.brightness}")
    click.echo(f"  Contrast: {cfg.contrast}")
    click.echo(f"  Characters: {'Braille' if cfg.use_braille else repr(cfg.ascii_chars)}")
    click.echo(f"  Compression: {cfg.compression}")
    click.echo(f"  Format: {cfg.storage_format}")
    
    # Initialize processor
    processor = VideoToASCII(cfg)
    
    # Preview if requested
    if preview:
        click.echo(f"\n{Fore.YELLOW}Generating preview...{Style.RESET_ALL}")
        frames_gen = processor.extract_frames(video_file)
        first_frame = next(frames_gen)
        enhanced = processor.enhance_frame(first_frame)
        
        if cfg.use_braille or cfg.dithering or cfg.edge_detection:
            ascii_frame = processor.frame_to_ascii_custom(enhanced)
        else:
            ascii_frame = processor.frame_to_ascii_magic(enhanced)
            
        ASCIIPlayer.preview_frame(ascii_frame, "First Frame Preview", auto_fit=True)
        
        if not click.confirm("\nContinue with conversion?"):
            return
            
    # Process video
    click.echo(f"\n{Fore.GREEN}Processing video...{Style.RESET_ALL}")
    frames = processor.process_video(video_file)
    
    # Save animation
    click.echo(f"\n{Fore.GREEN}Saving animation...{Style.RESET_ALL}")
    storage = ASCIIStorage(cfg)
    storage.save(frames, output)
    
    # Show stats
    file_size = storage.get_file_size_mb(output if cfg.compression == 'none' 
                                       else f"{output}.{cfg.compression[:2]}")
    click.echo(f"\n{Fore.GREEN}Conversion complete!{Style.RESET_ALL}")
    click.echo(f"  Total frames: {len(frames)}")
    click.echo(f"  Output file: {output}")
    click.echo(f"  File size: {file_size:.2f} MB")
    

@cli.command()
@click.argument('animation_file', type=click.Path(exists=True))
@click.option('--simple', is_flag=True, help='Use simple playback without controls')
@click.option('--loop', is_flag=True, help='Loop the animation')
@click.option('--speed', default=1.0, help='Playback speed multiplier')
@click.option('--no-resize', is_flag=True, help='Disable automatic resizing')
def play(animation_file, simple, loop, speed, no_resize):
    """Play an ASCII animation file."""
    
    # Load animation
    click.echo(f"Loading animation from {animation_file}...")
    
    # Create config for loading
    temp_cfg = ASCIIConfig()
    storage = ASCIIStorage(temp_cfg)
    data = storage.load(animation_file)
    
    # Create config from saved data
    cfg = ASCIIConfig(**data['config'])
    cfg.loop = loop
    cfg.playback_speed = speed
    cfg.auto_resize_playback = not no_resize
    
    # Show info
    click.echo(f"\n{Fore.GREEN}Animation Info:{Style.RESET_ALL}")
    click.echo(f"  Frames: {data['metadata']['frame_count']}")
    click.echo(f"  FPS: {data['metadata']['fps']}")
    click.echo(f"  Original dimensions: {data['metadata']['dimensions']}")
    click.echo(f"  Playback speed: {cfg.playback_speed}x")
    
    # Get current terminal size
    term_width, term_height = get_terminal_size()
    click.echo(f"  Terminal size: {term_width}x{term_height}")
    
    if not no_resize and data['metadata']['dimensions'][0] > term_width:
        click.echo(f"  {Fore.YELLOW}Auto-resize enabled (press R to toggle){Style.RESET_ALL}")
    
    # Play animation
    player = ASCIIPlayer(cfg)
    player.auto_resize = not no_resize
    
    if simple:
        click.echo(f"\n{Fore.YELLOW}Starting simple playback (Ctrl+C to stop)...{Style.RESET_ALL}")
        player.play_simple(data['frames'], data['metadata']['fps'])
    else:
        click.echo(f"\n{Fore.YELLOW}Starting interactive playback...{Style.RESET_ALL}")
        click.echo("Controls: Q=Quit, Space=Pause, ←/→=Seek, +/-=Speed, R=Resize, C=Center")
        click.pause("Press any key to start...")
        player.play(data['frames'], data['metadata']['fps'])
        

@cli.command()
@click.option('-o', '--output', default='config.yaml', help='Output config file')
def generate_config(output):
    """Generate a sample configuration file."""
    cfg = ASCIIConfig()
    cfg.to_yaml(output)
    click.echo(f"Generated config file: {output}")
    click.echo("Edit this file to customize your conversion settings.")
    

@cli.command()
@click.argument('video_file', type=click.Path(exists=True))
@click.option('--width', default=80, help='Terminal width')
@click.option('--height', default=40, help='Terminal height')
@click.option('--auto-terminal', is_flag=True, help='Auto-detect terminal size')
@click.option('--brightness', default=1.0, help='Brightness adjustment')
@click.option('--contrast', default=1.0, help='Contrast adjustment')
def preview(video_file, width, height, auto_terminal, brightness, contrast):
    """Preview different settings on the first frame."""
    
    # Get terminal size
    term_width, term_height = get_terminal_size()
    click.echo(f"Terminal size: {term_width}x{term_height}")
    
    if auto_terminal:
        cfg = ASCIIConfig()
        cfg.apply_terminal_size(term_width, term_height)
        width = cfg.width
        height = cfg.height
        click.echo(f"Using auto-detected size: {width}x{height}")
    
    cfg = ASCIIConfig(
        width=width,
        height=height,
        brightness=brightness,
        contrast=contrast
    )
    
    processor = VideoToASCII(cfg)
    
    # Get first frame
    frames_gen = processor.extract_frames(video_file)
    first_frame = next(frames_gen)
    
    # Show different variations
    click.echo(f"\n{Fore.GREEN}Preview with current settings:{Style.RESET_ALL}")
    
    # Standard ASCII
    enhanced = processor.enhance_frame(first_frame)
    ascii_frame = processor.frame_to_ascii_custom(enhanced)
    ASCIIPlayer.preview_frame(ascii_frame, "Standard ASCII", auto_fit=True)
    
    # With Braille
    cfg.use_braille = True
    processor = VideoToASCII(cfg)
    ascii_frame = processor.frame_to_ascii_custom(enhanced)
    ASCIIPlayer.preview_frame(ascii_frame, "Braille Characters", auto_fit=True)
    
    # With dithering
    cfg.use_braille = False
    cfg.dithering = True
    processor = VideoToASCII(cfg)
    ascii_frame = processor.frame_to_ascii_custom(enhanced)
    ASCIIPlayer.preview_frame(ascii_frame, "With Dithering", auto_fit=True)
    
    # With edge detection
    cfg.dithering = False
    cfg.edge_detection = True
    processor = VideoToASCII(cfg)
    enhanced = processor.enhance_frame(first_frame)
    ascii_frame = processor.frame_to_ascii_custom(enhanced)
    ASCIIPlayer.preview_frame(ascii_frame, "Edge Detection", auto_fit=True)


if __name__ == '__main__':
    cli() 