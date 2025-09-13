## inspector-image

Inspector-image is a program that reads and analyzes the binary data of a JPEG which was created using a [steganography technique](#steganography).

## Steganography

Steganography is the practice of representing information within another message or physical object. In this particular case a JPEG image was used to hide a PGP key as a simple string at the end of the JPEG binary. This is what the output looks like if you read the content of the JPEG as binary (Python represents binary values as hexadecimal when ouputting to the console):

```
...
\xd9\xf8?\xc0\xfe\x1f\xd0\xad\xf4o\x1cj\xb6\x9alZn\x99\r\xaaYAs\xe1\xbdnk\x88\xa1X\xd4\x08\xd2Yc\x8eGU\xc0wEf\xc9\x00\xd0\x07A\xe1O\xf4O\xdak\xe2N\x9di\xfb\x9bK\x9f\x07\xf8KV\x9a\x08\xfeX\xe5\xbe\x92\xeb[\xb7\x92\xe5\x94p\xd34\x16Vq4\x87\xe61\xda\xc0\x84\xed\x8d\x00\x00\xff\xd9Enter   -----BEGIN PGP PUBLIC KEY BLOCK-----  \nVersion: 01  \n  \nmQENBGIwpy4BCACFayWXCgHH2QqXkicbqD1ZlMUALpyGxDFiWh1SErFUPJOO/CgU  \n2688bAd26kxDSGShiL9YUOQJ6MS+zJ0KlBkeKPoQlPHRBVpH7vjcRbZNgDxd82uE  \n7mhM6AH+W3fAim/PhU3lm661UGMCHM3YLupa/N0Dhhmfimtg+0AimCoXk6Q6WJxg  \nao8XY1Wqacd2L0ssASY5EkMahNgtX0Ri8snbTlImd5Jq/sC4buZq96IlxyhtX0ew  \nzD/md0U++8SxG9+gi+uuImqV8Wq1YHvJH5BtIbfcNG9V00+03ikEX9tppKxCkhzx  \n9rSqvyH6Uirs3FVhFtoXUSg8IeYgSH6p5tsVABEBAAG0CDAxQDAxLjAxiQEcBBAB  \nAgAGBQJiMKcuAAoJEAJuInmYDhhbO3gIAITZhEtLBj524y1oeBKI5fZDwgCQum6B  \nD9ZaUq1+dI98HsiRAiUqw1YbuJQgeUVGCmqXeC3E7VTPCPZsaCLfWWZVeosRIqB8  \nPwGxcY6vXHYR4S6T8rHwsNASw+Vo2pmQIGn4tABmtyappqJbwSz+5yg73DjYXiX/  \ne/f6i9nrFFsfMjjKd71cAyHjV8u0z7fGDXpR22vo7CdloXMxsZRyHjd/4ofUgvu0  \n6hWYG2zBWTXpwaYRU9u1NCr1gfKnukm8gbILSSgjr8pQ3OLWHleJXc0sCEJFKSbg  \n+I0KJP7Ccrxy0MaKYk0T0tYbBrvqQCzXqzAqcjn+1GoDDS1J8WBJopM=  \n=N8hc  \n-----END PGP PUBLIC KEY BLOCK----- Enter
```

As we can see from the example above, the last hexadecimal value before the hidden key is xd9 which marks the end of the actual image and adding any data after that marker will not 'break' the image. For JPEGs the hidden data could also added before the start of the image marker.

Steganography is also used to 'hide' info about the image like the GPS location where the image was created. These values are stored in the Exif metadata tags, which are also marked by different values. The program uses Pythons standard library Pillow to retrieve those values.

## Requirements

[Python 3.x](https://www.python.org/downloads/)

## Dependencies

No other dependencies apart from standard libraries were used.

## Usage: how to run

To run the project enter the command `python3 main.py -<option> <fileName>`.
