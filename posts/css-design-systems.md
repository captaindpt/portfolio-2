---
layout: layout.liquid
title: Creating a CSS Design System with Custom Properties
date: 2024-12-18
tags: ["css", "design-systems", "frontend"]
excerpt: "How I built a maintainable design system using CSS custom properties for consistent theming across my portfolio."
---

# Creating a CSS Design System with Custom Properties

Building a consistent visual identity across a website can be challenging. CSS custom properties (variables) provide an elegant solution for creating maintainable design systems.

## The Problem

Without a systematic approach to styling, projects often suffer from:

- **Inconsistent spacing** between elements
- **Color variations** that don't follow a cohesive palette  
- **Typography chaos** with random font sizes and weights
- **Maintenance nightmares** when design changes are needed

## Enter CSS Custom Properties

CSS custom properties allow us to define reusable values that can be referenced throughout our stylesheets:

```css
:root {
  /* Color palette */
  --color-primary: #2563eb;
  --color-text: #1f2937;
  --color-background: #ffffff;
  
  /* Typography scale */
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  
  /* Spacing system */
  --spacing-xs: 0.5rem;
  --spacing-sm: 1rem;
  --spacing-md: 1.5rem;
  --spacing-lg: 2rem;
}
```

## My Design Token Strategy

For this portfolio, I organized tokens into logical categories:

### Colors
```css
:root {
  --color-text-primary: rgb(6, 6, 6);
  --color-background-primary: rgb(227, 227, 227);
  --color-border: #ccc;
}
```

### Typography
```css
:root {
  --font-family-light: "Martina Light", serif;
  --font-family-bold: "Martina Bold", serif;
  --font-size-heading: 40px;
  --line-height-base: 1.6;
}
```

### Layout & Spacing
```css
:root {
  --layout-max-width: 740px;
  --layout-sidebar-width: 280px;
  --spacing-lg: 2em;
}
```

## Benefits in Action

### 1. Consistent Spacing
Instead of random margins and padding:
```css
/* ❌ Inconsistent */
.card { margin: 15px; padding: 8px; }
.button { margin: 20px; padding: 12px; }

/* ✅ Systematic */
.card { 
  margin: var(--spacing-md); 
  padding: var(--spacing-sm); 
}
.button { 
  margin: var(--spacing-lg); 
  padding: var(--spacing-sm); 
}
```

### 2. Easy Theme Updates
Want to change your primary color? Update one variable:
```css
:root {
  --color-primary: #dc2626; /* Was #2563eb */
}
```

### 3. Responsive Design
Variables can change based on context:
```css
:root {
  --font-size-heading: 24px;
}

@media (min-width: 768px) {
  :root {
    --font-size-heading: 32px;
  }
}
```

## Implementation Tips

1. **Start small** - Begin with colors and spacing
2. **Use semantic names** - `--color-primary` not `--blue`
3. **Document your system** - Comments in CSS are your friend
4. **Be consistent** - Stick to your naming conventions

## Browser Support

CSS custom properties are well-supported in modern browsers. For legacy support, consider:

- PostCSS plugins for fallbacks
- Sass variables as backup
- Progressive enhancement approach

## Conclusion

CSS custom properties transformed how I approach styling. They bring order to chaos and make maintaining large stylesheets actually enjoyable.

The upfront investment in creating a design system pays dividends in development speed and design consistency. Your future self will thank you! 