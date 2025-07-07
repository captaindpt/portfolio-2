#!/bin/bash

set -e  # Exit on any error

echo "🚀 Starting build process..."

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
fi

# Clean previous build
echo "🧹 Cleaning previous build..."
npm run clean

# Build the site
echo "🔨 Building site with Eleventy..."
npm run build

# Check if build was successful
if [ $? -eq 0 ]; then
    echo "✅ Build completed successfully!"
    echo "📁 Site generated in _site/ directory"
else
    echo "❌ Build failed!"
    exit 1
fi