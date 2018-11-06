# Youtube_Download
一个从YouTube上下载MV数据的程序

## 新版本特性：
1. 采用youtube-dl作为下载工具，速度提升为原先两倍
2. 下载完成之后音频格式自动转换为"mp3"，目前音频和视频都同时下载在vedio文件夹下，后续会出一个小工具将其分离到audio文件夹。

## v1.1新版操作步骤：
1. 将该仓库克隆到你的机器上
2. 将群里的文件"YouTube-music-video-5M.zip"下载并解压缩到该仓库目录下
3. 安装pytube库
4. 安装youtube-dl (pip install youtube-dl)
5. [安装ffmpeg](https://blog.csdn.net/lanchunhui/article/details/70477042)
6. 通过修改download_v1.1文件中的参数来选择下载哪份id文件中的MV，以及打算下载这个id文件中哪些歌手的MV。
7. 所下载之文件全部在vedio文件夹中（包括音频）。后续会出小工具把这部分音频放入音频文件夹中。已经将视频格式固定为"fps = 30, resolution = '360p', format = 'mp4'"。
8. 在实验时发现可能有命令行输出错位的情况，但目前没有发现影响下载。


## v1.0操作步骤：
1. 将该仓库克隆到你的机器上
2. 将群里的文件"YouTube-music-video-5M.zip"下载并解压缩到该仓库目录下
3. 安装pytube库
4. 建议将Shadowsocks的代理模式调整为“全局”。（因为我在自己的机器上试验时发现不这么做就会报错）
5. 通过修改download_v1.0文件中的参数来选择下载哪份id文件中的MV，以及打算下载这个id文件中哪些歌手的MV。
6. 所下载的视频在vedio文件夹中，音频在audio文件夹中。视频可能仍带有音频，也可能没有音频。目前设定的视频格式参数为"fps = 30, resolution = '360p', format = 'mp4'"，视频格式参数为 "format = 'mp4'"。可以在"YouTube_download"这一函数中修改具体的视频参数。配对的音频和视频会具有相同的名字（分处不同文件夹）。
