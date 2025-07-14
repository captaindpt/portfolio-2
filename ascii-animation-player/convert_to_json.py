#!/usr/bin/env python3
"""Convert existing ASCII animation from pickle to JSON format."""
import sys
sys.path.append('src')

from storage import ASCIIStorage
from config import ASCIIConfig

# Create a temp config for loading
config = ASCIIConfig()
storage = ASCIIStorage(config)

# Load the existing animation
print("Loading existing animation...")
data = storage.load('animations/d2_boat_bright1.5_contrast1.5.pkl.gz.gz')

print(f"Loaded {data['metadata']['frame_count']} frames")
print(f"Dimensions: {data['metadata']['dimensions']}")
print(f"FPS: {data['metadata']['fps']}")

# Update config for JSON output
config.storage_format = 'json'
config.compression = 'none'
storage = ASCIIStorage(config)

# Save as JSON
print("Converting to JSON...")
storage.save(data['frames'], '../assets/boat-animation.json', data['metadata'])
print("Saved to ../assets/boat-animation.json")