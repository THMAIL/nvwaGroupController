<template>
	<el-card :body-style="{ padding: '0px' }" id="container">
		<div id="mobile">
			<img
				id="mobileImage"
				v-bind:src="imgsrc"
				v-on:mouseover="MouseOver"
				v-on:mouseout="MouseOut"
				v-on:mousedown="MouseDown"
				v-on:mousemove="MouseMove"
				v-on:mouseup="MouseUp"
				ondragstart="return false;"
				ref="mobileImage"
			/>
			<div id="mobileButtons">
				<svg v-on:click="menu" t="1579411918897" class="mobileButton" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2794">
					<path
						d="M384 480H192c-52.8 0-96-43.2-96-96V192c0-52.8 43.2-96 96-96h192c52.8 0 96 43.2 96 96v192c0 52.8-43.2 96-96 96zM192 160c-17.6 0-32 14.4-32 32v192c0 17.6 14.4 32 32 32h192c17.6 0 32-14.4 32-32V192c0-17.6-14.4-32-32-32H192zM832 480H640c-52.8 0-96-43.2-96-96V192c0-52.8 43.2-96 96-96h192c52.8 0 96 43.2 96 96v192c0 52.8-43.2 96-96 96zM640 160c-17.6 0-32 14.4-32 32v192c0 17.6 14.4 32 32 32h192c17.6 0 32-14.4 32-32V192c0-17.6-14.4-32-32-32H640zM384 928H192c-52.8 0-96-43.2-96-96V640c0-52.8 43.2-96 96-96h192c52.8 0 96 43.2 96 96v192c0 52.8-43.2 96-96 96zM192 608c-17.6 0-32 14.4-32 32v192c0 17.6 14.4 32 32 32h192c17.6 0 32-14.4 32-32V640c0-17.6-14.4-32-32-32H192zM832 928H640c-52.8 0-96-43.2-96-96V640c0-52.8 43.2-96 96-96h192c52.8 0 96 43.2 96 96v192c0 52.8-43.2 96-96 96zM640 608c-17.6 0-32 14.4-32 32v192c0 17.6 14.4 32 32 32h192c17.6 0 32-14.4 32-32V640c0-17.6-14.4-32-32-32H640z"
						p-id="2795"
						fill="#ffffff"
					></path>
				</svg>
				<svg v-on:click="home" t="1579412220811" class="mobileButton" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4339">
					<path
						d="M96 480c-9.6 0-19.2-3.2-25.6-12.8-12.8-12.8-9.6-35.2 3.2-44.8l377.6-310.4c35.2-25.6 86.4-25.6 118.4 0l377.6 307.2c12.8 9.6 16 32 3.2 44.8-12.8 12.8-32 16-44.8 3.2L531.2 166.4c-9.6-6.4-28.8-6.4-38.4 0L115.2 473.6c-6.4 6.4-12.8 6.4-19.2 6.4zM816 928H608c-19.2 0-32-12.8-32-32v-150.4c0-22.4-38.4-44.8-67.2-44.8-28.8 0-64 19.2-64 44.8V896c0 19.2-12.8 32-32 32H211.2C163.2 928 128 892.8 128 848V544c0-19.2 12.8-32 32-32s32 12.8 32 32v304c0 9.6 6.4 16 19.2 16H384v-118.4c0-64 67.2-108.8 128-108.8s131.2 44.8 131.2 108.8V864h176c9.6 0 16 0 16-19.2V544c0-19.2 12.8-32 32-32s32 12.8 32 32v304C896 896 864 928 816 928z"
						fill="#ffffff"
						p-id="4340"
					></path>
				</svg>
				<svg v-on:click="back" t="1579411953857" class="mobileButton" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3566">
					<path d="M877.216 491.808" p-id="3567" fill="#ffffff"></path>
					<path
						d="M758.528 949.984c12.512-12.512 13.248-31.872 2.048-43.776L384.096 529.696c-16.16-15.328-16.096-19.328 0-35.424L760.576 117.824c11.232-11.872 10.464-31.264-2.048-43.776-12.736-12.736-32.608-13.44-44.448-1.632L295.872 490.592C290.72 495.744 288.416 502.464 288 509.376l0 5.248c0.448 6.944 2.752 13.632 7.872 18.784l418.176 418.176C725.92 963.392 745.824 962.688 758.528 949.984z"
						p-id="3568"
						fill="#ffffff"
					></path>
				</svg>
			</div>
		</div>

		<div id="bottom">
			<el-alert v-if="online" title="在线" type="success" :closable="false" center class="status"></el-alert>
			<el-alert v-else title="离线" type="error" :closable="false" center class="status"></el-alert>

			<span class="MobileName">
				<!-- <span v-if="changeName"><el-input v-model="inputName"></el-input></span> -->
				<!-- <span v-else>{{ MobileName }}</span> -->
				{{MobileName}}

		<!-- 		<span v-if="changeName" class="operateName" v-on:click="save">保存</span>
				<span v-else class="operateName" v-on:click="edit">&nbsp;修改</span> -->
			</span>
		</div>
	</el-card>
</template>

<script>
import test from '../../assets/img/test.png';

export default {
	name: 'MobileCard',
	data() {
		return {
			imgsrc: test,
			online: false,
			changeName: false,
			inputName: ''
		};
	},
	props:['MobileName','MobileId'],
	methods: {
		init() {
			this.down = false;
			this.mobileImage = document.querySelector('#mobileImage');
			this.chatSocket = new WebSocket('ws://' + '127.0.0.1:8000' + '/ws/' + '?id=' + this.MobileId);
			this.chatSocket.onmessage = this.websocketmessage;
			this.chatSocket.onclose = this.websocketclose;
		},

		websocketmessage(e) {
			// console.log(e)
			this.imgsrc = window.URL.createObjectURL(e.data);
			// console.log(this.imgsrc);
		},

		websocketclose() {
			//连接中断
			console.error('Chat socket closed unexpectedly');
		},

		websocketonerror() {
			//连接建立失败重连
			this.initWebSocket();
		},

		websocketsend(Data) {
			//数据发送
			this.chatSocket.send(Data);
		},

		sendCMD(action, x = 0, y = 0) {
			// var width = document.querySelector('#mobileImage').iconWidth;
			// var height = document.querySelector('#mobileImage').iconHeight;

			var width = this.$refs.mobileImage.width;
			var height = this.$refs.mobileImage.height;

			console.log(width + ' : ' + height);

			if (x < 0) {
				x = 0;
			}

			if (y < 0) {
				y = 0;
			}

			x = x / width;
			y = y / height;

			console.log(x + ':' + y);

			// cmd = "{action:" + action + ", x:" + x + ", y:" + y + "}";
			var cmd = '{"action":"' + action + '", "x":"' + x + '", "y":"' + y + '"}';
			this.websocketsend(cmd);
			console.log(cmd);
		},

		MouseOver(e) {
			// 初始化
			if (this.down) {
				mobileImage.trigger('mouseup');
				// console.log('over');
				this.MouseUp(e);
				this.down = false;
			}
		},

		MouseOut(e) {
			// 清除
			if (this.down) {
				console.log('out');
				// mobileImage.trigger('mouseup');
				// this.$refs.mobileImage
				this.MouseUp(e);
				this.down = false;
			}
		},

		MouseDown(e) {
			this.down = true;
			this.sendCMD('DOWN', e.offsetX, e.offsetY);
			return false;
		},

		MouseMove(e) {
			if (this.down) {
				this.sendCMD('MOVE', e.offsetX, e.offsetY);
				return false;
			}
		},

		MouseUp(e) {
			this.down = false;
			console.log('up');
			this.sendCMD('UP', e.offsetX, e.offsetY);
			return false;
		},

		menu() {
			this.websocketsend('MENU');
			return false;
		},

		home() {
			this.websocketsend('HOME');
			return false;
		},

		back() {
			this.websocketsend('BACK');
			return false;
		},

		// edit() {
		// 	this.inputName = this.MobileName;
		// 	this.changeName = true;
		// },

		// save() {
		// 	this.MobileName = this.inputName;
		// 	this.changeName = false;
		// },

		DragStart() {
			return false;
		}
	},
	created() {
		this.init();
	}
};
</script>

<style>
#container {
	margin-bottom: 10%;
}

#mobile {
	background-image: url('../../assets/img/blackMobile.png');
	background-repeat: no-repeat;
	background-size: 100% 95%;
	display: flex;
	flex-direction: column;
	align-items: center;
	padding-top: 18%;
}

#mobileImage {
	width: 90.5%;
	height: 100%;
	display: block;
}

.mobileButton {
	width: 12%;
}

#mobileButtons {
	padding-top: 3%;
	padding-left: 10%;
	padding-right: 10%;
	padding-bottom: 14%;
	display: flex;
	justify-content: space-between;
}

.status {
	width: 35%;
	margin: 0px;
	padding: 0px;
}

#bottom {
	display: flex;
	flex-direction: column;
	align-items: center;
	margin-top: -8%;
}

.operateName {
	color: #409eff;
}

* {
	-moz-user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
	-khtml-user-select: none;
	user-select: none;
}
</style>
