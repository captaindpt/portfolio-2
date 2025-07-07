# Portfolio Website

A modern, responsive portfolio website built with [Eleventy](https://www.11ty.dev/) (11ty) static site generator.

## Features

- 📱 **Responsive Design** - Mobile-first approach with desktop optimizations
- ⚡ **Fast Performance** - Static site generation for optimal loading speeds
- 🎨 **Design System** - CSS custom properties for consistent theming
- 📝 **Content Management** - Markdown-based posts with front matter
- 🔍 **SEO Ready** - Proper meta tags and semantic HTML
- 🛠️ **Developer Experience** - Hot reload, build scripts, and formatting tools

## Quick Start

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd portfolio-2

# Install dependencies
npm install

# Start development server
npm run dev
```

Visit `http://localhost:8080` to see your site.

## Development

### Available Scripts

```bash
npm run dev          # Start development server with hot reload
npm run build        # Build for production
npm run start        # Alias for npm run dev
npm run clean        # Remove build directory
npm run format       # Format code with Prettier
npm run format:check # Check code formatting
```

### Alternative Script Usage

You can also use the provided shell scripts:

```bash
./scripts/dev.sh     # Start development server
./scripts/build.sh   # Build with error handling
```

## Project Structure

```
├── _data/              # Global data files
│   └── site.json       # Site configuration
├── _includes/          # Templates and layouts
│   ├── layout.liquid   # Main layout template
│   └── partials/       # Reusable components
│       ├── head.liquid
│       ├── navigation.liquid
│       └── footer.liquid
├── _site/              # Generated site (build output)
├── assets/             # Static assets
│   └── fonts/          # Custom fonts
├── css/                # Stylesheets
│   └── style.css       # Main stylesheet with design tokens
├── js/                 # JavaScript files
├── posts/              # Blog posts
│   ├── posts.json      # Posts directory data
│   └── *.md            # Individual posts
├── scripts/            # Build and development scripts
├── .eleventy.js        # Eleventy configuration
└── package.json        # Dependencies and scripts
```

## Content Management

### Writing Posts

Create new posts in the `posts/` directory:

```markdown
---
layout: layout.liquid
title: "Your Post Title"
date: 2024-01-15
tags: ["tag1", "tag2"]
excerpt: "Brief description of your post"
---

# Your Post Title

Your content here...
```

### Site Configuration

Edit `_data/site.json` to customize:

```json
{
  "title": "Your Site Title",
  "description": "Your site description",
  "author": "Your Name",
  "url": "https://yoursite.com",
  "navigation": [
    {"title": "Home", "url": "/"},
    {"title": "Posts", "url": "/posts/"},
    {"title": "About", "url": "/about/"}
  ]
}
```

## Customization

### Design System

The site uses CSS custom properties for consistent theming. Modify variables in `css/style.css`:

```css
:root {
  /* Colors */
  --color-text-primary: rgb(6, 6, 6);
  --color-background-primary: rgb(227, 227, 227);
  
  /* Typography */
  --font-family-light: "Martina Light", serif;
  --font-family-bold: "Martina Bold", serif;
  
  /* Spacing */
  --spacing-sm: 1em;
  --spacing-md: 1.5em;
  --spacing-lg: 2em;
}
```

### Adding Pages

Create new `.md` files in the root directory:

```markdown
---
layout: layout.liquid
title: "About"
permalink: /about/
---

# About Me

Your about content...
```

### Custom Fonts

Place font files in `assets/fonts/` and reference them in your CSS:

```css
@font-face {
  font-family: 'YourFont';
  src: url('../assets/fonts/your-font.woff2') format('woff2');
}
```

## Deployment

### Build for Production

```bash
npm run build
```

The generated site will be in the `_site/` directory, ready for deployment to any static hosting service.

### Deployment Options

- **Netlify**: Connect your repository and set build command to `npm run build`
- **Vercel**: Import project and use default settings
- **GitHub Pages**: Use GitHub Actions with the build output
- **Traditional Hosting**: Upload `_site/` contents via FTP

## Development Workflow

1. **Start development**: `npm run dev`
2. **Make changes**: Edit content, styles, or templates
3. **Auto-reload**: Changes are reflected immediately
4. **Format code**: `npm run format` before committing
5. **Build**: `npm run build` to test production build
6. **Deploy**: Push to your hosting service

## Technologies Used

- **[Eleventy](https://www.11ty.dev/)** - Static site generator
- **[Liquid](https://liquidjs.com/)** - Templating engine
- **CSS Custom Properties** - Modern CSS features
- **Markdown** - Content authoring
- **Prettier** - Code formatting

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Format code with `npm run format`
5. Test with `npm run build`
6. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Support

For questions or issues, please open an issue on the repository or contact [your-email@example.com].