import traceback
import os
import pathlib
import numpy
import cv2
import random

nextline = lambda :print("")
def pause():
	nextline()
	os.system("pause")
def printshift(obj,n: int):
	间隔 = "\t" * n
	分行 = "\n" + 间隔
	if(not(isinstance(obj,str))):
		obj = repr(obj)
	print(间隔 + 分行.join(obj.split("\n")))


输入图片文件夹 = None
输出图片文件夹 = None

def main():
	图片路径 = pathlib.Path()
	# 路径为 pathlib.Path
	try:
		图片路径 = 输入图片文件夹 / "8.png"
	# 路径为 str
	except AttributeError:
		try:
			图片路径 = pathlib.Path(输入图片文件夹) / "8.png"
		except:
			raise FileNotFoundError("未找到文件夹“{}”".format(输入图片文件夹))
	except FileNotFoundError:
		raise FileNotFoundError("未找到文件夹“{}”".format(输入图片文件夹))
	except:
		raise Exception("未知错误")
	print("获取图片    “{}”".format(图片路径))
	print()

	图片文件内容 = numpy.fromfile(图片路径,dtype=numpy.uint8)
	图片数据 = cv2.imdecode(图片文件内容, flags = cv2.IMREAD_COLOR)
	图片长 = 图片数据.shape[1]
	图片宽 = 图片数据.shape[0]

	#cv2.imshow("V",cv2.cvtColor(图片数据, cv2.COLOR_BGR2GRAY))
	#cv2.waitKey()
	#cv2.destroyAllWindows()
	灰度图像 = cv2.cvtColor(图片数据, cv2.COLOR_BGR2GRAY)
	滤波灰度图像 = cv2.medianBlur(灰度图像, 5)
	边缘检测图像 = cv2.Canny(灰度图像,threshold1=50,threshold2=150)

	cv2.imshow("canny",边缘检测图像)
	cv2.waitKey()
	cv2.destroyAllWindows()
	所有圆形 = cv2.HoughCircles(
		image=边缘检测图像,                                # 需要输入灰度图像
		method=cv2.HOUGH_GRADIENT,                         # 检测方法
		dp=1,                                              # 累加器分辨率参数
		minDist=30,                                        # 圆心之间最小距离
		param1=50,                                         # 边缘检测最大阈值
		param2=20,                                         # 圆环结果投票票数阈值？（值越大圆环越少，越精准）
		minRadius=0,
		maxRadius=0)
	# cv2.imshow("V",滤波灰度图像)
	# cv2.waitKey()
	# cv2.destroyAllWindows()
	print(所有圆形)

	检测绘图 = 图片数据
	for 圆心x,圆心y,半径 in 所有圆形[0]:
		cv2.imshow("part",边缘检测图像[int(numpy.ceil(圆心y-半径)):int(round(圆心y+半径)),int(round(圆心x-半径)):int(round(圆心x+半径))])
		cv2.waitKey()
		cv2.destroyAllWindows()
		检测验证 = cv2.HoughCircles(
			image=边缘检测图像[int(round(圆心y-半径)):int(round(圆心y+半径)),int(round(圆心x-半径)):int(round(圆心x+半径))],
			method=cv2.HOUGH_GRADIENT,
			dp=1,
			minDist=30,
			param1=50,
			param2=20,
			minRadius=0,
			maxRadius=0)
		print(检测验证)
		if not(isinstance(检测验证,type(None))):
			检测绘图 = cv2.rectangle(
				img=图片数据,
				pt1=(round(圆心x-半径),round(圆心y-半径)),
				pt2=(round(圆心x+半径),round(圆心y+半径)),
				color=(255,0,0),
				thickness=1
				)
	cv2.imshow("test",检测绘图)
	cv2.waitKey()
	cv2.destroyAllWindows()










if __name__ == "__main__":
	try:
		输入图片文件夹 = pathlib.Path(__file__).parents[1] / "输入图片"
		输出图片文件夹 = pathlib.Path(__file__).parents[1] / "输出图片"
		main()
		print()
	except:
		traceback.print_exc()
		print()
	finally:
		os.system("pause")
		print()
		print()