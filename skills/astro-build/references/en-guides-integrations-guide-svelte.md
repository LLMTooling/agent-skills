<!-- Source: https://docs.astro.build/en/guides/integrations-guide/svelte/ -->

# @astrojs/ svelte

v7.2.5
[GitHub](https://github.com/withastro/astro/tree/main/packages/integrations/svelte/)
[npm](https://www.npmjs.com/package/@astrojs/svelte)
[Changelog](https://github.com/withastro/astro/tree/main/packages/integrations/svelte/CHANGELOG.md)

This **[Astro integration](/en/guides/integrations-guide/)** enables rendering and client-side hydration for your [Svelte](https://svelte.dev/) 5 components. For Svelte 3 and 4 support, install `@astrojs/svelte@5` instead.

## Installation

[Section titled “Installation”](#installation)

Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can [install integrations manually](#manual-install) instead.

To install `@astrojs/svelte`, run the following from your project directory and follow the prompts:



* [npm](#tab-panel-3001)
* [pnpm](#tab-panel-3002)
* [Yarn](#tab-panel-3003)

Terminal window

```
npx astro add svelte
```

Terminal window

```
pnpm astro add svelte
```

Terminal window

```
yarn astro add svelte
```



If you run into any issues, [feel free to report them to us on GitHub](https://github.com/withastro/astro/issues) and try the manual installation steps below.

### Manual Install

[Section titled “Manual Install”](#manual-install)

First, install the `@astrojs/svelte` package:

* [npm](#tab-panel-3004)
* [pnpm](#tab-panel-3005)
* [Yarn](#tab-panel-3006)

Terminal window

```
npm install @astrojs/svelte
```

Terminal window

```
pnpm add @astrojs/svelte
```

Terminal window

```
yarn add @astrojs/svelte
```

Most package managers will install associated peer dependencies as well. If you see a `Cannot find package 'svelte'` (or similar) warning when you start up Astro, you’ll need to install Svelte and TypeScript:

* [npm](#tab-panel-3007)
* [pnpm](#tab-panel-3008)
* [Yarn](#tab-panel-3009)

Terminal window

```
npm install svelte typescript
```

Terminal window

```
pnpm add svelte typescript
```

Terminal window

```
yarn add svelte typescript
```

Then, apply the integration to your `astro.config.*` file using the `integrations` property:

astro.config.mjs

```
import { defineConfig } from 'astro/config';



import svelte from '@astrojs/svelte';



export default defineConfig({



// ...



integrations: [svelte()],



});
```

And create a new file called `svelte.config.js` in your project root directory and add the following code:

svelte.config.js

```
import { vitePreprocess } from '@astrojs/svelte';



export default {



preprocess: vitePreprocess(),



}
```

## Getting started

[Section titled “Getting started”](#getting-started)

To use your first Svelte component in Astro, head to our [UI framework documentation](/en/guides/framework-components/#using-framework-components). You’ll explore:

* 📦 how framework components are loaded,
* 💧 client-side hydration options, and
* 🤝 opportunities to mix and nest frameworks together

## Options

[Section titled “Options”](#options)

This integration is powered by `@sveltejs/vite-plugin-svelte`. To customize the Svelte compiler, options can be provided to the integration. See the [`@sveltejs/vite-plugin-svelte` docs](https://github.com/sveltejs/vite-plugin-svelte/blob/HEAD/docs/config.md) for more details.

You can set options either by passing them to the `svelte` integration in `astro.config.mjs` or in `svelte.config.js`. The options in `astro.config.mjs` will take precedence over the options in `svelte.config.js` if both are present:

astro.config.mjs

```
import { defineConfig } from 'astro/config';



import svelte from '@astrojs/svelte';



export default defineConfig({



integrations: [svelte({ extensions: ['.svelte'] })],



});
```

svelte.config.js

```
export default {



extensions: ['.svelte'],



};
```

## Preprocessors

[Section titled “Preprocessors”](#preprocessors)

**Added in:**
`@astrojs/svelte@2.0.0`

If you’re using SCSS or Stylus in your Svelte files, you can create a `svelte.config.js` file so that they are preprocessed by Svelte, and the Svelte IDE extension can correctly parse the Svelte files.

svelte.config.js

```
import { vitePreprocess } from '@astrojs/svelte';



export default {



preprocess: vitePreprocess(),



};
```

This config file will be automatically added for you when you run `astro add svelte`. See the [`@sveltejs/vite-plugin-svelte` docs](https://github.com/sveltejs/vite-plugin-svelte/blob/HEAD/docs/preprocess.md) for more details about `vitePreprocess`.

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

![Scrimba](/_astro/Scrimba.ByZ1pAIN_1PqoUV.webp)
![](/_astro/JamesQuick.BYVczE5K_Z27c5s6.webp)

## **Learn Astro** with James Q Quick

Build your first site with 35 interactive Scrimba lessons

[Get 20% off](https://scrimba.com/intro-to-astro-c00ar0fi5u?via=astro)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/integrations-guide/svelte.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

SolidJS](/en/guides/integrations-guide/solid-js/)
[Next

Vue](/en/guides/integrations-guide/vue/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)