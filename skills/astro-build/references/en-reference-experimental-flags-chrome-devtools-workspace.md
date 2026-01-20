<!-- Source: https://docs.astro.build/en/reference/experimental-flags/chrome-devtools-workspace/ -->

# Experimental Chrome DevTools workspace

**Type:** `boolean`
**Default:** `false`

**Added in:**
`astro@5.13.0`

Enables experimental [Chrome DevTools workspace integration](https://developer.chrome.com/docs/devtools/workspaces) for the Astro dev server.

This feature allows you to edit files directly in Chrome DevTools and have those changes reflected in your local file system via a connected workspace folder. This is useful for applying edits such as adjusting CSS values without leaving your browser tab.

With this feature enabled, running `astro dev` will automatically configure a Chrome DevTools workspace for your project. Your project will then appear as an available [workspace source that you can connect](#connecting-your-project). Then, changes that you make in the “Sources” panel are automatically saved to your project source code.

To enable this feature, add the experimental flag `chromeDevtoolsWorkspace` to your Astro config:

astro.config.mjs

```
import { defineConfig } from 'astro/config';



export default defineConfig({



experimental: {



chromeDevtoolsWorkspace: true,



},



});
```

## Connecting your project

[Section titled “Connecting your project”](#connecting-your-project)

Astro will create the necessary configuration file to support Chrome DevTools workspaces. However, your project must also be [connected as a source](https://developer.chrome.com/docs/devtools/workspaces#manual-connection) to enable file saving.

1. [Start the Astro dev server](/en/develop-and-build/#start-the-astro-dev-server) with the appropriate CLI command for your package manager.
2. Navigate to your site preview (e.g. `http://localhost:4321/`) in Chrome and open DevTools.
3. Under the **Sources** > **Workspaces** tab, you will find your Astro project folder. Click **Connect** to add your directory as a workspace.

See the [Chrome DevTools workspace documentation](https://developer.chrome.com/docs/devtools/workspaces#connect) for more information.

Reference

![Scrimba](/_astro/Scrimba.ByZ1pAIN_1PqoUV.webp)
![](/_astro/JamesQuick.BYVczE5K_Z27c5s6.webp)

## **Learn Astro** with James Q Quick

Build your first site with 35 interactive Scrimba lessons

[Get 20% off](https://scrimba.com/intro-to-astro-c00ar0fi5u?via=astro)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/reference/experimental-flags/chrome-devtools-workspace.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Private meta environment variables inlining](/en/reference/experimental-flags/static-import-meta-env/)
[Next

Prerender conflict error](/en/reference/experimental-flags/fail-on-prerender-conflict/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)