# -*- coding: utf-8 -*-
# Python2.7
# Author: ZER0-Nu1L

import base64
filename = 'secretrendezvous-cut.bin'
tofilename = 'secretrendezvous.docx'
with open(filename, 'rb') as f:
    base64_data = f.read()
    str = base64.b64decode(base64_data)
    with open(tofilename, 'wb') as f:
        f.write(str)