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
            this.resizeHandler = () => this.handleResize();
            window.addEventListener('resize', this.resizeHandler);
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
        const frameHeight = lines.length;
        
        // Calculate available space (accounting for padding and borders)
        const availableWidth = Math.floor((containerWidth - 40) / 6); // Approximate char width
        
        // If frame fits, return original
        if (frameWidth <= availableWidth) {
            return frame;
        }
        
        // Calculate scale to fit width while maintaining aspect ratio
        const scale = availableWidth / frameWidth;
        const targetWidth = Math.floor(frameWidth * scale);
        const targetHeight = Math.floor(frameHeight * scale);
        
        // Resize both width and height proportionally
        const resizedLines = [];
        for (let y = 0; y < targetHeight; y++) {
            const sourceY = Math.floor(y / scale);
            if (sourceY < lines.length) {
                const sourceLine = lines[sourceY];
                let resizedLine = '';
                
                for (let x = 0; x < targetWidth; x++) {
                    const sourceX = Math.floor(x / scale);
                    if (sourceX < sourceLine.length) {
                        resizedLine += sourceLine[sourceX];
                    } else {
                        resizedLine += ' ';
                    }
                }
                resizedLines.push(resizedLine);
            }
        }
        
        return resizedLines.join('\n');
    }
    
    handleResize() {
        if (this.frames.length === 0) return;
        
        const container = this.container;
        const containerWidth = container.clientWidth;
        const viewportHeight = window.innerHeight;
        const viewportWidth = window.innerWidth;
        
        // Get original frame dimensions
        const sampleFrame = this.frames[0];
        const lines = sampleFrame.split('\n');
        const frameWidth = Math.max(...lines.map(line => line.length));
        const frameHeight = lines.length;
        
        // Calculate font size based on character dimensions
        // For monospace fonts, character width is roughly 0.6 times the font size
        // Character height is roughly equal to the font size
        const maxFontSizeForWidth = Math.floor((containerWidth * 0.95) / (frameWidth * 0.6));
        const maxFontSizeForHeight = Math.floor((viewportHeight * 0.7) / (frameHeight * 0.9)); // 0.9 for line-height
        
        // Use the smaller value to ensure it fits
        let fontSize = Math.min(maxFontSizeForWidth, maxFontSizeForHeight);
        
        // Set reasonable bounds based on viewport size
        const minSize = Math.max(3, Math.floor(viewportWidth / 200));
        const maxSize = Math.min(16, Math.floor(viewportWidth / 80));
        fontSize = Math.max(minSize, Math.min(fontSize, maxSize));
        
        // Apply the calculated font size
        this.display.style.fontSize = fontSize + 'px';
        this.display.style.lineHeight = '0.9';
        
        // Trigger frame redisplay
        this.displayFrame();
    }
    
    destroy() {
        this.pause();
        if (this.options.autoResize && this.resizeHandler) {
            window.removeEventListener('resize', this.resizeHandler);
        }
        if (this.display && this.container.contains(this.display)) {
            this.container.removeChild(this.display);
        }
    }
}

// Initialize animation when DOM is ready or when navigating
function initializeAnimation() {
    const animationContainer = document.getElementById('ascii-animation-container');
    if (animationContainer) {
        // Clean up existing player if it exists
        if (window.asciiPlayer) {
            try {
                window.asciiPlayer.destroy();
            } catch (e) {
                console.log('Player cleanup error:', e);
            }
            window.asciiPlayer = null;
        }
        
        // Always create a new player
        const player = new ASCIIAnimationPlayer(animationContainer, {
            autoResize: true,
            loop: true
        });
        
        player.loadAnimation('/assets/ascii-animation.json');
        
        // Store player instance
        window.asciiPlayer = player;
    }
}

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', initializeAnimation);

// Initialize when page becomes visible (for SPA-like navigation)
document.addEventListener('visibilitychange', function() {
    if (!document.hidden) {
        setTimeout(initializeAnimation, 100); // Small delay to ensure DOM is ready
    }
});

// Initialize on page load (for direct navigation)
window.addEventListener('load', initializeAnimation);

// Initialize on focus (when returning to tab/page)
window.addEventListener('focus', initializeAnimation);