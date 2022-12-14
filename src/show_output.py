import matplotlib.pyplot as plt
from matplotlib import gridspec
import cv2

def show_output(patch, image, output, threshhold):
    #print the result
    fig = plt.figure(dpi=200, tight_layout=True)
    gs = gridspec.GridSpec(nrows = 1, ncols = 3, width_ratios = [1, 8, 8])

    ax0 = plt.subplot(gs[0])
    ax0.imshow(patch)
    ax0.set_title('patch')
    ax0.set_xticks([])
    ax0.set_yticks([])

    #show output results.
    ax1 = plt.subplot(gs[1])
    im = ax1.imshow(output, cmap="rainbow", interpolation= 'bilinear')
    ax1.set_title('cross correlation')
    ax1.set_xticks([])
    ax1.set_yticks([])

    #make colorbar
    cb = fig.colorbar(im, ax = ax1, shrink = 0.7)
    
    #find the bounding box
    ax2 = plt.subplot(gs[2])

    image_tmp = image.copy()

    for i in range (output.shape[0]):
        for j in range (output.shape[1]):
            if output[i,j] >= threshhold:
                image_tmp = cv2.rectangle(image_tmp, (j, i), (j + patch.shape[1], i + patch.shape[0]), color = (0, 0, 255), thickness = 2)

    image_RGB = image_tmp[:,:,::-1] # BGR -> RGB
    ax2.imshow(image_RGB)
    ax2.set_title('results')
    ax2.set_xticks([])
    ax2.set_yticks([])

    plt.show()