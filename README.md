# Youtube_Download
一个从YouTube上下载数据的程序
## 操作步骤：
1. 将该仓库克隆到你的机器上
2. 将群里的文件"YouTube-music-video-5M.zip"下载并解压缩到该仓库目录下
3. 安装pytube库
2. 建议将Shadowsocks的代理模式调整为“全局”。（因为我在自己的机器上试验时发现不这么做就会报错）
3. 通过修改download文件来选择下载哪份id文件中的MV，打算下载这个id种哪些歌手的MV。
4. 所下载的视频在vedio文件夹中，音频在audio文件夹中。视频可能仍带有音频，也可能没有音频。目前设定的视频格式参数为"fps = 30, resolution = '360p', format = 'mp4'"，视频格式参数为 "format = 'mp4'"。可以在"YouTube_download"这一函数中修改具体的视频参数。
