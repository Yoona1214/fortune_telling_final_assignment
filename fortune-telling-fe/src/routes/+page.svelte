<script lang="ts">
	import { GenderSelect, DatePicker, MainMsgBox } from '$lib';
	import MsgBox from '$lib/components/msg-box.svelte';
	import { createQuery } from '@tanstack/svelte-query';

	type Step = 'welcome' | 'form' | 'overall' | 'detail';

	let step = $state<Step>('welcome');
	let date = $state<Date>(new Date('2000-01-01'));
	let dateSelected = $state(false);
	let gender = $state<'male' | 'female'>();

	const query = createQuery({
		queryKey: ['fortune'],
		queryFn: () =>
			fetch('/api/analyze', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					year: date?.getFullYear(),
					month: (date?.getMonth() || 0) + 1,
					day: date?.getDate(),
					hour: 12,
					sex: gender === 'male' ? 'M' : 'F'
				})
			}).then((res) => res.json() as Promise<{ success?: boolean; results?: [string, string] }>),
		enabled: false
	});

	let overallMsg = $derived($query.data?.results?.[0]);
	let detailMsg = $derived($query.data?.results?.[1]);

	async function analyze() {
		const res = await $query.refetch();
		if (res.data?.success && res.data?.results?.length) {
			step = 'overall';
			return;
		}
		alert('分析失败，请稍后再试');
	}
</script>

<div
	class="bg-illustration flex h-screen w-full flex-col items-center justify-end pb-[50px]"
	class:bg-on-answer-page={step === 'overall' || step === 'detail'}
>
	{#snippet formFields()}
		<div class="flex items-center gap-x-[24px]">
			<DatePicker bind:value={date} onSelectedChange={(selected) => (dateSelected = selected)} />
			<GenderSelect bind:value={gender} />
		</div>
	{/snippet}

	{#if step === 'welcome'}
		<MainMsgBox btnText="开始" onBtnClick={() => (step = 'form')}>
			{#snippet customMsg()}
				<p class="pb-[20px] text-lg">
					想知道未来会发生什么有趣的事吗？让我帮你算命，聊聊你的命运吧！
				</p>
			{/snippet}
		</MainMsgBox>
	{:else if step === 'form'}
		<MainMsgBox
			customMsg={formFields}
			btnText={$query.isFetching ? '分析中...' : '确定'}
			btnDisabled={!dateSelected || !date || !gender}
			onBtnClick={analyze}
		/>
		<MsgBox class="fixed bottom-1/2 right-1/2 -translate-x-[116px] -translate-y-[128px]">
			<p class="w-[214px] text-base">
				输入你的生日，这样我可以根据你的生辰信息为你提供一些有趣的命理分析和建议。
			</p>
		</MsgBox>
	{:else if step === 'overall'}
		<MainMsgBox
			msg={overallMsg}
			msgTextSize="md"
			btnText="下一页"
			onBtnClick={() => (step = 'detail')}
		/>
	{:else if step === 'detail'}
		<MainMsgBox
			msg={detailMsg}
			msgTextSize="md"
			btnText="上一页"
			extraBtnText="结束"
			onBtnClick={() => (step = 'overall')}
			onExtraBtnClick={() => {
				step = 'welcome';
				date = new Date('2000-01-01');
				gender = undefined;
			}}
		/>
	{/if}
</div>

<style scoped>
	.bg-illustration {
		background-image: url(/illustration-bg-normal.png);
		background-size: 1680px 870px;
		background-position: 40% calc(50% - 42px);
		background-repeat: no-repeat;
	}

	.bg-on-answer-page {
		background-image: url(/illustration-bg-answer.png);
	}
</style>
