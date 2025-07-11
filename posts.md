---
layout: layout.liquid
title: Posts
permalink: /posts/
---

# Posts

{% if collections.posts.size > 0 %}
{% for post in collections.posts %}
<article class="post-preview">
  <h2><a href="{{ post.url }}">{{ post.data.title }}</a></h2>
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
  {% if post.data.excerpt %}
  <p class="post-excerpt">{{ post.data.excerpt }}</p>
  {% else %}
  <p class="post-excerpt">{{ post.templateContent | excerpt }}</p>
  {% endif %}
  <a href="{{ post.url }}" class="read-more">Read more →</a>
</article>
{% endfor %}
{% else %}
<p>No posts yet. Check back soon!</p>
{% endif %}