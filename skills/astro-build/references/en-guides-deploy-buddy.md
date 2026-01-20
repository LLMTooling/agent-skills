<!-- Source: https://docs.astro.build/en/guides/deploy/buddy/ -->

# Deploy your Astro Site with Buddy

You can deploy your Astro project using [Buddy](https://buddy.works/), a CI/CD solution that can build your site and push it to many different deploy targets including FTP servers and cloud hosting providers.

Note

Buddy itself will not host your site. Instead, it helps you manage the build process and deliver the result to a deploy platform of your choice.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

1. [Create a **Buddy** account](https://buddy.works/sign-up).
2. Create a new project and connect it with a git repository (GitHub, GitLab, BitBucket, any private Git Repository or you can use Buddy Git Hosting).
3. Add a new pipeline.
4. In the newly created pipeline add a **[Node.js](https://buddy.works/actions/node-js)** action.
5. In this action add:

   Terminal window

   ```
   npm install



   npm run build
   ```
6. Add a deployment action — there are many to choose from, you can browse them in [Buddy’s actions catalog](https://buddy.works/actions). Although their settings can differ, remember to set the **Source path** to `dist`.
7. Press the **Run** button.

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

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/deploy/buddy.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Azion](/en/guides/deploy/azion/)
[Next

Cleavr](/en/guides/deploy/cleavr/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)