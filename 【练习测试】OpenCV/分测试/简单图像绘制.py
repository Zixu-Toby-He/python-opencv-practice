import traceback
import os
import pathlib
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import numpy
import cv2
import random
import PIL
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont


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
	输出图片数据 = numpy.full(shape=(1080,1920,3),fill_value=255,dtype=numpy.uint8)
	cv2.imshow("empty",输出图片数据)
	cv2.waitKey()
	cv2.destroyAllWindows()

	黑色 = numpy.array([  0,  0,  0])
	蓝色 = numpy.array([255,  0,  0])
	绿色 = numpy.array([  0,255,  0])
	红色 = numpy.array([  0,  0,255])
	白色 = numpy.array([255,255,255])
	
	# 区域涂色
	输出图片数据[  0:100,  0:100,:] = 黑色
	输出图片数据[  0:100,100:200,:] = 蓝色
	输出图片数据[100:200,  0:100,:] = 红色
	输出图片数据[100:200,100:200,:] = 绿色
	cv2.imshow("paint 1",输出图片数据)
	cv2.waitKey()
	cv2.destroyAllWindows()

	# 画线段
	输出图片数据 = cv2.line(输出图片数据, pt1=(300,50), pt2=(400,100), color=0.75*绿色+0.25*红色, thickness=5)
	cv2.imshow("paint 2",输出图片数据)
	cv2.waitKey()
	cv2.destroyAllWindows()

	# 画矩形
	输出图片数据 = cv2.rectangle(输出图片数据,pt1=(500,20),pt2=(600,70),color=0.75*红色+0.25*蓝色, thickness=3)
	cv2.imshow("paint 3",输出图片数据)
	cv2.waitKey()
	cv2.destroyAllWindows()

	# 画圆形（thickness=-1：实心）
	输出图片数据 = cv2.circle(输出图片数据,center=(700,50),radius=30,color=0.75*蓝色+0.25*绿色, thickness=-1)
	cv2.imshow("paint 4",输出图片数据)
	cv2.waitKey()
	cv2.destroyAllWindows()

	# 画多边形
	顶点 = numpy.array(
		[
			[20,220],
			[80,210],
			[90,320],
			[10,280],
		],dtype=numpy.int32)
	输出图片数据 = cv2.polylines(
		输出图片数据,
		pts=[顶点],
		isClosed=True,
		color=0.5*白色,
		thickness=5)
	cv2.imshow("paint 5",输出图片数据)
	cv2.waitKey()
	cv2.destroyAllWindows()

	# 绘制文字
	输出图片数据 = cv2.putText(
		输出图片数据,
		text="Text in English",
		org=(300,300),
		fontFace=cv2.FONT_ITALIC+cv2.FONT_HERSHEY_TRIPLEX,
		fontScale=2,
		color=0.25*绿色+0.75*红色)
	cv2.imshow("paint 6",输出图片数据)
	cv2.waitKey()
	cv2.destroyAllWindows()

	# opencv不支持中文绘制，可以使用PIL库来绘制
	PIL图片数据 = PIL.Image.fromarray(cv2.cvtColor(输出图片数据,cv2.COLOR_BGR2RGB))
	print(PIL图片数据)
	PIL绘图对象 = PIL.ImageDraw.Draw(PIL图片数据)
	字体 = PIL.ImageFont.truetype(
		font=r"C:/Windows/Fonts/simsun.ttc",
		size=30,
		encoding="utf-8")
	PIL绘图对象.text(
		xy=(400,400),
		text="中文文本",
		fill=tuple(numpy.int32(0.25*红色[::-1]+0.75*蓝色[::-1])),
		font=字体)
	输出图片数据 = cv2.cvtColor(numpy.asarray(PIL图片数据),cv2.COLOR_RGB2BGR)
	输出图片数据 = cv2.rectangle(输出图片数据,pt1=(400,400),pt2=(400+30*4,400+30),color=0.25*蓝色+0.75*绿色,thickness=1)
	cv2.imshow("paint 7",输出图片数据)
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