---
layout: layout.liquid
title: My Work
permalink: /my-work/
---

<div class="work-container">
  <div class="work-section work-experience">
    <h2>Professional Experience</h2>
    <p>My journey through various roles in technology, from IT administration to AI research.</p>
    <div class="experience-list">
      {% for job in site.experience %}
      <div class="experience-item">
        <div class="experience-header">
          <h3 class="job-title">{{ job.title }}</h3>
          <div class="job-meta">
            <span class="company">{{ job.company }}</span>
            <span class="period">{{ job.period }}</span>
          </div>
        </div>
        <p class="job-description">{{ job.description }}</p>
        <div class="technologies">
          {%- for tech in job.technologies -%}
          <span class="tech-tag">{{ tech }}</span>
          {%- endfor -%}
        </div>
      </div>
      {% endfor %}
    </div>
    
    <div class="additional-experience">
      <p class="additional-experience-text">
        I have also worked in the capacity of 
        <span class="job-cycler" id="job-cycler">construction worker</span>.
      </p>
    </div>
  </div>

  <div class="work-divider"></div>

  <div class="work-section work-projects">
    <h2>Side Projects & Experiments</h2>
    <p>Personal projects and explorations in various technologies and domains.</p>
    <div class="side-projects-grid">
      {%- assign sorted_projects = site.side_projects | sort: 'date' | reverse -%}
      {%- for project in sorted_projects -%}
      <div class="side-project-card">
        <div class="project-header">
          <h3 class="project-title">
            <a href="{{ project.url }}" target="_blank" rel="noopener noreferrer">{{ project.name }}</a>
          </h3>
          {%- if project.date -%}
          <span class="project-date">{{ project.date | date: "%B %Y" }}</span>
          {%- endif -%}
        </div>
        <p class="project-description">{{ project.description }}</p>
        <div class="technologies">
          {%- for tech in project.technologies -%}
          <span class="tech-tag">{{ tech }}</span>
          {%- endfor -%}
        </div>
      </div>
      {%- endfor -%}
    </div>
  </div>

  <div class="work-divider"></div>

  <div class="work-section work-everything-else">
    <h2>Everything Else</h2>
    <p>Additional interests, activities, and miscellaneous projects worth mentioning.</p>
    <div class="everything-else-grid">
      {%- if site.everything_else -%}
      {%- assign sorted_everything_else = site.everything_else | sort: 'date' | reverse -%}
      {%- for item in sorted_everything_else -%}
      <div class="everything-else-card">
        <div class="everything-else-header">
          <span class="period">{{ item.period }}</span>
        </div>
        <p class="item-description">{{ item.description }}</p>
      </div>
      {%- endfor -%}
      {%- else -%}
      <div class="everything-else-card">
        <h3 class="item-title">Photography</h3>
        <p class="item-description">Landscape and street photography as a creative outlet. Exploring composition, lighting, and storytelling through visual media.</p>
        <div class="technologies">
          <span class="tech-tag">Creative</span>
          <span class="tech-tag">Visual Arts</span>
        </div>
      </div>
      <div class="everything-else-card">
        <h3 class="item-title">Technical Writing</h3>
        <p class="item-description">Writing technical articles and documentation to share knowledge and help other developers learn complex concepts.</p>
        <div class="technologies">
          <span class="tech-tag">Communication</span>
          <span class="tech-tag">Documentation</span>
        </div>
      </div>
      {%- endif -%}
    </div>
  </div>
</div>
