"""Terminal utilities for size detection and frame resizing."""
import os
import sys
import shutil
import subprocess
from typing import Tuple, List
import textwrap


def get_terminal_size() -> Tuple[int, int]:
    """Get current terminal size (columns, rows)."""
    try:
        # Try using shutil first (most reliable)
        size = shutil.get_terminal_size(fallback=(80, 24))
        
        # Sanity check - if height is unreasonably small, try other methods
        if size.lines < 10:
            # Try tput command
            try:
                cols = int(subprocess.check_output(['tput', 'cols']).decode().strip())
                lines = int(subprocess.check_output(['tput', 'lines']).decode().strip())
                if lines >= 10:
                    return cols, lines
            except:
                pass
                
            # Try stty command
            try:
                stty_size = subprocess.check_output(['stty', 'size']).decode().strip().split()
                if len(stty_size) == 2:
                    lines, cols = int(stty_size[0]), int(stty_size[1])
                    if lines >= 10:
                        return cols, lines
            except:
                pass
                
            # If all methods return small height, assume it's a limited view
            # Return width with a reasonable default height
            return size.columns, 40
            
        return size.columns, size.lines
    except:
        # Final fallback
        return 80, 40


def resize_ascii_frame(frame: str, target_width: int, target_height: int = None) -> str:
    """Resize an ASCII frame to fit within terminal dimensions."""
    lines = frame.strip().split('\n')
    
    # Get current frame dimensions
    current_height = len(lines)
    current_width = max(len(line) for line in lines) if lines else 0
    
    # If frame already fits, return as is
    if current_width <= target_width and (target_height is None or current_height <= target_height):
        return frame
    
    # Handle width resizing
    if current_width > target_width:
        # Option 1: Truncate (simple but may lose info)
        resized_lines = [line[:target_width] for line in lines]
        
        # Option 2: Scale down (better but more complex)
        # We'll implement simple sampling for now
        scale_factor = target_width / current_width
        sampled_lines = []
        
        for line in lines:
            if not line:
                sampled_lines.append('')
                continue
                
            # Sample characters from the line
            sampled_chars = []
            for i in range(target_width):
                source_index = int(i / scale_factor)
                if source_index < len(line):
                    sampled_chars.append(line[source_index])
                else:
                    sampled_chars.append(' ')
            sampled_lines.append(''.join(sampled_chars))
        
        resized_lines = sampled_lines
    else:
        resized_lines = lines
    
    # Handle height resizing if specified
    if target_height and len(resized_lines) > target_height:
        # Sample rows
        scale_factor = target_height / len(resized_lines)
        sampled_indices = [int(i / scale_factor) for i in range(target_height)]
        resized_lines = [resized_lines[i] for i in sampled_indices if i < len(resized_lines)]
    
    return '\n'.join(resized_lines)


def center_frame(frame: str, terminal_width: int, terminal_height: int = None) -> str:
    """Center an ASCII frame within terminal dimensions."""
    lines = frame.strip().split('\n')
    
    # Get frame dimensions
    frame_width = max(len(line) for line in lines) if lines else 0
    frame_height = len(lines)
    
    # Center horizontally
    if frame_width < terminal_width:
        padding = (terminal_width - frame_width) // 2
        lines = [' ' * padding + line for line in lines]
    
    # Center vertically if height is specified
    if terminal_height and frame_height < terminal_height:
        vertical_padding = (terminal_height - frame_height) // 2
        lines = [''] * vertical_padding + lines + [''] * vertical_padding
    
    return '\n'.join(lines)


def wrap_text(text: str, width: int) -> List[str]:
    """Wrap text to fit within specified width."""
    return textwrap.wrap(text, width=width)


def clear_terminal():
    """Clear the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')


def move_cursor_up(lines: int):
    """Move cursor up by specified number of lines."""
    sys.stdout.write(f'\033[{lines}A')
    sys.stdout.flush()


def hide_cursor():
    """Hide the terminal cursor."""
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()


def show_cursor():
    """Show the terminal cursor."""
    sys.stdout.write('\033[?25h')
    sys.stdout.flush() 