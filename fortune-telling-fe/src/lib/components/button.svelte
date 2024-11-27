<script lang="ts">
	import type { MouseEventHandler } from 'svelte/elements';
	import type { Snippet } from 'svelte';

	let {
		children,
		type = 'button',
		disabled = false,
		className = '',
		onclick
	}: {
		children?: Snippet;
		type?: 'button' | 'submit' | 'reset';
		disabled?: boolean;
		className?: string;
		onclick?: MouseEventHandler<HTMLButtonElement>;
	} = $props();
</script>

<button
	{type}
	{disabled}
	class:cursor-not-allowed={disabled}
	class:pointer-events-none={disabled}
	class:opacity-50={disabled}
	class="h-[52px] w-[225px] border text-2xl text-[#FFF5A4] {className}"
	{onclick}
>
	{@render children?.()}
</button>

<style scoped>
	.border {
		border-image-source: url(/btn-bg.png);
		border-image-width: 23px;
		border-image-slice: 46 fill;
	}
</style>
