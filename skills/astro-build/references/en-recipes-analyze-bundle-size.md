<!-- Source: https://docs.astro.build/en/recipes/analyze-bundle-size/ -->

# Analyze bundle size

Understanding what is a part of an Astro bundle is important for improving site performance. Visualizing the bundle can give clues as to where changes can be made in your project to reduce the bundle size.

## Recipe

[Section titled “Recipe”](#recipe)

The [`rollup-plugin-visualizer` library](https://github.com/btd/rollup-plugin-visualizer) allows you to visualize and analyze your Rollup bundle to see which modules are taking up space.

1. Install `rollup-plugin-visualizer`:



   * [npm](#tab-panel-1854)
   * [pnpm](#tab-panel-1855)
   * [Yarn](#tab-panel-1856)

   Terminal window

   ```
   npm install rollup-plugin-visualizer --save-dev
   ```

   Terminal window

   ```
   pnpm add rollup-plugin-visualizer --save-dev
   ```

   Terminal window

   ```
   yarn add rollup-plugin-visualizer --save-dev
   ```
2. Add the plugin to the `astro.config.mjs` file:

   ```
   // @ts-check



   import { defineConfig } from 'astro/config';



   import { visualizer } from "rollup-plugin-visualizer";



   export default defineConfig({



   vite: {



   plugins: [visualizer({



   emitFile: true,



   filename: "stats.html",



   })]



   }



   });
   ```
3. Run the build command:

   * [npm](#tab-panel-1857)
   * [pnpm](#tab-panel-1858)
   * [Yarn](#tab-panel-1859)

   Terminal window

   ```
   npm run build
   ```

   Terminal window

   ```
   pnpm build
   ```

   Terminal window

   ```
   yarn build
   ```
4. Find the `stats.html` file(s) for your project.

   This will be at the root of your `dist/` directory for entirely static sites and will allow you to see what is included in the bundle.

   If your Astro project uses on-demand rendering, you will have two `stats.html` files. One will be for the client, and the other for the server, and each will be located at the root of the `dist/client` and `dist/server/` directories.

   See [the Rollup Plugin Visualizer documentation](https://github.com/btd/rollup-plugin-visualizer#how-to-use-generated-files) for guidance on how to interpret these files, or configure specific options.

Note

Given Astro’s unique approach to hydration, the build isn’t necessarily representative of the bundle
that the client will receive.

The Rollup visualizer shows all dependencies that are used across the site, but it does not break down the bundle size on a per-page basis.

Recipes

![](/_astro/CodingInPublic.DpaYu7Qd_5sx41.webp)

## Learn Astro with **Coding in Public**

150+ video lessons
•
Astro v5 ready

[Get 20% off](https://learnastro.dev?code=ASTRO_PROMO)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/recipes/analyze-bundle-size.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Installing a Vite or Rollup plugin](/en/recipes/add-yaml-support/)
[Next

Build a custom image component](/en/recipes/build-custom-img-component/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)