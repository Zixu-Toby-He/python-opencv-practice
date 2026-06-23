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

	图片文件内容 = numpy.fromfile(图片路径,dtype=numpy.uint8)
	图片数据 = cv2.imdecode(图片文件内容, flags = cv2.IMREAD_COLOR)

	printshift(图片数据,1)
	cv2.imshow("Successfully get image", 图片数据)
	cv2.waitKey()
	cv2.destroyAllWindows()
	print()

	# 拆分通道
	蓝色数据, 绿色数据, 红色数据 = cv2.split(图片数据)
	全暗数据 = numpy.zeros_like(蓝色数据)
	全一数据 = numpy.ones_like(蓝色数据)
	全亮数据 = numpy.full_like(蓝色数据, fill_value=255)
	cv2.imshow("Blue",  蓝色数据)
	cv2.imshow("Green", 绿色数据)
	cv2.imshow("Red",   红色数据)
	cv2.waitKey()
	cv2.destroyAllWindows()

	# 通道合并
	合并数据 = cv2.merge([蓝色数据, 绿色数据, 红色数据])
	cv2.imshow("Merge", 合并数据)
	cv2.waitKey()
	cv2.destroyAllWindows()

	# 按照对应颜色显示对应通道数据

	cv2.imshow("Merge", 图片数据)
	cv2.imshow("Blue",  cv2.merge([蓝色数据, 全暗数据, 全暗数据]))
	cv2.imshow("Green", cv2.merge([全暗数据, 绿色数据, 全暗数据]))
	cv2.imshow("Red",   cv2.merge([全暗数据, 全暗数据, 红色数据]))
	cv2.waitKey()
	cv2.destroyAllWindows()

	# HSV拆分
	H色调数据, S饱和度数据, V亮度数据 = cv2.split(cv2.cvtColor(图片数据,cv2.COLOR_BGR2HSV))
	cv2.imshow("Merge", 图片数据)
	cv2.imshow("H", H色调数据)
	cv2.imshow("S", S饱和度数据)
	cv2.imshow("V", V亮度数据)
	cv2.waitKey()
	cv2.destroyAllWindows()

	# 图片混色
	cv2.imshow("Blue + Green", cv2.merge([蓝色数据, 绿色数据, 全暗数据]))
	cv2.imshow("Red + Blue",   cv2.merge([蓝色数据, 全暗数据, 红色数据]))
	cv2.imshow("Red + Green",  cv2.merge([全暗数据, 绿色数据, 红色数据]))
	cv2.waitKey()
	#cv2.destroyAllWindows()

	cv2.imshow("Full Red",   cv2.merge([蓝色数据, 绿色数据, 全亮数据]))
	cv2.imshow("Full Green", cv2.merge([蓝色数据, 全亮数据, 红色数据]))
	cv2.imshow("Full Blue",  cv2.merge([全亮数据, 绿色数据, 红色数据]))
	cv2.waitKey()
	cv2.destroyAllWindows()

	cv2.imshow("Blue",  cv2.merge([蓝色数据, 全暗数据, 全暗数据]))
	cv2.imshow("Green", cv2.merge([全暗数据, 绿色数据, 全暗数据]))
	cv2.imshow("Red",   cv2.merge([全暗数据, 全暗数据, 红色数据]))
	cv2.waitKey()

	cv2.imshow("Blue + Full Red + Full Green", cv2.merge([蓝色数据, 全亮数据, 全亮数据]))
	cv2.imshow("Green + Full Red + Full Blue", cv2.merge([全亮数据, 绿色数据, 全亮数据]))
	cv2.imshow("Red + Full Blue + Full Green", cv2.merge([全亮数据, 全亮数据, 红色数据]))
	cv2.waitKey()
	cv2.destroyAllWindows()

	# 色调，饱和度，亮度混合
	cv2.imshow("origianal",   cv2.cvtColor(cv2.merge([H色调数据,                              S饱和度数据, V亮度数据]), cv2.COLOR_HSV2BGR))
	cv2.imshow("H = 0",       cv2.cvtColor(cv2.merge([全暗数据,                               S饱和度数据, V亮度数据]), cv2.COLOR_HSV2BGR))
	cv2.imshow("H = 25%",     cv2.cvtColor(cv2.merge([(H色调数据*0.25).astype(dtype="uint8"), S饱和度数据, V亮度数据]), cv2.COLOR_HSV2BGR))
	cv2.imshow("H = 50%",     cv2.cvtColor(cv2.merge([(H色调数据*0.5 ).astype(dtype="uint8"), S饱和度数据, V亮度数据]), cv2.COLOR_HSV2BGR))
	cv2.imshow("H = 75%",     cv2.cvtColor(cv2.merge([(H色调数据*0.75).astype(dtype="uint8"), S饱和度数据, V亮度数据]), cv2.COLOR_HSV2BGR))
	cv2.waitKey()
	cv2.destroyAllWindows()

	cv2.imshow("origianal",   cv2.cvtColor(cv2.merge([H色调数据,    S饱和度数据, V亮度数据]),cv2.COLOR_HSV2BGR))
	cv2.imshow("H = all 179", cv2.cvtColor(cv2.merge([全亮数据,     S饱和度数据, V亮度数据]),cv2.COLOR_HSV2BGR))
	cv2.imshow("H = all 120", cv2.cvtColor(cv2.merge([127*全一数据, S饱和度数据, V亮度数据]),cv2.COLOR_HSV2BGR))
	cv2.imshow("H = all  60", cv2.cvtColor(cv2.merge([ 64*全一数据, S饱和度数据, V亮度数据]),cv2.COLOR_HSV2BGR))
	cv2.imshow("H = all   0", cv2.cvtColor(cv2.merge([全暗数据,     S饱和度数据, V亮度数据]),cv2.COLOR_HSV2BGR))
	cv2.waitKey()
	cv2.destroyAllWindows()
	print("色调值越低，图片越红")

	全暗零数据 = 全暗数据
	基本一数据 = 全一数据
	全高值数据 = 全亮数据
	cv2.imshow("origianal",   cv2.cvtColor(cv2.merge([H色调数据, S饱和度数据,                              V亮度数据]), cv2.COLOR_HSV2BGR))
	cv2.imshow("S = 0",       cv2.cvtColor(cv2.merge([H色调数据,  全暗零数据,                              V亮度数据]), cv2.COLOR_HSV2BGR))
	cv2.imshow("S = 25%",     cv2.cvtColor(cv2.merge([H色调数据, (S饱和度数据*0.25).astype(dtype="uint8"), V亮度数据]), cv2.COLOR_HSV2BGR))
	cv2.imshow("S = 50%",     cv2.cvtColor(cv2.merge([H色调数据, (S饱和度数据*0.5 ).astype(dtype="uint8"), V亮度数据]), cv2.COLOR_HSV2BGR))
	cv2.imshow("S = 75%",     cv2.cvtColor(cv2.merge([H色调数据, (S饱和度数据*0.75).astype(dtype="uint8"), V亮度数据]), cv2.COLOR_HSV2BGR))
	cv2.waitKey()
	cv2.destroyAllWindows()

	cv2.imshow("origianal",   cv2.cvtColor(cv2.merge([H色调数据, S饱和度数据,    V亮度数据]),cv2.COLOR_HSV2BGR))
	cv2.imshow("S = all 255", cv2.cvtColor(cv2.merge([H色调数据, 全高值数据,     V亮度数据]),cv2.COLOR_HSV2BGR))
	cv2.imshow("S = all 191", cv2.cvtColor(cv2.merge([H色调数据, 191*基本一数据, V亮度数据]),cv2.COLOR_HSV2BGR))
	cv2.imshow("S = all 127", cv2.cvtColor(cv2.merge([H色调数据, 127*基本一数据, V亮度数据]),cv2.COLOR_HSV2BGR))
	cv2.imshow("S = all  64", cv2.cvtColor(cv2.merge([H色调数据,  64*基本一数据, V亮度数据]),cv2.COLOR_HSV2BGR))
	cv2.imshow("S = all   0", cv2.cvtColor(cv2.merge([H色调数据, 全暗零数据,     V亮度数据]),cv2.COLOR_HSV2BGR))
	cv2.waitKey()
	cv2.destroyAllWindows()
	print("饱和度越高，色彩越鲜艳")
	del 全暗零数据
	del 基本一数据
	del 全高值数据

	cv2.imshow("origianal",   cv2.cvtColor(cv2.merge([H色调数据, S饱和度数据, V亮度数据]),                              cv2.COLOR_HSV2BGR))
	cv2.imshow("V = 0",       cv2.cvtColor(cv2.merge([H色调数据, S饱和度数据, 全暗数据]),                               cv2.COLOR_HSV2BGR))
	cv2.imshow("V = 25%",     cv2.cvtColor(cv2.merge([H色调数据, S饱和度数据, (V亮度数据*0.25).astype(dtype="uint8")]), cv2.COLOR_HSV2BGR))
	cv2.imshow("V = 50%",     cv2.cvtColor(cv2.merge([H色调数据, S饱和度数据, (V亮度数据*0.5 ).astype(dtype="uint8")]), cv2.COLOR_HSV2BGR))
	cv2.imshow("V = 75%",     cv2.cvtColor(cv2.merge([H色调数据, S饱和度数据, (V亮度数据*0.75).astype(dtype="uint8")]), cv2.COLOR_HSV2BGR))
	cv2.waitKey()
	cv2.destroyAllWindows()

	cv2.imshow("origianal",   cv2.cvtColor(cv2.merge([H色调数据, S饱和度数据, V亮度数据]),    cv2.COLOR_HSV2BGR))
	cv2.imshow("V = all 255", cv2.cvtColor(cv2.merge([H色调数据, S饱和度数据, 全亮数据]),     cv2.COLOR_HSV2BGR))
	cv2.imshow("V = all 191", cv2.cvtColor(cv2.merge([H色调数据, S饱和度数据, 191*全一数据]), cv2.COLOR_HSV2BGR))
	cv2.imshow("V = all 127", cv2.cvtColor(cv2.merge([H色调数据, S饱和度数据, 127*全一数据]), cv2.COLOR_HSV2BGR))
	cv2.imshow("V = all  64", cv2.cvtColor(cv2.merge([H色调数据, S饱和度数据,  64*全一数据]), cv2.COLOR_HSV2BGR))
	cv2.imshow("V = all   0", cv2.cvtColor(cv2.merge([H色调数据, S饱和度数据, 全暗数据]),     cv2.COLOR_HSV2BGR))
	cv2.waitKey()
	cv2.destroyAllWindows()
	print("亮度越高，图片越亮")

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