---
layout: layout.liquid
title: Posts
permalink: /posts/
---

# posts

notes from the build — some technical, some philosophical, most somewhere in between.

{% if collections.posts.size > 0 %}
{% for post in collections.posts %}
<article class="post-preview">
  <h2><a href="{{ post.url }}">{{ post.data.title }}</a></h2>
  {% if post.data.excerpt %}
  <p class="post-subtitle">{{ post.data.excerpt }}</p>
  {% endif %}
  <div class="post-meta">
    <time datetime="{{ post.data.date | date: '%Y-%m-%d' }}">{{ post.data.date | dateFormat }}</time>
    {% if post.data.tags.size > 0 %}
    <span class="post-tags">
      {% for tag in post.data.tags %}
      <span class="tag">{{ tag }}</span>
      {% endfor %}
    </span>
    {% endif %}
  </div>
</article>
{% endfor %}
{% else %}
<p>no posts yet. check back soon!</p>
{% endif %}
