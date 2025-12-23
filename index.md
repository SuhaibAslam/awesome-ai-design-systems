---
layout: page
title: Awesome AI-Native Design Systems
description: Curated index of AI-native design systems, UIs, and protocols.
---

<section class="hero">
	<h2 style="margin:0.25rem 0">Explore AI-Native Design Systems</h2>
	<p style="color:#4b5563;margin:0.25rem 0">Search and filter the curated registry of AI-first UI systems, chat/agent UX kits, schema-to-UI libraries, and protocols.</p>
</section>

<link rel="stylesheet" href="{{ site.baseurl }}/assets/explore.css">

<section class="explore-controls">
	<input id="search" type="search" placeholder="Search name, org, tags" aria-label="Search" />
	<select id="typeFilter" aria-label="Filter by type">
		<option value="">All Types</option>
	</select>
	<select id="maturityFilter" aria-label="Filter by maturity">
		<option value="">All Maturities</option>
		<option>Production</option>
		<option>Active</option>
		<option>Experimental</option>
		<option>Inactive</option>
	</select>
</section>

<section id="results" class="card-grid" aria-live="polite"></section>

<template id="cardTpl">
	<article class="card">
		<header>
			<h3 class="name"></h3>
			<span class="badge maturity"></span>
		</header>
		<p class="org"></p>
		<p class="type"></p>
		<p class="features"></p>
		<p class="integrations"></p>
		<div class="tags"></div>
		<footer>
			<a class="link" target="_blank" rel="noopener noreferrer">Project</a>
		</footer>
	</article>
	</template>

<script>
	window.SITE_BASEURL = '{{ site.baseurl }}';
	window.JSON_PATH = window.SITE_BASEURL + '/data/ai-design-systems.json';
</script>
<script src="{{ site.baseurl }}/assets/js/explore.js"></script>

- Dataset (source of truth): [data/ai-design-systems.json](data/ai-design-systems.json)
- Generated Table: [TABLE.md](TABLE.md)

For definitions and criteria:

- Taxonomy: [docs/taxonomy.md](docs/taxonomy.md)
- Inclusion Criteria: [docs/inclusion-criteria.md](docs/inclusion-criteria.md)

Contribute via pull requests. Start with [CONTRIBUTING.md](CONTRIBUTING.md).
