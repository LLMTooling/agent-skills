<!-- Source: https://docs.astro.build/en/recipes/modified-time/ -->

# Add last modified time

Learn how to build a [remark plugin](https://github.com/remarkjs/remark) that adds the last modified time to the frontmatter of your Markdown and MDX files. Use this property to display the modified time in your pages.

Uses Git history

This recipe calculates time based on your repository’s Git history and may not be accurate on some deployment platforms. Your host may be performing **shallow clones** which do not retrieve the full git history.

## Recipe

[Section titled “Recipe”](#recipe)

1. Install Helper Packages

   Install [`Day.js`](https://www.npmjs.com/package/dayjs) to modify and format times:



   * [npm](#tab-panel-1894)
   * [pnpm](#tab-panel-1895)
   * [Yarn](#tab-panel-1896)

   Terminal window

   ```
   npm install dayjs
   ```

   Terminal window

   ```
   pnpm add dayjs
   ```

   Terminal window

   ```
   yarn add dayjs
   ```
2. Create a Remark Plugin

   This plugin uses `execSync` to run a Git command that returns the timestamp of the latest commit in ISO 8601 format. The timestamp is then added to the frontmatter of the file.

   remark-modified-time.mjs

   ```
   import { execSync } from "child_process";



   export function remarkModifiedTime() {



   return function (tree, file) {



   const filepath = file.history[0];



   const result = execSync(`git log -1 --pretty="format:%cI" "${filepath}"`);



   file.data.astro.frontmatter.lastModified = result.toString();



   };



   }
   ```

   Using the file system instead of Git

   Although using Git is the recommended way to get the last modified timestamp from a file, it is possible to use the file system modified time.
   This plugin uses `statSync` to get the `mtime` (modified time) of the file in ISO 8601 format. The timestamp is then added to the frontmatter of the file.

   remark-modified-time.mjs

   ```
   import { statSync } from "fs";



   export function remarkModifiedTime() {



   return function (tree, file) {



   const filepath = file.history[0];



   const result = statSync(filepath);



   file.data.astro.frontmatter.lastModified = result.mtime.toISOString();



   };



   }
   ```
3. Add the plugin to your config

   astro.config.mjs

   ```
   import { defineConfig } from 'astro/config';



   import { remarkModifiedTime } from './remark-modified-time.mjs';



   export default defineConfig({



   markdown: {



   remarkPlugins: [remarkModifiedTime],



   },



   });
   ```

   Now all Markdown documents will have a `lastModified` property in their frontmatter.
4. Display Last Modified Time

   If your content is stored in a [content collection](/en/guides/content-collections/), access the `remarkPluginFrontmatter` from the `render(entry)` function. Then render `lastModified` in your template wherever you would like it to appear.

   src/pages/posts/[slug].astro

   ```
   ---



   import { getCollection, render } from 'astro:content';



   import dayjs from "dayjs";



   import utc from "dayjs/plugin/utc";



   dayjs.extend(utc);



   export async function getStaticPaths() {



   const blog = await getCollection('blog');



   return blog.map(entry => ({



   params: { slug: entry.id },



   props: { entry },



   }));



   }



   const { entry } = Astro.props;



   const { Content, remarkPluginFrontmatter } = await render(entry);



   const lastModified = dayjs(remarkPluginFrontmatter.lastModified)



   .utc()



   .format("HH:mm:ss DD MMMM YYYY UTC");



   ---



   <html>



   <head>...</head>



   <body>



   ...



   <p>Last Modified: {lastModified}</p>



   ...



   </body>



   </html>
   ```

   If you’re using a [Markdown layout](/en/basics/layouts/#markdown-layouts), use the `lastModified` frontmatter property from `Astro.props` in your layout template.

   src/layouts/BlogLayout.astro

   ```
   ---



   import dayjs from "dayjs";



   import utc from "dayjs/plugin/utc";



   dayjs.extend(utc);



   const lastModified = dayjs()



   .utc(Astro.props.frontmatter.lastModified)



   .format("HH:mm:ss DD MMMM YYYY UTC");



   ---



   <html>



   <head>...</head>



   <body>



   <p>{lastModified}</p>



   <slot />



   </body>



   </html>
   ```

Recipes

![](/_astro/CodingInPublic.DpaYu7Qd_5sx41.webp)

## Learn Astro with **Coding in Public**

150+ video lessons
•
Astro v5 ready

[Get 20% off](https://learnastro.dev?code=ASTRO_PROMO)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/recipes/modified-time.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Create a dev toolbar app](/en/recipes/making-toolbar-apps/)
[Next

Add reading time](/en/recipes/reading-time/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)