import numpy as np

def pad_image():
    # https://stackoverflow.com/questions/43391205/add-padding-to-images-to-get-them-into-the-same-shape
    # image = np.pad(
    #     image, 
    #     (patch_height//2, patch_height//2, patch_width//2, patch_width//2), 
    #     mode = 'constant', 
    #     constant_values = 0
    # )
    pass

def correlation(image, patch):
    """Apply correlation filtering to image

    Args:
        image(np.ndarray): 2D signal of shape (height, width)
        patch(np.ndarray): 2D filter of shape (height, width)
    
    Return:
        (np.ndarray): 2D output of correlation filtering
    """
    image_tmp = image.copy()
    patch_tmp = patch.copy()

    # compute correlation
    # output[h, w] = np.sum(image[h:h+patch_height, w:w+patch_width] * patch)
    image_height, image_width = image.shape
    patch_height, patch_width = patch.shape
    output = np.empty(
        (
            image_height - patch_height + 1, 
            image_width - patch_width + 1
        ), 
        dtype='float64'
    )
    for h in range(image_height - patch_height + 1):
        for w in range(image_width - patch_width + 1):
            output[h, w] = np.sum(image_tmp[h : h + patch_height, w : w + patch_width] * patch_tmp)

    return output


def three_channel_correlation(image, patch):
    """Apply correlation filtering to color image with color filter

    Args:
        image(np.ndarray): 3D signal of shape (height, width, color=3)
        patch(np.ndarray): 3D filter of shape (height, width, color=3)
    
    Return:
        (np.ndarray): 2D output of correlation filtering
    """
    assert image.shape[-1] == 3, "Last axis should be color axis"
    # -1 은 마지막 인덱스..
    outputs = [correlation(image[:, :, color], patch[:, :, color]) for color in range(image.shape[-1])]
    return outputs[0] + outputs[1] + outputs[2]


def convolution_patch(image):
    """Change the x axis to reverse of color image

    Args:
        patch(np.ndarray): 3D filter of shape (height, width, color=3)
    
    Return:
        (np.ndarray): 3D output of correlation filtering
    """
    image_tmp = image.copy()
    # Convert image type type
    # do normalization by dividing by whole image 
    image_tmp = image_tmp[:,::-1,:]
    return image_tmp
