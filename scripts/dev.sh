#!/bin/bash

set -e  # Exit on any error

echo "🚀 Starting development server..."

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
fi

# Start development server
echo "🔧 Starting Eleventy development server..."
echo "👀 Watching for file changes..."
echo "🌐 Server will be available at http://localhost:8080"
echo "💡 Press Ctrl+C to stop the server"
echo "---"

npm run dev