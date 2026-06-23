# -*- coding: utf-8 -*-
import cv2
import numpy
import bisect
import pathlib

def 生成视频(数据, 幅面=(1920, 1080), 底色=(0,0,0), 每秒帧数=30, 输出路径="output.mp4"):
	# 计算最大时间点
	if not 数据:
		print("错误：空数据")
		return
	
	最大时刻 = max(原点位置[0] for 圆 in 数据 for 原点位置 in 圆["O"])
	
	# 计算总帧数 (覆盖t_max时间点)
	总帧数 = int(最大时刻 * 每秒帧数) + 1
	
	# 创建视频写入器
	图片长度, 图片高度 = 幅面
	四字符代码编号 = cv2.VideoWriter_fourcc(*'mp4v')
	视频对象 = cv2.VideoWriter(
		filename  = pathlib.Path(输出路径),
		fourcc    = 四字符代码编号,
		fps       = 每秒帧数,
		frameSize = (图片长度, 图片高度)
	)
	
	if not 视频对象.isOpened():
		print("无法创建视频文件")
		return

	for 当前帧 in range(总帧数):
		# 计算当前时间
		t = 当前帧 / 每秒帧数
		
		# 创建背景
		当前帧	 = numpy.empty((图片高度, 图片长度, 3), dtype=numpy.uint8)
		当前帧[:] = 底色
		
		# 绘制所有圆
		for 圆 in 数据:
			# 获取轨迹数据
			时间轴 = [点[0] for 点 in 圆["O"]]
			坐标轴 = [点[1] for 点 in 圆["O"]]
			
			# 二分查找当前时间点
			i = bisect.bisect_right(时间轴, t) - 1
			
			# 计算坐标
			if i < 0:
				x, y = 坐标轴[0]
			elif i >= len(时间轴)-1:
				x, y = 坐标轴[-1]
			else:
				# 线性插值
				t0, (x0, y0) = 圆["O"][i]
				t1, (x1, y1) = 圆["O"][i+1]
				dt = t1 - t0
				if dt == 0:
					x, y = x1, y1
				else:
					比例 = (t - t0) / dt
					x = x0 + 比例*(x1 - x0)
					y = y0 + 比例*(y1 - y0)
			
			# 绘制圆
			cv2.circle(
				当前帧,
				(int(round(x)), int(round(y))),
				圆["r"],
				圆["color"],
				thickness = -1
			)
		
		# 写入帧
		视频对象.write(当前帧)
	
	视频对象.release()
	print(f"视频已生成：{输出路径}")

if __name__ == "__main__":
	# 测试数据
	测试数据 = [
		{
			"name": "蓝色圆1",
			"r": 50,
			"color": (255, 0, 0),
			"O": [
				(0, (200, 500)),
				(4, (1000, 200)),
				(8, (1700, 800))
			]
		},
		{
			"name": "蓝色圆2",
			"r": 20,
			"color": (255, 0, 0),
			"O": [
				(0, (100,   50)),
				(6, (1300, 900)),
				(8, (500,  450))
			]
		},
		{
			"name": "红色圆1",
			"r": 30,
			"color": (0, 0, 255),
			"O": [
				(0, (1700, 800)),
				(4, (300, 400)),
				(8, (1500, 200))
			]
		},
		{
			"name": "红色圆2",
			"r": 40,
			"color": (0, 0, 255),
			"O": [
				(0, (1700, 800)),
				(4, (680,  430)),
				(6, (295,  331)),
				(8, (540, 1000))
			]
		},
		{
			"name": "绿色圆3",
			"r": 15,
			"color": (0, 255, 0),
			"O": [
				(0, (1700, 800)),
				(8, ( 10,  200))
			]
		},
	]
	
	生成视频(
		测试数据,
		幅面=(1920, 1080),
		每秒帧数=30,
		输出路径="视频.mp4"
	)