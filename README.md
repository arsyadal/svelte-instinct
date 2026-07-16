# svelte-best-practices

A Claude Code skill that enforces correct Svelte 4 and Svelte 5 best practices, automatically detects Svelte versions in your codebase, and prevents mixing paradigms with React or Vue.

## Installation

Add this skill to your Claude Code agent with:

```bash
npx skills add arsyadal/svelte-best-practices --skill svelte-best-practices --agent claude-code -g
```

*(Ganti `arsyadal` dengan username GitHub Anda jika Anda memindahkan repositori ini ke akun lain)*

## Features

- **Automatic Version Detection:** Reads `package.json` or analyzes `.svelte` files to determine whether to apply Svelte 4 or Svelte 5 rules.
- **Strict Guidelines:** Ensures Svelte 4 uses standard `let` / `export let` / `$:`, while Svelte 5 enforces Runes (`$state`, `$derived`, `$props`, `$effect`), Snippets, and new event handlers (`onclick` instead of `on:click`).
- **TypeScript & SvelteKit Support:** Provides clear patterns for typing props and receiving data from page load functions.

## Version Override

If your project doesn't have a `package.json` at the workspace root, or you want to explicitly force a specific Svelte version for a file, place one of these comments at the very beginning of the `.svelte` file:

```html
<!-- svelte-version: 4 -->
```
or
```html
<!-- svelte-version: 5 -->
```
