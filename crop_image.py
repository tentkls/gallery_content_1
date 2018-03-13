import Image
from resizeimage import resizeimage

def crop(image, output, w, h):
    fd_img = open(image, 'r')
    img = Image.open(fd_img)
    width, height = img.size    
    scale = max(w/float(width), h/float(height)) + 0.1
    print scale
    img = img.resize((int(width*scale), int(height*scale)), Image.BILINEAR)    
    half_the_width = img.size[0] / 2
    half_the_height = img.size[1] / 2
    img = img.crop(
      (
        half_the_width - w/2,
        half_the_height - h/2,
        half_the_width + w/2,
        half_the_height + h/2
      )
    )
    img.save(output, img.format)
    fd_img.close()

crop('../app/app/src/main/res/drawable/icon_template.png', '../app/app/src/main/res/drawable/icon.png', 512, 512)
crop('../app/app/src/main/res/drawable/icon_template.png', '../app/app/src/main/res/drawable/banner.png', 1024, 500)
