<!-- Source: https://docs.astro.build/en/guides/backend/sentry/ -->

# Monitor your Astro Site with Sentry

[Sentry](https://sentry.io) offers a comprehensive application monitoring and error tracking service designed to help developers identify, diagnose, and resolve issues in real-time.

Read more on our blog about [Astro’s partnership with Sentry](https://astro.build/blog/sentry-official-monitoring-partner/) and Sentry’s Spotlight dev toolbar app that brings a rich debug overlay into your Astro development environment. Spotlight shows errors, traces, and important context right in your browser during local development.

Sentry’s Astro SDK enables automatic reporting of errors and tracing data in your Astro application.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

A full list of prerequisites can be found in [the Sentry guide for Astro](https://docs.sentry.io/platforms/javascript/guides/astro/#prerequisites).

## Install

[Section titled “Install”](#install)

Sentry captures data by using an SDK within your application’s runtime.

Install the SDK by running the following command for the package manager of your choice in the Astro CLI:



* [npm](#tab-panel-2708)
* [pnpm](#tab-panel-2709)
* [Yarn](#tab-panel-2710)

Terminal window

```
npx astro add @sentry/astro
```

Terminal window

```
pnpm astro add @sentry/astro
```

Terminal window

```
yarn astro add @sentry/astro
```



The astro CLI installs the SDK package and adds the Sentry integration to your `astro.config.mjs` file.

## Configure

[Section titled “Configure”](#configure)

To configure the Sentry integration, you need to provide the following credentials in your `astro.config.mjs` file.

1. **Client key (DSN)** - You can find the DSN in your Sentry project settings under *Client keys (DSN)*.
2. **Project name** - You can find the project name in your Sentry project settings under *General settings*.
3. **Auth token** - You can create an auth token in your Sentry organization settings under *Auth tokens*.

Note

If you are creating a new Sentry project, select Astro as your platform to get all the necessary information to configure the SDK.

astro.config.mjs

```
import { defineConfig } from 'astro/config';



import sentry from '@sentry/astro';



export default defineConfig({



integrations: [



sentry({



dsn: 'https://examplePublicKey@o0.ingest.sentry.io/0',



sourceMapsUploadOptions: {



project: 'example-project',



authToken: process.env.SENTRY_AUTH_TOKEN,



},



}),



],



});
```

Once you’ve configured your `sourceMapsUploadOptions` and added your `dsn`, the SDK will automatically capture and send errors and performance events to Sentry.

## Test your setup

[Section titled “Test your setup”](#test-your-setup)

Add the following `<button>` element to one of your `.astro` pages. This will allow you to manually trigger an error so you can test the error reporting process.

src/pages/index.astro

```
<button onclick="throw new Error('This is a test error')">Throw test error</button>
```

To view and resolve the recorded error, log into [sentry.io](https://sentry.io/) and open your project.

## More backend service guides

* ![](/logos/appwriteio.svg)

  ### [Appwrite](/en/guides/backend/appwrite/)
* ![](/logos/firebase.svg)

  ### [Firebase](/en/guides/backend/firebase/)
* ![](/logos/neon.svg)

  ### [Neon](/en/guides/backend/neon/)
* ![](/logos/prisma-postgres.svg)

  ### [Prisma Postgres](/en/guides/backend/prisma-postgres/)
* ![](/logos/sentry.svg)

  ### [Sentry](/en/guides/backend/sentry/)
* ![](/logos/supabase.svg)

  ### [Supabase](/en/guides/backend/supabase/)
* ![](/logos/turso.svg)

  ### [Turso](/en/guides/backend/turso/)
* ![](/logos/xata.svg)

  ### [Xata](/en/guides/backend/xata/)

Recipes

![](/_astro/CodingInPublic.DpaYu7Qd_5sx41.webp)

## Learn Astro with **Coding in Public**

150+ video lessons
•
Astro v5 ready

[Get 20% off](https://learnastro.dev?code=ASTRO_PROMO)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/backend/sentry.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Prisma Postgres](/en/guides/backend/prisma-postgres/)
[Next

Supabase](/en/guides/backend/supabase/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)