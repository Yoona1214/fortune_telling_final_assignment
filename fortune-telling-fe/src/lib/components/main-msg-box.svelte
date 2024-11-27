<script lang="ts">
	import type { Snippet } from 'svelte';
	import MsgBox from './msg-box.svelte';
	import Button from './button.svelte';

	let {
		msg,
		customMsg,
		btnText,
		btnDisabled,
		extraBtnText,
		msgTextSize = 'md',
		onBtnClick,
		onExtraBtnClick
	}: {
		msg?: string;
		customMsg?: Snippet;
		btnText?: string;
		btnDisabled?: boolean;
		extraBtnText?: string;
		msgTextSize?: 'sm' | 'md' | 'lg';
		onBtnClick?: () => void;
		onExtraBtnClick?: () => void;
	} = $props();
</script>

<MsgBox>
	{#if customMsg}
		{@render customMsg()}
	{:else}
		<p
			class:text-xs={msgTextSize === 'sm'}
			class:text-base={msgTextSize === 'md'}
			class:text-lg={msgTextSize === 'lg'}
			class="max-w-[674px]"
		>
			{msg}
		</p>
	{/if}
	<div class="mt-[10px] flex items-center justify-center gap-4">
		<Button disabled={btnDisabled} onclick={onBtnClick}>{btnText}</Button>
		{#if extraBtnText}
			<Button onclick={onExtraBtnClick}>{extraBtnText}</Button>
		{/if}
	</div>
</MsgBox>
