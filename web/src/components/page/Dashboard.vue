<template>
	<div>
		<el-row :gutter="20">
			<el-col :span="8">
				<el-card shadow="hover" class="mgb20" style="height:252px;">
					<div class="user-info">
						<img src="../../assets/img/img.jpg" class="user-avator" alt />
						<div class="user-info-cont">
							<div class="user-info-name">{{ name }}</div>
							<div>{{ role }}</div>
						</div>
					</div>
					<div class="ip">
						局域网IP：
						<span>{{ LANIP }}</span>
					</div>
					<div class="ip">
						公网IP：
						<span>{{ WANIP }}</span>
					</div>
				</el-card>
				<el-card shadow="hover" style="height:252px;">
					<div slot="header" class="clearfix"><span>营销用户分析</span></div>
					知乎用户
					<el-progress :percentage="71.3" color="#42b983"></el-progress>
					微信用户
					<el-progress :percentage="24.1" color="#f1e05a"></el-progress>
					QQ用户
					<el-progress :percentage="13.7"></el-progress>
					陌陌用户
					<el-progress :percentage="5.9" color="#f56c6c"></el-progress>
				</el-card>
			</el-col>
			<el-col :span="16">
				<el-row :gutter="20" class="mgb20">
					<el-col :span="8">
						<el-card shadow="hover" :body-style="{ padding: '0px' }">
							<div class="grid-content grid-con-1">
								<i class="el-icon-lx-people grid-con-icon"></i>
								<div class="grid-cont-right">
									<div class="grid-num">{{ mobileCountOnline }}</div>
									<div>在线手机</div>
								</div>
							</div>
						</el-card>
					</el-col>
					<el-col :span="8">
						<el-card shadow="hover" :body-style="{ padding: '0px' }">
							<div class="grid-content grid-con-3">
								<i class="el-icon-lx-goods grid-con-icon"></i>
								<div class="grid-cont-right">
									<div class="grid-num">{{ mobileCountOffline }}</div>
									<div>离线手机</div>
								</div>
							</div>
						</el-card>
					</el-col>
					<el-col :span="8">
						<el-card shadow="hover" :body-style="{ padding: '0px' }">
							<div class="grid-content grid-con-2">
								<i class="el-icon-lx-notice grid-con-icon"></i>
								<div class="grid-cont-right">
									<div class="grid-num">{{ systemMessage }}</div>
									<div>系统消息</div>
								</div>
							</div>
						</el-card>
					</el-col>
				</el-row>
				<el-card shadow="hover" style="height:403px;">
					<div slot="header" class="clearfix">
						<span>待办事项</span>
						<el-button v-if="editStatus" style="float: right; padding: 3px 3px" type="text" v-on:click="edit()">编辑</el-button>
						<el-button v-else style="float: right; padding: 3px 3px" type="text" v-on:click="cancel()">取消</el-button>
						<el-button v-if="editStatus" style="float: right; padding: 3px 3px" type="text" v-on:click="add">添加</el-button>
						<el-button v-else style="float: right; padding: 3px 3px" type="text" v-on:click="save()">保存</el-button>
					</div>
					<el-table :show-header="false" :data="todoList" style="width:100%;" max-height="320px">
						<el-table-column width="40">
							<template slot-scope="scope">
								<el-checkbox v-model="scope.row.status"></el-checkbox>
							</template>
						</el-table-column>
						<el-table-column>
							<template slot-scope="scope">
								<div v-if="editStatus" class="todo-item" :class="{ 'todo-item-del': scope.row.status }">{{ scope.row.title }}</div>
								<div v-else><el-input v-model="scope.row.input" placeholder="请输入内容"></el-input></div>
							</template>
						</el-table-column>
						<!-- <el-table-column width="60">
							<template>
								<svg t="1579419681409" class="operateTODOList" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5844"><path d="M810.667 810.667c1.046 0 0 0.93 0 4.74v-4.74z m0 0V524.463c0-23.564 19.102-42.667 42.666-42.667 23.564 0 42.667 19.103 42.667 42.667v290.944C896 861.11 856.749 896 810.667 896H213.333C167.251 896 128 861.11 128 815.407V208.593C128 162.89 167.251 128 213.333 128h390.084c23.564 0 42.666 19.103 42.666 42.667s-19.102 42.666-42.666 42.666H213.333v597.334h597.334z m-597.334 0v4.74c0-3.81-1.046-4.74 0-4.74z m0-602.074v4.74c-1.046 0 0-0.93 0-4.74zM542.17 584.837c-16.662 16.662-43.678 16.662-60.34 0-16.662-16.663-16.662-43.678 0-60.34l341.333-341.334c16.663-16.662 43.678-16.662 60.34 0 16.663 16.663 16.663 43.678 0 60.34L542.17 584.837z" p-id="5845"></path></svg>
								<svg t="1579419521160" class="operateTODOList" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5114"><path d="M382.4 876 7.4 501 43.1 465.4 380.9 803.2 983.6 149.7 1020.7 183.9Z" p-id="5115"></path></svg>
							</template>
						</el-table-column> -->
					</el-table>
				</el-card>
			</el-col>
		</el-row>
		<!-- <el-row :gutter="20">
            <el-col :span="12">
                <el-card shadow="hover">
                    <schart ref="bar" class="schart" canvasId="bar" :options="options"></schart>
                </el-card>
            </el-col>
            <el-col :span="12">
                <el-card shadow="hover">
                    <schart ref="line" class="schart" canvasId="line" :options="options2"></schart>
                </el-card>
            </el-col>
        </el-row> -->
	</div>
</template>

<script>
import Schart from 'vue-schart';
import bus from '../common/bus';
export default {
	name: 'dashboard',
	data() {
		return {
			name: localStorage.getItem('ms_username'),
			WANIP: '0.0.0.0',
			LANIP: '0.0.0.0',
			mobileCountOffline: 0,
			mobileCountOnline: 0,
			systemMessage: 0,
			editStatus: true,
			input: '09876',
			todoList: [
				{
					title: '定一个小目标',
					input: '',
					status: false
				},
				{
					title: '先挣它一个亿',
					input: '',
					status: false
				},
				{
					title: '为了财务自由，冲啊，奥利给',
					input: '',
					status: false
				},
				{
					title: '今天要挣100万',
					input: '',
					status: false
				},
				{
					title: '今天要给作者捐100块钱，让他继续开发维护',
					input: '',
					status: false
				},
				{
					title: '我先捐为敬',
					input: '',
					status: false
				},
				{
					title: '作者大大666',
					input: '',
					status: false
				},
				{
					title: '今天又挣了一个亿，赏给作者一千块钱',
					input: '',
					status: false
				},
				{
					title: '今年实现财务自由，当老板',
					input: '',
					status: true
				}
			],
			data: []
		};
	},
	components: {
		Schart
	},
	computed: {
		role() {
			return this.name === 'admin' ? '超级管理员' : '普通用户';
		}
	},
	// created() {
	//     this.handleListener();
	//     this.changeDate();
	// },
	// activated() {
	//     this.handleListener();
	// },
	// deactivated() {
	//     window.removeEventListener('resize', this.renderChart);
	//     bus.$off('collapse', this.handleBus);
	// },
	methods: {
		changeDate() {
			const now = new Date().getTime();
			this.data.forEach((item, index) => {
				const date = new Date(now - (6 - index) * 86400000);
				item.name = `${date.getFullYear()}/${date.getMonth() + 1}/${date.getDate()}`;
			});
		},

		initData() {
			var testData = '{"lan":"0.0.0.1","wan":"0.0.0.2","online":"10","offline":"12","systemmessage":"80"}';
			var deviceData = JSON.parse(testData);
			// console.log(deviceData);
			this.WANIP = deviceData.wan;
			this.LANIP = deviceData.lan;
			this.mobileCountOnline = deviceData.online;
			this.mobileCountOffline = deviceData.offline;
			this.systemMessage = deviceData.systemmessage;
		},

		edit() {
			this.todoList.forEach(function(item) {
				if (item) {
					item['input'] = item['title'];
				}
			});
			this.editStatus = !this.editStatus;
		},

		save() {
			this.deleteEmptyElement();
			this.todoList.forEach(function(item) {
				if (item) {
					var input = item['input'];
					if (input) {
						item['title'] = input;
					}
				}
			});
			this.editStatus = true;
		},

		cancel() {
			this.deleteEmptyElement();
			this.todoList.forEach(function(item) {
				if (item) {
					item['input'] = '';
				}
			});
			this.editStatus = true;
		},

		add() {
			this.todoList.forEach(function(item) {
				if (item) {
					item['input'] = item['title'];
				}
			});
			this.todoList.unshift({ title: '', input: '', status: '' });
			this.editStatus = false;
		},

		deleteEmptyElement() {
			//清除空的todo且清空input
			for (var i = 0, len = this.todoList.length; i < len; i++) {
				if (this.todoList[i]) {
					//判断元素是否为undefined
					if (!this.todoList[i]['title'] && !this.todoList[i]['input']) {
						delete this.todoList[i];
					}
				}
			}
		}
	},
	mounted: function() {
		this.initData();
		window.setInterval(this.initData, 8000);
	},
	created: function() {
		// //设置在线手机数量
		// bus.$on('setMobileCountsOnline', msg => {
		// 	this.mobileCountOnline = localStorage.mobileCountOnline;
		// 	if(!this.mobileCountOnline){
		// 		this.mobileCountOnline = 0;
		// 	}
		// });
		// //设置离线手机数量
		// bus.$on('setMobileCountsOffline', msg => {
		// 	this.mobileCountOffline = localStorage.mobileCountOffline;
		// 	if(!this.mobileCountOffline){
		// 		this.mobileCountOffline = 0;
		// 	}
		// });
		// //设置系统消息数量
		// bus.$on('setSystemMessageCount', msg =>{
		// 	this.systemMessage = localStorage.systemMessage;
		// 	if(!this.systemMessage){
		// 		this.systemMessage = 0;
		// 	}
		// });
		// //初始化数据
		// bus.$emit('setMobileCountsOnline');
		// bus.$emit('setMobileCountsOffline');
		// bus.$emit('setSystemMessageCount');
	},
	mounted() {
		var cnzz_protocol = 'https:' == document.location.protocol ? 'https://' : 'http://';
		document.write(
			unescape(
				"%3Cspan style='display:none' id='cnzz_stat_icon_1278589391'%3E%3C/span%3E%3Cscript src='" +
					cnzz_protocol +
					"s4.cnzz.com/z_stat.php%3Fid%3D1278589391' type='text/javascript'%3E%3C/script%3E"
			)
		);
	}
};
</script>

<style scoped>
.el-row {
	margin-bottom: 20px;
}

.grid-content {
	display: flex;
	align-items: center;
	height: 100px;
}

.grid-cont-right {
	flex: 1;
	text-align: center;
	font-size: 14px;
	color: #999;
}

.grid-num {
	font-size: 30px;
	font-weight: bold;
}

.grid-con-icon {
	font-size: 50px;
	width: 100px;
	height: 100px;
	text-align: center;
	line-height: 100px;
	color: #fff;
}

.grid-con-1 .grid-con-icon {
	background: rgb(45, 140, 240);
}

.grid-con-1 .grid-num {
	color: rgb(45, 140, 240);
}

.grid-con-2 .grid-con-icon {
	background: rgb(100, 213, 114);
}

.grid-con-2 .grid-num {
	color: rgb(45, 140, 240);
}

.grid-con-3 .grid-con-icon {
	background: rgb(242, 94, 67);
}

.grid-con-3 .grid-num {
	color: rgb(242, 94, 67);
}

.user-info {
	display: flex;
	align-items: center;
	padding-bottom: 20px;
	border-bottom: 2px solid #ccc;
	margin-bottom: 20px;
}

.user-avator {
	width: 120px;
	height: 120px;
	border-radius: 50%;
}

.user-info-cont {
	padding-left: 50px;
	flex: 1;
	font-size: 14px;
	color: #999;
}

.user-info-cont div:first-child {
	font-size: 30px;
	color: #222;
}

.ip {
	font-size: 14px;
	color: #999;
	line-height: 25px;
}

.user-info-list span {
	margin-left: 70px;
}

.mgb20 {
	margin-bottom: 20px;
}

.todo-item {
	font-size: 14px;
}

.todo-item-del {
	text-decoration: line-through;
	color: #999;
}

.schart {
	width: 100%;
	height: 300px;
}

.operateTODOList {
	width: 40%;
	height: 40%;
	margin-right: 4px;
}
</style>
