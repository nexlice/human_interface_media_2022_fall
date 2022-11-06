def normalize_image(image):
    # Convert image type type
    image = image.astype('float64')
    # do normalization for image and the patch (in-place operation)
    image -= 128
    return image
