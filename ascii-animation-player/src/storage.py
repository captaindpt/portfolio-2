"""Storage functionality for ASCII animations."""
import pickle
import gzip
import lzma
import bz2
import json
import numpy as np
from typing import List, Dict, Any
from pathlib import Path
from config import ASCIIConfig


class ASCIIStorage:
    """Handle storage and retrieval of ASCII animations."""
    
    def __init__(self, config: ASCIIConfig):
        self.config = config
        
    def save(self, frames: List[str], output_path: str, metadata: Dict[str, Any] = None):
        """Save ASCII frames with metadata."""
        # Prepare data structure
        data = {
            'frames': frames,
            'config': self.config.__dict__,
            'metadata': metadata or {},
            'version': '1.0'
        }
        
        # Add frame metadata
        data['metadata'].update({
            'frame_count': len(frames),
            'fps': self.config.target_fps,
            'dimensions': (self.config.width, self.config.height),
        })
        
        # Choose storage format
        if self.config.storage_format == 'pickle':
            self._save_pickle(data, output_path)
        elif self.config.storage_format == 'json':
            self._save_json(data, output_path)
        elif self.config.storage_format == 'npz':
            self._save_npz(data, output_path)
        else:
            raise ValueError(f"Unknown storage format: {self.config.storage_format}")
            
    def load(self, input_path: str) -> Dict[str, Any]:
        """Load ASCII frames and metadata."""
        path = Path(input_path)
        
        # Determine format from extension
        if path.suffix in ['.pkl', '.pickle']:
            return self._load_pickle(input_path)
        elif path.suffix == '.json':
            return self._load_json(input_path)
        elif path.suffix == '.npz':
            return self._load_npz(input_path)
        else:
            # Try to detect format
            try:
                return self._load_pickle(input_path)
            except:
                try:
                    return self._load_json(input_path)
                except:
                    return self._load_npz(input_path)
                    
    def _save_pickle(self, data: Dict[str, Any], output_path: str):
        """Save using pickle format with optional compression."""
        if self.config.compression == 'none':
            with open(output_path, 'wb') as f:
                pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
        elif self.config.compression == 'gzip':
            with gzip.open(f"{output_path}.gz", 'wb') as f:
                pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
        elif self.config.compression == 'lzma':
            with lzma.open(f"{output_path}.xz", 'wb') as f:
                pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
        elif self.config.compression == 'bz2':
            with bz2.open(f"{output_path}.bz2", 'wb') as f:
                pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
                
    def _save_json(self, data: Dict[str, Any], output_path: str):
        """Save using JSON format with optional compression."""
        json_str = json.dumps(data, indent=2)
        
        if self.config.compression == 'none':
            with open(output_path, 'w') as f:
                f.write(json_str)
        elif self.config.compression == 'gzip':
            with gzip.open(f"{output_path}.gz", 'wt', encoding='utf-8') as f:
                f.write(json_str)
        elif self.config.compression == 'lzma':
            with lzma.open(f"{output_path}.xz", 'wt', encoding='utf-8') as f:
                f.write(json_str)
        elif self.config.compression == 'bz2':
            with bz2.open(f"{output_path}.bz2", 'wt', encoding='utf-8') as f:
                f.write(json_str)
                
    def _save_npz(self, data: Dict[str, Any], output_path: str):
        """Save using NumPy compressed format."""
        # Convert frames to numpy array for efficient storage
        # Encode strings as bytes
        frames_bytes = [frame.encode('utf-8') for frame in data['frames']]
        
        # Save as compressed numpy archive
        np.savez_compressed(
            output_path,
            frames=frames_bytes,
            config=json.dumps(data['config']),
            metadata=json.dumps(data['metadata']),
            version=data['version']
        )
        
    def _load_pickle(self, input_path: str) -> Dict[str, Any]:
        """Load from pickle format."""
        open_func = open
        
        if input_path.endswith('.gz'):
            open_func = gzip.open
        elif input_path.endswith('.xz'):
            open_func = lzma.open
        elif input_path.endswith('.bz2'):
            open_func = bz2.open
            
        with open_func(input_path, 'rb') as f:
            return pickle.load(f)
            
    def _load_json(self, input_path: str) -> Dict[str, Any]:
        """Load from JSON format."""
        open_func = open
        mode = 'r'
        
        if input_path.endswith('.gz'):
            open_func = gzip.open
            mode = 'rt'
        elif input_path.endswith('.xz'):
            open_func = lzma.open
            mode = 'rt'
        elif input_path.endswith('.bz2'):
            open_func = bz2.open
            mode = 'rt'
            
        with open_func(input_path, mode) as f:
            return json.load(f)
            
    def _load_npz(self, input_path: str) -> Dict[str, Any]:
        """Load from NumPy format."""
        data = np.load(input_path, allow_pickle=True)
        
        # Decode frames from bytes
        frames = [frame.decode('utf-8') for frame in data['frames']]
        
        return {
            'frames': frames,
            'config': json.loads(str(data['config'])),
            'metadata': json.loads(str(data['metadata'])),
            'version': str(data['version'])
        }
        
    def get_file_size_mb(self, file_path: str) -> float:
        """Get file size in MB."""
        return Path(file_path).stat().st_size / (1024 * 1024) 