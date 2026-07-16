<script>
  let { name = 'World' } = $props();
  let count = $state(0);
  let double = $derived(count * 2);
</script>

<h1>Hello {name}!</h1>
<button onclick={() => count++}>Count: {count} (double: {double})</button>
