<template>
	<el-collapse v-model="activeName" accordion>
		<el-collapse-item title="使用方法" name="1">
			<div>1.手机通过usb连接电脑 =》 打开开发者模式 =》信任电脑</div>
			<div>2.系统会自动添加并显示新设备到页面</div>
			<div>3.若一直没有添加成功，则尝试重新插拔usb连接</div>
		</el-collapse-item>
	</el-collapse>
</template>

<script>
export default {
	data() {
		return {
			activeName: '1'
		};
	}
};
</script>

<style></style>
