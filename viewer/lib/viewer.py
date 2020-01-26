# -*-coding=utf-8-*-

import socket
import time
import base64

'''

作用：与手机server端通讯，读取图片信息，写入控制信息

'''


class viewer():

    def __init__(self, host='127.0.0.1', port=8888):
        self.socket = socket.socket()  # 创建 socket 对象
        self.host = host
        self.port = port
        self.socket.connect((self.host, self.port))

    # return binary array for pic
    def getPic(self):
        # 校验版本号
        version = self.getVersion()
        if (not version or version != 2):
            return

        # 读取图片二进制流
        length = self.getLength()
        # print(length)
        pic = self.socket.recv(length)
        while (length > len(pic)):
            pic = pic + self.socket.recv(length - len(pic))

        return pic

    def setQuality(self, quality):
        cmd = 'DEGREE' + str(quality)
        self.sendCMD(cmd)

    # notice that , the x,y is not coordinates，it's The proportion！！！

    def UP(self, x, y):
        x = str(x)
        y = str(y)
        cmd = 'UP' + x + '#' + y
        self.sendCMD(cmd)

    def DOWN(self, x, y):
        x = str(x)
        y = str(y)
        cmd = 'DOWN' + x + '#' + y
        self.sendCMD(cmd)

    def MOVE(self, x, y):
        x = str(x)
        y = str(y)
        cmd = 'MOVE' + x + '#' + y
        self.sendCMD(cmd)

    def MENU(self):
        cmd = 'MENU'
        self.sendCMD(cmd)

    def HOME(self):
        cmd = 'HOME'
        self.sendCMD(cmd)

    def BACK(self):
        cmd = 'BACK'
        self.sendCMD(cmd)

    def sendCMD(self, cmd):
        self.socket.send(bytes(str(cmd) + '\r\n', 'utf-8'))

    def getVersion(self):

        version = self.socket.recv(1)
        try:
            version = version[0]
        except IndexError as error:
            return False
        version = int(version)

        return version

    def getLength(self):
        temp = self.socket.recv(4)
        length = (temp[0] << 24) | (temp[1] << 16) | (temp[2] << 8) | temp[3]

        return length


if __name__ == '__main__':
    viewer = viewer()

    # for i in range(10):
    #     with open('test' + str(i) + '.png', 'wb') as f:
    #         f.write(viewer.getPic())

    x = 0.5
    y = 0.5

    viewer.DOWN(x, y)
    # time.sleep(0.3)
    viewer.MOVE(0, y)
    # time.sleep(5.3)

    viewer.UP(0, y)
