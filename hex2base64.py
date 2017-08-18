""" Decode a base16 string and encode it to base64 using the `base64 standard library module`

base16 is hex

Cryptopals Rule: "Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing."
"""

import sys
import base64

for i in sys.argv[1:]:
    try:
        # casefold must be True in b16decode
        print(base64.b64encode(base64.b16decode(i, True)))
    except Exception as e:
        print("There was some issue: {}".format(e))

