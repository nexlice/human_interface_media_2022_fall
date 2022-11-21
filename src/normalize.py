def normalize_subtraction(image):
    image_tmp = image.copy()
    # Convert image type type
    image_tmp = image_tmp.astype('float64')
    # do normalization for image and the patch (in-place operation)
    image_tmp -= 128
    return image_tmp

def normalize_pixel(image):
    image_tmp = image.copy()
    # Convert image type type
    image_tmp = image_tmp.astype('float64')
    # do normalization by dividing by whole image 
    denominator =  image_tmp.shape[0] * image_tmp.shape[1]
    image_tmp /= denominator
    return image_tmp

def normalize_reverse(image):
    image_tmp = image.copy()
    # Convert image type type
    image_tmp = image_tmp.astype('float64')
    # do normalization by dividing by whole image 
    image_tmp = 255 - image_tmp
    return image_tmp

def normalize_0to1(image):
    image_tmp = image.copy()
    output_normalized = image_tmp + image_tmp.min()
    output_normalized /= output_normalized.max()
    return output_normalized