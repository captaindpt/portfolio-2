---
layout: layout.liquid
title: Home
---

<section class="hero">
  <p class="label"><span class="idx">::</span>Guelph, Ontario — engineer, builder</p>
  <h1>i make things. paintings, beats, robots — lately, <em>the tools that make chips</em>.</h1>
  <p class="subline">my goal is technology that lets anyone make anything. right now that means closing the loop between machine learning and silicon.</p>
</section>

<section class="section">
  <p class="label"><span class="idx">01</span>Now</p>
  <ul class="now-list">
    <li>finishing my engineering degree at the <strong>university of guelph</strong></li>
    <li>building <strong>analog-gradients</strong> — LLM agents orchestrating commercial EDA tools: PyTorch model in, silicon PPA metrics out, ~11 minutes end to end</li>
    <li>reverse-engineering undocumented industrial binary formats at <strong>flodraulic systems</strong></li>
    <li>running <strong>calibur labs</strong> — the long game is compute sovereignty: chip design accessible enough that intelligence infrastructure stays distributed</li>
  </ul>
</section>

<section class="section">
  <p class="label"><span class="idx">02</span>Selected work</p>
  <div class="index-list">
    <a class="index-row" href="https://github.com/captaindpt/torch2rtl" target="_blank" rel="noopener noreferrer">
      <span class="when">2025 —</span>
      <span class="what">
        <h3>analog-gradients<span class="flag">flagship</span></h3>
        <p>autonomous chip design exploration. produced a working 4-lane SIMD GPU and ran the lowRISC Ibex core through 12 configurations within 1–15% of published references.</p>
      </span>
    </a>
    <a class="index-row" href="/my-work/">
      <span class="when">2026</span>
      <span class="what">
        <h3>p1p-observer</h3>
        <p>reverse-engineered a proprietary binary format with zero documentation — 85+ record types, 1,200+ pages of industrial control data made searchable in natural language.</p>
      </span>
    </a>
    <a class="index-row" href="/my-work/">
      <span class="when">2025</span>
      <span class="what">
        <h3>truth terminal</h3>
        <p>a bloomberg-style workspace for polymarket and emerging prediction markets.</p>
      </span>
    </a>
    <a class="index-row" href="/my-work/">
      <span class="when">2025</span>
      <span class="what">
        <h3>ccs aperture</h3>
        <p>semantic search over youtube and books — my own notebookLM, built from sentence transformers and an embedding cache.</p>
      </span>
    </a>
    <a class="index-row" href="/my-work/">
      <span class="when">2025</span>
      <span class="what">
        <h3>wispr</h3>
        <p>voice-to-text for macOS — Fn key as global trigger, native Cocoa, real-time streaming transcription.</p>
      </span>
    </a>
  </div>
  <a class="see-all" href="/my-work/">the full index, including a bunch of robots →</a>
</section>

<section class="section">
  <p class="label"><span class="idx">03</span>Writing</p>
  {% if collections.posts.size > 0 %}
  <div class="index-list">
    {% for post in collections.posts limit: 3 %}
    <a class="index-row" href="{{ post.url }}">
      <span class="when">{{ post.data.date | date: "%b %Y" | downcase }}</span>
      <span class="what">
        <h3>{{ post.data.title }}</h3>
        {% if post.data.excerpt %}<p>{{ post.data.excerpt }}</p>{% endif %}
      </span>
    </a>
    {% endfor %}
  </div>
  <a class="see-all" href="/posts/">all posts →</a>
  {% else %}
  <p>nothing published yet — drafts are brewing.</p>
  {% endif %}
</section>

<section class="contact">
  <p class="label"><span class="idx">04</span>Get in touch</p>
  <p style="margin: 1.75rem 0 0;">
    <a class="big-link" href="mailto:manirash94@gmail.com">manirash94@gmail.com</a>
  </p>
  <div class="socials">
    <a href="https://x.com/mafiajoeg" target="_blank" rel="noopener noreferrer">x / twitter</a>
    <a href="https://linkedin.com/in/mani-rashahmadi" target="_blank" rel="noopener noreferrer">linkedin</a>
    <a href="https://instagram.com/manisoffline" target="_blank" rel="noopener noreferrer">instagram</a>
    <a href="https://github.com/captaindpt" target="_blank" rel="noopener noreferrer">github</a>
  </div>
</section>
