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
    with Image.open(image) as im:
        for size in SIZES:
            im.thumbnail(size=(size, size))
            im.save(os.path.join(str(size), image_name), format='JPEG')
    shutil.move(image, os.path.join('fullsize', os.path.basename(image)))
    print(f'Resized: {os.path.basename(image)}')
    