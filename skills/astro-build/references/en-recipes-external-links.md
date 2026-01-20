<!-- Source: https://docs.astro.build/en/recipes/external-links/ -->

# Add icons to external links

Using a rehype plugin, you can identify and modify links in your Markdown files that point to external sites. This example adds icons to the end of each external link, so that visitors will know they are leaving your site.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* An Astro project using Markdown for content pages.

## Recipe

[Section titled “Recipe”](#recipe)

1. Install the `rehype-external-links` plugin.



   * [npm](#tab-panel-1878)
   * [pnpm](#tab-panel-1879)
   * [Yarn](#tab-panel-1880)

   Terminal window

   ```
   npm install rehype-external-links
   ```

   Terminal window

   ```
   pnpm add rehype-external-links
   ```

   Terminal window

   ```
   yarn add rehype-external-links
   ```
2. Import the plugin into your `astro.config.mjs` file.

   Pass `rehypeExternalLinks` to the `rehypePlugins` array, along with an options object that includes a content property. Set this property’s `type` to `text` if you want to add plain text to the end of the link. To add HTML to the end of the link instead, set the property `type` to `raw`.

   ```
   // ...



   import rehypeExternalLinks from 'rehype-external-links';



   export default defineConfig({



   // ...



   markdown: {



   rehypePlugins: [



   [



   rehypeExternalLinks,



   {



   content: { type: 'text', value: ' 🔗' }



   }



   ],



   ]



   },



   });
   ```

   Note

   The value of the `content` property is [not represented in the accessibility tree](https://developer.mozilla.org/en-US/docs/Web/CSS/content#accessibility_concerns). As such, it’s best to make clear that the link is external in the surrounding content, rather than relying on the icon alone.

## Resources

[Section titled “Resources”](#resources)

* [rehype-external-links](https://www.npmjs.com/package/rehype-external-links)

Recipes

![Scrimba](/_astro/Scrimba.ByZ1pAIN_1PqoUV.webp)
![](/_astro/JamesQuick.BYVczE5K_Z27c5s6.webp)

## **Learn Astro** with James Q Quick

Build your first site with 35 interactive Scrimba lessons

[Get 20% off](https://scrimba.com/intro-to-astro-c00ar0fi5u?via=astro)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/recipes/external-links.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Dynamically import images](/en/recipes/dynamically-importing-images/)
[Next

Add i18n features](/en/recipes/i18n/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)