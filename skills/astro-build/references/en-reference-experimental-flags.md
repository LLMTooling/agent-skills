<!-- Source: https://docs.astro.build/en/reference/experimental-flags/ -->

# Configuring experimental flags

Experimental features are available only after enabling a flag in the Astro configuration file.

astro.config.mjs

```
import { defineConfig } from 'astro/config';



export default defineConfig({



experimental: {



// enable experimental flags



// to try out new features



},



});
```

Astro offers experimental flags to give users early access to new features for testing and feedback.

These flags allow you to participate in feature development by reporting issues and sharing your opinions. These features are not guaranteed to be stable and may include breaking changes even in small `patch` releases while the feature is actively developed.

We recommend [updating Astro](/en/upgrade-astro/#upgrade-to-the-latest-version) frequently, and keeping up with release notes in the [Astro changelog](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md) which will inform you of any changes needed to your project code. The experimental feature documentation will always be updated for the current released version only.

Reference

![Scrimba](/_astro/Scrimba.ByZ1pAIN_1PqoUV.webp)
![](/_astro/JamesQuick.BYVczE5K_Z27c5s6.webp)

## **Learn Astro** with James Q Quick

Build your first site with 35 interactive Scrimba lessons

[Get 20% off](https://scrimba.com/intro-to-astro-c00ar0fi5u?via=astro)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/reference/experimental-flags/index.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Programmatic Astro API (experimental)](/en/reference/programmatic-reference/)
[Next

Content Security Policy](/en/reference/experimental-flags/csp/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)