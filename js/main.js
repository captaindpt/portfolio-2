document.addEventListener('DOMContentLoaded', function () {
  // Theme toggle — persists choice, falls back to system preference
  var toggle = document.querySelector('.theme-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var dark = document.documentElement.classList.toggle('dark');
      localStorage.setItem('theme', dark ? 'dark' : 'light');
    });
  }

  // ASCII animation in the hero — a painting, rendered in characters
  var pane = document.querySelector('.ascii-pane');
  if (pane) {
    fetch(pane.dataset.src || '/assets/ascii-animation.json')
      .then(function (r) { return r.json(); })
      .then(function (d) {
        var pre = pane.querySelector('pre');
        var frames = d.frames;
        if (!pre || !frames || !frames.length) return;
        pre.textContent = frames[0];
        if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
        var i = 0;
        setInterval(function () {
          if (document.hidden) return;
          i = (i + 1) % frames.length;
          pre.textContent = frames[i];
        }, 1000 / 14);
      })
      .catch(function () {});
  }

  // Job cycler on the work page
  var cycler = document.getElementById('job-cycler');
  if (cycler) {
    var jobs = [
      'construction worker',
      'painter',
      'line cook',
      'social media manager',
      'door to door salesman',
      'private tutor'
    ];
    var i = 0;
    cycler.addEventListener('click', function () {
      i = (i + 1) % jobs.length;
      cycler.textContent = jobs[i];
    });
  }
});
