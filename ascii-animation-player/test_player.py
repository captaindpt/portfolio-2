#!/usr/bin/env python3
"""
Test script to verify the ASCII Animation Player package works correctly.
Run this to test the installation and basic functionality.
"""

import os
import sys

def test_package():
    """Test that all components work correctly."""
    print("🎬 Testing ASCII Animation Player Package...")
    
    # Test 1: Check if we can import all modules
    print("1. Testing imports...")
    try:
        sys.path.append('src')
        from config import ASCIIConfig
        from storage import ASCIIStorage  
        from player import ASCIIPlayer
        import main
        print("   ✅ All modules imported successfully")
    except ImportError as e:
        print(f"   ❌ Import failed: {e}")
        return False
    
    # Test 2: Check if animation files exist
    print("2. Testing animation files...")
    animations_dir = "animations"
    if not os.path.exists(animations_dir):
        print(f"   ❌ Animations directory not found: {animations_dir}")
        return False
    
    animation_files = [f for f in os.listdir(animations_dir) if f.endswith('.pkl.gz.gz')]
    if not animation_files:
        print("   ❌ No animation files found")
        return False
    
    print(f"   ✅ Found {len(animation_files)} animation files")
    
    # Test 3: Try loading an animation
    print("3. Testing animation loading...")
    try:
        config = ASCIIConfig()
        storage = ASCIIStorage(config)
        test_file = os.path.join(animations_dir, animation_files[0])
        data = storage.load(test_file)
        
        required_keys = ['frames', 'config', 'metadata']
        for key in required_keys:
            if key not in data:
                print(f"   ❌ Missing key in animation data: {key}")
                return False
        
        print(f"   ✅ Successfully loaded animation with {len(data['frames'])} frames")
        
    except Exception as e:
        print(f"   ❌ Failed to load animation: {e}")
        return False
    
    # Test 4: Check dependencies
    print("4. Testing dependencies...")
    try:
        import click
        import colorama
        import numpy
        import cv2
        import PIL
        import ascii_magic
        import tqdm
        print("   ✅ All dependencies available")
    except ImportError as e:
        print(f"   ❌ Missing dependency: {e}")
        print("   💡 Run: pip install -r requirements.txt")
        return False
    
    print("\n🎉 All tests passed! Package is ready to use.")
    print("\n🚀 Try running:")
    print("   cd src")
    print(f"   python main.py play ../animations/{animation_files[0]} --simple --loop")
    
    return True

if __name__ == '__main__':
    success = test_package()
    sys.exit(0 if success else 1) 