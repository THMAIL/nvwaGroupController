<template>
	<!-- <el-row>
		<el-col :span="6" v-for="(o, index) in 26" :key="o" :offset="index > 0 ? 0 : 0">
			<el-card :body-style="{ padding: '0px' }">
				<img src="../../assets/img/blackMobile.png" class="image" />
				<div style="padding: 14px;">
					<span>好吃的汉堡</span>
					<div class="bottom clearfix">
						<time class="time">{{ currentDate }}</time>
					</div>
				</div>
			</el-card>
		</el-col>
	</el-row> -->
	<span></span>
</template>

<script>
export default {
	data() {
		return {
			currentDate: new Date()
		};
	},
	mounted() {
		this.$alert('敬请期待', '功能大全', {
			confirmButtonText: '确定',
			callback: action => {}
		});
	}
};
</script>

<style>
.time {
	font-size: 13px;
	color: #999;
}

.bottom {
	margin-top: 13px;
	line-height: 12px;
}

.button {
	padding: 0;
	float: right;
}

.image {
	width: 80%;
	height: 80%;
	margin-top: 3%;
	margin-left: 10%;
	display: block;
}

.clearfix:before,
.clearfix:after {
	display: table;
	content: '';
}

.clearfix:after {
	clear: both;
}
</style>
