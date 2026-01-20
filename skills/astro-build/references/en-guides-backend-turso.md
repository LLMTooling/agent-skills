<!-- Source: https://docs.astro.build/en/guides/backend/turso/ -->

# Turso & Astro

[Turso](https://turso.tech) is a distributed database built on libSQL, a fork of SQLite. It is optimized for low query latency, making it suitable for global applications.

## Initializing Turso in Astro

[Section titled “Initializing Turso in Astro”](#initializing-turso-in-astro)

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* The [Turso CLI](https://docs.turso.tech/cli/introduction) installed and signed in
* A [Turso](https://turso.tech) Database with schema
* Your Database URL
* An Access Token

### Configure environment variables

[Section titled “Configure environment variables”](#configure-environment-variables)

Obtain your database URL using the following command:

Terminal window

```
turso db show <database-name> --url
```

Create an auth token for the database:

Terminal window

```
turso db tokens create <database-name>
```

Add the output from both commands above into your `.env` file at the root of your project. If this file does not exist, create one.

.env

```
TURSO_DATABASE_URL=libsql://...



TURSO_AUTH_TOKEN=
```

Caution

Do not use the `PUBLIC_` prefix when creating these private [environment variables](/en/guides/environment-variables/). This will expose these values on the client.

### Install LibSQL Client

[Section titled “Install LibSQL Client”](#install-libsql-client)

Install the `@libsql/client` to connect Turso to Astro:



* [npm](#tab-panel-2711)
* [pnpm](#tab-panel-2712)
* [Yarn](#tab-panel-2713)

Terminal window

```
npm install @libsql/client
```

Terminal window

```
pnpm add @libsql/client
```

Terminal window

```
yarn add @libsql/client
```



### Initialize a new client

[Section titled “Initialize a new client”](#initialize-a-new-client)

Create a file `turso.ts` in the `src` folder and invoke `createClient`, passing it `TURSO_DATABASE_URL` and `TURSO_AUTH_TOKEN`:

src/turso.ts

```
import { createClient } from "@libsql/client/web";



export const turso = createClient({



url: import.meta.env.TURSO_DATABASE_URL,



authToken: import.meta.env.TURSO_AUTH_TOKEN,



});
```

## Querying your database

[Section titled “Querying your database”](#querying-your-database)

To access information from your database, import `turso` and [execute a SQL query](https://docs.turso.tech/sdk/ts/reference#simple-query) inside any `.astro` component.

The following example fetches all `posts` from your table, then displays a list of titles in a `<BlogIndex />` component:

src/components/BlogIndex.astro

```
---



import { turso } from '../turso'



const { rows } = await turso.execute('SELECT * FROM posts')



---



<ul>



{rows.map((post) => (



<li>{post.title}</li>



))}



</ul>
```

### SQL Placeholders

[Section titled “SQL Placeholders”](#sql-placeholders)

The `execute()` method can take [an object to pass variables to the SQL statement](https://docs.turso.tech/sdk/ts/reference#placeholders), such as `slug`, or pagination.

The following example fetches a single entry from the `posts` table `WHERE` the `slug` is the retrieved value from `Astro.params`, then displays the title of the post.

src/pages/index.astro

```
---



import { turso } from '../turso'



const { slug } = Astro.params



const { rows } = await turso.execute({



sql: 'SELECT * FROM posts WHERE slug = ?',



args: [slug!]



})



---



<h1>{rows[0].title}</h1>
```

## Turso Resources

[Section titled “Turso Resources”](#turso-resources)

* [Turso Docs](https://docs.turso.tech)
* [Turso on GitHub](https://github.com/tursodatabase)
* [Using Turso to serve a Server-side Rendered Astro blog’s content](https://blog.turso.tech/using-turso-to-serve-a-server-side-rendered-astro-blogs-content-58caa6188bd5)

## More backend service guides

* ![](/logos/appwriteio.svg)

  ### [Appwrite](/en/guides/backend/appwrite/)
* ![](/logos/firebase.svg)

  ### [Firebase](/en/guides/backend/firebase/)
* ![](/logos/neon.svg)

  ### [Neon](/en/guides/backend/neon/)
* ![](/logos/prisma-postgres.svg)

  ### [Prisma Postgres](/en/guides/backend/prisma-postgres/)
* ![](/logos/sentry.svg)

  ### [Sentry](/en/guides/backend/sentry/)
* ![](/logos/supabase.svg)

  ### [Supabase](/en/guides/backend/supabase/)
* ![](/logos/turso.svg)

  ### [Turso](/en/guides/backend/turso/)
* ![](/logos/xata.svg)

  ### [Xata](/en/guides/backend/xata/)

Recipes

![](/_astro/CodingInPublic.DpaYu7Qd_5sx41.webp)

## Learn Astro with **Coding in Public**

150+ video lessons
•
Astro v5 ready

[Get 20% off](https://learnastro.dev?code=ASTRO_PROMO)

[Edit page](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/backend/turso.mdx)
[Translate this page](https://contribute.docs.astro.build/guides/i18n/)

[Previous

Supabase](/en/guides/backend/supabase/)
[Next

Xata](/en/guides/backend/xata/)

[Contribute](/en/contribute/)
[Community](https://astro.build/chat)
[Sponsor](https://opencollective.com/astrodotbuild)