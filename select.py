# !/usr/bin/env python3
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

soup = BeautifulSoup(html,'lxml')

# 1. 获取所有tr标签
# trs = soup.select('tr')
# for tr in trs:
#     print(tr)
#     print('^'*50)
#       print(type(tr))#<class 'bs4.element.Tag'>
#       break
# 2. 获取第2个tr标签
# tr = soup.select('tr')[1]
# print(tr)
# 3. 获取所有class等于的even的tr标签
# trs = soup.select('.even')
# trs = soup.select("tr[class='even']")
# for tr in trs:
#     print(tr)
#     print('#'*50)

# 4. 获取所有a标签的href属性
aList = soup.select('a')
# for a in aList:
#     # href = a['href']
#     href = a.attrs['href']
#     print(href)

# 5. 获取所有的职位信息(在纯文本)
trs = soup.select('tr')
for tr in trs:
    infos = list(tr.stripped_strings)
    print(infos)
