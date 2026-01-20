<!-- Source: https://docs.astro.build/en/recipes/tailwind-rendered-markdown/ -->

# Style rendered Markdown with Tailwind Typography

You can use [Tailwind](https://tailwindcss.com)’s Typography plugin to style rendered Markdown from sources such as Astro’s [**content collections**](/en/guides/content-collections/).

This recipe will teach you how to create a reusable Astro component to style your Markdown content using Tailwind’s utility classes.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

An Astro project that:

* has [Tailwind’s Vite plugin](/en/guides/styling/#tailwind) installed.
* uses Astro’s [content collections](/en/guides/content-collections/).

## Setting Up `@tailwindcss/typography`

[Section titled “Setting Up @tailwindcss/typography”](#setting-up-tailwindcsstypography)

First, install `@tailwindcss/typography` using your preferred package manager.



* [npm](#tab-panel-1932)
* [pnpm](#tab-panel-1933)
* [Yarn](#tab-panel-1934)

Terminal window

```
npm install -D @tailwindcss/typography
```

Terminal window

```
pnpm add -D @tailwindcss/typography
```

Terminal window

```
yarn add --dev @tailwindcss/typography
```



Then, add the package as a plugin in your Tailwind configuration file.

src/styles/global.css

```
@import 'tailwindcss';



@plugin '@tailwindcss/typography';
```

## Recipe

[Section titled “Recipe”](#recipe)

1. Create a `<Prose />` component to provide a wrapping `<div>` with a `<slot />` for your rendered Markdown. Add the style class `prose` alongside any desired [Tailwind element modifiers](https://tailwindcss.com/docs/typography-plugin#element-modifiers) in the parent element.

   src/components/Prose.astro

   ```
   ---



   ---



   <div



   class="prose dark:prose-invert



   prose-h1:font-bold prose-h1:text-xl



   prose-a:text-blue-600 prose-p:text-justify prose-img:rounded-xl



   prose-headings:underline">



   <slot />



   </div>
   ```

   Tip

   The `@tailwindcss/typography` plugin uses [**element modifiers**](https://tailwindcss.com/docs/typography-plugin#element-modifiers) to style child components of a container with the `prose` class.

   These modifiers follow the following general syntax:

   ```
   prose-[element]:class-to-apply
   ```

   For example, `prose-h1:font-bold` gives all `<h1>` tags the `font-bold` Tailwind class.
2. Query your collection entry on the page you want to render your Markdown. Pass the `<Content />` component from `await render(entry)` to `<Prose />` as a child to wrap your Markdown content in Tailwind styles.

   src/pages/index.astro

   ```
   ---



   import Prose from '../components/Prose.astro';



   import Layout from '../layouts/Layout.astro';



   import { getEntry, render } from 'astro:content';



   const entry = await getEntry('collection', 'entry');



   const { Content } = await render(entry);



   ---



   <Layout>



   <Prose>



   <Content />



   </Prose>



   </Layout>
   ```

## Resources

[Section titled “Resources”](#resources)

* [Tailwind Typography Documentation](https://tailwindcss.com/docs/typography-plugin)

Recipes

![Scrimba](/_astro/Scrimba.ByZ1pAIN_1PqoUV.webp)
![](/_astro/JamesQuick.BYVczE5K_Z27c5s6.webp)

## **Learn Astro** with James Q Quick

Build your first site with 35 interactive Scrimba lessons

[Get 20% off](https://scrimba.com/intro-to-astro-c00ar0fi5u?via=astro)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/recipes/tailwind-rendered-markdown.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Using streaming to improve page performance](/en/recipes/streaming-improve-page-performance/)
[Next

Contribute to Astro](/en/contribute/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)