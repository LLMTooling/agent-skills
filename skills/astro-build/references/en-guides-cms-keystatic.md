<!-- Source: https://docs.astro.build/en/guides/cms/keystatic/ -->

# Keystatic & Astro

[Keystatic](https://keystatic.com/) is an open source, headless content-management system that allows you to structure your content and sync it with GitHub.

Tip

If you’re starting a **new Astro + Keystatic project from scratch**, you can use the [Keystatic CLI](https://keystatic.com/docs/quick-start#keystatic-cli) to generate a new project in seconds:



* [npm](#tab-panel-2750)
* [pnpm](#tab-panel-2751)
* [Yarn](#tab-panel-2752)

Terminal window

```
npm create @keystatic@latest
```

Terminal window

```
pnpm create @keystatic@latest
```

Terminal window

```
yarn create @keystatic
```



Select the Astro template, and you’ll be ready to [deploy](#deploying-keystatic--astro)!

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* An existing Astro project [with an adapter configured](/en/guides/on-demand-rendering/).

Note

If you intend to sync Keystatic’s data with GitHub, you will also need **a GitHub account with `write` permissions** on the repository for this project.

## Installing dependencies

[Section titled “Installing dependencies”](#installing-dependencies)

Add both the Markdoc (for content entries) and the React (for the Keystatic Admin UI Dashboard) integrations to your Astro project, using the `astro add` command for your package manager.

* [npm](#tab-panel-2753)
* [pnpm](#tab-panel-2754)
* [Yarn](#tab-panel-2755)

Terminal window

```
npx astro add react markdoc
```

Terminal window

```
pnpm astro add react markdoc
```

Terminal window

```
yarn astro add react markdoc
```

You will also need two Keystatic packages:

* [npm](#tab-panel-2756)
* [pnpm](#tab-panel-2757)
* [Yarn](#tab-panel-2758)

Terminal window

```
npm install @keystatic/core @keystatic/astro
```

Terminal window

```
pnpm add @keystatic/core @keystatic/astro
```

Terminal window

```
yarn add @keystatic/core @keystatic/astro
```

## Adding the Astro integration

[Section titled “Adding the Astro integration”](#adding-the-astro-integration)

Add the Astro integration from `@keystatic/astro` in your Astro config file:

astro.config.mjs

```
import { defineConfig } from 'astro/config'



import react from '@astrojs/react'



import markdoc from '@astrojs/markdoc'



import keystatic from '@keystatic/astro'



// https://astro.build/config



export default defineConfig({



integrations: [react(), markdoc(), keystatic()],



output: 'static',



})
```

## Creating a Keystatic config file

[Section titled “Creating a Keystatic config file”](#creating-a-keystatic-config-file)

A Keystatic config file is required to define your content schema. This file will also allow you to connect a project to a specific GitHub repository (if you decide to do so).

Create a file called `keystatic.config.ts` in the root of the project and add the following code to define both your storage type (`local`) and a single content collection (`posts`):

keystatic.config.ts

```
import { config, fields, collection } from '@keystatic/core';



export default config({



storage: {



kind: 'local',



},



collections: {



posts: collection({



label: 'Posts',



slugField: 'title',



path: 'src/content/posts/*',



format: { contentField: 'content' },



schema: {



title: fields.slug({ name: { label: 'Title' } }),



content: fields.markdoc({



label: 'Content',



}),



},



}),



},



});
```

Already using content collections?

If you are already using [content collections](/en/guides/content-collections/) in your Astro project, then update the schema above to exactly match the collection(s) defined in your existing schema.

Keystatic is now configured to manage your content based on your schema.

## Running Keystatic locally

[Section titled “Running Keystatic locally”](#running-keystatic-locally)

To launch your Keystatic Admin UI dashboard, start Astro’s dev server:

Terminal window

```
npm run dev
```

Visit `http://127.0.0.1:4321/keystatic` in the browser to see the Keystatic Admin UI running.

## Creating a new post

[Section titled “Creating a new post”](#creating-a-new-post)

1. In the Keystatic Admin UI dashboard, click on the “Posts” collection.
2. Use the button to create a new post. Add the title “My First Post” and some content, then save the post.
3. This post should now be visible from your “Posts” collection. You can view and edit your individual posts from this dashboard page.
4. Return to view your Astro project files. You will now find a new `.mdoc` file inside the `src/content/posts` directory for this new post:

   * Directorysrc/
     + Directorycontent/
       - Directoryposts/
         * **my-first-post.mdoc**
5. Navigate to that file in your code editor and verify that you can see the Markdown content you entered. For example:

   ```
   ---



   title: My First Post



   ---



   This is my very first post. I am **super** excited!
   ```

## Rendering Keystatic content

[Section titled “Rendering Keystatic content”](#rendering-keystatic-content)

Use Astro’s Content Collections API to [query and display your posts and collections](/en/guides/content-collections/#querying-collections), just as you would in any Astro project.

### Displaying a collection list

[Section titled “Displaying a collection list”](#displaying-a-collection-list)

The following example displays a list of each post title, with a link to an individual post page.

```
---



import { getCollection } from 'astro:content'



const posts = await getCollection('posts')



---



<ul>



{posts.map(post => (



<li>



<a href={`/posts/${post.slug}`}>{post.data.title}</a>



</li>



))}



</ul>
```

### Displaying a single entry

[Section titled “Displaying a single entry”](#displaying-a-single-entry)

To display content from an individual post, you can import and use the `<Content />` component to [render your content to HTML](/en/guides/content-collections/#rendering-body-content):

```
---



import { getEntry } from 'astro:content'



const post = await getEntry('posts', 'my-first-post')



const { Content } = await post.render()



---



<main>



<h1>{post.data.title}</h1>



<Content />



</main>
```

For more information on querying, filtering, displaying your collections content and more, see the full content [collections documentation](/en/guides/content-collections/).

## Deploying Keystatic + Astro

[Section titled “Deploying Keystatic + Astro”](#deploying-keystatic--astro)

To deploy your website, visit our [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

You’ll also probably want to [connect Keystatic to GitHub](https://keystatic.com/docs/connect-to-github) so you can manage content on the deployed instance of the project.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* Check out [the official Keystatic guide](https://keystatic.com/docs/installation-astro)
* [Keystatic starter template](https://github.com/Thinkmill/keystatic/tree/main/templates/astro)

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

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/cms/keystatic.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

JekyllPad](/en/guides/cms/jekyllpad/)
[Next

KeystoneJS](/en/guides/cms/keystonejs/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)