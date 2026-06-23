import traceback
import os
import numpy
import cv2
import time

def pause():
	print()
	os.system("pause")
def printshift(obj,n: int):
	间隔 = "\t" * n
	分行 = "\n" + 间隔
	if(not(isinstance(obj,str))):
		obj = repr(obj)
	print(间隔 + 分行.join(obj.split("\n")))

def main():
	所有摄像头对象 = []
	摄像头数量上限 = 4
	目标宽度 = 1920
	目标高度 = 1080
	for i in range(摄像头数量上限):
		摄像头对象 = cv2.VideoCapture(i)
		if not(摄像头对象.isOpened()):
			break
		else:
			摄像头对象.set(cv2.CAP_PROP_FRAME_WIDTH, 目标宽度)
			摄像头对象.set(cv2.CAP_PROP_FRAME_HEIGHT,目标高度)
			所有摄像头对象.append(摄像头对象)
	if (len(所有摄像头对象) == 0):
		raise ValueError("未成功开启摄像头")
	else:
		所有图像 = [numpy.zeros(shape=(480,360,3))]*len(所有摄像头对象)
		while(True):
			# 读取一帧
			for i in range(len(所有摄像头对象)):
				摄像头对象 = 所有摄像头对象[i]
				成功获取图片, 图像 = 摄像头对象.read()
				if 成功获取图片:
					所有图像[i] = 图像
					print("摄像头{}：".format(i),type(图像),图像.shape)
					cv2.imshow("Camera {}".format(i), 图像)
			
			# 按下'q'键退出循环（ord：根据字母返回ascii码）
			if cv2.waitKey(1) == ord("q"):
				break
			time.sleep(0.2)
		# 释放摄像头资源
		for 摄像头对象 in 所有摄像头对象:
			摄像头对象.release()
		# 关闭所有OpenCV窗口
		cv2.destroyAllWindows()


if __name__ == "__main__":
	try:
		main()
		print()
	except:
		traceback.print_exc()
		print()
	finally:
		os.system("pause")
		print()
		print()