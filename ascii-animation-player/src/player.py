"""ASCII animation player for terminal."""
import time
import sys
import os
import termios
import tty
import select
from typing import List, Dict, Any
from colorama import init, Fore, Back, Style
import threading
from config import ASCIIConfig
from terminal_utils import (
    get_terminal_size, resize_ascii_frame, center_frame, 
    clear_terminal, hide_cursor, show_cursor
)


class ASCIIPlayer:
    """Play ASCII animations in terminal with controls."""
    
    def __init__(self, config: ASCIIConfig = None):
        self.config = config or ASCIIConfig()
        self.is_playing = False
        self.current_frame = 0
        self.total_frames = 0
        self.terminal_width, self.terminal_height = get_terminal_size()
        self.auto_resize = True  # Auto-resize frames to fit terminal
        self.center_content = False  # Center content in terminal
        init()  # Initialize colorama
        
    def play(self, frames: List[str], fps: int = None):
        """Play ASCII animation with controls."""
        self.total_frames = len(frames)
        self.current_frame = 0
        self.is_playing = True
        
        fps = fps or self.config.target_fps
        frame_delay = 1.0 / (fps * self.config.playback_speed)
        
        # Set up terminal for non-blocking input
        old_settings = termios.tcgetattr(sys.stdin)
        
        try:
            tty.setraw(sys.stdin.fileno())
            hide_cursor()
            
            # Start playback thread
            playback_thread = threading.Thread(
                target=self._playback_loop,
                args=(frames, frame_delay)
            )
            playback_thread.daemon = True
            playback_thread.start()
            
            # Handle keyboard input
            self._handle_controls()
            
        finally:
            # Restore terminal settings
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
            show_cursor()
            self._clear_screen()
            
    def _playback_loop(self, frames: List[str], frame_delay: float):
        """Main playback loop running in separate thread."""
        while self.is_playing:
            if self.current_frame >= self.total_frames:
                if self.config.loop:
                    self.current_frame = 0
                else:
                    self.is_playing = False
                    break
                    
            # Update terminal size periodically
            self.terminal_width, self.terminal_height = get_terminal_size()
            
            # Display current frame
            self._display_frame(frames[self.current_frame])
            
            # Wait for next frame
            time.sleep(frame_delay)
            self.current_frame += 1
            
    def _display_frame(self, frame: str):
        """Display a single frame with automatic resizing."""
        if self.config.clear_screen:
            self._clear_screen()
            
        # Move cursor to top-left
        sys.stdout.write('\033[H')
        
        # Resize frame if needed
        if self.auto_resize:
            # Leave room for status bar (2 lines)
            available_height = self.terminal_height - 3
            frame = resize_ascii_frame(frame, self.terminal_width, available_height)
            
        # Center frame if requested
        if self.center_content:
            frame = center_frame(frame, self.terminal_width, self.terminal_height - 3)
        
        # Apply color if configured
        if self.config.color_mode != "mono":
            sys.stdout.write(Fore.GREEN)
            
        sys.stdout.write(frame)
        
        # Reset color
        if self.config.color_mode != "mono":
            sys.stdout.write(Style.RESET_ALL)
            
        # Show status bar
        self._show_status()
        sys.stdout.flush()
        
    def _show_status(self):
        """Show playback status bar."""
        # Move to bottom of terminal
        sys.stdout.write(f'\033[{self.terminal_height - 1};0H')
        
        status = f"[Frame {self.current_frame + 1}/{self.total_frames}] "
        status += f"[{'PLAYING' if self.is_playing else 'PAUSED'}] "
        status += f"[Speed: {self.config.playback_speed}x] "
        status += f"[Size: {self.terminal_width}x{self.terminal_height}] "
        
        controls = "[Q: Quit | Space: Pause | ←/→: Seek | +/-: Speed | R: Resize | C: Center]"
        
        # Truncate if needed
        if len(status) + len(controls) > self.terminal_width:
            controls = "[Q|Spc|←→|+-|R|C]"
            
        sys.stdout.write(f"{Fore.CYAN}{status}{controls}{Style.RESET_ALL}")
        
    def _handle_controls(self):
        """Handle keyboard controls."""
        while True:
            if select.select([sys.stdin], [], [], 0.1)[0]:
                key = sys.stdin.read(1)
                
                if key.lower() == 'q':
                    self.is_playing = False
                    break
                elif key == ' ':
                    self.is_playing = not self.is_playing
                elif key == '+' or key == '=':
                    self.config.playback_speed = min(4.0, self.config.playback_speed + 0.25)
                elif key == '-':
                    self.config.playback_speed = max(0.25, self.config.playback_speed - 0.25)
                elif key.lower() == 'r':
                    self.auto_resize = not self.auto_resize
                elif key.lower() == 'c':
                    self.center_content = not self.center_content
                elif key == '\x1b':  # Arrow keys
                    if sys.stdin.read(1) == '[':
                        arrow = sys.stdin.read(1)
                        if arrow == 'C':  # Right arrow
                            self.current_frame = min(self.total_frames - 1, self.current_frame + 5)
                        elif arrow == 'D':  # Left arrow
                            self.current_frame = max(0, self.current_frame - 5)
                            
            if not self.is_playing and self.current_frame >= self.total_frames - 1:
                break
                
    def _clear_screen(self):
        """Clear terminal screen."""
        clear_terminal()
        
    def play_simple(self, frames: List[str], fps: int = None):
        """Simple playback without controls (for testing)."""
        fps = fps or self.config.target_fps
        frame_delay = 1.0 / (fps * self.config.playback_speed)
        
        try:
            hide_cursor()
            while True:
                for i, frame in enumerate(frames):
                    # Update terminal size
                    self.terminal_width, self.terminal_height = get_terminal_size()
                    
                    if self.config.clear_screen:
                        self._clear_screen()
                        
                    # Auto-resize frame
                    if self.auto_resize:
                        frame = resize_ascii_frame(frame, self.terminal_width, self.terminal_height - 2)
                        
                    print(frame)
                    print(f"\nFrame {i + 1}/{len(frames)} | Terminal: {self.terminal_width}x{self.terminal_height}")
                    
                    time.sleep(frame_delay)
                
                # If not looping, break after one complete playthrough
                if not self.config.loop:
                    break
                    
        except KeyboardInterrupt:
            print("\nPlayback interrupted.")
        finally:
            show_cursor()
            
    @staticmethod
    def preview_frame(frame: str, title: str = "Preview", auto_fit: bool = True):
        """Preview a single frame with optional auto-fitting."""
        term_width, term_height = get_terminal_size()
        
        if auto_fit:
            # Resize to fit terminal with room for title and border
            frame = resize_ascii_frame(frame, term_width - 4, term_height - 5)
            
        print(f"\n{Fore.YELLOW}=== {title} ==={Style.RESET_ALL}\n")
        print(frame)
        print(f"\n{Fore.YELLOW}{'=' * (len(title) + 8)}{Style.RESET_ALL}")
        print(f"Terminal size: {term_width}x{term_height}") 