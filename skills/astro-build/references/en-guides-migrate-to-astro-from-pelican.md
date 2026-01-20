<!-- Source: https://docs.astro.build/en/guides/migrate-to-astro/from-pelican/ -->

# Migrating from Pelican

[Pelican](https://getpelican.com) is an open-source static site generator built on Python.

## Key Similarities between Pelican and Astro

[Section titled “Key Similarities between Pelican and Astro”](#key-similarities-between-pelican-and-astro)

Pelican and Astro share some similarities that will help you migrate your project:

* Pelican and Astro are both static-site generators, ideally suited to [content-driven websites](/en/concepts/why-astro/#content-driven) like blogs.
* Pelican and Astro both have built-in support for [writing in Markdown](/en/guides/markdown-content/), including frontmatter YAML properties for page metadata. However, Astro has very few reserved frontmatter properties compared to Pelican. Even though many of your existing Pelican frontmatter properties will not be “special” in Astro, you can continue to use your existing Markdown files and frontmatter values.

## Key Differences between Pelican and Astro

[Section titled “Key Differences between Pelican and Astro”](#key-differences-between-pelican-and-astro)

When you rebuild your Pelican site in Astro, you will notice some important differences:

* Pelican supports writing content in Markdown and reStructured Text (`.rst`). Astro supports [creating pages from Markdown and MDX](/en/guides/markdown-content/) files, but does not support reStructured Text.
* Pelican uses HTML files and Jinja syntax for templating. [Astro syntax](/en/basics/astro-components/) is a JSX-like superset of HTML. All valid HTML is valid `.astro` syntax.
* Pelican was designed to build content-rich websites like blogs and has some built-in, blog features that you would have to build yourself in Astro. Instead, Astro offers some of these features included in an [official blog theme](https://github.com/withastro/astro/tree/latest/examples/blog).

## Switch from Pelican to Astro

[Section titled “Switch from Pelican to Astro”](#switch-from-pelican-to-astro)

To convert a Pelican documentation site to Astro, start with our official [Starlight docs theme starter template](https://starlight.astro.build), or explore more community themes in our [theme showcase](https://astro.build/themes/).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](/en/install-and-setup/#install-from-the-cli-wizard).



* [npm](#tab-panel-3087)
* [pnpm](#tab-panel-3088)
* [Yarn](#tab-panel-3089)

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



Bring your existing Markdown content files to [create Markdown pages](/en/guides/markdown-content/). You can still take advantage of [file-based routing](/en/guides/routing/) by copying these documents from Pelican’s `content/` folder into `src/pages/` in Astro. You may wish to read about [Astro’s project structure](/en/basics/project-structure/) to learn where files should be located.

Pelican may have handled much of your site layout and metadata for you. You may wish to read about [building Astro Layouts as Markdown page wrappers](/en/basics/layouts/#markdown-layouts) to see how to manage templating yourself in Astro, including your page `<head>`.

Like Pelican, Astro has many plugins that extend its functionality. Explore the [official list of integrations](/en/guides/integrations-guide/) for adding features such as MDX support, and find hundreds more of community-maintained integrations in the [Astro Integrations Directory](https://astro.build/integrations/). You can even use the [Astro Integration API](/en/reference/integrations-reference/) to build your own custom integration to extend your project’s features.

To convert other types of sites, such as a portfolio or a blog, see more official starter templates on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in IDX, StackBlitz, CodeSandbox and Gitpod online development environments.

## Community Resources

[Section titled “Community Resources”](#community-resources)

Have a resource to share?

If you found (or made!) a helpful video or blog post about converting a Pelican site to Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/migrate-to-astro/from-pelican.mdx)!

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

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/migrate-to-astro/from-pelican.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

NuxtJS](/en/guides/migrate-to-astro/from-nuxtjs/)
[Next

SvelteKit](/en/guides/migrate-to-astro/from-sveltekit/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)