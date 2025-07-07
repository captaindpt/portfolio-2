// This file is no longer needed for Markdown rendering with Eleventy.
// It can be used for other client-side interactivity later if needed. 

// Hamburger menu functionality
document.addEventListener('DOMContentLoaded', function() {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            // Toggle active class on button (for animation)
            navToggle.classList.toggle('active');
            
            // Toggle active class on menu (to show/hide)
            navMenu.classList.toggle('active');
        });

        // Close menu when clicking on a link
        const navLinks = document.querySelectorAll('.nav-menu a');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            const isClickInsideNav = navToggle.contains(event.target) || navMenu.contains(event.target);
            
            if (!isClickInsideNav && navMenu.classList.contains('active')) {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
            }
        });
    }
    
    // Job cycler functionality
    const jobCycler = document.querySelector('#job-cycler');
    
    if (jobCycler) {
        const jobs = [
            'construction worker',
            'painter', 
            'line cook',
            'social media marketing',
            'door to door salesman',
            'private tutor'
        ];
        
        let currentJobIndex = 0;
        
        jobCycler.addEventListener('click', function() {
            currentJobIndex = (currentJobIndex + 1) % jobs.length;
            jobCycler.textContent = jobs[currentJobIndex];
        });
    }
    
    // Dark mode toggle functionality
    const siteLogo = document.querySelector('.site-logo');
    
    if (siteLogo) {
        // Check for saved theme preference or default to light mode
        const currentTheme = localStorage.getItem('theme') || 'light';
        
        // Apply the saved theme (if not already applied by head script)
        if (currentTheme === 'dark' && !document.documentElement.classList.contains('dark-mode')) {
            document.documentElement.classList.add('dark-mode');
        }
        
        // Add click event listener to toggle dark mode
        siteLogo.addEventListener('click', function() {
            document.documentElement.classList.toggle('dark-mode');
            
            // Save theme preference
            const isDarkMode = document.documentElement.classList.contains('dark-mode');
            localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
            
            // Optional: Add a subtle feedback animation
            siteLogo.style.transform = 'scale(0.95)';
            setTimeout(() => {
                siteLogo.style.transform = '';
            }, 150);
        });
    }
}); 