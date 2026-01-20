<!-- Source: https://docs.astro.build/en/guides/deploy/firebase/ -->

# Deploy your Astro Site to Google’s Firebase Hosting

[Firebase Hosting](https://firebase.google.com/products/hosting) is a service provided by Google’s [Firebase](https://firebase.google.com/) app development platform, which can be used to deploy an Astro site.

See our separate guide for [adding Firebase backend services](/en/guides/backend/firebase/) such as databases, authentication, and storage.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

Your Astro project can be deployed to Firebase as a static site, or as a server-side rendered site (SSR).

### Static Site

[Section titled “Static Site”](#static-site)

Your Astro project is a static site by default. You don’t need any extra configuration to deploy a static Astro site to Firebase.

### Adapter for SSR

[Section titled “Adapter for SSR”](#adapter-for-ssr)

To enable SSR in your Astro project and deploy on Firebase add the [Node.js adapter](/en/guides/integrations-guide/node/).

Note

Deploying an SSR Astro site to Firebase requires the [Blaze plan](https://firebase.google.com/pricing) or higher.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

1. Install the [Firebase CLI](https://github.com/firebase/firebase-tools). This is a command-line tool that allows you to interact with Firebase from the terminal.



   * [npm](#tab-panel-2811)
   * [pnpm](#tab-panel-2812)
   * [Yarn](#tab-panel-2813)

   Terminal window

   ```
   npm install firebase-tools
   ```

   Terminal window

   ```
   pnpm add firebase-tools
   ```

   Terminal window

   ```
   yarn add firebase-tools
   ```
2. Authenticate the Firebase CLI with your Google account. This will open a browser window where you can log in to your Google account.

   * [npm](#tab-panel-2814)
   * [pnpm](#tab-panel-2815)
   * [Yarn](#tab-panel-2816)

   Terminal window

   ```
   npx firebase login
   ```

   Terminal window

   ```
   pnpm exec firebase login
   ```

   Terminal window

   ```
   yarn firebase login
   ```
3. Enable experimental web frameworks support. This is an experimental feature that allows the Firebase CLI to detect and configure your deployment settings for Astro.

   * [npm](#tab-panel-2817)
   * [pnpm](#tab-panel-2818)
   * [Yarn](#tab-panel-2819)

   Terminal window

   ```
   npx firebase experiments:enable webframeworks
   ```

   Terminal window

   ```
   pnpm exec firebase experiments:enable webframeworks
   ```

   Terminal window

   ```
   yarn firebase experiments:enable webframeworks
   ```
4. Initialize Firebase Hosting in your project. This will create a `firebase.json` and `.firebaserc` file in your project root.

   * [npm](#tab-panel-2820)
   * [pnpm](#tab-panel-2821)
   * [Yarn](#tab-panel-2822)

   Terminal window

   ```
   npx firebase init hosting
   ```

   Terminal window

   ```
   pnpm exec firebase init hosting
   ```

   Terminal window

   ```
   yarn firebase init hosting
   ```
5. Deploy your site to Firebase Hosting. This will build your Astro site and deploy it to Firebase.

   * [npm](#tab-panel-2823)
   * [pnpm](#tab-panel-2824)
   * [Yarn](#tab-panel-2825)

   Terminal window

   ```
   npx firebase deploy --only hosting
   ```

   Terminal window

   ```
   pnpm exec firebase deploy --only hosting
   ```

   Terminal window

   ```
   yarn firebase deploy --only hosting
   ```

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

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/deploy/firebase.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

EdgeOne Pages](/en/guides/deploy/edgeone-pages/)
[Next

Fleek](/en/guides/deploy/fleek/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)