# 《百万英雄》题库

![](https://img.shields.io/badge/百万英雄-题库-brightgreen.svg)
![](https://mindcont.com/bigdata/static/img/build-with-love.svg)

<!-- ![](http://static.mindcont.com/blog/images/resources/ixigua-qa.png) -->


## Update

> - 2018-02-22 因[今日头条诉答题助手为不正当竞争](http://tech.sina.com.cn/i/2018-02-22/doc-ifyrvspi0615003.shtml) 该方法已失效!!!
> - 2018-02-15 因[广电总局加强管制网络视听直播答题活动](http://www.nbd.com.cn/articles/2018-02-19/1193173.html)，百万英雄官微宣布第一季结束。

```json
    __  ____ _____             __  __                      ____    ___
   /  |/  (_) / (_)___  ____  / / / /__  _________        / __ \  /   |
  / /|_/ / / / / / __ \/ __ \/ /_/ / _ \/ ___/ __ \______/ / / / / /| |
 / /  / / / / / / /_/ / / / / __  /  __/ /  / /_/ /_____/ /_/ / / ___ |
/_/  /_/_/_/_/_/\____/_/ /_/_/ /_/\___/_/   \____/      \___\_\/_/  |_|

```
> 《百万英雄》是一档全民知识互动游戏，在《百万英雄》里每场12道题目全部回答正确的人，将瓜分奖金。


## Install
First install some dependencies like `git`, `requests`.
```css
sudo apt-get install git
pip install -r requirements.txt

# or install by manual
pip install requests
```
then use python. Open a terminal, in windows press `win + R ` or in ubunut press `ctrl + alt +t`

```css
git clone https://github.com/mindcont/MillionHero-QA.git
cd MillionHero-QA
chmod +x million-answer-spider.py
python million-answer-spider.py
```
the result will be in some filename like `百万英雄题库-20180112.txt`
```json

2018年1月12日	21:00场 300万
====================================================
1	下列哪一项不是我国十二生肖中的动物?	猫
2	以下不是新疆籍贯的90后小花是?	关晓彤
3	六分之五这个分数中,6是分母,那5是什么?	分子
4	下列哪种动物是我国特有的?	大熊猫
5	特色面食“肉夹馍”是哪个地区的美食?	陕西
6	以下球类运动中,按球体积大小排序,错误的是?	足球>乒乓球>网球
7	“天生我才必有用,千金散尽还复来”的作者是谁?	李白
8	《十面埋伏》是我国哪种传统乐器的名曲?	琵琶
9	下列哪位球员有在NBA打球的经历?	易建联
10	湖南省境内旅游景点风景秀丽,名胜众多,其中不包括?	乌镇
11	一般情况下,家用冰箱冷藏室的温度维持在?	2c到10°c
12	中国神话中有“龙生九子”一说,以下属于这“九子的是?	饕餮
====================================================

```
enjoy and have fun :heart: ~
