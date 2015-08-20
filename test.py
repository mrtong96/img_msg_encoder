# for testing stuff

import numpy as np
from PIL import Image

# create a 100 x 100 black image and display it
# numbers are height, width, RGB
rgb = np.zeros([20,10,3], dtype='uint8')

img = Image.fromarray(rgb)

img.save('test.png')

# now reading the image...

img_name = 'test.png'
img = Image.open(img_name)

# size shows tuple of (width, height)
print 'img size: {}.'.format(img.size)

# len(data) = width * height * 3, 3 for RGB
data = img.tobytes()
print len(data)
print ':'.join(x.encode('hex') for x in data[0:3])

# how to reassign pixel values
img.putpixel((0,0), (0xAA, 0xBB, 0xCC))
data = img.tobytes()
print ':'.join(x.encode('hex') for x in data[0:3])

# getpixel() returns (R, G, B) tuple, location is (width, height)
print img.getpixel((9,0))

img.show()
