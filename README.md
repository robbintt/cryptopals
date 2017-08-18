## Cryptopals in Python and C

I'm solving these in Python as a sketch then solving them in C.


### Cryptopals Rules

1. Section 1.1 `base16->base64`: "Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing."


### Base64

- wikipedia: [base64](https://en.wikipedia.org/wiki/Base64)
- Python: [base64 module](https://docs.python.org/2/library/base64.html)
    - `base64` wraps [binascii](https://docs.python.org/2/library/binascii.html)
- [4-column ascii](https://garbagecollected.org/2017/01/31/four-column-ascii/)
