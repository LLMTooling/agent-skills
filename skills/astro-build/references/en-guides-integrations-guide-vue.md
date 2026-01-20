<!-- Source: https://docs.astro.build/en/guides/integrations-guide/vue/ -->

# @astrojs/ vue

v5.1.4
[GitHub](https://github.com/withastro/astro/tree/main/packages/integrations/vue/)
[npm](https://www.npmjs.com/package/@astrojs/vue)
[Changelog](https://github.com/withastro/astro/tree/main/packages/integrations/vue/CHANGELOG.md)

This **[Astro integration](/en/guides/integrations-guide/)** enables rendering and client-side hydration for your [Vue 3](https://vuejs.org/) components.

## Installation

[Section titled “Installation”](#installation)

Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can [install integrations manually](#manual-install) instead.

To install `@astrojs/vue`, run the following from your project directory and follow the prompts:



* [npm](#tab-panel-3019)
* [pnpm](#tab-panel-3020)
* [Yarn](#tab-panel-3021)

Terminal window

```
npx astro add vue
```

Terminal window

```
pnpm astro add vue
```

Terminal window

```
yarn astro add vue
```



If you run into any issues, [feel free to report them to us on GitHub](https://github.com/withastro/astro/issues) and try the manual installation steps below.

### Manual Install

[Section titled “Manual Install”](#manual-install)

First, install the `@astrojs/vue` package:

* [npm](#tab-panel-3022)
* [pnpm](#tab-panel-3023)
* [Yarn](#tab-panel-3024)

Terminal window

```
npm install @astrojs/vue
```

Terminal window

```
pnpm add @astrojs/vue
```

Terminal window

```
yarn add @astrojs/vue
```

Most package managers will install associated peer dependencies as well. If you see a `Cannot find package 'vue'` (or similar) warning when you start up Astro, you’ll need to install Vue:

* [npm](#tab-panel-3025)
* [pnpm](#tab-panel-3026)
* [Yarn](#tab-panel-3027)

Terminal window

```
npm install vue
```

Terminal window

```
pnpm add vue
```

Terminal window

```
yarn add vue
```

Then, apply the integration to your `astro.config.*` file using the `integrations` property:

astro.config.mjs

```
import { defineConfig } from 'astro/config';



import vue from '@astrojs/vue';



export default defineConfig({



// ...



integrations: [vue()],



});
```

## Getting started

[Section titled “Getting started”](#getting-started)

To use your first Vue component in Astro, head to our [UI framework documentation](/en/guides/framework-components/#using-framework-components). You’ll explore:

* 📦 how framework components are loaded,
* 💧 client-side hydration options, and
* 🤝 opportunities to mix and nest frameworks together

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

For help, check out the `#support` channel on [Discord](https://astro.build/chat). Our friendly Support Squad members are here to help!

You can also check our [Astro Integration Documentation](/en/guides/integrations-guide/) for more on integrations.

## Contributing

[Section titled “Contributing”](#contributing)

This package is maintained by Astro’s Core team. You’re welcome to submit an issue or PR!

## Options

[Section titled “Options”](#options)

This integration is powered by `@vitejs/plugin-vue`. To customize the Vue compiler, options can be provided to the integration. See the `@vitejs/plugin-vue` [docs](https://www.npmjs.com/package/@vitejs/plugin-vue) for more details.

astro.config.mjs

```
import { defineConfig } from 'astro/config';



import vue from '@astrojs/vue';



export default defineConfig({



// ...



integrations: [



vue({



template: {



compilerOptions: {



// treat any tag that starts with ion- as custom elements



isCustomElement: (tag) => tag.startsWith('ion-'),



},



},



// ...



}),



],



});
```

### `appEntrypoint`

[Section titled “appEntrypoint”](#appentrypoint)

**Type:** `string`

**Added in:**
`@astrojs/vue@1.2.0`

You can extend the Vue `app` instance setting the `appEntrypoint` option to a root-relative import specifier (for example, `appEntrypoint: "/src/pages/_app"`).

The default export of this file should be a function that accepts a Vue `App` instance prior to rendering, allowing the use of [custom Vue plugins](https://vuejs.org/guide/reusability/plugins.html), `app.use`, and other customizations for advanced use cases.

astro.config.mjs

```
import { defineConfig } from 'astro/config';



import vue from '@astrojs/vue';



export default defineConfig({



// ...



integrations: [vue({ appEntrypoint: '/src/pages/_app' })],



});
```

src/pages/\_app.ts

```
import type { App } from 'vue';



import i18nPlugin from 'my-vue-i18n-plugin';



export default (app: App) => {



app.use(i18nPlugin);



};
```

### `jsx`

[Section titled “jsx”](#jsx)

**Type:** `boolean | object`

**Added in:**
`@astrojs/vue@1.2.0`

You can use Vue JSX by setting `jsx: true`.

astro.config.mjs

```
import { defineConfig } from 'astro/config';



import vue from '@astrojs/vue';



export default defineConfig({



// ...



integrations: [vue({ jsx: true })],



});
```

This will enable rendering for both Vue and Vue JSX components. To customize the Vue JSX compiler, pass an options object instead of a boolean. See the `@vitejs/plugin-vue-jsx` [docs](https://www.npmjs.com/package/@vitejs/plugin-vue-jsx) for more details.

astro.config.mjs

```
import { defineConfig } from 'astro/config';



import vue from '@astrojs/vue';



export default defineConfig({



// ...



integrations: [



vue({



jsx: {



// treat any tag that starts with ion- as custom elements



isCustomElement: (tag) => tag.startsWith('ion-'),



},



}),



],



});
```

### `devtools`

[Section titled “devtools”](#devtools)

**Type:** `boolean | object`

**Added in:**
`@astrojs/vue@4.2.0`

You can enable [Vue DevTools](https://devtools-next.vuejs.org/) in development by passing an object with `devtools: true` to your `vue()` integration config:

astro.config.mjs

```
import { defineConfig } from 'astro/config';



import vue from '@astrojs/vue';



export default defineConfig({



// ...



integrations: [vue({ devtools: true })],



});
```

#### Customizing Vue DevTools

[Section titled “Customizing Vue DevTools”](#customizing-vue-devtools)

**Added in:**
`@astrojs/vue@4.3.0`

For more customization, you can instead pass options that the [Vue DevTools Vite Plugin](https://devtools-next.vuejs.org/guide/vite-plugin#options) supports. (Note: `appendTo` is not supported.)

For example, you can set `launchEditor` to your preferred editor if you are not using Visual Studio Code:

astro.config.mjs

```
import { defineConfig } from "astro/config";



import vue from "@astrojs/vue";



export default defineConfig({



// ...



integrations: [



vue({



devtools: { launchEditor: "webstorm" },



}),



],



});
```

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

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/integrations-guide/vue.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Svelte](/en/guides/integrations-guide/svelte/)
[Next

Cloudflare](/en/guides/integrations-guide/cloudflare/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)