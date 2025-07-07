#!/bin/bash

echo "----------------------------------"
echo "Building Eleventy site..."
echo "----------------------------------"

# Run the Eleventy build command
npx @11ty/eleventy

# Check if the build command was successful
if [ $? -ne 0 ]; then
  echo "----------------------------------"
  echo "Eleventy build failed. Exiting."
  echo "----------------------------------"
  exit 1
fi

echo "----------------------------------"
echo "Build successful. Starting server..."
echo "----------------------------------"

# Change into the output directory
cd _site

# Start the Python server
PORT=8000
echo "Server starting in directory: $(pwd)"
echo "Access site at: http://localhost:$PORT"
echo "Press Ctrl+C to stop the server."
echo "----------------------------------"

python -m http.server $PORT

# Note: The script will stay on the python server command until you stop it (Ctrl+C)
cd .. # Go back to root when server stops (optional, but good practice)
echo "----------------------------------"
echo "Server stopped."
echo "----------------------------------" 