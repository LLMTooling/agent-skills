<!-- Source: https://docs.astro.build/en/recipes/build-forms-api/ -->

# Build forms with API routes

An HTML form causes the browser to refresh the page or navigate to a new one. To send form data to an API endpoint instead, you must intercept the form submission using JavaScript.

This recipe shows you how to send form data to an API endpoint and handle that data.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* A project with [an adapter for on-demand rendering](/en/guides/on-demand-rendering/)
* A [UI Framework integration](/en/guides/framework-components/) installed

## Recipe

[Section titled “Recipe”](#recipe)

1. Create a `POST` API endpoint at `/api/feedback` that will receive the form data. Use `request.formData()` to process it. Be sure to validate the form values before you use them.

   This example sends a JSON object with a message back to the client.

   src/pages/api/feedback.ts

   ```
   export const prerender = false; // Not needed in 'server' mode



   import type { APIRoute } from "astro";



   export const POST: APIRoute = async ({ request }) => {



   const data = await request.formData();



   const name = data.get("name");



   const email = data.get("email");



   const message = data.get("message");



   // Validate the data - you'll probably want to do more than this



   if (!name || !email || !message) {



   return new Response(



   JSON.stringify({



   message: "Missing required fields",



   }),



   { status: 400 }



   );



   }



   // Do something with the data, then return a success response



   return new Response(



   JSON.stringify({



   message: "Success!"



   }),



   { status: 200 }



   );



   };
   ```
2. Create a form component using your UI framework. Each input should have a `name` attribute that describes the value of that input.

   Be sure to include a `<button>` or `<input type="submit">` element to submit the form.



   * [Preact](#tab-panel-1860)
   * [React](#tab-panel-1861)
   * [Solid](#tab-panel-1862)
   * [Svelte](#tab-panel-1863)
   * [Vue](#tab-panel-1864)

   src/components/FeedbackForm.tsx

   ```
   export default function Form() {



   return (



   <form>



   <label>



   Name



   <input type="text" id="name" name="name" required />



   </label>



   <label>



   Email



   <input type="email" id="email" name="email" required />



   </label>



   <label>



   Message



   <textarea id="message" name="message" required />



   </label>



   <button>Send</button>



   </form>



   );



   }
   ```

   src/components/FeedbackForm.tsx

   ```
   export default function Form() {



   return (



   <form>



   <label>



   Name



   <input type="text" id="name" name="name" required />



   </label>



   <label>



   Email



   <input type="email" id="email" name="email" required />



   </label>



   <label>



   Message



   <textarea id="message" name="message" required />



   </label>



   <button>Send</button>



   </form>



   );



   }
   ```

   src/components/FeedbackForm.tsx

   ```
   export default function Form() {



   return (



   <form>



   <label>



   Name



   <input type="text" id="name" name="name" required />



   </label>



   <label>



   Email



   <input type="email" id="email" name="email" required />



   </label>



   <label>



   Message



   <textarea id="message" name="message" required />



   </label>



   <button>Send</button>



   </form>



   );



   }
   ```

   src/components/FeedbackForm.svelte

   ```
   <form>



   <label>



   Name



   <input type="text" id="name" name="name" required />



   </label>



   <label>



   Email



   <input type="email" id="email" name="email" required />



   </label>



   <label>



   Message



   <textarea id="message" name="message" required />



   </label>



   <button>Send</button>



   </form>
   ```

   src/components/FeedbackForm.vue

   ```
   <template>



   <form>



   <label>



   Name



   <input type="text" id="name" name="name" required />



   </label>



   <label>



   Email



   <input type="email" id="email" name="email" required />



   </label>



   <label>



   Message



   <textarea id="message" name="message" required />



   </label>



   <button>Send</button>



   </form>



   </template>
   ```
3. Create a function that accepts a submit event, then pass it as a `submit` handler to your form.

   In the function:

   * Call `preventDefault()` on the event to override the browser’s default submission process.
   * Create a `FormData` object and send it in a `POST` request to your endpoint using `fetch()`.

   * [Preact](#tab-panel-1865)
   * [React](#tab-panel-1866)
   * [Solid](#tab-panel-1867)
   * [Svelte](#tab-panel-1868)
   * [Vue](#tab-panel-1869)

   src/components/FeedbackForm.tsx

   ```
   import { useState } from "preact/hooks";



   export default function Form() {



   const [responseMessage, setResponseMessage] = useState("");



   async function submit(e: SubmitEvent) {



   e.preventDefault();



   const formData = new FormData(e.target as HTMLFormElement);



   const response = await fetch("/api/feedback", {



   method: "POST",



   body: formData,



   });



   const data = await response.json();



   if (data.message) {



   setResponseMessage(data.message);



   }



   }



   return (



   <form onSubmit={submit}>



   <label>



   Name



   <input type="text" id="name" name="name" required />



   </label>



   <label>



   Email



   <input type="email" id="email" name="email" required />



   </label>



   <label>



   Message



   <textarea id="message" name="message" required />



   </label>



   <button>Send</button>



   {responseMessage && <p>{responseMessage}</p>}



   </form>



   );



   }
   ```

   src/components/FeedbackForm.tsx

   ```
   import { useState } from "react";



   import type { FormEvent } from "react";



   export default function Form() {



   const [responseMessage, setResponseMessage] = useState("");



   async function submit(e: FormEvent<HTMLFormElement>) {



   e.preventDefault();



   const formData = new FormData(e.target as HTMLFormElement);



   const response = await fetch("/api/feedback", {



   method: "POST",



   body: formData,



   });



   const data = await response.json();



   if (data.message) {



   setResponseMessage(data.message);



   }



   }



   return (



   <form onSubmit={submit}>



   <label htmlFor="name">



   Name



   <input type="text" id="name" name="name" autoComplete="name" required />



   </label>



   <label htmlFor="email">



   Email



   <input type="email" id="email" name="email" autoComplete="email" required />



   </label>



   <label htmlFor="message">



   Message



   <textarea id="message" name="message" autoComplete="off" required />



   </label>



   <button>Send</button>



   {responseMessage && <p>{responseMessage}</p>}



   </form>



   );



   }
   ```

   src/components/FeedbackForm.tsx

   ```
   import { createSignal, createResource, Suspense } from "solid-js";



   async function postFormData(formData: FormData) {



   const response = await fetch("/api/feedback", {



   method: "POST",



   body: formData,



   });



   const data = await response.json();



   return data;



   }



   export default function Form() {



   const [formData, setFormData] = createSignal<FormData>();



   const [response] = createResource(formData, postFormData);



   function submit(e: SubmitEvent) {



   e.preventDefault();



   setFormData(new FormData(e.target as HTMLFormElement));



   }



   return (



   <form onSubmit={submit}>



   <label>



   Name



   <input type="text" id="name" name="name" required />



   </label>



   <label>



   Email



   <input type="email" id="email" name="email" required />



   </label>



   <label>



   Message



   <textarea id="message" name="message" required />



   </label>



   <button>Send</button>



   <Suspense>{response() && <p>{response().message}</p>}</Suspense>



   </form>



   );



   }
   ```

   src/components/FeedbackForm.svelte

   ```
   <script lang="ts">



   let responseMessage: string;



   async function submit(e: SubmitEvent) {



   e.preventDefault();



   const formData = new FormData(e.currentTarget as HTMLFormElement);



   const response = await fetch("/api/feedback", {



   method: "POST",



   body: formData,



   });



   const data = await response.json();



   responseMessage = data.message;



   }



   </script>



   <form on:submit={submit}>



   <label>



   Name



   <input type="text" id="name" name="name" required />



   </label>



   <label>



   Email



   <input type="email" id="email" name="email" required />



   </label>



   <label>



   Message



   <textarea id="message" name="message" required />



   </label>



   <button>Send</button>



   {#if responseMessage}



   <p>{responseMessage}</p>



   {/if}



   </form>
   ```

   src/components/FeedbackForm.vue

   ```
   <script setup lang="ts">



   import { ref } from "vue";



   const responseMessage = ref<string>();



   async function submit(e: Event) {



   e.preventDefault();



   const formData = new FormData(e.currentTarget as HTMLFormElement);



   const response = await fetch("/api/feedback", {



   method: "POST",



   body: formData,



   });



   const data = await response.json();



   responseMessage.value = data.message;



   }



   </script>



   <template>



   <form @submit="submit">



   <label>



   Name



   <input type="text" id="name" name="name" required />



   </label>



   <label>



   Email



   <input type="email" id="email" name="email" required />



   </label>



   <label>



   Message



   <textarea id="message" name="message" required />



   </label>



   <button>Send</button>



   <p v-if="responseMessage">{{ responseMessage }}</p>



   </form>



   </template>
   ```
4. Import and include your `<FeedbackForm />` component on a page. Be sure to use a `client:*` directive to ensure that the form logic is hydrated when you want it to be.

   * [Preact](#tab-panel-1870)
   * [React](#tab-panel-1871)
   * [Solid](#tab-panel-1872)
   * [Svelte](#tab-panel-1873)
   * [Vue](#tab-panel-1874)

   src/pages/index.astro

   ```
   ---



   import FeedbackForm from "../components/FeedbackForm"



   ---



   <FeedbackForm client:load />
   ```

   src/pages/index.astro

   ```
   ---



   import FeedbackForm from "../components/FeedbackForm"



   ---



   <FeedbackForm client:load />
   ```

   src/pages/index.astro

   ```
   ---



   import FeedbackForm from "../components/FeedbackForm"



   ---



   <FeedbackForm client:load />
   ```

   src/pages/index.astro

   ```
   ---



   import FeedbackForm from "../components/FeedbackForm.svelte"



   ---



   <FeedbackForm client:load />
   ```

   src/pages/index.astro

   ```
   ---



   import FeedbackForm from "../components/FeedbackForm.vue"



   ---



   <FeedbackForm client:load />
   ```

Recipes

![Scrimba](/_astro/Scrimba.ByZ1pAIN_1PqoUV.webp)
![](/_astro/JamesQuick.BYVczE5K_Z27c5s6.webp)

## **Learn Astro** with James Q Quick

Build your first site with 35 interactive Scrimba lessons

[Get 20% off](https://scrimba.com/intro-to-astro-c00ar0fi5u?via=astro)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/recipes/build-forms-api.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Build HTML forms in Astro pages](/en/recipes/build-forms/)
[Next

Use Bun with Astro](/en/recipes/bun/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)