<script lang="ts">
	import type { Snippet } from 'svelte';

	let { children, class: className }: { children?: Snippet; class?: string } = $props();
</script>

<div class="w-fit border px-[38px] py-[30px] transition-all {className}">
	{@render children?.()}
</div>

<style scoped>
	.border {
		border-image-source: url(/msg-bg.png);
		border-image-width: 48px;
		border-image-slice: 96 fill;
	}
</style>
