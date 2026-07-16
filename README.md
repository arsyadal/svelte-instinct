# svelte-instinct

A Claude Code skill that enforces correct Svelte 4 and Svelte 5 best practices, automatically detects Svelte versions in your codebase, and prevents mixing paradigms with React or Vue.

## Installation

Add this skill to your Claude Code agent with:

```bash
npx skills add arsyadal/svelte-instinct --skill svelte-instinct --agent claude-code -g
```

## Comparison

### 1. Generated WITHOUT Svelte-Instinct Skill (Buggy Reactivity)
When AI is not guided, it often writes static properties or mixes legacy syntax, resulting in broken reactivity. In the example below, clicking the button increments the local counter, but the calculated "Double" value remains stuck at `0`:

![Without Svelte-Instinct](demo-without-skill.png)

### 2. Generated WITH Svelte-Instinct Skill (Perfect Svelte 5 Runes)
With the skill active, Claude Code is guided to use `$state()` and `$derived()` Runes correctly. Everything updates dynamically in real-time as expected:

![With Svelte-Instinct](demo-with-skill.png)

## Features

- **Automatic Version Detection:** Reads `package.json` or analyzes `.svelte` files to determine whether to apply Svelte 4 or Svelte 5 rules.
- **Strict Guidelines:** Ensures Svelte 4 uses standard `let` / `export let` / `$:`, while Svelte 5 enforces Runes (`$state`, `$derived`, `$props`, `$effect`), Snippets, and new event handlers (`onclick` instead of `on:click`).
- **TypeScript & SvelteKit Support:** Provides clear patterns for typing props and receiving data from page load functions.
- **Advanced Core Cases:** Fully supports two-way bindings with `$bindable()`, Svelte 5 lifecycle cleanups inside `$effect()`, and reactive state in `.svelte.js`/`.svelte.ts` files instead of legacy stores.

## Version Override

If your project doesn't have a `package.json` at the workspace root, or you want to explicitly force a specific Svelte version for a file, place one of these comments at the very beginning of the `.svelte` file:

```html
<!-- svelte-version: 4 -->
```
or
```html
<!-- svelte-version: 5 -->
```
