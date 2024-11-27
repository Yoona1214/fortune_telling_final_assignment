<script lang="ts">
	let { value = $bindable() }: { value?: 'male' | 'female' } = $props();
</script>

<select
	bind:value
	class:text-black={value}
	class="h-[37px] w-[154px] appearance-none rounded-full border-none bg-[#79322C26] py-[6px] text-center text-lg leading-[25px] text-[#00000040] outline-none"
>
	<option value="" disabled selected hidden>性别</option>
	<option value="male">男</option>
	<option value="female">女</option>
</select>
