<script lang="ts">
	import { Datepicker } from 'svelte-calendar';

	let {
		value = $bindable(),
		onSelectedChange
	}: { value?: Date; onSelectedChange?: (selected: boolean) => void } = $props();

	let store = $state<any>();

	const startDay = new Date('1919-12-31');
	const endDay = new Date('2019-12-31');
	const theme = {
		calendar: {
			width: '280px',
			maxWidth: '100vw',
			legend: {
				height: '45px'
			},
			shadow: '0px 10px 26px rgba(0, 0, 0, 0.25)',
			colors: {
				text: {
					primary: '#333',
					highlight: '#FFF5A4'
				},
				background: {
					primary: '#fff',
					highlight: '#78312C',
					hover: '#ECDBC6'
				},
				border: '#eee'
			},
			font: {
				regular: '1.5em',
				large: '14em'
			},
			grid: {
				disabledOpacity: '.35',
				outsiderOpacity: '.6'
			}
		}
	};

	let year = $derived(($store.selected as Date)?.getFullYear());
	let month = $derived((($store.selected as Date)?.getMonth() ?? 0) + 1);
	let day = $derived(($store.selected as Date)?.getDate());

	$effect(() => {
		onSelectedChange?.($store.hasChosen);
	});
</script>

<Datepicker bind:selected={value} bind:store let:key let:send let:receive start={startDay} end={endDay} {theme}>
	<button
		class="flex items-center gap-x-[24px]"
		in:receive|local={{ key }}
		out:send|local={{ key }}
	>
		<div
			class:text-black={$store.hasChosen}
			class="h-[37px] w-[154px] rounded-full bg-[#79322C26] py-[6px] text-center text-lg leading-[25px] text-[#00000040]"
		>
			{$store.hasChosen ? year : '年'}
		</div>
		<div
			class:text-black={$store.hasChosen}
			class="h-[37px] w-[154px] rounded-full bg-[#79322C26] py-[6px] text-center text-lg leading-[25px] text-[#00000040]"
		>
			{$store.hasChosen ? month : '月'}
		</div>
		<div
			class:text-black={$store.hasChosen}
			class="h-[37px] w-[154px] rounded-full bg-[#79322C26] py-[6px] text-center text-lg leading-[25px] text-[#00000040]"
		>
			{$store.hasChosen ? day : '日'}
		</div>
	</button>
</Datepicker>
