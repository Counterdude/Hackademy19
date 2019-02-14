from PIL import Image
import code
import os


def rotate_box(an_image):
    box = (100,100,400,400)
    region = an_image.crop(box)
    transposed = region.transpose(Image.ROTATE_180)
    an_image.paste(transposed,box)
    return an_image

# im = Image.open("C:\\Users\\Counter\\Pictures\\picture1.jpg")
# print(im.size)
# print(im.format)


# box = (100,100,400,400)
# region = im.crop(box)
# transposed = region.transpose(Image.ROTATE_180)
# im.paste(transposed,box)


# im2 = Image.open("C:\\Users\\Counter\\Pictures\\picture2.jpg")
# im2 = rotate_box(im2)

# im.show()
# im2.show()


pic_list = code.get_filenames("C:\\Users\\Counter\\Pictures\\pics")
print(pic_list)

# for pic_name in pic_list:
#     im = Image.open(pic_name)
#     im = rotate_box(im)


def to_grayscale(an_image):
    grayscale_im = an_image.convert("L")
    return grayscale_im

# im = Image.open("C:\\Users\\Counter\\Pictures\\pics\\picture1.jpg")
# im = to_grayscale(im)
# im.show()

num = 0
for pic_name in pic_list:
    filename = "picrotate" + str(num) + ".jpg"
    num = num + 1
    im = Image.open(pic_name)
    im = rotate_box(im)
    im = to_grayscale(im)
    newpath = os.path.join("C:\\Users\\Counter\\Pictures\\pics\\grayscale", filename)
    im.save(newpath)