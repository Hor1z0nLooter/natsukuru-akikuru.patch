# natsukuru-akikuru.patch
夏日云幽幽（なつくもゆるる）、秋夜梦莹莹（あきゆめくくる）的机器翻译补丁

夏日云幽幽（以下简称夏滚滚）的补丁下载地址：下面网址里的patch.xp3和xp3filter.tjs（仅安卓版本需要）
https://github.com/Hor1z0nLooter/natsukuru-akikuru.patch/tree/main/natsukuru
秋夜梦莹莹（以下简称秋滚滚）的补丁下载地址：下面网址里的patch.xp3
https://github.com/Hor1z0nLooter/natsukuru-akikuru.patch/tree/main/akikuru

夏滚滚和秋滚滚的机器翻译版本，使用GalTransl（https://github.com/XD2333/GalTransl）工具进行翻译，使用gpt3.5版本，第三方的api。
patch.xp3放入游戏根目录即可，pc平台需要转区运行否则立绘无法显示。安卓平台使用Kirikiroid2 v1.3.9可以正常运行，其中夏滚滚需要放入xp3filter.tjs

夏滚滚的封包带加密，所以使用XP3Viewer进行解包和封包，得到txt格式的文本，用提供的TxtToJson.py转换成GalTransl能识别的json，翻译后用jsontotxt.py转换回txt，再用XP3Viewer封包
秋滚滚的封包没加密，用GARbro-v1.5.44.2904解包得到.scn格式的文本，实际上是psb格式的，用FreeMoteToolkit/PsbDecompile.exe（https://github.com/UlyssesWu/FreeMote）得到json格式文本。再写代码转换成GalTransl能识别的json，翻译后转回，用FreeMoteToolkit/PsBuild.exe打包成psb格式，改文件名的psb为scn后，用GARbro-v1.5.44.2904封包，压缩选项：版本2，无加密，勾选压缩目录，压缩内容，不勾选保持目录结构
