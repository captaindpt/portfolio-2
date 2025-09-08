# Posts Instructions & Markdown Reference

**This file demonstrates all available markdown formatting methods for posts in this Eleventy site.**

## Front Matter Structure
```yaml
---
layout: layout.liquid
title: Your Post Title
date: 2025-07-09
tags: ["tag1", "tag2", "tag3"]
excerpt: "Brief description that appears in post previews and meta tags."
---
```

## Headers
# H1 Header
## H2 Header  
### H3 Header
#### H4 Header
##### H5 Header
###### H6 Header

## Text Formatting
**Bold text**
*Italic text*
***Bold and italic***
~~Strikethrough~~

## Links and References
[Link text](https://example.com)
[Link with title](https://example.com "Link title")

## Lists

### Unordered Lists
* Item 1
* Item 2
  * Nested item
  * Another nested item
* Item 3

### Ordered Lists
1. First item
2. Second item
   1. Nested numbered item
   2. Another nested item
3. Third item

## Mathematical Notation
Use HTML tags for mathematical expressions:

**Subscripts:** H<sub>2</sub>O, a<sub>0</sub>, x<sub>i</sub>
**Superscripts:** E = mc<sup>2</sup>, x<sup>n</sup>, s<sup>(n-1)</sup>

**Complex equations:**
a<sub>0</sub>s<sup>n</sup> + a<sub>1</sub>s<sup>(n-1)</sup> + ... + a<sub>n</sub> = 0

## Code

### Inline Code
Use `backticks` for inline code like `console.log()` or `npm install`.

### Code Blocks
```javascript
// JavaScript example
function hello(name) {
    console.log(`Hello, ${name}!`);
}
```

```python
# Python example
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

```bash
# Bash commands
npm run dev
git status
```

```css
/* CSS styling */
.example {
    color: #333;
    margin: 1rem 0;
}
```

## Blockquotes
> This is a blockquote. Use it for citations, emphasizing important text, or highlighting key points.
> 
> You can have multiple paragraphs in blockquotes.

> **Pro tip:** Blockquotes can contain other markdown formatting like **bold** and *italic* text.

## Horizontal Rules
Use three dashes for horizontal dividers:

---

## Tables
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1    | Data     | More data|
| Row 2    | Info     | Details  |
| Row 3    | Content  | Values   |

## Images
![Alt text](../assets/image.png "Optional title")

## HTML Tags
Since this is processed by Eleventy, you can use HTML tags:

<details>
<summary>Click to expand</summary>
Hidden content that can be revealed.
</details>

<mark>Highlighted text</mark>

<small>Small text for footnotes</small>

## Special Characters
Em dash: —
En dash: –
Ellipsis: …
Copyright: ©
Trademark: ™

## Escaping Characters
Use backslashes to escape special characters:
\*Not italic\*
\`Not code\`
\# Not a header

## Line Breaks
End a line with two spaces for a line break  
Like this.

Or use a blank line for paragraph breaks.

## Task Lists (if supported)
- [x] Completed task
- [ ] Incomplete task
- [ ] Another task

---

**Note:** This file is excluded from the website build but remains in the posts directory for reference.