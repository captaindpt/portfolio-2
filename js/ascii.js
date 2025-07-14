document.addEventListener('DOMContentLoaded', () => {
  async function renderAsciiArt() {
    const containers = document.querySelectorAll('.ascii-art-container');
    if (!containers.length) return;

    // wait for font
    try { await document.fonts.load('100px "AlmaMono"'); } catch(e){}

    const safetyMargin = 2;

    for (const container of containers) {
      // Skip if already processed
      if (container.dataset.rendered) continue;

      const src = container.dataset.src || '/assets/ascii-art.txt';

      // Ensure pre element
      let pre = container.querySelector('pre.ascii-art');
      if (!pre) {
        pre = document.createElement('pre');
        pre.className = 'ascii-art';
        container.appendChild(pre);
      }

      try {
        const res = await fetch(src);
        if(!res.ok) throw new Error('fetch');
        const text = await res.text();
        pre.textContent = text;
        pre.style.setProperty('font-size','8px','important');
      } catch(err){
        pre.textContent = 'Error loading art.';
        continue;
      }

      const fit = () => {
        const cw = container.clientWidth - safetyMargin;
        if(cw<=0) return;
        const currentWidth = pre.scrollWidth;
        if(currentWidth===0) return;
        const currentFont = parseFloat(getComputedStyle(pre).fontSize);
        const newFont = currentFont * (cw/currentWidth);
        pre.style.setProperty('font-size', `${newFont}px`, 'important');
      };

      fit();
      setTimeout(fit,100);
      window.addEventListener('resize', fit);

      container.dataset.rendered='true';
    }
  }

  window.renderAsciiArt = renderAsciiArt;
  renderAsciiArt();
}); 