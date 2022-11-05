import cv2
# https://inhovation97.tistory.com/56
import matplotlib.pyplot as plt
from matplotlib import gridspec

#load image
image = cv2.imread('image01.jpg')
image = image[:,:,::-1] # BGR -> RGB
width = len(image[0,:,0]) #850
height = len(image[:,0,0]) #1202

#load pre-defined patch
for i in range(3):

    #load the image.
    globals()["patch{}".format(i + 1)] = cv2.imread('patch' + str(i + 1) + '.png')[:,:,::-1] # BGR -> RGB

    #inverse the patch.
    globals()["patch_inversed{}".format(i + 1)] = globals()["patch{}".format(i + 1)][:,::-1,:] # BGR -> RGB, x inversed

    #define convolution map.
    globals()["convolution_map{}".format(i + 1)] = [[0 for col in range(width + len(globals()["patch{}".format(i + 1)][0,:,0]))] for row in range(height+len(globals()['patch' + str(i + 1)][:,0,0]))]

#do convolution.
for p in range(3):
    patch_width = len(globals()['patch' + str(p + 1)][0,:,0]) # 280
    patch_height = len(globals()['patch' + str(p + 1)][:,0,0])# 280

    #https://stackoverflow.com/questions/43391205/add-padding-to-images-to-get-them-into-the-same-shape
    #do padding for patch size.
    globals()["image{}".format(p + 1)] = cv2.copyMakeBorder(src = image.copy(), top = 10, bottom = 10, left = 10, right = 10, borderType = cv2.BORDER_CONSTANT, value= [0, 0, 0])
    # for img_y in range(height):
    #     for img_x in range(width):
    #         for patch_y in range(patch_height):
    #             for patch_x in range(patch_width):


#show convolution results.


#find the bounding box


#print the result
fig = plt.figure(dpi=200, tight_layout=True)
gs = gridspec.GridSpec(nrows = 3, ncols = 4,width_ratios = [8, 1, 8, 8])

#patch1
# ax0 = plt.subplot(gs[0])
# ax0.imshow(globals()['patch1'])
# ax0.set_title('patch1')
# ax0.set_xticks([])
# ax0.set_yticks([])

ax1 = plt.subplot(gs[1])
ax1.imshow(globals()['patch1'])
ax1.set_title('patch1')
ax1.set_xticks([])
ax1.set_yticks([])

ax2 = plt.subplot(gs[2])
ax2.imshow(image)
#ax2.imshow(globals()['image1'])
ax2.set_title('convolution')
ax2.set_xticks([])
ax2.set_yticks([])

ax3 = plt.subplot(gs[3])
ax3.imshow(image)
ax3.set_title('results')
ax3.set_xticks([])
ax3.set_yticks([])

#patch2
ax4 = plt.subplot(gs[4])
ax4.imshow(image)
ax4.set_title('original')
ax4.set_xticks([])
ax4.set_yticks([])

ax5 = plt.subplot(gs[5])
ax5.imshow(globals()['patch_inversed2'])
ax5.set_title('patch2')
ax5.set_xticks([])
ax5.set_yticks([])

ax6 = plt.subplot(gs[6])
ax6.imshow(image)
ax6.set_xticks([])
ax6.set_yticks([])

ax7 = plt.subplot(gs[7])
ax7.imshow(image)
ax7.set_xticks([])
ax7.set_yticks([])

#patch3
# ax8 = plt.subplot(gs[8])
# ax8.imshow(globals()['patch3'])
# ax8.set_title('patch3')
# ax8.set_xticks([])
# ax8.set_yticks([])

ax9 = plt.subplot(gs[9])
ax9.imshow(globals()['patch3'])
ax9.set_title('patch3')
ax9.set_xticks([])
ax9.set_yticks([])

ax10 = plt.subplot(gs[10])
ax10.imshow(image)
ax10.set_xticks([])
ax10.set_yticks([])

ax11 = plt.subplot(gs[11])
ax11.imshow(image)
ax11.set_xticks([])
ax11.set_yticks([])

plt.show()
# plt.subplot(3,4,1)
# plt.imshow(globals()['patch1'])
# plt.title('patch1')
# plt.xticks([])
# plt.yticks([])

# plt.subplot(3,4,2)
# plt.imshow(image)
# plt.title('original')
# plt.xticks([])
# plt.yticks([])

# plt.subplot(3,4,3)
# plt.imshow(image)
# plt.title('convolution - heatmap')
# plt.xticks([])
# plt.yticks([])

# plt.subplot(3,4,4)
# plt.imshow(image)
# plt.title('results')
# plt.xticks([])
# plt.yticks([])

# plt.subplot(3,4,5)
# plt.imshow(globals()['patch2'])
# plt.title('patch2')
# plt.xticks([])
# plt.yticks([])

# plt.subplot(3,4,6)
# plt.imshow(image)
# plt.title('original')
# plt.xticks([])
# plt.yticks([])

# plt.subplot(3,4,7)
# plt.imshow(image)
# plt.title('convolution - heatmap')
# plt.xticks([])
# plt.yticks([])

# plt.subplot(3,4,8)
# plt.imshow(image)
# plt.title('results')
# plt.xticks([])
# plt.yticks([])

# plt.subplot(3,4,9)
# plt.imshow(globals()['patch3'])
# plt.title('patch3')
# plt.xticks([])
# plt.yticks([])

# plt.subplot(3,4,10)
# plt.imshow(image)
# plt.title('original')
# plt.xticks([])
# plt.yticks([])

# plt.subplot(3,4,11)
# plt.imshow(image)
# plt.title('convolution - heatmap')
# plt.xticks([])
# plt.yticks([])

# plt.subplot(3,4,12)
# plt.imshow(image)
# plt.title('results')
# plt.xticks([])
# plt.yticks([])

# plt.show()