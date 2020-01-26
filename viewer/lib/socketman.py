# -*-coding=utf-8-*-

from channels.generic.websocket import WebsocketConsumer
import threading
import json


class socketman(WebsocketConsumer):
    def connect(self):
        from viewer.lib.viewer import viewer
        self.accept()
        self.viewer = viewer()
        self.worker = transferPic('123', 'test', self)
        self.worker.setDaemon(True)
        self.worker.start()

    def disconnect(self, close_code):
        self.worker.stop()

    def receive(self, text_data):
        # print(text_data)
        text_data_json = json.loads(text_data)
        action = text_data_json['action'].lower()
        x = text_data_json['x']
        y = text_data_json['y']
        if (action == 'up'):
            self.viewer.UP(x, y)
        elif (action == 'down'):
            self.viewer.DOWN(x, y)
        elif (action == 'move'):
            self.viewer.MOVE(x, y)
        elif(action == 'home'):
            self.viewer.HOME()
        elif(action == 'back'):
            self.viewer.BACK()
        elif(action == 'menu'):
            self.viewer.MENU()
        else:
            pass


class transferPic(threading.Thread):
    def __init__(self, threadID, name, socketman):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.socketman = socketman
        self.stopped = False

    def run(self):
        print("开始远程图像传输")
        while True:
            if (not self.stopped):
                pic = self.socketman.viewer.getPic()
                self.socketman.send(bytes_data=pic)
            else:
                self.socketman.close()
                break
        print("结束远程图像传输")

    def stop(self):
        self.stopped = True
