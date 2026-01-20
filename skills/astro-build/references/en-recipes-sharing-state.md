<!-- Source: https://docs.astro.build/en/recipes/sharing-state/ -->

# Share state between Astro components

Tip

Using framework components? See [how to share state between Islands](/en/recipes/sharing-state-islands/)!

When building an Astro website, you may need to share state across components. Astro recommends the use of [Nano Stores](https://github.com/nanostores/nanostores) for shared client storage.

## Recipe

[Section titled “Recipe”](#recipe)

1. Install Nano Stores:



   * [npm](#tab-panel-1929)
   * [pnpm](#tab-panel-1930)
   * [Yarn](#tab-panel-1931)

   Terminal window

   ```
   npm install nanostores
   ```

   Terminal window

   ```
   pnpm add nanostores
   ```

   Terminal window

   ```
   yarn add nanostores
   ```
2. Create a store. In this example, the store tracks whether a dialog is open or not:

   src/store.js

   ```
   import { atom } from 'nanostores';



   export const isOpen = atom(false);
   ```
3. Import and use the store in a `<script>` tag in the components that will share state.

   The following `Button` and `Dialog` components each use the shared `isOpen` state to control whether a particular `<div>` is hidden or displayed:

   src/components/Button.astro

   ```
   <button id="openDialog">Open</button>



   <script>



   import { isOpen } from '../store.js';



   // Set the store to true when the button is clicked



   function openDialog() {



   isOpen.set(true);



   }



   // Add an event listener to the button



   document.getElementById('openDialog').addEventListener('click', openDialog);



   </script>
   ```

   src/components/Dialog.astro

   ```
   <div id="dialog" style="display: none">Hello world!</div>



   <script>



   import { isOpen } from '../store.js';



   // Listen to changes in the store, and show/hide the dialog accordingly



   isOpen.subscribe(open => {



   if (open) {



   document.getElementById('dialog').style.display = 'block';



   } else {



   document.getElementById('dialog').style.display = 'none';



   }



   })



   </script>
   ```

## Resources

[Section titled “Resources”](#resources)

* [Nano Stores on NPM](https://www.npmjs.com/package/nanostores)
* [Nano Stores documentation for Vanilla JS](https://github.com/nanostores/nanostores#vanilla-js)

Recipes

![](/_astro/CodingInPublic.DpaYu7Qd_5sx41.webp)

## Learn Astro with **Coding in Public**

150+ video lessons
•
Astro v5 ready

[Get 20% off](https://learnastro.dev?code=ASTRO_PROMO)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/recipes/sharing-state.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Add an RSS feed](/en/recipes/rss/)
[Next

Share state between islands](/en/recipes/sharing-state-islands/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)