---
layout: layout.liquid
title: My Work
permalink: /my-work/
---

# work

a journey from IT administration to autonomous chip design. if you want a PDF copy of my resume, you can <a href="https://drive.google.com/file/d/1tFymABAQl-0r06U2AT83Jpexy8WlVKfI/view?usp=drive_link" target="_blank" rel="noopener noreferrer">get it here</a>.

<section class="section">
  <p class="label"><span class="idx">01</span>Experience</p>
  <div class="index-list">
    {%- for job in site.experience -%}
    <div class="xp-item">
      <div class="xp-when">{{ job.period }}</div>
      <div class="xp-body">
        <h3>{{ job.title }}</h3>
        <p class="company">{{ job.company }}</p>
        <p class="desc">{{ job.description }}</p>
        <div class="tags">
          {%- for tech in job.technologies -%}
          <span>{{ tech }}</span>
          {%- endfor -%}
        </div>
      </div>
    </div>
    {%- endfor -%}
  </div>
  <p class="aside-note">i have also worked in the capacity of <span class="job-cycler" id="job-cycler">construction worker</span>.</p>
</section>

<section class="section">
  <p class="label"><span class="idx">02</span>Projects &amp; experiments</p>
  <div class="index-list">
    {%- assign sorted_projects = site.side_projects | sort: 'date' | reverse -%}
    {%- for project in sorted_projects -%}
    {%- if project.url == "#" or project.url == blank -%}
    <div class="index-row">
    {%- else -%}
    <a class="index-row" href="{{ project.url }}" target="_blank" rel="noopener noreferrer">
    {%- endif -%}
      <span class="when">{{ project.date | date: "%b %Y" | downcase }}</span>
      <span class="what">
        <h3>{{ project.name }}{% if project.tier == 'flagship' %}<span class="flag">flagship</span>{% endif %}{% if project.status %}<span class="flag">{{ project.status }}</span>{% endif %}</h3>
        <p>{{ project.description }}</p>
        <span class="tags" style="margin-top: 0.6rem;">
          {%- for tech in project.technologies -%}
          <span>{{ tech }}</span>
          {%- endfor -%}
        </span>
      </span>
    {%- if project.url == "#" or project.url == blank -%}
    </div>
    {%- else -%}
    </a>
    {%- endif -%}
    {%- endfor -%}
  </div>
</section>
