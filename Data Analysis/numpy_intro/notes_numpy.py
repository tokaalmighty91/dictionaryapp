n=numpy.arange(27)
n.reshapre(3,9)

#convert plain pandas list to numpy array
numpy.asarray([[],[],[]])

#install OpenCV (cv2) image processing library
pip install opencv-python
import cv2

#OpenCV uses bgr color order
image=cv2.imread('something.png',0) #0 to read in b/w, 1 to read in color
image2=cv2.imwrite('something_else.png', image) #return True if img created
#Python index slicing is right exclusive [2:3)

for i in image.T #transpose
for i in image.flat
	print (i) #break down list items, print one at a time

#horizontal stacking
numpy.hstack(image,image) #concatenate each row
#vertical stacking
numpy.vstack(image,image)
#stacking arrays with different dimensions will return error

#horizontal splitting
numpy.hsplit(image,<divided into how many arrays based on columns>)
#vertical splitting
numpy.vsplit(image,<divided into how many arrays based on rows>)
 