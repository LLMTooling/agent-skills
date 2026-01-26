# Agent Skills Collection

A curated collection of specialized skills designed to extend the capabilities of AI agents such as Claude Code and Gemini CLI. Each skill has been personally built and rigorously tested to ensure reliability and performance.

## What are Agent Skills?

Agent Skills are an open format for providing AI agents with new capabilities and expertise. They are packages containing instructions, scripts, and resources that allow agents to:

*   **Extend functionalities** on demand.
*   **Incorporate specialized knowledge** (e.g., specific frameworks, languages).
*   **Execute repeatable workflows** across compatible agent environments.

For more detailed information, visit [agentskills.io](https://agentskills.io/home).

## Available Skills

This repository includes a variety of skills located in the `skills/` directory:

### Development & Frameworks
*   **astro-build**: Comprehensive documentation for Astro, the web framework for content-driven websites.
*   **auto-animate**: Zero-config animation utility (AutoAnimate) for smooth transitions.
*   **best-practices**: Universal software engineering best practices for any language or project (SOLID, DRY, KISS, YAGNI, architectural patterns).
*   **biome**: Comprehensive integration for Biome (linting, formatting) in TypeScript/JavaScript.
*   **claude-code-hooks**: Interactive skill for setting up Claude Code hooks in any workspace (automation, notifications, validation).
*   **code-cleanup-final-pass**: Deep code review and cleanup workflow for final quality checks.
*   **electron**: Complete Electron documentation for building cross-platform desktop applications with JavaScript, HTML, and CSS.
*   **electron-builder**: Electron app packaging and distribution configuration for macOS, Windows, and Linux.
*   **electron-store**: Data persistence library for Electron apps (JSON file storage, schema validation, migrations).
*   **electron-vite**: Build Electron apps with Vite.
*   **eslint**: Professional-grade ESLint setup and management for JS/TS projects.
*   **expo**: Production-grade Expo and React Native development framework with SDK documentation, EAS integration, and navigation.
*   **expo-android-widgets**: Build Android home screen widgets for React Native Expo apps.
*   **fastmcp-v3-migration**: Production-ready migration guide from FastMCP v2.x to v3.0.
*   **gemini-cli**: Programmatic interaction with Google's Gemini models via gemini-cli headless mode.
*   **gemini-collaborate**: Agentic collaboration with Google Gemini for large-context code reviews and analysis.
*   **gemini-genkit**: Guide for building AI apps with Google's Gemini API and Firebase Genkit.
*   **go-best-practices**: Go development guidelines based on Google's Go Style Guide.
*   **go2rtc**: Camera streaming application supporting 30+ streaming protocols and camera brands.
*   **home-assistant-dev**: Development guide for Home Assistant custom integrations.
*   **ink-tui**: Build interactive Terminal User Interfaces (TUIs) with React and Ink.
*   **lenis**: Lightweight smooth scroll library documentation and implementation.
*   **lucide-react**: Lucide React icon toolkit for React applications.
*   **mcp-setup**: Set up MCP (Model Context Protocol) servers in Claude Code workspaces for testing.
*   **mcp-test-harness**: Build fully automated integration test suites for MCP servers using STDIO transport.
*   **modern-frontend-design**: Principles for creating high-quality, modern frontend interfaces.
*   **motion**: Animation library guide for React, vanilla JS, and Vue.
*   **mypy**: Professional static type checking for Python.
*   **nativewind**: NativeWind v4 for React Native - use Tailwind CSS to style React Native components.
*   **playwright-cli**: Browser automation and testing with Playwright CLI.
*   **pydantic-dev**: Data validation and serialization with Pydantic v2.
*   **radix-ui**: Comprehensive documentation for Radix UI (Themes, Primitives, Colors).
*   **react-19**: Documentation and features for React 19.
*   **react-native**: Complete React Native framework documentation for building native mobile apps with JavaScript.
*   **react-three-fiber**: Guide for building 3D experiences with React Three Fiber (R3F).
*   **ruff-dev**: Extremely fast Python linting and formatting with Ruff.
*   **rust-dev**: Rust development best practices and tooling.
*   **shadcn**: Guide for using shadcn/ui components and theming.
*   **svelte5**: Comprehensive guide for Svelte 5 (runes, components, SvelteKit).
*   **tailwind-css**: Professional development with Tailwind CSS (v3 and v4).
*   **threejs**: Comprehensive Three.js documentation and reference for 3D graphics.
*   **trpc**: Comprehensive tRPC documentation and reference covering v10.x and v11.x.
*   **typescript-best-practices**: TypeScript best practices and patterns for writing type-safe, maintainable code.
*   **vite**: Vite 7.x build tool documentation for core configuration, dev server, and HMR.
*   **zod**: TypeScript-first schema validation with static type inference.

### Utilities & Tools
*   **get-time**: Utilities to retrieve current local time and date.
*   **github-wikis**: Guide for managing and editing GitHub repository wikis.
*   **gsap**: Professional animation development with GreenSock (GSAP).
*   **local-skill-creator**: Toolkit for creating and packaging your own skills locally.
*   **motion**: Animation library guide for React, vanilla JS, and Vue.
*   **pdf-to-markdown**: Convert PDF documents to LLM-friendly Markdown.
*   **plugin-builder**: Build, package, and publish Claude Code plugins.
*   **uiverse**: Extract HTML and CSS code from UIVerse.io UI components.
*   **v0-version-planner**: Planning tool for validating dependency versions before prototyping.
*   **web-scraper**: Web scraping utility with Cloudflare bypass capabilities.

### Migration
*   **node-to-bun-migration**: Guide for migrating Node.js projects to Bun.
*   **node-to-deno-migration**: Guide for migrating Node.js projects to Deno 2.0+.
*   **npm-to-pnpm**: Migrate projects from npm to pnpm including lockfile conversion and workspace setup.

## Usage

Each skill is packaged as a `.skill` file in the `skills/` directory. Consult your specific AI agent's documentation on how to import or enable these skills.