import cv2
# https://inhovation97.tistory.com/56
import matplotlib.pyplot as plt
from matplotlib import gridspec
from tqdm import tqdm

#load image
image = cv2.imread('image01_small.jpg')
image = image[:,:,::-1] # BGR -> RGB
width = len(image[0,:,0]) 
height = len(image[:,0,0]) 

#load pre-defined patch
for i in range(3):

    #load the patch image.
    globals()["patch{}".format(i + 1)] = cv2.imread('patch' + str(i + 1) + '_small.jpg')[:,:,::-1] # BGR -> RGB

    #inverse the patch.
    globals()["patch_inversed{}".format(i + 1)] = globals()["patch{}".format(i + 1)][:,::-1,:] # BGR -> RGB, x inversed

    #normalize the patch.
    globals()["patch_inversed{}".format(i + 1)] = globals()["patch_inversed{}".format(i + 1)].astype('float64') - 128

    #define convolution map.
    globals()["convolution_map{}".format(i + 1)] = image.copy()

    #change datatype to prevent overflow.
    globals()["convolution_map{}".format(i + 1)] = globals()["convolution_map{}".format(i + 1)].astype('float64')

#do convolution.
for p in range(3):
    patch_width = len(globals()['patch' + str(p + 1)][0,:,0]) 
    patch_height = len(globals()['patch' + str(p + 1)][:,0,0])

    #https://stackoverflow.com/questions/43391205/add-padding-to-images-to-get-them-into-the-same-shape
    #do padding for patch size.
    #normalize by subtracting 128.
    globals()["image{}".format(p + 1)] = cv2.copyMakeBorder(src = image.copy(), top = int(patch_height/2), bottom = int(patch_height/2), left = int(patch_width/2), right = int(patch_width/2), borderType = cv2.BORDER_CONSTANT, value= [0, 0, 0]).astype('float64') - 128

    #do normalization for patch and the original image.

    #do convolution.
    for img_y in tqdm(range(height)):
        for img_x in range(width):
            for rgb in range(3):
                globals()["convolution_map" + str(p + 1)][img_y, img_x, rgb] = 0
                for patch_y in range(patch_height):
                    for patch_x in range(patch_width):
                        globals()["convolution_map" + str(p + 1)][img_y, img_x, rgb] +=  globals()["patch_inversed" + str(p + 1)][patch_y, patch_x, rgb].astype('float64') * globals()["image" + str(p + 1)][img_y + patch_y, img_x + patch_x, rgb].astype('float64')


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
#ax2.imshow(image)
ax2.imshow(globals()['image1'])
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