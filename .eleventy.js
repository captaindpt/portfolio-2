module.exports = function(eleventyConfig) {
  // Copy static assets
  eleventyConfig.addPassthroughCopy("css");
  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("js");

  // Create posts collection
  eleventyConfig.addCollection("posts", function(collectionApi) {
    return collectionApi.getFilteredByGlob("posts/*.md").sort((a, b) => {
      return new Date(b.date) - new Date(a.date); // Sort by date, newest first
    });
  });

  // Add date filter for formatting
  eleventyConfig.addFilter("dateFormat", function(date) {
    return new Date(date).toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric"
    });
  });

  // Add excerpt filter
  eleventyConfig.addFilter("excerpt", function(content) {
    const excerpt = content.split("\n\n")[0];
    return excerpt.length > 150 ? excerpt.substring(0, 150) + "..." : excerpt;
  });

  // Watch for changes in CSS and JS
  eleventyConfig.addWatchTarget("./css/");
  eleventyConfig.addWatchTarget("./js/");

  return {
    dir: {
      input: ".",
      includes: "_includes",
      data: "_data",
      output: "_site"
    },
    passthroughFileCopy: true,
    markdownTemplateEngine: "liquid",
    htmlTemplateEngine: "liquid"
  };
}; 