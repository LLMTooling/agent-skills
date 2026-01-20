<!-- Source: https://docs.astro.build/en/guides/deploy/cloudflare/ -->

# Deploy your Astro Site to Cloudflare

You can deploy full-stack applications, including front-end static assets and back-end APIs, as well as on-demand rendered sites, to both [Cloudflare Workers](https://developers.cloudflare.com/workers/static-assets/) and [Cloudflare Pages](https://pages.cloudflare.com/).

This guide includes:

* [How to deploy to Cloudflare Workers](#cloudflare-workers)
* [How to deploy to Cloudflare Pages](#cloudflare-pages)

Note

Cloudflare recommends using Cloudflare Workers for new projects. For existing Pages projects, refer to [Cloudflare’s migration guide](https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/) and [compatibility matrix](https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/#compatibility-matrix).

Read more about [using the Cloudflare runtime](/en/guides/integrations-guide/cloudflare/) in your Astro project.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need:

* A Cloudflare account. If you don’t already have one, you can create a free Cloudflare account during the process.

## Cloudflare Workers

[Section titled “Cloudflare Workers”](#cloudflare-workers)

### How to deploy with Wrangler

[Section titled “How to deploy with Wrangler”](#how-to-deploy-with-wrangler)

1. Install [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/get-started/).

   Terminal window

   ```
   npm install wrangler@latest --save-dev
   ```
2. If your site uses on-demand rendering, install the [`@astrojs/cloudflare` adapter](/en/guides/integrations-guide/cloudflare/).

   This will install the adapter and make the appropriate changes to your `astro.config.mjs` file in one step.

   * [npm](#tab-panel-2796)
   * [pnpm](#tab-panel-2797)
   * [Yarn](#tab-panel-2798)

   Terminal window

   ```
   npx astro add cloudflare
   ```

   Terminal window

   ```
   pnpm astro add cloudflare
   ```

   Terminal window

   ```
   yarn astro add cloudflare
   ```

   Read more about [on-demand rendering in Astro](/en/guides/on-demand-rendering/).
3. Create a [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/).

   Running `astro add cloudflare` will create this for you; if you are not using the adapter, you’ll need to create it yourself.



   * [Static](#tab-panel-2792)
   * [On demand](#tab-panel-2793)

   wrangler.jsonc

   ```
   {



   "name": "my-astro-app",



   "compatibility_date": "YYYY-MM-DD", // Update to the day you deploy



   "assets": {



   "directory": "./dist",



   }



   }
   ```

   wrangler.jsonc

   ```
   {



   "main": "dist/_worker.js/index.js",



   "name": "my-astro-app",



   "compatibility_date": "YYYY-MM-DD", // Update to the day you deploy



   "compatibility_flags": [



   "nodejs_compat",



   "global_fetch_strictly_public"



   ],



   "assets": {



   "binding": "ASSETS",



   "directory": "./dist"



   },



   "observability": {



   "enabled": true



   }



   }
   ```
4. Preview your project locally with Wrangler.

   Terminal window

   ```
   npx astro build && npx wrangler dev
   ```
5. Deploy using `npx wrangler deploy`.

   Terminal window

   ```
   npx astro build && npx wrangler deploy
   ```

After your assets are uploaded, Wrangler will give you a preview URL to inspect your site.

Read more about using [Cloudflare runtime APIs](/en/guides/integrations-guide/cloudflare/) such as bindings.

### How to deploy with CI/CD

[Section titled “How to deploy with CI/CD”](#how-to-deploy-with-cicd)

You can also use a CI/CD system such as [Workers Builds (BETA)](https://developers.cloudflare.com/workers/ci-cd/builds/) to automatically build and deploy your site on push.

If you’re using Workers Builds:

1. Follow Steps 1-3 from the Wrangler section above.
2. Log in to the [Cloudflare dashboard](https://dash.cloudflare.com/) and navigate to `Workers & Pages`. Select `Create`.
3. Under `Import a repository`, select a Git account and then the repository containing your Astro project.
4. Configure your project with:

   * Build command: `npx astro build`
   * Deploy command: `npx wrangler deploy`
5. Click `Save and Deploy`. You can now preview your Worker at its provided `workers.dev` subdomain.

## Cloudflare Pages

[Section titled “Cloudflare Pages”](#cloudflare-pages)

### How to deploy with Wrangler

[Section titled “How to deploy with Wrangler”](#how-to-deploy-with-wrangler-1)

1. Install [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/get-started/).

   * [npm](#tab-panel-2799)
   * [pnpm](#tab-panel-2800)
   * [Yarn](#tab-panel-2801)

   Terminal window

   ```
   npm install wrangler@latest --save-dev
   ```

   Terminal window

   ```
   pnpm add wrangler@latest --save-dev
   ```

   Terminal window

   ```
   yarn add wrangler@latest --dev
   ```
2. If your site uses on-demand rendering, install the [`@astrojs/cloudflare` adapter](/en/guides/integrations-guide/cloudflare/).

   This will install the adapter and make the appropriate changes to your `astro.config.mjs` file in one step.

   * [npm](#tab-panel-2802)
   * [pnpm](#tab-panel-2803)
   * [Yarn](#tab-panel-2804)

   Terminal window

   ```
   npx astro add cloudflare
   ```

   Terminal window

   ```
   pnpm astro add cloudflare
   ```

   Terminal window

   ```
   yarn astro add cloudflare
   ```
3. Create a [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/).

   Because Cloudflare recommends new projects use Workers instead of Pages, the `astro add cloudflare` command creates a `wrangler.jsonc` and `public/.assetsignore` file, which are specific to Workers projects. You will need to delete the `public/.assetsignore` file and change your `wrangler.jsonc` file. If you are not using the adapter you’ll need to create it yourself.

   Ensure your `wrangler.jsonc` file is structured like this:

   * [Static](#tab-panel-2794)
   * [On demand](#tab-panel-2795)

   wrangler.jsonc

   ```
   {



   "name": "my-astro-app",



   "compatibility_date": "YYYY-MM-DD", // Update to the day you deploy



   "pages_build_output_dir": "./dist"



   }
   ```

   wrangler.jsonc

   ```
   {



   "name": "my-astro-app",



   "compatibility_date": "YYYY-MM-DD", // Update to the day you deploy



   "compatibility_flags": [



   "nodejs_compat",



   "disable_nodejs_process_v2"



   ],



   "pages_build_output_dir": "./dist"



   }
   ```

   Read more about [on-demand rendering in Astro](/en/guides/on-demand-rendering/).
4. Preview your project locally with Wrangler.

   * [npm](#tab-panel-2805)
   * [pnpm](#tab-panel-2806)
   * [Yarn](#tab-panel-2807)

   Terminal window

   ```
   npx astro build && wrangler pages dev ./dist
   ```

   Terminal window

   ```
   pnpm astro build && wrangler pages dev ./dist
   ```

   Terminal window

   ```
   yarn astro build && wrangler pages dev ./dist
   ```
5. Deploy using `npx wrangler deploy`.

   * [npm](#tab-panel-2808)
   * [pnpm](#tab-panel-2809)
   * [Yarn](#tab-panel-2810)

   Terminal window

   ```
   npx astro build && wrangler pages deploy ./dist
   ```

   Terminal window

   ```
   pnpm astro build && wrangler pages deploy ./dist
   ```

   Terminal window

   ```
   yarn astro build && wrangler pages deploy ./dist
   ```

After your assets are uploaded, Wrangler will give you a preview URL to inspect your site.

### How to deploy a site with CI/CD

[Section titled “How to deploy a site with CI/CD”](#how-to-deploy-a-site-with-cicd)

1. Push your code to your git repository (e.g. GitHub, GitLab).
2. Log in to the [Cloudflare dashboard](https://dash.cloudflare.com/) and navigate to **Compute (Workers) > Workers & Pages**. Select **Create** and then select the **Pages** tab. Connect your git repository.
3. Configure your project with:

   * **Framework preset**: `Astro`
   * **Build command:** `npm run build`
   * **Build output directory:** `dist`
4. Click the **Save and Deploy** button.

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

### 404 behavior

[Section titled “404 behavior”](#404-behavior)

For Workers projects, you will need to set `not_found_handling` if you want to serve a custom 404 page. You can read more about this in the [Routing behavior section](https://developers.cloudflare.com/workers/static-assets/#routing-behavior) of Cloudflare’s documentation.

wrangler.jsonc

```
{



"assets": {



"directory": "./dist",



"not_found_handling": "404-page"



}



}
```

For Pages projects, if you include a custom 404 page, it will be served by default. Otherwise, Pages will default to [Cloudflare’s single-page application rendering behavior](https://developers.cloudflare.com/pages/configuration/serving-pages/#single-page-application-spa-rendering) and redirect to the home page instead of showing a 404 page.

### Client-side hydration

[Section titled “Client-side hydration”](#client-side-hydration)

Client-side hydration may fail as a result of Cloudflare’s Auto Minify setting. If you see `Hydration completed but contains mismatches` in the console, make sure to disable Auto Minify under Cloudflare settings.

### Node.js runtime APIs

[Section titled “Node.js runtime APIs”](#nodejs-runtime-apis)

If you are building a project that is using on-demand rendering with [the Cloudflare adapter](/en/guides/integrations-guide/cloudflare/) and the server fails to build with an error message such as `[Error] Could not resolve "XXXX. The package "XXXX" wasn't found on the file system but is built into node.`:

* This means that a package or import you are using in the server-side environment is not compatible with the [Cloudflare runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/nodejs/).
* If you are directly importing a Node.js runtime API, please refer to the Astro documentation on Cloudflare’s [Node.js compatibility](/en/guides/integrations-guide/cloudflare/#nodejs-compatibility) for further steps on how to resolve this.
* If you are importing a package that imports a Node.js runtime API, check with the author of the package to see if they support the `node:*` import syntax. If they do not, you may need to find an alternative package.

## More Deployment Guides

* ![](/logos/aws.svg)

  ### [AWS](/en/guides/deploy/aws/)
* ![](/logos/flightcontrol.svg)

  ### [AWS via Flightcontrol](/en/guides/deploy/aws-via-flightcontrol/)
* ![](/logos/sst.svg)

  ### [AWS via SST](/en/guides/deploy/aws-via-sst/)
* ![](/logos/azion.svg)

  ### [Azion](/en/guides/deploy/azion/)
* ![](/logos/buddy.svg)

  ### [Buddy](/en/guides/deploy/buddy/)
* ![](/logos/cleavr.svg)

  ### [Cleavr](/en/guides/deploy/cleavr/)
* ![](/logos/clever-cloud.svg)

  ### [Clever Cloud](/en/guides/deploy/clever-cloud/)
* ![](/logos/cloudflare-pages.svg)

  ### [Cloudflare](/en/guides/deploy/cloudflare/)
* ![](/logos/cloudray.svg)

  ### [CloudRay](/en/guides/deploy/cloudray/)
* ![](/logos/deno.svg)

  ### [Deno Deploy](/en/guides/deploy/deno/)
* ![](/logos/deployhq.svg)

  ### [DeployHQ](/en/guides/deploy/deployhq/)
* ![](/logos/edgeone-pages.svg)

  ### [EdgeOne Pages](/en/guides/deploy/edgeone-pages/)
* ![](/logos/firebase.svg)

  ### [Firebase](/en/guides/deploy/firebase/)
* ![](/logos/fleek.svg)

  ### [Fleek](/en/guides/deploy/fleek/)
* ![](/logos/flyio.svg)

  ### [Fly.io](/en/guides/deploy/flyio/)
* ![](/logos/github.svg)

  ### [GitHub Pages](/en/guides/deploy/github/)
* ![](/logos/gitlab.svg)

  ### [GitLab Pages](/en/guides/deploy/gitlab/)
* ![](/logos/google-cloud.svg)

  ### [Google Cloud](/en/guides/deploy/google-cloud/)
* ![](/logos/heroku.svg)

  ### [Heroku](/en/guides/deploy/heroku/)
* ![](/logos/juno.svg)

  ### [Juno](/en/guides/deploy/juno/)
* ![](/logos/kinsta.svg)

  ### [Kinsta](/en/guides/deploy/kinsta/)
* ![](/logos/microsoft-azure.svg)

  ### [Microsoft Azure](/en/guides/deploy/microsoft-azure/)
* ![](/logos/netlify.svg)

  ### [Netlify](/en/guides/deploy/netlify/)
* ![](/logos/railway.svg)

  ### [Railway](/en/guides/deploy/railway/)
* ![](/logos/render.svg)

  ### [Render](/en/guides/deploy/render/)
* ![](/logos/seenode.svg)

  ### [Seenode](/en/guides/deploy/seenode/)
* ![](/logos/stormkit.svg)

  ### [Stormkit](/en/guides/deploy/stormkit/)
* ![](/logos/surge.svg)

  ### [Surge](/en/guides/deploy/surge/)
* ![](/logos/vercel.svg)

  ### [Vercel](/en/guides/deploy/vercel/)
* ![](/logos/zeabur.svg)

  ### [Zeabur](/en/guides/deploy/zeabur/)
* ![](/logos/zephyr.svg)

  ### [Zephyr Cloud](/en/guides/deploy/zephyr/)
* ![](/logos/zerops.svg)

  ### [Zerops](/en/guides/deploy/zerops/)

Recipes

![Scrimba](/_astro/Scrimba.ByZ1pAIN_1PqoUV.webp)
![](/_astro/JamesQuick.BYVczE5K_Z27c5s6.webp)

## **Learn Astro** with James Q Quick

Build your first site with 35 interactive Scrimba lessons

[Get 20% off](https://scrimba.com/intro-to-astro-c00ar0fi5u?via=astro)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/deploy/cloudflare.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Clever Cloud](/en/guides/deploy/clever-cloud/)
[Next

CloudRay](/en/guides/deploy/cloudray/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)