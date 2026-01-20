<!-- Source: https://docs.astro.build/en/guides/migrate-to-astro/from-gitbook/ -->

# Migrating from GitBook

[GitBook](https://gitbook.com) is a web-based platform for creating and publishing documentation and books in a collaborative manner, with version control integration and customizable features.

## Key Similarities between GitBook and Astro

[Section titled “Key Similarities between GitBook and Astro”](#key-similarities-between-gitbook-and-astro)

GitBook and Astro share some similarities that will help you migrate your project:

* Both Astro and GitBook support [Markdown](/en/guides/markdown-content/). You can migrate all your existing documentation utilizing GitBook’s Git Sync feature.
* Both Astro and GitBook use some form of [file-based routing](/en/guides/routing/). Using Astro’s file structure for your existing content and when adding new pages should feel familiar.

## Key Differences between GitBook and Astro

[Section titled “Key Differences between GitBook and Astro”](#key-differences-between-gitbook-and-astro)

When you migrate your GitBook docs to Astro, you will notice some important differences:

* A GitBook site is edited using an online dashboard. In Astro, you will use a [code editor](/en/editor-setup/) and development environment to maintain your site. You can develop locally on your machine, or choose a cloud editor/development environment like IDX, StackBlitz, CodeSandbox, or Gitpod.
* GitBook stores your content in a database. In Astro, you will have individual files (typically Markdown or MDX) in your [project directory](/en/basics/project-structure/) for each page’s content. Or, you can choose to use a [CMS for your content](/en/guides/cms/) and use Astro to fetch and present the data.
* GitBook uses a custom syntax on top of Markdown for content. Astro supports Markdoc via the optional [Markdoc integration](/en/guides/integrations-guide/markdoc/), which features a similar syntax to the one you would use in GitBook.

## Switch from GitBook to Astro

[Section titled “Switch from GitBook to Astro”](#switch-from-gitbook-to-astro)

To convert a GitBook documentation site to Astro, start with our official [Starlight docs theme starter template](https://starlight.astro.build), or explore more community docs themes in our [theme showcase](https://astro.build/themes?search=&categories%5B%5D=docs).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](/en/install-and-setup/#install-from-the-cli-wizard).



* [npm](#tab-panel-3054)
* [pnpm](#tab-panel-3055)
* [Yarn](#tab-panel-3056)

Terminal window

```
npm create astro@latest -- --template starlight
```

Terminal window

```
pnpm create astro@latest --template starlight
```

Terminal window

```
yarn create astro --template starlight
```



Once you have a new Astro project, you can sync your existing GitBook content to your new Astro project. GitBook has a [Git Sync feature](https://docs.gitbook.com/product-tour/git-sync) that will automatically sync your GitBook content to a GitHub/GitLab repository.

To sync directly to the docs template’s content collection, specify `src/content/docs/en` or `src/content/docs` as the project directory.

Caution

When enabling Git Sync be sure to specify “**GitBook to GitHub**” as the priority. This will ensure that your GitBook content is synced to your GitHub repository. Otherwise, you will overwrite your existing GitBook content.

After syncing the content, you will now have a copy of your GitBook content in your Astro repository. Disable git sync to prevent future syncing with GitBook.

Note that although you now have your content migrated to your Astro project, it will not be immediately usable. To use this content in your Astro site, you will need to spend some time manually changing GitBook’s syntax into a format compatible with Astro. In particular:

* Astro’s [Markdoc integration](/en/guides/integrations-guide/markdoc/) requires that the file extension be `.mdoc`. This is to avoid conflicts with other Markdown extensions like `.mdx` and `.md`.
* GitBook syntax differs from Markdoc where the `/` prefix denoting a closing tag is replaced with `end` for GitBook files. You will need to update this notation throughout your files.
* Some features of GitBook rely on custom components. These components will not exist in Astro and must be created and added to your project through [Markdoc’s config `tags` attribute](/en/guides/integrations-guide/markdoc/#use-astro-components-as-markdoc-tags) or removed from your files.

## Community Resources

[Section titled “Community Resources”](#community-resources)

Have a resource to share?

If you found (or made!) a helpful video or blog post about converting a GitBook site to Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/migrate-to-astro/from-gitbook.mdx)!

## More migration guides

* ![](/logos/create-react-app.svg)

  ### [Create React App](/en/guides/migrate-to-astro/from-create-react-app/)
* ![](/logos/docusaurus.svg)

  ### [Docusaurus](/en/guides/migrate-to-astro/from-docusaurus/)
* ![](/logos/eleventy.svg)

  ### [Eleventy](/en/guides/migrate-to-astro/from-eleventy/)
* ![](/logos/gatsby.svg)

  ### [Gatsby](/en/guides/migrate-to-astro/from-gatsby/)
* ![](/logos/gitbook.svg)

  ### [GitBook](/en/guides/migrate-to-astro/from-gitbook/)
* ![](/logos/gridsome.svg)

  ### [Gridsome](/en/guides/migrate-to-astro/from-gridsome/)
* ![](/logos/hugo.svg)

  ### [Hugo](/en/guides/migrate-to-astro/from-hugo/)
* ![](/logos/jekyll.png)

  ### [Jekyll](/en/guides/migrate-to-astro/from-jekyll/)
* ![](/logos/nextjs.svg)

  ### [Next.js](/en/guides/migrate-to-astro/from-nextjs/)
* ![](/logos/nuxtjs.svg)

  ### [NuxtJS](/en/guides/migrate-to-astro/from-nuxtjs/)
* ![](/logos/pelican.svg)

  ### [Pelican](/en/guides/migrate-to-astro/from-pelican/)
* ![](/logos/sveltekit.svg)

  ### [SvelteKit](/en/guides/migrate-to-astro/from-sveltekit/)
* ![](/logos/vuepress.png)

  ### [VuePress](/en/guides/migrate-to-astro/from-vuepress/)
* ![](/logos/wordpress.svg)

  ### [WordPress](/en/guides/migrate-to-astro/from-wordpress/)

Recipes

![Scrimba](/_astro/Scrimba.ByZ1pAIN_1PqoUV.webp)
![](/_astro/JamesQuick.BYVczE5K_Z27c5s6.webp)

## **Learn Astro** with James Q Quick

Build your first site with 35 interactive Scrimba lessons

[Get 20% off](https://scrimba.com/intro-to-astro-c00ar0fi5u?via=astro)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/migrate-to-astro/from-gitbook.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Gatsby](/en/guides/migrate-to-astro/from-gatsby/)
[Next

Gridsome](/en/guides/migrate-to-astro/from-gridsome/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)