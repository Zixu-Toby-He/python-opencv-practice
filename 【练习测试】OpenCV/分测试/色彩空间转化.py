import traceback
import os
import pathlib
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
		图片路径 = next(输入图片文件夹.iterdir())
	# 路径为 str
	except AttributeError:
		try:
			图片路径 = pathlib.Path(os.listdir(输入图片文件夹)[0])
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

	print("BGR色彩空间数据：{}    shape={}".format(type(图片数据),图片数据.shape))
	printshift(图片数据,1)
	cv2.imshow("original", 图片数据)
	cv2.waitKey(delay=5000) # 单位：毫秒
	print()

	# 转化为 Gray 色彩空间
	Gray图片数据 = cv2.cvtColor(图片数据,cv2.COLOR_BGR2GRAY)
	print("Gray色彩空间数据：{}    shape={}".format(type(Gray图片数据),Gray图片数据.shape))
	printshift(Gray图片数据,1)
	cv2.imshow("Gray", Gray图片数据)
	cv2.waitKey(delay=5000) # 单位：毫秒
	print()

	# 转化为 HSV 色彩空间
	HSV图片数据 = cv2.cvtColor(图片数据,cv2.COLOR_BGR2HSV)
	print("HSV色彩空间数据：{}    shape={}".format(type(HSV图片数据),HSV图片数据.shape))
	printshift(HSV图片数据,1)
	cv2.imshow("HSV", HSV图片数据)
	cv2.waitKey(delay=5000) # 单位：毫秒

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
