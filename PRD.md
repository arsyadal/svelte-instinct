# PRD: Svelte Best Practices Agent Skill

## 1. Core Objectives
This skill instructs Claude Code (and other AI agents) to:
1. **Write Clean, Correct Svelte:** Prevent rendering framework mixups (no React/Vue syntax in Svelte files).
2. **Support Svelte 4 & 5 Automatically:** Apply version-specific rules based on the project's Svelte version.
3. **Avoid Anti-patterns:** Block legacy reactivity habits in Svelte 5, and prevent direct mutations of props in Svelte 4.

## 2. Automatic Version Detection
The skill checks the active project environment using this sequence:
1. **package.json:** Scan the nearest `package.json` for the `svelte` dependency version.
   - Version `>= 5.0.0-0` -> Svelte 5 (Runes Mode)
   - Version `< 5.0.0` -> Svelte 4 (Legacy Mode)
2. **Syntax Fallback:** If no `package.json` is found, scan the active file content:
   - Contains `$state(`, `$derived(`, `$effect(` -> Svelte 5
   - Contains `$:`, `writable(` -> Svelte 4
3. **Explicit Override:** If a file starts with `<!-- svelte-version: 4 -->` or `<!-- svelte-version: 5 -->`, use that version directly.
4. **Default:** Svelte 5.

## 3. Rulesets & Guardrails

### A. Svelte 4 (Legacy Mode)
- **State:** Declare local state with standard variables: `let count = 0;`.
- **Props:** Declare props with `export let name;`.
- **Reactivity:** Use label `$: double = count * 2;` for derived values and side effects.
- **Global State (Stores):** Use `writable`, `readable`, `derived` from `svelte/store`. Subscribe in markup using the `$` prefix (e.g., `$myStore`).
- **Slots:** Use `<slot />` for children composition.
- **Events:** Use `on:click={handler}` for DOM events, and `createEventDispatcher` for custom events.
- **TypeScript:** Annotate inline (`export let name: string;`).
- **SvelteKit Route Data:** Bind route page data via `export let data;`.

### B. Svelte 5 (Modern Runes Mode)
- **State:** Use `$state()` rune: `let count = $state(0);`.
- **Props:** Use `$props()` rune: `let { name, age } = $props();`.
- **Derived Values:** Use `$derived()` rune: `let double = $derived(count * 2);`. Do not use `$:`.
- **Effects:** Use `$effect()` rune for post-rendering side effects. Do not use `$:`.
- **Global State:** Prefer standard state objects or runes in shared JS/TS files. Avoid the `$` store prefix in Rune-based components.
- **Slots/Snippets:** Use snippets `{#snippet children()}...{/snippet}` and the `children` prop. Do not use `<slot />`.
- **Events:** Use native HTML event attributes `onclick={handler}`. For custom parent events, use function callbacks passed via `$props()` (e.g., `let { onnotify } = $props();`).
- **TypeScript:** Define types directly on the destructured `$props()` statement.
- **SvelteKit Route Data:** Bind route page data via `let { data } = $props();`.
