/* Minimal client-side explorer for AI design systems */
(function () {
  const state = {
    entries: [],
    filtered: [],
    types: new Set(),
  };

  const els = {
    search: document.getElementById('search'),
    typeFilter: document.getElementById('typeFilter'),
    maturityFilter: document.getElementById('maturityFilter'),
    results: document.getElementById('results'),
    tpl: document.getElementById('cardTpl'),
  };

  const normalize = (s) => (s || '').toLowerCase();

  function renderOptions() {
    state.types.forEach((t) => {
      const opt = document.createElement('option');
      opt.value = t; opt.textContent = t;
      els.typeFilter.appendChild(opt);
    });
  }

  function matches(entry) {
    const q = normalize(els.search.value);
    const type = els.typeFilter.value;
    const maturity = els.maturityFilter.value;

    const textHit = !q || [entry.name, entry.org, entry.tags.join(' ')].map(normalize).some(s => s.includes(q));
    const typeHit = !type || entry.type === type;
    const maturityHit = !maturity || entry.maturity === maturity;
    return textHit && typeHit && maturityHit;
  }

  function render() {
    els.results.innerHTML = '';
    state.filtered.forEach((e) => {
      const node = els.tpl.content.cloneNode(true);
      node.querySelector('.name').textContent = e.name;
      node.querySelector('.maturity').textContent = e.maturity;
      node.querySelector('.org').textContent = e.org;
      node.querySelector('.type').textContent = e.type;
      node.querySelector('.features').textContent = e.ai_features;
      node.querySelector('.integrations').textContent = 'Integrations: ' + e.integrations;
      const tags = node.querySelector('.tags');
      e.tags.forEach((t) => {
        const span = document.createElement('span');
        span.className = 'tag';
        span.textContent = t;
        tags.appendChild(span);
      });
      const link = node.querySelector('.link');
      link.href = e.url;
      els.results.appendChild(node);
    });
  }

  function applyFilters() {
    state.filtered = state.entries.filter(matches);
    render();
  }

  async function init() {
    const res = await fetch(window.JSON_PATH);
    const entries = await res.json();
    // collect types
    entries.forEach((e) => state.types.add(e.type));
    state.entries = entries.sort((a, b) => a.name.localeCompare(b.name));
    renderOptions();
    applyFilters();

    els.search.addEventListener('input', applyFilters);
    els.typeFilter.addEventListener('change', applyFilters);
    els.maturityFilter.addEventListener('change', applyFilters);
  }

  init().catch((err) => {
    console.error('Failed to init explorer', err);
    els.results.textContent = 'Failed to load entries.';
  });
})();