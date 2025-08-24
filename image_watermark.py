import os
from PIL import Image

def watermark_image(input_img, watermark_img,output_img):
    base_img = Image.open(input_img)
    watermark = Image.open(watermark_img).convert("RGBA")
    position = base_img.size
    newsize = (int(position[0]*8/100),int(position[0]*8/100))

    watermark = watermark.resize(newsize)


    newposition = position[0]-newsize[0]-20, position[1]-newsize[1]-20
    transparent = Image.new(mode="RGBA", size =position,color = (0,0,0,0))
    transparent.paste(base_img,(0,0))
    transparent.paste(watermark, newposition,watermark)
    image_mode = base_img.mode

    print(image_mode)
    if image_mode == "RGB":
        transparent = transparent.convert(image_mode)

    else:
        transparent = transparent.convert('P')

    transparent.save(output_img,optimize=True, quality=100)
    print("Saving"+output_img+"........>>>>")

folder = input("Enter the folder path : ")
watermark = input("Enter the watermark path : ")
os.chdir(folder)
files = os.listdir(os.getcwd())
print(files)

if not os.path.isdir("output"):
    os.mkdir("output")

c = 1
for f in files:
    if os.path.isfile(os.path.abspath(f)):
        if f.endswith(".png")or f.endswith(".jpg"):
            watermark_image(f,watermark,"output/"+f)
