## 介绍
女娲群控系统，免root控制安卓手机，安卓4.4版本以上的全部兼容

![Jietu20200126-152902.jpg](https://i.loli.net/2020/01/26/Jvl7jyp9OuILgaX.jpg)
![Jietu20200126-152948.jpg](https://i.loli.net/2020/01/26/c7lvKAwhTByELI2.jpg)


## 使用方法
1. 下载代码
`git clone https://github.com/zhongxia245/weiqunkong.git`
2. 使用Pycharm打开项目
3. 安装依赖`pip install -r requirements.txt`
4. 运行项目
5. 进入web文件夹，执行`npm serve`(需要先安装nodejs)
6. 浏览器打开`127.0.0.1:8000`
7. 手机连接到电脑，打开开发者模式，并信任电脑(电脑要安装adb)
  * 执行`adb push Main.dex /sdcard/Main.dex`
  * 执行`adb shell`
  * 执行命令 `export CLASSPATH=/sdcard/Main.dex`
  * 执行命令 `exec app_process /sdcard com.wanjian.puppet.Main &`
  * 执行`exit`，然后`adb forward tcp:8888 localabstract:puppet-ver1`
