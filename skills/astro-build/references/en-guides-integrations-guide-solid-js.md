<!-- Source: https://docs.astro.build/en/guides/integrations-guide/solid-js/ -->

# @astrojs/ solid-js

v5.1.3
[GitHub](https://github.com/withastro/astro/tree/main/packages/integrations/solid/)
[npm](https://www.npmjs.com/package/@astrojs/solid-js)
[Changelog](https://github.com/withastro/astro/tree/main/packages/integrations/solid/CHANGELOG.md)

This **[Astro integration](/en/guides/integrations-guide/)** enables rendering and client-side hydration for your [SolidJS](https://www.solidjs.com/) components.

## Installation

[Section titled “Installation”](#installation)

Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can [install integrations manually](#manual-install) instead.

To install `@astrojs/solid-js`, run the following from your project directory and follow the prompts:



* [npm](#tab-panel-2989)
* [pnpm](#tab-panel-2990)
* [Yarn](#tab-panel-2991)

Terminal window

```
npx astro add solid
```

Terminal window

```
pnpm astro add solid
```

Terminal window

```
yarn astro add solid
```



If you run into any issues, [feel free to report them to us on GitHub](https://github.com/withastro/astro/issues) and try the manual installation steps below.

### Manual Install

[Section titled “Manual Install”](#manual-install)

First, install the `@astrojs/solid-js` package:

* [npm](#tab-panel-2992)
* [pnpm](#tab-panel-2993)
* [Yarn](#tab-panel-2994)

Terminal window

```
npm install @astrojs/solid-js
```

Terminal window

```
pnpm add @astrojs/solid-js
```

Terminal window

```
yarn add @astrojs/solid-js
```

Most package managers will install associated peer dependencies as well. If you see a `Cannot find package 'solid-js'` (or similar) warning when you start up Astro, you’ll need to install SolidJS:

* [npm](#tab-panel-2995)
* [pnpm](#tab-panel-2996)
* [Yarn](#tab-panel-2997)

Terminal window

```
npm install solid-js
```

Terminal window

```
pnpm add solid-js
```

Terminal window

```
yarn add solid-js
```

Then, apply the integration to your `astro.config.*` file using the `integrations` property:

astro.config.mjs

```
import { defineConfig } from 'astro/config';



import solidJs from '@astrojs/solid-js';



export default defineConfig({



// ...



integrations: [solidJs()],



});
```

And add the following code to the `tsconfig.json` file.

tsconfig.json

```
{



"extends": "astro/tsconfigs/strict",



"include": [".astro/types.d.ts", "**/*"],



"exclude": ["dist"],



"compilerOptions": {



"jsx": "preserve",



"jsxImportSource": "solid-js"



}



}
```

## Getting started

[Section titled “Getting started”](#getting-started)

To use your first SolidJS component in Astro, head to our [UI framework documentation](/en/guides/framework-components/#using-framework-components). You’ll explore:

* 📦 how framework components are loaded,
* 💧 client-side hydration options, and
* 🤝 opportunities to mix and nest frameworks together

## Configuration

[Section titled “Configuration”](#configuration)

### `devtools`

[Section titled “devtools”](#devtools)

**Type:** `boolean`

**Added in:**
`@astrojs/solid-js@4.2.0`

You can enable [Solid DevTools](https://github.com/thetarnav/solid-devtools) in development by passing an object with `devtools: true` to your `solid()` integration config and adding `solid-devtools` to your project dependencies:

* [npm](#tab-panel-2998)
* [pnpm](#tab-panel-2999)
* [Yarn](#tab-panel-3000)

Terminal window

```
npm install solid-devtools
```

Terminal window

```
pnpm add solid-devtools
```

Terminal window

```
yarn add solid-devtools
```

astro.config.mjs

```
import { defineConfig } from 'astro/config';



import solid from '@astrojs/solid-js';



export default defineConfig({



// ...



integrations: [solid({ devtools: true })],



});
```

## Options

[Section titled “Options”](#options)

### Combining multiple JSX frameworks

[Section titled “Combining multiple JSX frameworks”](#combining-multiple-jsx-frameworks)

When you are using multiple JSX frameworks (React, Preact, Solid) in the same project, Astro needs to determine which JSX framework-specific transformations should be used for each of your components. If you have only added one JSX framework integration to your project, no extra configuration is needed.

Use the `include` (required) and `exclude` (optional) configuration options to specify which files belong to which framework. Provide an array of files and/or folders to `include` for each framework you are using. Wildcards may be used to include multiple file paths.

We recommend placing common framework components in the same folder (e.g. `/components/react/` and `/components/solid/`) to make specifying your includes easier, but this is not required:

astro.config.mjs

```
import { defineConfig } from 'astro/config';



import preact from '@astrojs/preact';



import react from '@astrojs/react';



import svelte from '@astrojs/svelte';



import vue from '@astrojs/vue';



import solid from '@astrojs/solid-js';



export default defineConfig({



// Enable many frameworks to support all different kinds of components.



// No `include` is needed if you are only using a single JSX framework!



integrations: [



preact({



include: ['**/preact/*'],



}),



react({



include: ['**/react/*'],



}),



solid({



include: ['**/solid/*', '**/node_modules/@suid/material/**'],



}),



],



});
```

## Usage

[Section titled “Usage”](#usage)

Use a SolidJS component as you would any [UI framework component](/en/guides/framework-components/).

### Suspense Boundaries

[Section titled “Suspense Boundaries”](#suspense-boundaries)

In order to support Solid Resources and Lazy Components without excessive configuration, server-only and hydrating components are automatically wrapped in top-level Suspense boundaries and rendered on the server using the [`renderToStringAsync`](https://www.solidjs.com/docs/latest/api#rendertostringasync) function. Therefore, you do not need to add a top-level Suspense boundary around async components.

For example, you can use Solid’s [`createResource`](https://www.solidjs.com/docs/latest/api#createresource) to fetch async remote data on the server. The remote data will be included in the initial server-rendered HTML from Astro:

CharacterName.tsx

```
function CharacterName() {



const [name] = createResource(() =>



fetch('https://swapi.dev/api/people/1')



.then((result) => result.json())



.then((data) => data.name)



);



return (



<>



<h2>Name:</h2>



{/* Luke Skywalker */}



<div>{name()}</div>



</>



);



}
```

Similarly, Solid’s [Lazy Components](https://www.solidjs.com/docs/latest/api#lazy) will also be resolved and their HTML will be included in the initial server-rendered page.

Non-hydrating [`client:only` components](/en/reference/directives-reference/#clientonly) are not automatically wrapped in Suspense boundaries.

Feel free to add additional Suspense boundaries according to your preference.

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

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/integrations-guide/solid-js.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

React](/en/guides/integrations-guide/react/)
[Next

Svelte](/en/guides/integrations-guide/svelte/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)