<!-- Source: https://docs.astro.build/en/recipes/add-yaml-support/ -->

# Installing a Vite or Rollup plugin

Astro builds on top of Vite, and supports both Vite and Rollup plugins. This recipe uses a Rollup plugin to add the ability to import a YAML (`.yml`) file in Astro.

## Recipe

[Section titled “Recipe”](#recipe)

1. Install `@rollup/plugin-yaml`:



   * [npm](#tab-panel-1851)
   * [pnpm](#tab-panel-1852)
   * [Yarn](#tab-panel-1853)

   Terminal window

   ```
   npm install @rollup/plugin-yaml --save-dev
   ```

   Terminal window

   ```
   pnpm add @rollup/plugin-yaml --save-dev
   ```

   Terminal window

   ```
   yarn add @rollup/plugin-yaml --dev
   ```
2. Import the plugin in your `astro.config.mjs` and add it to the Vite plugins array:

   astro.config.mjs

   ```
   import { defineConfig } from 'astro/config';



   import yaml from '@rollup/plugin-yaml';



   export default defineConfig({



   vite: {



   plugins: [yaml()]



   }



   });
   ```
3. Finally, you can import YAML data using an `import` statement:

   ```
   import yml from './data.yml';
   ```

   Note

   While you can now import YAML data in your Astro project, your editor will not provide types for the imported data. To add types, create or find an existing `*.d.ts` file in the `src` directory of your project and add the following:

   src/files.d.ts

   ```
   // Specify the file extension you want to import



   declare module "*.yml" {



   const value: any; // Add type definitions here if desired



   export default value;



   }
   ```

   This will allow your editor to provide type hints for your YAML data.

Recipes

![](/_astro/CodingInPublic.DpaYu7Qd_5sx41.webp)

## Learn Astro with **Coding in Public**

150+ video lessons
•
Astro v5 ready

[Get 20% off](https://learnastro.dev?code=ASTRO_PROMO)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/recipes/add-yaml-support.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Recipes overview](/en/recipes/)
[Next

Analyze bundle size](/en/recipes/analyze-bundle-size/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)