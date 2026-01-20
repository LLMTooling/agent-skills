<!-- Source: https://docs.astro.build/en/guides/integrations-guide/partytown/ -->

# @astrojs/ partytown

v2.1.4
[GitHub](https://github.com/withastro/astro/tree/main/packages/integrations/partytown/)
[npm](https://www.npmjs.com/package/@astrojs/partytown)
[Changelog](https://github.com/withastro/astro/tree/main/packages/integrations/partytown/CHANGELOG.md)

This **[Astro integration](/en/guides/integrations-guide/)** enables [Partytown](https://partytown.qwik.dev/) in your Astro project.

## Why Astro Partytown

[Section titled “Why Astro Partytown”](#why-astro-partytown)

Partytown is a lazy-loaded library to help relocate resource intensive scripts into a [web worker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API), and off of the [main thread](https://developer.mozilla.org/en-US/docs/Glossary/Main_thread).

If you’re using third-party scripts for things like analytics or ads, Partytown is a great way to make sure that they don’t slow down your site.

The Astro Partytown integration installs Partytown for you and makes sure it’s enabled on all of your pages.

## Installation

[Section titled “Installation”](#installation)

Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can [install integrations manually](#manual-install) instead.

Run one of the following commands in a new terminal window.



* [npm](#tab-panel-2959)
* [pnpm](#tab-panel-2960)
* [Yarn](#tab-panel-2961)

Terminal window

```
npx astro add partytown
```

Terminal window

```
pnpm astro add partytown
```

Terminal window

```
yarn astro add partytown
```



If you run into any issues, [feel free to report them to us on GitHub](https://github.com/withastro/astro/issues) and try the manual installation steps below.

### Manual Install

[Section titled “Manual Install”](#manual-install)

First, install the `@astrojs/partytown` package:

* [npm](#tab-panel-2962)
* [pnpm](#tab-panel-2963)
* [Yarn](#tab-panel-2964)

Terminal window

```
npm install @astrojs/partytown
```

Terminal window

```
pnpm add @astrojs/partytown
```

Terminal window

```
yarn add @astrojs/partytown
```

Then, apply the integration to your `astro.config.*` file using the `integrations` property:

astro.config.mjs

```
import { defineConfig } from 'astro/config';



import partytown from '@astrojs/partytown';



export default defineConfig({



// ...



integrations: [partytown()],



});
```

## Usage

[Section titled “Usage”](#usage)

Partytown should be ready to go with zero config. If you have an existing 3rd party script on your site, try adding the `type="text/partytown"` attribute:

```
<script type="text/partytown" src="fancy-analytics.js"></script>
```

If you open the “Network” tab from [your browser’s dev tools](https://developer.chrome.com/docs/devtools/open/), you should see the `partytown` proxy intercepting this request.

## Configuration

[Section titled “Configuration”](#configuration)

To configure this integration, pass a ‘config’ object to the `partytown()` function call in `astro.config.mjs`.

astro.config.mjs

```
export default defineConfig({



// ...



integrations: [



partytown({



config: {



// options go here



},



}),



],



});
```

This mirrors the [Partytown config object](https://partytown.qwik.dev/configuration/) and all options can be set in `partytown.config`. Some common configuration options for Astro projects are described on this page.

### Enabling debug mode

[Section titled “Enabling debug mode”](#enabling-debug-mode)

Partytown ships with a `debug` mode; enable or disable it by passing `true` or `false` to `config.debug`. If [`debug` mode](https://partytown.qwik.dev/debugging) is enabled, it will output detailed logs to the browser console.

If this option isn’t set, `debug` mode will be on by default in [dev](/en/reference/cli-reference/#astro-dev) or [preview](/en/reference/cli-reference/#astro-preview) mode.

astro.config.mjs

```
export default defineConfig({



// ...



integrations: [



partytown({



// Example: Disable debug mode.



config: { debug: false },



}),



],



});
```

### Forwarding variables

[Section titled “Forwarding variables”](#forwarding-variables)

Third-party scripts typically add variables to the `window` object so that you can communicate with them throughout your site. But when a script is loaded in a web-worker, it doesn’t have access to that global `window` object.

To solve this, Partytown can “patch” variables to the global window object and forward them to the appropriate script.

You can specify which variables to forward with the `config.forward` option. [Read more in Partytown’s documentation.](https://partytown.qwik.dev/forwarding-events)

astro.config.mjs

```
export default defineConfig({



// ...



integrations: [



partytown({



// Example: Add dataLayer.push as a forwarding-event.



config: {



forward: ['dataLayer.push'],



},



}),



],



});
```

### Proxying requests

[Section titled “Proxying requests”](#proxying-requests)

Some third-party scripts may require [proxying](https://partytown.qwik.dev/proxying-requests/) through `config.resolveUrl()`, which runs inside the service worker. You can set this configuration option to check for a specific URL, and optionally return a proxied URL instead:

astro.config.mjs

```
export default defineConfig({



// ...



integrations: [



partytown({



// Example: proxy Facebook's analytics script



config: {



resolveUrl: (url) => {



const proxyMap = {



"connect.facebook.net": "my-proxy.com"



}



url.hostname = proxyMap[url.hostname] || url.hostname;



return url;



},



}



}),



],



});
```

However since the `config` object is serialized when sent to the client, some limitations on functions passed to your configuration apply:

* Functions cannot reference anything outside of the function scope.
* Functions can only be written in JavaScript.

In some advanced use cases, you may need to pass data to this function while initializing Partytown. To do so, you can set `resolveUrl()` on `window.partytown` instead of the integration config:

Head.astro

```
---



const proxyMap = {



"connect.facebook.net": "my-proxy.com"



};



---



<script is:inline set:html={`



window.partytown = {



resolveUrl: (url) => {



const proxyMap = ${JSON.stringify(proxyMap)};



url.hostname = proxyMap[url.hostname] || url.hostname;



return url;



},



};



`} />
```

Note that the integration config will override `window.partytown` if you set a property in both.

## Examples

[Section titled “Examples”](#examples)

* [Browse projects with Astro Partytown on GitHub](https://github.com/search?q=%22%40astrojs%2Fpartytown%22+path%3A**%2Fpackage.json&type=code) for more examples!

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [Implementing Google Tag Manager with Partytown and Astro](https://medium.com/@tagperfect/implementing-google-tag-manager-with-partytown-js-in-astro-my-modest-experience-983388907b35)
* [Optimise Google Analytics using Partytown in Astro](https://ricostacruz.com/posts/google-analytics-in-astro)

## More integrations

### Front-end frameworks

* ![](/logos/alpine-js.svg)

  ### [@astrojs/alpinejs](/en/guides/integrations-guide/alpinejs/)
* ![](/logos/preact.svg)

  ### [@astrojs/preact](/en/guides/integrations-guide/preact/)
* ![](/logos/react.svg)

  ### [@astrojs/react](/en/guides/integrations-guide/react/)
* ![](/logos/solid.svg)

  ### [@astrojs/solid⁠-⁠js](/en/guides/integrations-guide/solid-js/)
* ![](/logos/svelte.svg)

  ### [@astrojs/svelte](/en/guides/integrations-guide/svelte/)
* ![](/logos/vue.svg)

  ### [@astrojs/vue](/en/guides/integrations-guide/vue/)

### Adapters

* ![](/logos/cloudflare-pages.svg)

  ### [@astrojs/cloudflare](/en/guides/integrations-guide/cloudflare/)
* ![](/logos/netlify.svg)

  ### [@astrojs/netlify](/en/guides/integrations-guide/netlify/)
* ![](/logos/node.svg)

  ### [@astrojs/node](/en/guides/integrations-guide/node/)
* ![](/logos/vercel.svg)

  ### [@astrojs/vercel](/en/guides/integrations-guide/vercel/)

### Other integrations

* ![](/logos/db.svg)

  ### [@astrojs/db](/en/guides/integrations-guide/db/)
* ![](/logos/markdoc.svg)

  ### [@astrojs/markdoc](/en/guides/integrations-guide/markdoc/)
* ![](/logos/mdx.svg)

  ### [@astrojs/mdx](/en/guides/integrations-guide/mdx/)
* ![](/logos/partytown.svg)

  ### [@astrojs/partytown](/en/guides/integrations-guide/partytown/)
* ![](/logos/sitemap.svg)

  ### [@astrojs/sitemap](/en/guides/integrations-guide/sitemap/)

Learn

![](/_astro/CodingInPublic.DpaYu7Qd_5sx41.webp)

## Learn Astro with **Coding in Public**

150+ video lessons
•
Astro v5 ready

[Get 20% off](https://learnastro.dev?code=ASTRO_PROMO)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/integrations-guide/partytown.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

MDX](/en/guides/integrations-guide/mdx/)
[Next

Sitemap](/en/guides/integrations-guide/sitemap/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)