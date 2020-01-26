<template>
	<span></span>
</template>

<script>
import VueClipboard from 'vue-clipboard2';

export default {
	methods: {
		feedback() {
			this.$alert('反馈建议请在github上提交https://github.com/THMAIL/nvwaGroupController', '反馈建议', {
				confirmButtonText: '确定',
				callback: action => {
					
				}
			});
		},
		// 复制成功
		onCopy(e) {
			this.$message({
				message: '复制成功！',
				type: 'success'
			});
		},
		// 复制失败
		onError(e) {
			this.$message({
				message: '复制失败！',
				type: 'error'
			});
		}
	},
	mounted() {
		this.feedback();
	}
};
</script>
<style></style>
