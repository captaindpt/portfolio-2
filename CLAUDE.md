# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Core Commands
- `npm run dev` - Start development server with hot reload (http://localhost:8080)
- `npm run build` - Build site for production
- `npm run clean` - Remove build directory (_site)
- `npm run format` - Format code with Prettier
- `npm run format:check` - Check code formatting

### Alternative Scripts
- `./scripts/dev.sh` - Start development server with dependency check
- `./scripts/build.sh` - Build with error handling and cleanup

## Architecture Overview

This is an Eleventy (11ty) static site generator portfolio website using:

- **Template Engine**: Liquid templates in `_includes/`
- **Content Management**: Markdown files with front matter
- **Build Output**: Static site generated to `_site/`
- **Assets**: Static files (CSS, JS, fonts) passed through to build

### Key Architectural Patterns

- **Layout System**: Single main layout (`_includes/layout.liquid`) with reusable partials
- **Collection System**: Posts collection auto-generated from `posts/*.md`, sorted by date (newest first)
- **Data-Driven Content**: Site configuration and project data centralized in `_data/site.json`
- **Design System**: CSS custom properties for consistent theming in `css/style.css`

### Directory Structure Logic

```
_data/site.json         # Global site data (nav, projects, experience)
_includes/              # Liquid templates and partials
  layout.liquid         # Main page layout
  partials/             # Reusable components
posts/                  # Blog posts (auto-collected)
  posts.json           # Directory-specific data
css/style.css          # Design system with CSS custom properties
```

### Eleventy Configuration (.eleventy.js)

- **Collections**: Automatic posts collection with date sorting
- **Filters**: `dateFormat` and `excerpt` for content processing  
- **Watch Targets**: Live reload for CSS and JS changes
- **Passthrough**: Static assets copied to build

### Content Structure

Posts use front matter with:
- `layout: layout.liquid`
- `title`, `date`, `tags`, `excerpt`

Site data includes structured sections for projects, experience, and side projects with consistent schemas.

## Custom Fonts

Uses two custom font families:
- **Perfectly Nineties**: Used for headers and headings (script-style font)
- **Polysans**: Used for body text and navigation (sans-serif with multiple weights)

Fonts stored in `assets/fonts/` with `@font-face` declarations in CSS. Polysans includes neutral, median, and bulky weights.

## Development Notes

- Hot reload available for all content and assets
- Prettier formatting enforced
- Build process includes dependency checking and cleanup
- No test framework currently configured