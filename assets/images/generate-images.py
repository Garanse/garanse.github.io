from PIL import Image
import glob
import os
import shutil

SIZES = [1080, 720, 480, 360, 240]

for folder in ['fullsize', *map(str, SIZES)]:
    if not os.path.exists(folder):
        os.makedirs(folder)
        
image_list = glob.glob('*.jpg') + glob.glob('*.jpeg') + glob.glob('*.png')

for image in image_list:
    image_name = os.path.basename(image)
    with Image.open(image_list[0]) as im:
        for size in [1080, 360, 32]:
            im.thumbnail(size=(size, size))
            im.save(os.path.join(str(size), image_name), format='JPEG')

for file in image_list:
    shutil.move(file, os.path.join('fullsize', os.path.basename(file)))