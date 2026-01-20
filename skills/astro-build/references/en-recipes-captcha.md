<!-- Source: https://docs.astro.build/en/recipes/captcha/ -->

# Verify a Captcha

[Server endpoints](/en/guides/endpoints/#server-endpoints-api-routes) can be used as REST API endpoints to run functions such as authentications, database access, and verifications without exposing sensitive data to the client.

In this recipe, an API route is used to verify Google reCAPTCHA v3 without exposing the secret to clients.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* A project with [SSR](/en/guides/on-demand-rendering/) (`output: 'server'`) enabled

## Recipe

[Section titled “Recipe”](#recipe)

1. Create a `POST` endpoint that accepts recaptcha data, then verifies it with reCAPTCHA’s API. Here, you can safely define secret values or read environment variables.

   src/pages/recaptcha.js

   ```
   export async function POST({ request }) {



   const data = await request.json();



   const recaptchaURL = 'https://www.google.com/recaptcha/api/siteverify';



   const requestHeaders = {



   'Content-Type': 'application/x-www-form-urlencoded'



   };



   const requestBody = new URLSearchParams({



   secret: "YOUR_SITE_SECRET_KEY",   // This can be an environment variable



   response: data.recaptcha          // The token passed in from the client



   });



   const response = await fetch(recaptchaURL, {



   method: "POST",



   headers: requestHeaders,



   body: requestBody.toString()



   });



   const responseData = await response.json();



   return new Response(JSON.stringify(responseData), { status: 200 });



   }
   ```
2. Access your endpoint using `fetch` from a client script:

   src/pages/index.astro

   ```
   <html>



   <head>



   <script is:inline src="https://www.google.com/recaptcha/api.js"></script>



   </head>



   <body>



   <button class="g-recaptcha"



   data-sitekey="PUBLIC_SITE_KEY"



   data-callback="onSubmit"



   data-action="submit"> Click me to verify the captcha challenge! </button>



   <script is:inline>



   function onSubmit(token) {



   fetch("/recaptcha", {



   method: "POST",



   body: JSON.stringify({ recaptcha: token })



   })



   .then((response) => response.json())



   .then((gResponse) => {



   if (gResponse.success) {



   // Captcha verification was a success



   } else {



   // Captcha verification failed



   }



   })



   }



   </script>



   </body>



   </html>
   ```

Recipes

![Scrimba](/_astro/Scrimba.ByZ1pAIN_1PqoUV.webp)
![](/_astro/JamesQuick.BYVczE5K_Z27c5s6.webp)

## **Learn Astro** with James Q Quick

Build your first site with 35 interactive Scrimba lessons

[Get 20% off](https://scrimba.com/intro-to-astro-c00ar0fi5u?via=astro)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/recipes/captcha.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Call endpoints from the server](/en/recipes/call-endpoints/)
[Next

Customize file names in the build output](/en/recipes/customizing-output-filenames/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)