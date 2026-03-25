---
layout: layout.liquid
title: Home
---

<div class="ascii-art-container">
<pre class="ascii-art"></pre>
</div>

# hey, i'm mani

i build systems that turn chaos into structure.

right now my main thing is [analog-gradients](https://github.com/captaindpt/torch2rtl) — an autonomous chip design exploration platform that takes a PyTorch model and produces silicon-grade timing, area, and power metrics in ~11 minutes. LLM agents orchestrate commercial EDA tools end to end. it's the first feedback loop between ML model design and physical silicon.

i also build AI-powered tools that reverse-engineer undocumented systems into searchable knowledge. i've done this across industrial control systems (proprietary binary formats at [flodraulic](https://flodraulic.com)), university IT infrastructure (RAG pipelines and MCP servers at uofg), and government/institutional sensor data.

i'm finishing my engineering degree at the university of guelph, consulting for a [startup in san francisco](https://firstprinciplesresearch.com), and running a co-op at a hydraulics company where i proposed and am driving their long-term AI strategy.

long-term i'm interested in compute sovereignty — making chip design accessible so intelligence infrastructure is distributed, not centralized. the tools to build silicon shouldn't be locked behind billion-dollar licenses and decade-long learning curves.


## selected work

### flagship

<div class="selected-work-flagship">

**analog-gradients** <span class="status-tag status-active">[active]</span>
autonomous chip design exploration platform. LLM agents orchestrate commercial EDA tools (Cadence Genus/Innovus, Synopsys PrimeTime, GPDK045 PDK). PyTorch model in, silicon PPA metrics out, ~11 minutes end to end. produced a working 4-lane SIMD GPU (320 params, int8 quantized, 25.8 kGE, 118 MHz, 0.6 mW). ran the lowRISC Ibex RISC-V core through 12 configurations matching published references within 1–15%. extended with analog neuromorphic research: coupled oscillator optimization over 24–52D parameter spaces using CMA-ES with 2,000+ Spectre simulations.
[torch2rtl](https://github.com/captaindpt/torch2rtl) · [eda-pilot](https://github.com/captaindpt/eda-pilot)

**p1p-observer** <span class="status-tag status-active">[active]</span>
reverse-engineered a proprietary binary file format used in industrial control systems, with zero existing documentation. parses 85+ binary record types, reconstructs page hierarchy, wire connectivity, and block naming across projects with 1,200+ pages and 3,700+ blocks. turns opaque industrial control data into natural-language-searchable documentation. *(closed source — IP retained under co-op agreement)*

</div>

### shipped

<div class="selected-work-shipped">

**uofg AI infrastructure** <span class="status-tag status-shipped">[shipped]</span>
built three RAG ingestion pipelines parsing unstructured institutional data (SharePoint, Teams, FootPrints) into searchable knowledge bases. deployed on Azure Container Instances with Docker. built custom MCP servers integrating LLMs with university systems. implemented Azure AD-integrated access control with SpiceDB for department-specific AI assistants with granular permissions.

**atlas network content engine** <span class="status-tag status-active">[ongoing]</span>
full-stack content engine for First Principles Research, Inc. (san francisco). Supabase, Vercel, Anthropic/Grok APIs. serverless functions, PostgreSQL schema design, API integrations for automated content processing and delivery.

**apple MCP** <span class="status-tag status-shipped">[shipped]</span>
contributed Apple Mail integration to the [apple-mcp](https://github.com/supermemoryai/apple-mcp) open source project (3,000+ GitHub stars). email search, attachments, scheduling, and error recovery for Model Context Protocol.

**zed IDE contributions** <span class="status-tag status-shipped">[shipped]</span>
contributed to agent framework and UI in [Zed](https://github.com/zed-industries/zed/pull/29115) code editor. enhanced terminal-based agent observability for failure recovery. PR accepted.

</div>

### archive

<details class="archive-details">
<summary>earlier projects</summary>

- **truth terminal** — a bloomberg-style workspace for polymarket and emerging prediction markets
- **ccs aperture** — a semantic search tool, like my own notebook LM for youtube and books
- **[wispr](https://github.com/captaindpt/wispr)** — production-grade voice-to-text system for macOS using Fn key as global trigger
- **[sorya](https://github.com/captaindpt/sorya/tree/main)** — novel AI architecture enabling LLMs to make irreversible internal commitments
- **[AEP](https://github.com/captaindpt/aep)** — attention event protocol for improving AI systems by tracking attention patterns
- **[the box](https://github.com/theboxproject)** — RFID-enhanced physical item tracker with Arduino + PWA
- **[calendar++](https://github.com/captaindpt/calendarplusplus)** — experimental AI-native calendar system
- **[mnist-from-scratch](https://github.com/captaindpt/mnist-from-scratch)** — neural network from scratch in Python
- **[typing-game](https://github.com/captaindpt/typing-game)** — React typing speed test
- **[cinefile](https://github.com/captaindpt/CineFile)** — movie archive assistant with IMDb API
- **a lot of websites** — various web projects and portfolio sites
- **a bunch of robots** — hardware projects combining software and mechanical design
- **arboro** — community event series for creatives, previously crescentia

</details>


## get in touch

you can reach me at [mani@caliburlabs.com](mailto:mani@caliburlabs.com).

<div class="social-links">
  <a href="https://x.com/mafiajoeg" target="_blank" rel="noopener noreferrer" class="social-link">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
      <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
    </svg>
  </a>

  <a href="https://linkedin.com/in/mani-rashahmadi" target="_blank" rel="noopener noreferrer" class="social-link">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
      <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
    </svg>
  </a>

  <a href="https://instagram.com/manisoffline" target="_blank" rel="noopener noreferrer" class="social-link">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
    </svg>
  </a>

  <a href="https://discord.com/users/manirashahmadi" target="_blank" rel="noopener noreferrer" class="social-link">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
      <path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028 14.09 14.09 0 0 0 1.226-1.994.076.076 0 0 0-.041-.106 13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.892.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.03zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418Z"/>
    </svg>
  </a>
</div>
