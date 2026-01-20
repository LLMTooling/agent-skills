<!-- Source: https://docs.astro.build/en/guides/cms/buttercms/ -->

# ButterCMS & Astro

[ButterCMS](https://buttercms.com/) is a headless CMS and blog engine that allows you to publish structured content to use in your project.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

Note

For a full blog site example, see the [Astro + ButterCMS Starter Project](https://buttercms.com/starters/astro-starter-project/).

In this section, we’ll use the [ButterCMS SDK](https://www.npmjs.com/package/buttercms) to bring your data into your Astro project.
To get started, you will need to have the following:

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

1. **An Astro project** - If you don’t have an Astro project yet, our [Installation guide](/en/install-and-setup/) will get you up and running in no time.
2. **A ButterCMS account**. If you don’t have an account, you can [sign up](https://buttercms.com/join/) for a free trial.
3. **Your ButterCMS API Token** - You can find your API Token on the [Settings](https://buttercms.com/settings/) page.

### Setup

[Section titled “Setup”](#setup)

1. Create a `.env` file in the root of your project and add your API token as an environment variable:

   .env

   ```
   BUTTER_TOKEN=YOUR_API_TOKEN_HERE
   ```

   Tip

   Read more about [using environment variables](/en/guides/environment-variables/) and `.env` files in Astro.
2. Install the ButterCMS SDK as a dependency:



   * [npm](#tab-panel-2720)
   * [pnpm](#tab-panel-2721)
   * [Yarn](#tab-panel-2722)

   Terminal window

   ```
   npm install buttercms
   ```

   Terminal window

   ```
   pnpm add buttercms
   ```

   Terminal window

   ```
   yarn add buttercms
   ```
3. Create a `buttercms.js` file in a new `src/lib/` directory in your project:

   src/lib/buttercms.js

   ```
   import Butter from "buttercms";



   export const butterClient = Butter(import.meta.env.BUTTER_TOKEN);
   ```

**This authenticates the SDK using your API Token and exports it to be used across your project.**

### Fetching Data

[Section titled “Fetching Data”](#fetching-data)

To fetch content, import this client and use one of its `retrieve` functions.

In this example, we [retrieve a collection](https://buttercms.com/docs/api/#retrieve-a-collection) that has three fields: a short text `name`, a number `price`, and a WYSIWYG `description`.

src/pages/ShopItem.astro

```
---



import { butterClient } from "../lib/buttercms";



const response = await butterClient.content.retrieve(["shopitem"]);



interface ShopItem {



name: string,



price: number,



description: string,



}



const items = response.data.data.shopitem as ShopItem[];



---



<body>



{items.map(item => <div>



<h2>{item.name} - ${item.price}</h2>



<p set:html={item.description}></p>



</div>)}



</body>
```

The interface mirrors the field types. The WYSIWYG `description` field loads as a string of HTML, and [`set:html`](/en/reference/directives-reference/#sethtml) lets you render it.

Similarly, you can [retrieve a page](https://buttercms.com/docs/api/#get-a-single-page) and display its fields:

src/pages/ShopItem.astro

```
---



import { butterClient } from "../lib/buttercms";



const response = await butterClient.page.retrieve("*", "simple-page");



const pageData = response.data.data;



interface Fields {



seo_title: string,



headline: string,



hero_image: string,



}



const fields = pageData.fields as Fields;



---



<html>



<title>{fields.seo_title}</title>



<body>



<h1>{fields.headline}</h1>



<img src={fields.hero_image} />



</body>



</html>
```

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Astro + ButterCMS Starter Project](https://buttercms.com/starters/astro-starter-project/)
* The [full ButterCMS API documentation](https://buttercms.com/docs/api/)
* ButterCMS’s [JavaScript Guide](https://buttercms.com/docs/api-client/javascript/)

## Community Resources

[Section titled “Community Resources”](#community-resources)

* Add yours!

## More CMS guides

* ![](/logos/apostrophecms.svg)

  ### [ApostropheCMS](/en/guides/cms/apostrophecms/)
* ![](/logos/builderio.svg)

  ### [Builder.io](/en/guides/cms/builderio/)
* ![](/logos/buttercms.svg)

  ### [ButterCMS](/en/guides/cms/buttercms/)
* ![](/logos/caisy.svg)

  ### [Caisy](/en/guides/cms/caisy/)
* ![](/logos/cloudcannon.svg)

  ### [CloudCannon](/en/guides/cms/cloudcannon/)
* ![](/logos/contentful.svg)

  ### [Contentful](/en/guides/cms/contentful/)
* ![](/logos/cosmic.svg)

  ### [Cosmic](/en/guides/cms/cosmic/)
* ![](/logos/craft-cms.svg)

  ### [Craft CMS](/en/guides/cms/craft-cms/)
* ![](/logos/craft-cross-cms.svg)

  ### [Craft Cross CMS](/en/guides/cms/craft-cross-cms/)
* ![](/logos/crystallize.svg)

  ### [Crystallize](/en/guides/cms/crystallize/)
* ![](/logos/datocms.svg)

  ### [DatoCMS](/en/guides/cms/datocms/)
* ![](/logos/decap-cms.svg)

  ### [Decap CMS](/en/guides/cms/decap-cms/)
* ![](/logos/directus.svg)

  ### [Directus](/en/guides/cms/directus/)
* ![](/logos/drupal.svg)

  ### [Drupal](/en/guides/cms/drupal/)
* ![](/logos/flotiq.svg)

  ### [Flotiq](/en/guides/cms/flotiq/)
* ![](/logos/frontmatter-cms.svg)

  ### [Front Matter CMS](/en/guides/cms/frontmatter-cms/)
* ![](/logos/ghost.png)

  ### [Ghost](/en/guides/cms/ghost/)
* ![](/logos/gitcms.svg)

  ### [GitCMS](/en/guides/cms/gitcms/)
* ![](/logos/hashnode.png)

  ### [Hashnode](/en/guides/cms/hashnode/)
* ![](/logos/hygraph.svg)

  ### [Hygraph](/en/guides/cms/hygraph/)
* ![](/logos/jekyllpad.svg)

  ### [JekyllPad](/en/guides/cms/jekyllpad/)
* ![](/logos/keystatic.svg)

  ### [Keystatic](/en/guides/cms/keystatic/)
* ![](/logos/keystonejs.svg)

  ### [KeystoneJS](/en/guides/cms/keystonejs/)
* ![](/logos/kontent-ai.svg)

  ### [Kontent.ai](/en/guides/cms/kontent-ai/)
* ![](/logos/microcms.svg)

  ### [microCMS](/en/guides/cms/microcms/)
* ![](/logos/optimizely.svg)

  ### [Optimizely CMS](/en/guides/cms/optimizely/)
* ![](/logos/payload.svg)

  ### [Payload CMS](/en/guides/cms/payload/)
* ![](/logos/preprcms.svg)

  ### [Prepr CMS](/en/guides/cms/preprcms/)
* ![](/logos/prismic.svg)

  ### [Prismic](/en/guides/cms/prismic/)
* ![](/logos/sanity.svg)

  ### [Sanity](/en/guides/cms/sanity/)
* ![](/logos/sitecore.svg)

  ### [Sitecore XM](/en/guides/cms/sitecore/)
* ![](/logos/sitepins.svg)

  ### [Sitepins](/en/guides/cms/sitepins/)
* ![](/logos/spinal.svg)

  ### [Spinal](/en/guides/cms/spinal/)
* ![](/logos/statamic.svg)

  ### [Statamic](/en/guides/cms/statamic/)
* ![](/logos/storyblok.svg)

  ### [Storyblok](/en/guides/cms/storyblok/)
* ![](/logos/strapi.svg)

  ### [Strapi](/en/guides/cms/strapi/)
* ![](/logos/studiocms.svg)

  ### [StudioCMS](/en/guides/cms/studiocms/)
* ![](/logos/tina-cms.svg)

  ### [Tina CMS](/en/guides/cms/tina-cms/)
* ![](/logos/umbraco.svg)

  ### [Umbraco](/en/guides/cms/umbraco/)
* ![](/logos/wordpress.svg)

  ### [Wordpress](/en/guides/cms/wordpress/)

Recipes

![Scrimba](/_astro/Scrimba.ByZ1pAIN_1PqoUV.webp)
![](/_astro/JamesQuick.BYVczE5K_Z27c5s6.webp)

## **Learn Astro** with James Q Quick

Build your first site with 35 interactive Scrimba lessons

[Get 20% off](https://scrimba.com/intro-to-astro-c00ar0fi5u?via=astro)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/cms/buttercms.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Builder.io](/en/guides/cms/builderio/)
[Next

Caisy](/en/guides/cms/caisy/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)