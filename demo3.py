#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
# __Author__ Aaron

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
		    <div>
		     我是div的中文	   
		    </div>
		    <p><!--我是注释字符串--></p>
		</body>
</html>
'''

from bs4.element import Tag
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')

# print(type(soup))#<class 'bs4.BeautifulSoup'>
#
# table = soup.find('table')
# print(type(table))#<class 'bs4.element.Tag'>

# div = soup.find('div')
# print(type(div.string))#<class 'bs4.element.NavigableString'>

from bs4 import Comment

# Comment：查找注释字符串
# p = soup.find('p')
# print(p.string)#把注释放在p标签的中间些方向就找不到了,因为存在换行符
# print(type(p.string))#<class 'bs4.element.Comment'>
# print(p.contents)#打印出包括换行符在内的所有字符

table = soup.find('table')
# 返回所有子节点的列表
# for element in table.contents:
#     print(element)
#     print('='*50)

# 返回所有子节点的迭代器
for element in table.children:
    print(element)
    print('='*50)
