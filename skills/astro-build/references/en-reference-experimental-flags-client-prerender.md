<!-- Source: https://docs.astro.build/en/reference/experimental-flags/client-prerender/ -->

# Experimental client prerendering

**Type:** `boolean`
**Default:** `false`

**Added in:**
`astro@4.2.0`

Enables pre-rendering your prefetched pages on the client in supported browsers.

This feature uses the experimental [Speculation Rules Web API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API) and enhances the default `prefetch` behavior globally to prerender links on the client.
You may wish to review the [possible risks when prerendering on the client](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API#unsafe_prefetching) before enabling this feature.

Enable client side prerendering in your `astro.config.mjs` along with any desired `prefetch` configuration options:

astro.config.mjs

```
{



prefetch: {



prefetchAll: true,



defaultStrategy: 'viewport',



},



experimental: {



clientPrerender: true,



},



}
```

Continue to use the `data-astro-prefetch` attribute on any `<a />` link on your site to opt in to prefetching.
Instead of appending a `<link>` tag to the head of the document or fetching the page with JavaScript, a `<script>` tag will be appended with the corresponding speculation rules.

Client side prerendering requires browser support. If the Speculation Rules API is not supported, `prefetch` will fallback to the supported strategy.

See the [Prefetch Guide](/en/guides/prefetch/) for more `prefetch` options and usage.

Reference

![Scrimba](/_astro/Scrimba.ByZ1pAIN_1PqoUV.webp)
![](/_astro/JamesQuick.BYVczE5K_Z27c5s6.webp)

## **Learn Astro** with James Q Quick

Build your first site with 35 interactive Scrimba lessons

[Get 20% off](https://scrimba.com/intro-to-astro-c00ar0fi5u?via=astro)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/reference/experimental-flags/client-prerender.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Live content collections](/en/reference/experimental-flags/live-content-collections/)
[Next

Intellisense for collections](/en/reference/experimental-flags/content-intellisense/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)