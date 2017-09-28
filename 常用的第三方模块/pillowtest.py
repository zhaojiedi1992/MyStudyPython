from PIL import Image

im = Image.open("mm.jpg")
w,h = im.size
print(w,h)
im.thumbnail((w//2,h//2))

im.save("mm2.jpg",'jpeg')