import numpy as np

def pad_image():
    # https://stackoverflow.com/questions/43391205/add-padding-to-images-to-get-them-into-the-same-shape
    # image = np.pad(
    #     image, 
    #     (patch_height//2, patch_height//2, patch_width//2, patch_width//2), 
    #     mode = 'constant', 
    #     constant_values = 0
    # )
    ...

def correlation(image, patch):
    """Apply correlation filtering to image

    Args:
        image(np.ndarray): 2D signal of shape (height, width)
        patch(np.ndarray): 2D filter of shape (height, width)
    
    Return:
        (np.ndarray): 2D output of correlation filtering
    """
    image = image.copy()
    patch = patch.copy()

    # Convert image type type
    image = image.astype('float64')
    patch = patch.astype('float64')
    
    # do normalization for image and the patch (in-place operation)
    image -= 128
    patch -= 128

    # 2. compute correlation
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
            output[h, w] = np.sum(image[h : h + patch_height, w : w + patch_width] * patch)

    return output
