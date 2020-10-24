from PIL import Image
import glob
import os
import shutil

SIZES = [1080, 720, 480, 360, 240]
EXTENSIONS = ['.png', '.jpg', '.jpeg']

for folder in ['fullsize', *map(str, SIZES)]:
    if not os.path.exists(folder):
        os.makedirs(folder)
        
image_list = [f for f in glob.glob('*') if os.path.splitext(f)[1].lower() in EXTENSIONS]

for image in image_list:
    image_name = os.path.basename(image).split('.')[0]
    with Image.open(image) as im:
        # Change format of fullsize image
        im.save(image_name + '.jpg', format='JPEG')
        # Create resized versions
        for size in SIZES:
            resized_im = im.resize((size, int(im.height/im.width * size)))
            resized_im.save(os.path.join(str(size), image_name + '.jpg'), format='JPEG')
    # Move original file into fullsize folder
    shutil.move(image_name + '.jpg', os.path.join('fullsize', image_name + '.jpg'))
    print(f'Resized: {image_name}')