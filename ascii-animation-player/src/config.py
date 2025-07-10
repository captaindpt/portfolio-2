"""Configuration settings for video-to-ASCII conversion."""
from dataclasses import dataclass, field
from typing import List, Tuple, Optional
import yaml


@dataclass
class ASCIIConfig:
    """Configuration for ASCII video conversion with all adjustable parameters."""
    
    # Video processing
    target_fps: int = 30  # Target framerate (will downsample from source)
    start_time: float = 0.0  # Start time in seconds
    end_time: Optional[float] = None  # End time in seconds (None = full video)
    
    # Resolution
    width: int = 80  # Terminal columns
    height: int = 40  # Terminal rows
    maintain_aspect_ratio: bool = True
    auto_terminal_size: bool = False  # Auto-detect terminal size
    terminal_margin: int = 2  # Margin to leave for UI elements
    
    # Image enhancement
    brightness: float = 1.0  # 0.5 = darker, 2.0 = brighter
    contrast: float = 1.0  # 0.5 = less contrast, 2.0 = more contrast
    saturation: float = 1.0  # 0.0 = grayscale, 2.0 = vivid colors
    sharpness: float = 1.0  # 0.0 = blurry, 2.0 = sharper
    gamma: float = 1.0  # Gamma correction
    
    # ASCII conversion
    ascii_chars: str = " .:-=+*#%@"  # Characters from dark to light
    reverse_chars: bool = False  # Reverse the character mapping
    color_mode: str = "mono"  # "mono", "ansi", "ansi256", "truecolor"
    background: str = "black"  # Background color for colored modes
    
    # Advanced ASCII options
    use_braille: bool = False  # Use Unicode Braille characters for higher resolution
    dithering: bool = False  # Apply dithering for smoother gradients
    edge_detection: bool = False  # Emphasize edges
    edge_threshold: float = 100.0  # Threshold for edge detection
    
    # Storage options
    compression: str = "gzip"  # "none", "gzip", "lzma", "bz2"
    storage_format: str = "pickle"  # "pickle", "json", "npz"
    
    # Playback options
    playback_speed: float = 1.0  # Speed multiplier
    loop: bool = False  # Loop the animation
    show_progress: bool = True  # Show progress bar during conversion
    clear_screen: bool = True  # Clear screen between frames
    auto_resize_playback: bool = True  # Auto-resize during playback
    
    @classmethod
    def from_yaml(cls, path: str) -> 'ASCIIConfig':
        """Load configuration from a YAML file."""
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
        return cls(**data)
    
    def to_yaml(self, path: str):
        """Save configuration to a YAML file."""
        with open(path, 'w') as f:
            yaml.dump(self.__dict__, f, default_flow_style=False)
    
    def get_frame_skip(self, source_fps: float) -> int:
        """Calculate frame skip based on source and target FPS."""
        if self.target_fps >= source_fps:
            return 1
        return int(source_fps / self.target_fps)
    
    def apply_terminal_size(self, term_width: int, term_height: int):
        """Apply terminal size with margins."""
        self.width = max(20, term_width - self.terminal_margin)  # Minimum 20 chars wide
        # For height, ensure we have reasonable minimum (use detected height or fallback)
        if term_height > 10:
            self.height = max(10, term_height - self.terminal_margin - 3)
        else:
            # Terminal is too small or detection failed, use sensible default
            self.height = 40  # Default height 