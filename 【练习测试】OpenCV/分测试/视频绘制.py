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

	print("视频信息：")
	视频名称 = ((图片路径.name).split("."))[0] + "-rotate.mp4"
	每秒帧数 = 60
	视频秒数 = 8
	总帧数 = int(视频秒数 * 每秒帧数) + 1
	幅面 = (图片彩色数据.shape[1],图片彩色数据.shape[0])
	输出路径 = 输出图片文件夹 / 视频名称
	四字符代码编号 = cv2.VideoWriter_fourcc(*'mp4v')
	print("\t总时长：         {} s".format(视频秒数))
	print("\t帧数：           {} 帧 / s".format(每秒帧数))
	print("\t四字符代码编号： {}".format(四字符代码编号))
	print("\t幅面：           {}".format(幅面))
	print("\t输出路径：")
	角度分割 = numpy.linspace(0, 360, 总帧数)
	视频对象 = cv2.VideoWriter(
		filename  = 输出路径,
		fourcc    = 四字符代码编号,
		fps       = 每秒帧数,
		frameSize = 幅面
	)

	for i,角度 in enumerate(角度分割):
		旋转矩阵 = cv2.getRotationMatrix2D(center=(幅面[0]/2, 幅面[1]/2), angle=角度, scale=1)
		当前帧 = cv2.warpAffine(src=图片彩色数据, M=旋转矩阵, dsize=幅面)
		视频对象.write(当前帧)
		print("当前进度：{} / {}".format(i+1, 总帧数))
	视频对象.release()
	print("视频生成完成")
	

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