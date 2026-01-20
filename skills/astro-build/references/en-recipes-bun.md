<!-- Source: https://docs.astro.build/en/recipes/bun/ -->

# Use Bun with Astro

[Bun](https://bun.sh/) is an all-in-one JavaScript runtime & toolkit. See [Bun’s documentation](https://bun.sh/docs) for more information.

Caution

Using Bun with Astro may reveal rough edges. Some integrations may not work as expected. Consult [Bun’s official documentation for working with Astro](https://bun.sh/guides/ecosystem/astro) for details.

If you have any problems using Bun, please [open an Issue on GitHub with Bun directly](https://github.com/oven-sh/bun/issues/new/choose).

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* Bun installed locally on your machine. See the [installation instructions](https://bun.sh/docs/installation) in Bun’s official documentation.

## Create a new Astro project with Bun

[Section titled “Create a new Astro project with Bun”](#create-a-new-astro-project-with-bun)

Create a new Astro project with Bun using the following `create-astro` command:

Terminal window

```
bun create astro my-astro-project-using-bun
```

## Install dependencies

[Section titled “Install dependencies”](#install-dependencies)

If you skipped the “Install dependencies?” step during the CLI wizard, then be sure to install your dependencies before continuing.

Terminal window

```
bun install
```

## Add Types

[Section titled “Add Types”](#add-types)

Bun publishes the [`@types/bun`](https://www.npmjs.com/package/@types/bun) package, containing the runtime types for Bun.

Install `@types/bun` using the following command:

Terminal window

```
bun add -d @types/bun
```

## CLI installation flags

[Section titled “CLI installation flags”](#cli-installation-flags)

### Using integrations

[Section titled “Using integrations”](#using-integrations)

You can also use any of the official Astro integrations with the `astro add` command:

Terminal window

```
bun astro add react
```

### Use a theme or starter template

[Section titled “Use a theme or starter template”](#use-a-theme-or-starter-template)

You can start a new Astro project based on an [official example](https://github.com/withastro/astro/tree/main/examples) or the main branch of any GitHub repository by passing a `--template` argument to the `create astro` command.

Run the following command in your terminal, substituting the official Astro starter template name, or the GitHub username and repository of the theme you want to use:

Terminal window

```
# create a new project with an official example



bun create astro@latest --template <example-name>



# create a new project based on a GitHub repository’s main branch



bun create astro@latest --template <github-username>/<github-repo>
```

## Develop and build

[Section titled “Develop and build”](#develop-and-build)

To run the development server, use following command:

Terminal window

```
bun run dev
```

### Build and preview your site

[Section titled “Build and preview your site”](#build-and-preview-your-site)

To build your site, use the following command:

Terminal window

```
bun run build
```

When the build is finished, run the appropriate preview command (e.g. `bun run preview`) in your terminal and you can view the built version of your site locally in the same browser preview window.

## Testing

[Section titled “Testing”](#testing)

Bun ships with a fast, built-in, Jest-compatible test runner through the [`bun test` command](https://bun.sh/docs/cli/test). You can also use any other [testing tools for Astro](/en/guides/testing/).

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Build an app with Astro and Bun](https://bun.sh/guides/ecosystem/astro)

## Community Resources

[Section titled “Community Resources”](#community-resources)

Using Bun with Astro? Add your blog post or video to this page!

* [Using Bun with Astro and Cloudflare Pages](https://handerson.hashnode.dev/using-bun-with-astro-and-cloudflare-pages) - blog post

Recipes

![Scrimba](/_astro/Scrimba.ByZ1pAIN_1PqoUV.webp)
![](/_astro/JamesQuick.BYVczE5K_Z27c5s6.webp)

## **Learn Astro** with James Q Quick

Build your first site with 35 interactive Scrimba lessons

[Get 20% off](https://scrimba.com/intro-to-astro-c00ar0fi5u?via=astro)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/recipes/bun.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Build forms with API routes](/en/recipes/build-forms-api/)
[Next

Call endpoints from the server](/en/recipes/call-endpoints/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)