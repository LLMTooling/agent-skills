<!-- Source: https://docs.astro.build/en/guides/deploy/seenode/ -->

# Deploy your Astro Site to Seenode

[Seenode](https://seenode.com) is a deployment platform for building and deploying web applications with databases, built-in observability, and auto-scaling. Astro sites can be deployed to Seenode using server-side rendering (SSR).

This guide includes instructions for deploying to Seenode through the web interface.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

### Adapter for SSR

[Section titled “Adapter for SSR”](#adapter-for-ssr)

To enable on-demand rendering in your Astro project and deploy to Seenode, add [the Node.js adapter](/en/guides/integrations-guide/node/) with the following `astro add` command. This will install the adapter and make the appropriate changes to your `astro.config.mjs` file in one step.



* [npm](#tab-panel-2861)
* [pnpm](#tab-panel-2862)
* [Yarn](#tab-panel-2863)

Terminal window

```
npx astro add node
```

Terminal window

```
pnpm astro add node
```

Terminal window

```
yarn astro add node
```



After installing the adapter, update your `astro.config.mjs` to configure the server for Seenode’s requirements:

astro.config.mjs

```
import { defineConfig } from 'astro/config';



import node from '@astrojs/node';



export default defineConfig({



output: 'server',



adapter: node({



mode: 'standalone'



}),



server: {



port: process.env.NODE_ENV === 'production' ? (Number(process.env.PORT) || 80) : 4321,



host: true



}



});
```

Update your `package.json` to include a start script that runs the built server:

package.json

```
{



"scripts": {



"dev": "astro dev",



"build": "astro build",



"preview": "astro preview",



"start": "NODE_ENV=production node ./dist/server/entry.mjs"



}



}
```

See [Seenode’s Astro deployment guide](https://seenode.com/docs/frameworks/javascript/astro/) for more configuration options and troubleshooting.

## How to Deploy

[Section titled “How to Deploy”](#how-to-deploy)

You can deploy to Seenode through the web interface by connecting your Git repository.

### Web Interface Deployment

[Section titled “Web Interface Deployment”](#web-interface-deployment)

1. Create a [Seenode account](https://cloud.seenode.com) and sign in.
2. Push your code to your Git repository (GitHub or GitLab).
3. From the [Seenode Dashboard](https://cloud.seenode.com/dashboard/applications/web/create), create a new **Web Service** and connect your repository.
4. Seenode will automatically detect your Astro project. Configure the deployment settings:

   * **Build Command:** `npm ci && npm run build` (or use `pnpm` / `yarn` equivalents)
   * **Start Command:** `npm start`
   * **Port:** `80` (required for web services)
5. Select your preferred instance size and click **Create Web Service**.
6. Your application will be built and deployed. Once complete, you’ll receive a URL to access your live Astro site after which you can link your domain.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Seenode Cloud](https://cloud.seenode.com) — Seenode dashboard
* [Seenode Documentation](https://seenode.com/docs) — complete platform documentation
* [Seenode Astro Guide](https://seenode.com/docs/frameworks/javascript/astro/) — detailed deployment guide and troubleshooting
* [Seenode Astro Template](https://github.com/seenode/example-astro) — pre-configured starter template

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

![](/_astro/CodingInPublic.DpaYu7Qd_5sx41.webp)

## Learn Astro with **Coding in Public**

150+ video lessons
•
Astro v5 ready

[Get 20% off](https://learnastro.dev?code=ASTRO_PROMO)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/deploy/seenode.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Render](/en/guides/deploy/render/)
[Next

Stormkit](/en/guides/deploy/stormkit/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)