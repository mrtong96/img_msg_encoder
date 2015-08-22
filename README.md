### Overview ###

Encodes messages in images and can decode messages from encoded images.

### How it Works ###

* Encoding takes an image and a text file and encodes the contents of the text file in an image.
* Decoding takes an image with an encoded string and returns the encoded string.
* Currently only supporst ASCII characters. (7 bits)
* Encodes by storing the ASCII value of each character in the least significant 2, 2, and 3 bits of the red, green, and blue color values of each pixel respectively.
* Decodes by looking at the least significant 2, 2, and 3 bits of the red, green and blue color values of each pixel and concatenates them to form 1 ASCII value. Then the character is generated from the ASCII value. This terminates when the decoder reaches the null character '\0'.

### Instructions ###

1) Download this repository

```
$ git clone git@github.com:mrtong96/img_msg_encoder.git
```

2) Install numpy and Pillow

```
$ pip install numpy
$ pip install Pilow
```

3) Enter this repository
```
$ cd img_msg_encoder
```

4) Run the demo

```
$ python encode.py
```
