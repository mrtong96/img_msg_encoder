import numpy as np
from PIL import Image

# runs some tests. Initializes black image
# then encodes a picture with message and then decodes it
def main():
    input_img = 'small_test.png'
    output_img = '{}_encoded.png'.format(input_img[:-4])
    message_file = 'msg.txt'

    create_black_img(10, 10, input_img)
    encode(input_img, output_img, message_file)
    result = decode(output_img)
    print 'small test output length: {}'.format(len(result))
    print 'small test output: {}'.format(result)
    print '-' * 80

    input_img = 'large_test.png'
    output_img = '{}_encoded.png'.format(input_img[:-4])
    message_file = 'RnJ.txt'

    create_black_img(400, 400, input_img)
    encode(input_img, output_img, message_file)
    result = decode(output_img)
    print 'large test output length: {}'.format(len(result))
    print 'sample from large test:\n{}'.format(result[0:800])
    print '-' * 80

    input_img = 'ftl_game.png'
    output_img = '{}_encoded.png'.format(input_img[:-4])
    message_file = 'RnJ.txt'

    encode(input_img, output_img, message_file)
    result = decode(output_img)
    print 'ftl screenshot output length: {}'.format(len(result))
    print 'sample from ftl screenshot output:\n{}'.format(result[0:800])
    print '-' * 80

def create_black_img(width, height, name):
    rgb = np.zeros([height, width, 3], dtype='uint8')
    img = Image.fromarray(rgb)
    img.save(name)

def encode(input_img, output_img, message_file):
    img = Image.open(input_img).convert('RGB')
    img_data = img.load()
    
    # null char for termination when decoding
    text = open(message_file, 'r').read() + '\0'
    img_w, img_h = img.size

    if len(text) > img_w * img_h:
        print 'message too long to be encoded into image'
        return

    for i, char in enumerate(text):
        x = i % img_w
        y = i / img_w

        r_value, g_value, b_value = img_data[x, y]
        ascii_value = ord(char)

        # split 2/2/3 among R/G/B
        r_value = r_value & 0xFC | ascii_value >> 5
        g_value = g_value & 0xFC | ascii_value >> 3 & 0x3
        b_value = b_value & 0xF8 | ascii_value & 0x7

        img_data[x, y] = (r_value, g_value, b_value)

    img.save(output_img)

def decode(input_img):
    img = Image.open(input_img).convert('RGB')
    img_data = img.load()
    img_w, img_h = img.size

    text = ''

    for y in range(img_h):
        for x in range(img_w):
            # RGB split is 2/2/3
            r_value, g_value, b_value = img_data[x,y]

            r_value = r_value & 0x3
            g_value = g_value & 0x3
            b_value = b_value & 0x7

            ascii_value = r_value << 5 | g_value << 3 | b_value
            char = chr(ascii_value)

            if ascii_value:
                text += char
            else:
                return text
    return text  # shouldn't happen, but just in case

if __name__ == '__main__':
    main()

