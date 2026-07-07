document.addEventListener('DOMContentLoaded', function () {
  // Theme toggle — persists choice, falls back to system preference
  var toggle = document.querySelector('.theme-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var dark = document.documentElement.classList.toggle('dark');
      localStorage.setItem('theme', dark ? 'dark' : 'light');
    });
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
