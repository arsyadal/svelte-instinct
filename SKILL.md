---
name: svelte-instinct
description: "Guidelines and rules for writing correct Svelte 4 and Svelte 5 components. Ensures automatic version detection and prevents React/Vue mixups."
version: "0.1.0"
---

# Svelte Instinct

This skill guides the AI to write idiomatic Svelte 4 and Svelte 5 code. It helps you detect the correct Svelte version of a project, write correct syntax, and avoid mixing paradigms with React or Vue.

## 1. Automatic Version Detection

Before writing or modifying any Svelte files, you must detect the version of Svelte used in the project. Follow this sequence:

1. **Check package.json:** Read the closest `package.json` file. Check the `dependencies` or `devDependencies` for `"svelte"`.
   - If the version is `>= 5.0.0-0`, apply **Svelte 5 (Runes Mode)**.
   - If the version is `< 5.0.0`, apply **Svelte 4 (Legacy Mode)**.
2. **Fallback Syntax Analysis:** If `package.json` is missing or the version is not specified, scan the existing `.svelte` files in the workspace:
   - If they contain `$state(`, `$derived(`, `$effect(`, or `$props(`, apply **Svelte 5**.
   - If they contain reactive labels (`$:`) or store imports (`writable`, `readable`), apply **Svelte 4**.
3. **Explicit Override:** If the file begins with the comment `<!-- svelte-version: 4 -->` or `<!-- svelte-version: 5 -->`, respect that override explicitly regardless of package.json.
4. **Default:** If undetected, default to **Svelte 5**.

---

## 2. Rulesets & Guardrails

### A. Svelte 4 (Legacy Mode)

Ensure you follow these syntax rules when Svelte 4 is active:

1. **Reactivity & State:**
   - Declare local state using standard `let` declarations: `let count = 0;`.
   - Never use runes like `$state()`, `$derived()`, `$props()`, or `$effect()`.
2. **Properties (Props):**
   - Declare properties to be passed by parents using `export let`: `export let name = 'World';`.
3. **Reactive Declarations & Statements:**
   - Use the `$:` label for derived values: `$: double = count * 2;`.
   - Use `$:` for reactive side effects: `$: console.log('count changed to', count);`.
4. **Stores:**
   - Use stores for global state (`writable`, `readable`, `derived` from `'svelte/store'`).
   - Subscribe to stores in the HTML markup using the `$` prefix (e.g., `{$userStore}`).
5. **Slots:**
   - Use `<slot />` or named slots `<slot name="header" />` for composing children.
6. **Events:**
   - Register event listeners using the `on:click={handler}` syntax.
   - Dispatch custom events using `createEventDispatcher` from `'svelte'`.
7. **TypeScript:**
   - Type props on the export statement: `export let name: string;`.
8. **SvelteKit route pages:**
   - Bind page data using: `export let data;`.
9. **Two-Way Bindings:**
   - In Svelte 4, bind props inside parent components with `bind:propName={variable}`. In child components, directly mutate the prop (`export let value; value = newValue`).
10. **Lifecycle Hooks:**
    - Import and use traditional lifecycle hooks from `'svelte'`: `onMount`, `beforeUpdate`, `afterUpdate`, and `onDestroy`.
11. **Shared State:**
    - Export stores from `.js` or `.ts` files:
      ```javascript
      import { writable } from 'svelte/store';
      export const countStore = writable(0);
      ```

### B. Svelte 5 (Modern Runes Mode)

Ensure you follow these syntax rules when Svelte 5 is active:

1. **Reactivity & State (Runes):**
   - Declare local state using the `$state()` rune: `let count = $state(0);`.
   - Never use the `$:` label or raw `let` variables for reactive values.
2. **Properties (Props):**
   - Declare properties using the `$props()` rune: `let { name = 'World', age } = $props();`.
   - Do not use `export let`.
3. **Derived Values:**
   - Declare derived/computed values using the `$derived()` rune: `let double = $derived(count * 2);`.
4. **Effects (Side Effects):**
   - Use `$effect()` for running code after DOM updates:
     ```javascript
     $effect(() => {
       console.log('count changed to', count);
     });
     ```
5. **Composing Components (Snippets & Children):**
   - Render children using the `children` prop: `let { children } = $props();` and `{@render children()}`.
   - Do not use `<slot />`. Use `{#snippet name()}...{/snippet}` and `{@render name()}` for template blocks.
6. **Events:**
   - Use native event properties like `onclick={handler}` (all lowercase, no colon).
   - Do not use `createEventDispatcher`. Pass custom event callbacks as functions in props:
     ```javascript
     let { onchange } = $props();
     // inside component:
     onchange(newValue);
     ```
7. **TypeScript:**
   - Type your props within the destructuring of `$props()`:
     ```typescript
     let { name, status }: { name: string; status: 'active' | 'inactive' } = $props();
     ```
8. **SvelteKit route pages:**
   - Receive data via the props rune: `let { data } = $props();`.
9. **Two-Way Bindings ($bindable):**
   - For variables that sync back to the parent, use the `$bindable()` rune inside `$props()`:
     ```typescript
     let { value = $bindable() } = $props();
     ```
   - On the parent side, call it using `bind:value={parentVariable}`.
10. **Lifecycle Hook Changes:**
    - Do not use `beforeUpdate`, `afterUpdate`, or `onDestroy` hooks in Svelte 5.
    - Use `$effect()` for post-render side effects.
    - Handle cleanup (destruction phase) by returning a function from `$effect()`:
      ```javascript
      $effect(() => {
        const listener = () => console.log('scrolled');
        window.addEventListener('scroll', listener);
        return () => window.removeEventListener('scroll', listener); // cleanup
      });
      ```
11. **Shared State in JS/TS (.svelte.js/.svelte.ts):**
    - Avoid `svelte/store` (writable/readable) for new Svelte 5 shared files.
    - Instead, use `.svelte.js` or `.svelte.ts` files containing `$state` objects or class-based reactive state:
      ```typescript
      // store.svelte.ts
      export const globalState = $state({
        user: null,
        theme: 'dark'
      });
      ```
      Import and use `globalState` directly. No `$` prefix subscription is needed.
