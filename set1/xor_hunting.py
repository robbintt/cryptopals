''' Find the single character that the hex encoded string has been xor'd against

The thing says to use a letter frequency checker.
I have done this a lot and skipped it.

result: ('X', "Cooking MC's like a pound of bacon")
'''
import base64

hex_encoded_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# turned them into characters even though we are using xor with ints
test_characters = [chr(x) for x in range(256)]


def xor_by_char(target, c):
    ''' XOR a target string by c

    target  => encoded hex string as python string
    c       => character as python string
    '''
    # decode from base16 to binary
    decoded_string = base64.b16decode(target, True)

    result = list()
    for letter in decoded_string:
        result.append(chr(ord(letter) ^ ord(c)))

    return ''.join(result)


if __name__ == '__main__':
    '''
    '''
    for c in test_characters:
        print(c, xor_by_char(hex_encoded_string, c))

