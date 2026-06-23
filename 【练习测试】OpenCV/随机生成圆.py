import cv2
import numpy

def 随机画圆(个数:int, 图片文件名:str):
	所有颜色  = numpy.random.randint(low=0,  high=255,  size=(个数,3), dtype=numpy.uint)
	所有位置x = numpy.random.randint(low=0,  high=1920, size=(个数,),  dtype=numpy.uint)
	所有位置y = numpy.random.randint(low=0,  high=1080, size=(个数,),  dtype=numpy.uint)
	所有半径  = numpy.random.randint(low=10, high=200,  size=(个数,),  dtype=numpy.uint)

	幅面 = numpy.zeros((1080, 1920, 3), dtype=numpy.uint8)

	for 颜色, x, y ,r in zip(所有颜色,所有位置x,所有位置y,所有半径):
		cv2.circle(
				img       = 幅面,
				center    = (x, y),
				radius    = r,
				color     = [int(i) for i in 颜色],
				thickness = -1
			)
	cv2.imwrite(图片文件名,幅面)

for i in range(10,20):
	随机画圆(个数=numpy.random.randint(low=0, high=15), 图片文件名="{}.png".format(i))