import cv2
# https://inhovation97.tistory.com/56
import matplotlib.pyplot as plt
from matplotlib import gridspec


# image = cv2.imread('image01.jpg')
# cv2.imshow('original', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# image_name = "image"
# number = 0
# input_number = 22

# for i in range(input_number):
#     number = i + 1
#     #https://alphahackerhan.tistory.com/55
#     number = format(number, '02')

#     image = cv2.imread('image' + str(number) + '.jpg')
#     cv2.imshow('original' + str(number), image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#load pre-defined patch
for i in range(3):
    globals()["patch{}".format(i + 1)] = cv2.imread('patch' + str(i + 1) + '.png')[:,:,::-1] # BGR -> RGB


#do convolution


#show convolution results.


#find the bounding box


#print the result

image = cv2.imread('image01.jpg')
image = image[:,:,::-1] # BGR -> RGB


fig = plt.figure(figsize = (15,10))
#gs = gridspec.GridSpec(nrows = 2, ncols = 3, height_ratios=[10, 1])

plt.subplot(3,4,1)
plt.imshow(globals()['patch1'])
plt.title('patch1')
plt.xticks([])
plt.yticks([])

plt.subplot(3,4,2)
plt.imshow(image)
plt.title('original')
plt.xticks([])
plt.yticks([])

plt.subplot(3,4,3)
plt.imshow(image)
plt.title('convolution - heatmap')
plt.xticks([])
plt.yticks([])

plt.subplot(3,4,4)
plt.imshow(image)
plt.title('results')
plt.xticks([])
plt.yticks([])

plt.subplot(3,4,5)
plt.imshow(globals()['patch2'])
plt.title('patch2')
plt.xticks([])
plt.yticks([])

plt.subplot(3,4,6)
plt.imshow(image)
plt.title('original')
plt.xticks([])
plt.yticks([])

plt.subplot(3,4,7)
plt.imshow(image)
plt.title('convolution - heatmap')
plt.xticks([])
plt.yticks([])

plt.subplot(3,4,8)
plt.imshow(image)
plt.title('results')
plt.xticks([])

plt.subplot(3,3,9)
plt.imshow(globals()['patch3'])
plt.title('patch3')
plt.xticks([])
plt.yticks([])

plt.subplot(3,4,10)
plt.imshow(image)
plt.title('original')
plt.xticks([])
plt.yticks([])

plt.subplot(3,4,11)
plt.imshow(image)
plt.title('convolution - heatmap')
plt.xticks([])
plt.yticks([])

plt.subplot(3,4,12)
plt.imshow(image)
plt.title('results')
plt.xticks([])

plt.show()