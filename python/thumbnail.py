from PIL import Image

def get_thumbnail(img: Image.Image) -> Image.Image:
    imgcopy = img.copy()
    imgcopy.thumbnail((48, 48))
    return imgcopy
