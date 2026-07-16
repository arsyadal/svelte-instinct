<script>
  export let name = 'World';
  let count = 0;
  $: double = count * 2;
</script>

<h1>Hello {name}!</h1>
<button on:click={() => count++}>Count: {count} (double: {double})</button>
