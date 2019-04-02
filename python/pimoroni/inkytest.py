#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pimoroni Inky Screen Test for PHAT"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from PIL import Image, ImageFont, ImageDraw
from font_source_sans_pro import SourceSansPro
from inky import InkyPHAT

inky_display = InkyPHAT('black')
scale_size = 1
padding = 0

inky_display.set_border(inky_display.BLACK)


def create_mask(source,
                mask=(inky_display.WHITE, inky_display.BLACK,
                      inky_display.RED)):
    """Create a transparency mask.
    Takes a paletized source image and converts it into a mask
    permitting all the colours supported by Inky pHAT (0, 1, 2)
    or an optional list of allowed colours.
    :param mask: Optional list of Inky pHAT colours to allow.
    """
    mask_image = Image.new("1", source.size)
    w, h = source.size
    for x in range(w):
        for y in range(h):
            p = source.getpixel((x, y))
            if p in mask:
                mask_image.putpixel((x, y), 255)

    return mask_image


icon_image = Image.open("pythonlogo.png")
icon_mask = create_mask(icon_image)

console_font = ImageFont.truetype(SourceSansPro, int(10 * scale_size))

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

img.paste(icon_image, (140, 0), icon_mask)

hello_x = 0
hello_y = 0
draw.text((hello_x, hello_y),
          ">>> print('Hello World!')\n\
>>> Hello World! \n\
>>> inky_display = InkyPHAT('black')\n\
>>> Image.open('pythonlogo')\n>>> ImageDraw.Draw(img))\n\
>>> inky_display.set_image(img)\n>>> inky_display.show()",
          inky_display.BLACK,
          font=console_font)

inky_display.set_image(img)
inky_display.show()
