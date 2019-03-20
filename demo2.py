#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
# __Author__ Aaron

from bs4 import BeautifulSoup

html = '''

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>职位搜索 | 社会招聘 | Tencent 腾讯招聘</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>

<body>

		    <table class="tablelist" cellpadding="0" cellspacing="0">
		    	<tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48699&keywords=&tid=81&lid=2218">29911-创意玩法设计师</a></td>
					<td>设计类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-03-20</td>
		    	</tr>
		    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48687&keywords=&tid=81&lid=2218">15571-3D场景设计师</a></td>
					<td>设计类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-03-20</td>
		    	</tr>
		    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48688&keywords=&tid=81&lid=2218">15571-2D概念设计师</a></td>
					<td>设计类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-03-20</td>
		    	</tr>
		    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48683&keywords=&tid=81&lid=2218">15571-手游-高级技术美术</a></td>
					<td>设计类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-03-20</td>
		    	</tr>
		    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48684&keywords=&tid=81&lid=2218">15571-CF手游资深动作设计师</a></td>
					<td>设计类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-03-20</td>
		    	</tr>
		    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48685&keywords=&tid=81&lid=2218">15571-3D特效设计师</a></td>
					<td>设计类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-03-20</td>
		    	</tr>
		    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48686&keywords=&tid=81&lid=2218">15571-多媒体设计师</a></td>
					<td>设计类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-03-20</td>
		    	</tr>
		    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48666&keywords=&tid=81&lid=2218">19511-视觉设计师（深圳）</a></td>
					<td>设计类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-03-20</td>
		    	</tr>
		    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48632&keywords=&tid=81&lid=2218">29303-视觉设计师</a></td>
					<td>设计类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-03-20</td>
		    	</tr>
		    	<tr class="odd">
		    		<td class="l square"><a id="test" class="test" target="_blank" href="position_detail.php?id=48619&keywords=&tid=81&lid=2218">15712-游戏高级交互设计师（深圳）</a></td>
					<td>设计类</td>
					<td>3</td>
					<td>深圳</td>
					<td>2019-03-20</td>
		    	</tr>
		    		
		    </table>
		</body>
</html>
'''

# 1. 获取所有tr标签
# 2. 获取第2个tr标签
# 3. 获取所有class等于的even的tr标签
# 4. 将所有id等于test,class也等于test的a标签提取出来
# 5. 获取所有a标签的href属性
# 6. 获取所有的职位信息(在纯文本)

soup = BeautifulSoup(html, "lxml")
# 1. 获取所有tr标签
# trs = soup.find_all('tr')
# for tr in trs:
#     print(tr)
#     print('='*50)
from bs4.element import Tag

# 2. 获取第2个tr标签
# 方法一：limit 限制获取多少个标签
# tr = soup.find_all('tr',limit=2)[1]
# 方法二:
# tr = soup.find_all('tr')[1]
# print(tr)

# 3. 获取所有class等于的even的tr标签
# 方法1
# trs = soup.find_all('tr',class_='even')
# 方法二
# trs = soup.find_all('tr',attrs={'class','even'})
# for tr in trs:
#     print(tr)
#     print('='*50)

# 4. 将所有id等于test,class也等于test的a标签提取出来
# 方法一:
# trs = soup.find_all('a', id='test', class_='test')
# 方法二：
# trs = soup.find_all('a',attrs={'id':'test','class':'test'})
# for tr in trs:
#     print(tr)
#     print('&'*50)

# 5. 获取所有a标签的href属性
# aList = soup.find_all('a')
# for a in aList:
    # 1.通过下标操作的方式
    # href = a['href']
    # print(href)
    # print(type(href))
    # 2.通过attrs属性的方式
    # href = a.attrs['href']
    # print(href)

# 6. 获取所有的职位信息(在纯文本)
trs = soup.find_all('tr')[1:]#第一个不是
positions=[]
for tr in trs:
    position={}
    # 方法一:

    # tds = tr.find_all('td')
    # title = tds[0].string
    # category = tds[1].string
    # nums = tds[2].string
    # city = tds[3].string
    # pubtime = tds[4].string
    # position['title'] = title
    # position['category'] = category
    # position['nums'] = nums
    # position['city'] = city
    # position['pubtime'] = pubtime

    # 方法二:
    # infos = list(tr.strings)#带有空白字符
    infos = list(tr.stripped_strings)
    # print(infos)
    position['title'] = infos[0]
    position['category'] = infos[1]
    position['nums'] = infos[2]
    position['city'] = infos[3]
    position['pubtime'] = infos[4]

    positions.append(position)

print(positions)