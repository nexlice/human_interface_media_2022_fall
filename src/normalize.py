def normalize_subtraction(image):
    # Convert image type type
    image = image.astype('float64')
    # do normalization for image and the patch (in-place operation)
    image -= 128
    return image

def normalize_pixel(image):
    # Convert image type type
    image = image.astype('float64')
    # do normalization by dividing by whole image 
    denominator =  image.shape[0] * image.shape[1]
    image /= denominator
    return image

def normalize_reverse(image):
    # Convert image type type
    image = image.astype('float64')
    # do normalization by dividing by whole image 
    image = 255 - image
    return image