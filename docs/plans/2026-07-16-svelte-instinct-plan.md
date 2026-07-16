# Svelte Instinct Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a Claude Code skill (`SKILL.md`) for Svelte Instinct, supporting version 4 and 5 with automatic detection, and verify it with a test suite.

**Architecture:** A single `SKILL.md` file containing rules and instructions. A helper Python validation script `scripts/validate.py` will read test directories and verify version detection logic.

**Tech Stack:** Markdown, YAML, Python (for validation script).

## Global Constraints
- Target Agent: Claude Code
- Support Versions: Svelte 4, Svelte 5, SvelteKit, TypeScript
- Must include automatic detection mechanism using `package.json` or syntax analysis

---

### Task 1: Create Validation Script & Test Scenarios

**Files:**
- Create: `svelte-instinct/scripts/validate.py`
- Create: `svelte-instinct/tests/svelte4/package.json`
- Create: `svelte-instinct/tests/svelte5/package.json`
- Create: `svelte-instinct/tests/fallback-svelte4/App.svelte`
- Create: `svelte-instinct/tests/fallback-svelte5/App.svelte`

**Interfaces:**
- Consumes: None
- Produces: Command line exit code 0 on success, 1 on failure.

- [ ] **Step 1: Create test directories and files representing different Svelte project structures**
- [ ] **Step 2: Write `scripts/validate.py` to parse package.json and detect version**
- [ ] **Step 3: Run the validation script and ensure it outputs correct detection results**
- [ ] **Step 4: Commit the test cases and script**

---

### Task 2: Write SKILL.md Instructions

**Files:**
- Create: `svelte-instinct/SKILL.md`

**Interfaces:**
- Consumes: Version detection rules and best practices list.
- Produces: Reusable instruction set compliant with Claude Code skill format.

- [ ] **Step 1: Write YAML frontmatter for `SKILL.md`**
- [ ] **Step 2: Add automatic version detection guidelines section**
- [ ] **Step 3: Add Svelte 4 specific guidelines section**
- [ ] **Step 4: Add Svelte 5 specific guidelines section**
- [ ] **Step 5: Add TypeScript and SvelteKit specific guidelines section**
- [ ] **Step 6: Verify YAML structure and commit**

---

### Task 3: Final Verification and README

**Files:**
- Create: `svelte-instinct/README.md`

**Interfaces:**
- Consumes: `SKILL.md`
- Produces: Clean user-facing documentation on how to install and use this skill.

- [ ] **Step 1: Create a simple README with installation commands and usage examples**
- [ ] **Step 2: Run a final validation checking all files**
- [ ] **Step 3: Commit all changes**
