import traceback
import os
import pathlib
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
	图片路径 = pathlib.Path()
	# 路径为 pathlib.Path
	try:
		图片路径 = random.sample(tuple(输入图片文件夹.iterdir())[:-1],1)[0]
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
	print("图片数据：",type(图片数据),图片数据.shape,图片数据.dtype)
	cv2.imshow("original",图片数据)
	cv2.waitKey()
	cv2.destroyAllWindows()


	蓝色数据, 绿色数据, 红色数据 = cv2.split(图片数据)
	蓝色数据 = numpy.asarray(蓝色数据, dtype="float")
	红色数据 = numpy.asarray(红色数据, dtype="float")
	绿色数据 = numpy.asarray(绿色数据, dtype="float")

	傅里叶变换数据_蓝色 = cv2.dft(蓝色数据, flags=cv2.DFT_COMPLEX_OUTPUT)
	傅里叶变换数据_红色 = cv2.dft(红色数据, flags=cv2.DFT_COMPLEX_OUTPUT)
	傅里叶变换数据_绿色 = cv2.dft(绿色数据, flags=cv2.DFT_COMPLEX_OUTPUT)

	print("傅里叶变换数据_蓝色：",type(傅里叶变换数据_蓝色),傅里叶变换数据_蓝色.shape)
	print("傅里叶变换数据_红色：",type(傅里叶变换数据_红色),傅里叶变换数据_红色.shape)
	print("傅里叶变换数据_绿色：",type(傅里叶变换数据_绿色),傅里叶变换数据_绿色.shape)

	cv2.imshow("blue  real",    傅里叶变换数据_蓝色)
	cv2.imshow("red   real",    傅里叶变换数据_红色)
	cv2.imshow("green real",    傅里叶变换数据_绿色)

	#傅里叶变换实部数据_蓝色 = 傅里叶变换数据_蓝色[:,:,0]
	#傅里叶变换实部数据_红色 = 傅里叶变换数据_红色[:,:,0]
	#傅里叶变换实部数据_绿色 = 傅里叶变换数据_绿色[:,:,0]
	#傅里叶变换虚部数据_蓝色 = 傅里叶变换数据_蓝色[:,:,1]
	#傅里叶变换虚部数据_红色 = 傅里叶变换数据_红色[:,:,1]
	#傅里叶变换虚部数据_绿色 = 傅里叶变换数据_绿色[:,:,1]

	#cv2.imshow("blue  real",    傅里叶变换实部数据_蓝色)
	#cv2.imshow("red   real",    傅里叶变换实部数据_红色)
	#cv2.imshow("green real",    傅里叶变换实部数据_绿色)
	#cv2.imshow("blue  imagine", 傅里叶变换虚部数据_蓝色)
	#cv2.imshow("red   imagine", 傅里叶变换虚部数据_红色)
	#cv2.imshow("green imagine", 傅里叶变换虚部数据_绿色)
	cv2.waitKey()
	cv2.destroyAllWindows()

	# 生成密文版
	#红色密文 = "红色密文"
	#蓝色密文 = "蓝色密文"
	#绿色密文 = "绿色密文"
	#def 生成密文板(单通道图片:numpy.ndarray, 文本:str="密文示例", 字体路径:str=r"C:/Windows/Fonts/simsun.ttc", 字体大小:int=0, 起始点:tuple = None):
	#	底板 = numpy.zeros_like(单通道图片)
	#	图片长 = 单通道图片.shape[1]
	#	图片宽 = 单通道图片.shape[0]
	#	PIL图片数据 = PIL.Image.fromarray(底板)
	#	PIL绘图对象 = PIL.ImageDraw.Draw(PIL图片数据)
	#	if 字体大小 <= 0:
	#		字体大小 = int(0.5*min(图片长/len(文本),图片宽))
	#	if 起始点 == None:
	#		起始点 = (int(图片长/2-字体大小*len(文本)/2),int(图片宽/2-字体大小/2))
	#	字体 = PIL.ImageFont.truetype(
	#		font=字体路径,
	#		size=字体大小,
	#		encoding="utf-8")
	#	PIL绘图对象.text(
	#		xy=起始点,
	#		text=文本,
	#		fill=1,
	#		font=字体)
	#	return numpy.asarray(PIL图片数据)
	#蓝色密文板 = 生成密文板(单通道图片 = 傅里叶变换数据_蓝色,文本 = 蓝色密文)
	#红色密文板 = 生成密文板(单通道图片 = 傅里叶变换数据_红色,文本 = 红色密文)
	#绿色密文板 = 生成密文板(单通道图片 = 傅里叶变换数据_绿色,文本 = 绿色密文)
	#cv2.imshow("blue  code",蓝色密文板)
	#cv2.imshow("red   code",红色密文板)
	#cv2.imshow("green code",绿色密文板)
	#cv2.waitKey()
	#cv2.destroyAllWindows()

	# 加密
	#傅里叶变换数据_蓝色[蓝色密文板>0] = 0
	#傅里叶变换数据_红色[红色密文板>0] = 0
	#傅里叶变换数据_绿色[绿色密文板>0] = 0
	#cv2.imshow("blue  real", 傅里叶变换数据_蓝色)
	#cv2.imshow("red   real", 傅里叶变换数据_红色)
	#cv2.imshow("green real", 傅里叶变换数据_绿色)
	#cv2.waitKey()
	#cv2.destroyAllWindows()

	# 组合还原
	#傅里叶变换数据_蓝色[:,:,0] = 傅里叶变换数据_蓝色
	#傅里叶变换数据_红色[:,:,0] = 傅里叶变换数据_红色
	#傅里叶变换数据_绿色[:,:,0] = 傅里叶变换数据_绿色
	蓝色数据 = cv2.idft(傅里叶变换数据_蓝色, flags=cv2.DFT_COMPLEX_OUTPUT)
	红色数据 = cv2.idft(傅里叶变换数据_红色, flags=cv2.DFT_COMPLEX_OUTPUT)
	绿色数据 = cv2.idft(傅里叶变换数据_绿色, flags=cv2.DFT_COMPLEX_OUTPUT)
	加密图片数据 = numpy.asarray(cv2.merge([蓝色数据,红色数据,绿色数据]),dtype="uint8")
	cv2.imshow("coded", 加密图片数据)
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