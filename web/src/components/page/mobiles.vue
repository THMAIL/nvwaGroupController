<template>
	<el-row>
		<!-- <el-alert title="成功提示的文案" type="success" effect="dark"></el-alert> -->
		<el-tabs v-model="activeName" @tab-click="handleClick" id="console">
			<el-tab-pane label="收起控制台" name="thirdth"></el-tab-pane>
			<el-tab-pane label="保存设备" name="first" class="consoleTab">
				<el-radio v-model="radio1" label="1">全选</el-radio>
				<el-radio v-model="radio1" label="2">全不选</el-radio>
				<el-button type="primary">保存</el-button>
				<el-button type="info">取消</el-button>
			</el-tab-pane>
			<el-tab-pane label="删除设备" name="second" class="consoleTab">
				<el-radio v-model="radio2" label="1">全选</el-radio>
				<el-radio v-model="radio2" label="2">全不选</el-radio>
				<el-button type="primary">保存</el-button>
				<el-button type="info">取消</el-button>
			</el-tab-pane>
			<el-tab-pane label="执行脚本" name="third" class="consoleTab">
				<el-radio v-model="radio3" label="1">全选</el-radio>
				<el-radio v-model="radio3" label="2">全不选</el-radio>
				<el-select v-model="value" placeholder="选择脚本">
					<el-option v-for="item in scripts" :key="item.value" :label="item.label" :value="item.value"></el-option>
				</el-select>
				<el-button type="primary">执行</el-button>
				<el-button type="info">取消</el-button>
			</el-tab-pane>
			<el-tab-pane label="定时任务" name="fourth" class="consoleTab">
				<el-radio v-model="radio4" label="1">全选</el-radio>
				<el-radio v-model="radio4" label="2">全不选</el-radio>
				<div class="block">
					<el-date-picker v-model="value1" type="datetime" placeholder="选择日期时间" style="width: 100%;"></el-date-picker>
				</div>
				<el-select v-model="value" placeholder="选择脚本">
					<el-option v-for="item in scripts" :key="item.value" :label="item.label" :value="item.value"></el-option>
				</el-select>
				<el-button type="primary">确认</el-button>
				<!-- <el-button type="info">取消</el-button> -->
			</el-tab-pane>
			<el-tab-pane label="状态说明" name="fifth" class="consoleTab">
				<el-alert title="在线设备:已保存的设备,且在线,关闭系统不会丢失" type="success" :closable="false"></el-alert>
				<el-alert title="离线设备:已保存的设备,且离线,关闭系统不会丢失" type="error" :closable="false"></el-alert>
				<el-alert title="临时设备:未保存的设备,临时使用,若离线直接消失,清除出系统,不会显示离线," type="warning" :closable="false"></el-alert>
			</el-tab-pane>
		</el-tabs>
		<!-- <el-col :span="6" v-for="(o, index) in 10" :key="o" :offset="index > 0 ? 0 : 0"> -->
		<el-col :span="6" :key="o" :offset="index > 0 ? 0 : 0">
			<MobileCard mobile-id='test' mobile-name='设备001'></MobileCard>
		</el-col>
		<el-backtop target=".page-component__scroll .el-scrollbar__wrap"></el-backtop>
	</el-row>
</template>

<script>
import bus from '../common/bus.js';
import MobileCard from '../common/MobileCard.vue';
export default {
	components: {
		MobileCard
	},
	data() {
		return {
			radio1: '1',
			radio2: '1',
			radio3: '1',
			radio4: '1',
			scripts: [
				{
					value: '选项1',
					label: '批量登录微信'
				},
				{
					value: '选项2',
					label: '批量发朋友圈'
				}
			],
			number:1
		};
	}
};
</script>

<style>
#console {
	margin-left: 25%;
	margin-right: 22%;
	margin-bottom: 5%;
	display: none;
}

.consoleTab {
	display: flex;
	flex-wrap: wrap;
	align-items: center;
	justify-content: space-around;
}

el-tab-pane {
	display: block;
}
</style>
