from PIL import Image
import glob
import os

out_dir = 'Practicas/P3/'
cnt = 0
for img in glob.glob('Practicas/P3/*.bmp'):
    filename= ".".join(os.path.basename(img).split('.')[:-1])
    Image.open(img).save(os.path.join(out_dir, filename + '.png'))
    cnt += 1