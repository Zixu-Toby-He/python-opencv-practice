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
	图片长 = 图片数据.shape[1]
	图片宽 = 图片数据.shape[0]
	对角线长 = numpy.sqrt(图片长*图片长+图片宽*图片宽)

	printshift(图片数据,1)
	cv2.imshow("Successfully get image", 图片数据)
	cv2.waitKey()
	cv2.destroyAllWindows()
	print()

	# 缩放
	dsize放大图片 = cv2.resize(src=图片数据, dsize=(int(图片长*1.5),int(图片宽*1.6)))
	cv2.imshow("original", 图片数据)
	cv2.imshow("dsize = (1920,1080)", dsize放大图片)
	cv2.waitKey()
	cv2.destroyAllWindows()

	fxfy缩小图片 = cv2.resize(图片数据, dsize=None, fx=0.7071, fy=0.7071)
	fxfy放大图片 = cv2.resize(图片数据, dsize=None, fx=1.414, fy=1.414)
	cv2.imshow("original", 图片数据)
	cv2.imshow("fx = 0.7071, fy= 0.7071", fxfy缩小图片)
	cv2.imshow("fx = 1.414, fy= 1.414",   fxfy放大图片)
	cv2.waitKey()
	cv2.destroyAllWindows()

	放缩后图形 = cv2.resize(图片数据, dsize=None, fx=0.5, fy=0.5)
	图片半长 = 放缩后图形.shape[1]
	图片半宽 = 放缩后图形.shape[0]
	对角线半长 = numpy.sqrt(图片半长 * 图片半长 + 图片半宽 * 图片半宽)

	# 对称
	轴标签 = {"x轴": 0, "y轴":1, "中心":-1}
	关于x轴翻转  = cv2.flip(放缩后图形, 轴标签["x轴"])
	关于y轴翻转  = cv2.flip(放缩后图形, 轴标签["y轴"])
	关于xy轴翻转 = cv2.flip(放缩后图形, 轴标签["中心"])
	cv2.imshow("half x half y original", 放缩后图形)
	cv2.imshow("flip on x",  关于x轴翻转)
	cv2.imshow("flip on y",  关于y轴翻转)
	cv2.imshow("flip on xy", 关于xy轴翻转)
	cv2.waitKey()
	cv2.destroyAllWindows()

	# 仿射变换：根据矩阵形式变换
	# M = [[m00,m01,m02],[m10,m11,m12]] -> 如下
	# x_new = m00 * x_old + m01 * y_old + m02
	# y_new = m10 * x_old + m11 * y_old + m12
	#
	## 平移 M = [[1,0,delta_x],[0,1,delta_y]]
	平移矩阵 = numpy.array([[1,0,50],[0,1,100]], dtype="float")
	cv2.imshow("original", 放缩后图形)
	平移图像 = cv2.warpAffine(src=放缩后图形, M=平移矩阵, dsize=(图片半长,图片半宽))
	cv2.imshow("translate", 平移图像)
	cv2.waitKey()
	cv2.destroyAllWindows()
	## 旋转 M = [[cos θ, sin θ, const_x],[-sin θ,cos θ, const_y]]
	## 利用 cv2.getRotationMatrix2D(center=旋转中心, angle=角度数, scale = 缩放比例) 可以得到对应仿射矩阵
	cv2.imshow("original", 放缩后图形)
	旋转矩阵 = cv2.getRotationMatrix2D(center=(图片半长/2,图片半宽/2), angle=30, scale=1)
	旋转图像 = cv2.warpAffine(src=放缩后图形, M=旋转矩阵, dsize=(int(图片半长),int(图片半宽)))
	cv2.imshow("rotate", 旋转图像)
	cv2.imshow("rotate whole",
		cv2.warpAffine(
			src = cv2.warpAffine(
				src=放缩后图形,
				M=numpy.float32([[1,0,0.5*(对角线半长-图片半长)],[0,1,0.5*(对角线半长-图片半宽)]]),
				dsize=(int(对角线半长),int(对角线半长))),
			M=cv2.getRotationMatrix2D(center=(对角线半长*0.5,对角线半长*0.5), angle=30, scale=1),
			dsize=(int(对角线半长),int(对角线半长))))
	cv2.waitKey()
	cv2.destroyAllWindows()

	# 倾斜
	cv2.imshow("original",放缩后图形)
	变换前样本点 = numpy.array([[0,0],[1,0],[0,1]],  dtype="float32")
	变换后样本点 = numpy.array([[0,0],[1,0],[0.5,1]],dtype="float32")
	倾斜矩阵 = cv2.getAffineTransform(变换前样本点,变换后样本点)
	cv2.imshow("clined",cv2.warpAffine(src=放缩后图形, M=倾斜矩阵, dsize=(int(对角线半长),int(对角线半长))))
	cv2.waitKey()
	cv2.destroyAllWindows()
	# 透视
	cv2.imshow("original",放缩后图形)
	变换前样本点 = numpy.array([[0,0],[图片半长,0],[0,图片半宽],[图片半长,图片半宽]],dtype = numpy.float32)
	变换后样本点 = numpy.array([[0.2*图片半长, 0],[0.8*图片半长,0],[0,图片半宽],[图片半长,图片半宽]],dtype = numpy.float32)
	透视矩阵 = cv2.getPerspectiveTransform(变换前样本点, 变换后样本点)
	cv2.imshow("clined",cv2.warpPerspective(src=放缩后图形, M=透视矩阵, dsize=(int(对角线半长),int(对角线半长))))
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