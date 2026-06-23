import traceback
import os
import pathlib
import random
import numpy
import cv2

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
		图片路径 = random.sample(tuple(输入图片文件夹.iterdir()),1)[0]
	# 路径为 str
	except AttributeError:
		try:
			图片路径 = pathlib.Path(random.sample(os.listdir(输入图片文件夹),1)[0])
		except:
			raise FileNotFoundError("未找到文件夹“{}”".format(输入图片文件夹))
	except FileNotFoundError:
		raise FileNotFoundError("未找到文件夹“{}”".format(输入图片文件夹))
	except:
		raise Exception("未知错误")
	print("获取图片    “{}”".format(图片路径))
	print()

	# 获取数据（中文路径方式，若为全ascii路径可用imread函数）
	图片文件内容 = numpy.fromfile(图片路径,dtype=numpy.uint8)
	图片彩色数据 = cv2.imdecode(图片文件内容, flags = cv2.IMREAD_COLOR)
	图片黑白数据 = cv2.imdecode(图片文件内容, flags = cv2.IMREAD_GRAYSCALE)

	print("彩色数据：")
	printshift(图片彩色数据,1)
	print("\t{} shape={}".format(type(图片彩色数据),图片彩色数据.shape))
	print("黑白数据：")
	printshift(图片黑白数据,1)
	print("\t{} shape={}".format(type(图片黑白数据),图片黑白数据.shape))

	# 展示图片
	cv2.imshow("Color",图片彩色数据)
	cv2.waitKey()
	cv2.imshow("Gray Scale",图片黑白数据)
	cv2.waitKey()
	cv2.destroyAllWindows()

	# 输出数据（中文路径方式，若为全ascii路径可用imwrite函数）
	文件名 = os.path.splitext(图片路径.name)[0]+"-彩色.jpg"
	print("将彩色图片输出到文件“{}”".format(文件名))
	输出缓冲 = cv2.imencode(".jpg",图片彩色数据)
	print("\t输出缓冲：{}".format(repr(输出缓冲)))
	输出缓冲[1].tofile(输出图片文件夹 / 文件名)

	文件名 = os.path.splitext(图片路径.name)[0]+"-黑白.jpg"
	print("将黑白图片输出到文件“{}”".format(文件名))
	输出缓冲 = cv2.imencode(".jpg",图片黑白数据)
	print("\t输出缓冲：{}".format(repr(输出缓冲)))
	输出缓冲[1].tofile(输出图片文件夹 / 文件名)


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