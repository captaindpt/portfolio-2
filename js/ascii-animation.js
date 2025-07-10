/**
 * ASCII Animation Player for Web
 * Plays ASCII animations converted from video files
 */

class ASCIIAnimationPlayer {
    constructor(container, options = {}) {
        this.container = container;
        this.options = {
            autoResize: true,
            loop: true,
            maxWidth: 120,
            maxHeight: 40,
            ...options
        };
        
        this.frames = [];
        this.currentFrame = 0;
        this.fps = 30;
        this.isPlaying = false;
        this.animationId = null;
        this.lastFrameTime = 0;
        
        this.init();
    }
    
    init() {
        // Create the display element
        this.display = document.createElement('pre');
        this.display.className = 'ascii-animation-display';
        
        this.container.appendChild(this.display);
        
        // Add loading message
        this.display.textContent = 'Loading animation...';
        
        // Add resize listener if auto-resize is enabled
        if (this.options.autoResize) {
            window.addEventListener('resize', () => this.handleResize());
        }
    }
    
    async loadAnimation(url) {
        try {
            const response = await fetch(url);
            const data = await response.json();
            
            this.frames = data.frames;
            this.fps = data.fps;
            this.currentFrame = 0;
            
            console.log(`Loaded animation: ${this.frames.length} frames at ${this.fps} FPS`);
            
            // Set initial size
            this.handleResize();
            
            // Start playing
            this.play();
            
        } catch (error) {
            console.error('Failed to load animation:', error);
            this.display.textContent = 'Failed to load animation';
        }
    }
    
    play() {
        if (this.frames.length === 0) return;
        
        this.isPlaying = true;
        this.lastFrameTime = performance.now();
        this.animate();
    }
    
    pause() {
        this.isPlaying = false;
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
        }
    }
    
    stop() {
        this.pause();
        this.currentFrame = 0;
        this.displayFrame();
    }
    
    animate() {
        if (!this.isPlaying) return;
        
        const currentTime = performance.now();
        const frameInterval = 1000 / this.fps;
        
        if (currentTime - this.lastFrameTime >= frameInterval) {
            this.displayFrame();
            this.currentFrame++;
            
            if (this.currentFrame >= this.frames.length) {
                if (this.options.loop) {
                    this.currentFrame = 0;
                } else {
                    this.pause();
                    return;
                }
            }
            
            this.lastFrameTime = currentTime;
        }
        
        this.animationId = requestAnimationFrame(() => this.animate());
    }
    
    displayFrame() {
        if (this.frames.length === 0) return;
        
        let frame = this.frames[this.currentFrame];
        
        // Apply resizing if needed
        if (this.options.autoResize) {
            frame = this.resizeFrame(frame);
        }
        
        this.display.textContent = frame;
    }
    
    resizeFrame(frame) {
        const container = this.container;
        const containerWidth = container.clientWidth;
        
        // Get frame dimensions
        const lines = frame.split('\n');
        const frameWidth = Math.max(...lines.map(line => line.length));
        
        // Calculate available width (accounting for padding and borders)
        const availableWidth = Math.floor((containerWidth - 40) / 6); // Approximate char width
        
        // If frame fits, return original
        if (frameWidth <= availableWidth) {
            return frame;
        }
        
        // Resize by sampling width only (preserve aspect ratio)
        const scale = availableWidth / frameWidth;
        const targetWidth = Math.floor(frameWidth * scale);
        
        const resizedLines = [];
        for (const line of lines) {
            if (!line) {
                resizedLines.push('');
                continue;
            }
            
            let resizedLine = '';
            for (let x = 0; x < targetWidth; x++) {
                const sourceX = Math.floor(x / scale);
                if (sourceX < line.length) {
                    resizedLine += line[sourceX];
                } else {
                    resizedLine += ' ';
                }
            }
            resizedLines.push(resizedLine);
        }
        
        return resizedLines.join('\n');
    }
    
    handleResize() {
        // Adjust font size based on container size
        const container = this.container;
        const containerWidth = container.clientWidth;
        
        // Calculate optimal font size
        let fontSize = 10;
        if (containerWidth < 600) {
            fontSize = 6;
        } else if (containerWidth < 900) {
            fontSize = 8;
        } else if (containerWidth > 1200) {
            fontSize = 12;
        }
        
        this.display.style.fontSize = fontSize + 'px';
        
        // Trigger frame redisplay
        if (this.frames.length > 0) {
            this.displayFrame();
        }
    }
    
    destroy() {
        this.pause();
        if (this.options.autoResize) {
            window.removeEventListener('resize', this.handleResize);
        }
        this.container.removeChild(this.display);
    }
}

// Initialize animation when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    const animationContainer = document.getElementById('ascii-animation-container');
    if (animationContainer) {
        const player = new ASCIIAnimationPlayer(animationContainer, {
            autoResize: true,
            loop: true
        });
        
        player.loadAnimation('/assets/ascii-animation.json');
        
        // Store player instance for potential cleanup
        window.asciiPlayer = player;
    }
});