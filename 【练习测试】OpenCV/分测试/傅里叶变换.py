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
	蓝色float数据 = numpy.asarray(蓝色数据, dtype="float")
	红色float数据 = numpy.asarray(红色数据, dtype="float")
	绿色float数据 = numpy.asarray(绿色数据, dtype="float")

	傅里叶变换数据_蓝色 = numpy.fft.fftshift(cv2.dft(蓝色float数据, flags=cv2.DFT_COMPLEX_OUTPUT))
	傅里叶变换数据_红色 = numpy.fft.fftshift(cv2.dft(红色float数据, flags=cv2.DFT_COMPLEX_OUTPUT))
	傅里叶变换数据_绿色 = numpy.fft.fftshift(cv2.dft(绿色float数据, flags=cv2.DFT_COMPLEX_OUTPUT))

	print("傅里叶变换数据_蓝色：",type(傅里叶变换数据_蓝色), 傅里叶变换数据_蓝色.shape)
	print("傅里叶变换数据_红色：",type(傅里叶变换数据_红色), 傅里叶变换数据_红色.shape)
	print("傅里叶变换数据_绿色：",type(傅里叶变换数据_绿色), 傅里叶变换数据_绿色.shape)

	cv2.imshow("blue  real",    傅里叶变换数据_蓝色[:,:,0])
	cv2.imshow("red   real",    傅里叶变换数据_红色[:,:,0])
	cv2.imshow("green real",    傅里叶变换数据_绿色[:,:,0])
	cv2.waitKey()
	cv2.destroyAllWindows()

	#蓝色数据 = cv2.idft(傅里叶变换数据_蓝色)
	#红色数据 = cv2.idft(傅里叶变换数据_红色)
	#绿色数据 = cv2.idft(傅里叶变换数据_绿色)
	#加密图片数据 = numpy.asarray(cv2.merge([蓝色数据,红色数据,绿色数据]),dtype="uint8")
	#cv2.imshow("coded", 加密图片数据)
	#cv2.waitKey()
	#cv2.destroyAllWindows()







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


## coding=utf-8
#import cv2
#import numpy as np
#from matplotlib import pyplot as plt
# 
#img = cv2.imread("/home/wl/3.jpg", 0)
#dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
#dft_shift = np.fft.fftshift(dft) # 用于作图
#rows, cols = img.shape
#crow, ccol = rows/2 , cols/2
## 滤波基板
#mask = np.zeros((rows,cols,2), np.uint8)
#mask[crow-30:crow+30, ccol-30:ccol+30] = 1
## apply mask and inverse DFT
#fshift = dft_shift*mask
#f_ishift = np.fft.ifftshift(fshift)
#img_back = cv2.idft(f_ishift)
#img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
#plt.subplot(121),plt.imshow(img, cmap = 'gray')
#plt.title('Input Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
#plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
#plt.show()