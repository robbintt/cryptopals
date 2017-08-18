''' Find the single character that the hex encoded string has been xor'd against

result: ('X', "Cooking MC's like a pound of bacon")
''' 
import base64
import logging

logging.basicConfig(filename='error.log', level=logging.DEBUG)

# turned them into characters even though we are using xor with ints
test_characters = [chr(x) for x in range(256)]

not_hex_inputs_filename = 'not-hex.log'

# use lower on the string you are testing
# frequencies are per 10,000 letters
# from: https://en.wikipedia.org/wiki/Letter_frequency
letter_frequency_index = {
        'e' : 1270,
        't' :  905,
        'a' :  817,
        'o' :  750,
        'i' :  697,
        'n' :  675,
        's' :  633,
        'h' :  609,
        'r' :  599,
        'd' :  425,
        'l' :  403,
        'c' :  278,
        'u' :  276,
        'm' :  241,
        'w' :  236,
        'f' :  223,
        'g' :  202,
        'y' :  197,
        'p' :  193,
        'b' :  149,
        'v' :   98,
        'k' :   77,
        'j' :   15,
        'x' :   15,
        'q' :   10,
        'z' :    7 }


def letter_frequency_scorer(test_str):
    ''' Return a score of test_str. Higher scores are more similar to English.

    I could also score based on whitespace requirements
        - This might hide actual english though without ascii whitespace

    I could also score based on how many non english characters are present

    FUTURE:
    I am convinced that bigrams is the way to go. Due to the nature of xor, it
    is quite common for SOME result to be very close to the english letter
    frequency space.  English bigram detection solves both english letter
    occurrence and english letter frequency with one pass.
    '''
    score = 0
    presence = 0
    for letter in test_str.lower():
        score += letter_frequency_index.get(letter, 0)
        if letter in letter_frequency_index:
            presence += 1

    # the raw score is based on the frequency of each letter in the english language
    # if a higher ratio of english letters are present, the score is higher
    return score * (float(presence)  / len(test_str))


def xor_by_char(target, c):
    ''' XOR a target string by c

    target  => encoded hex string as python string
    c       => character as python string
    '''
    # decode from base16 to binary
    try:
        decoded_string = base64.b16decode(target.upper(), True)
    except TypeError as e:
        logging.info("{} {}".format(e, target)) 
        with open(not_hex_inputs_filename, 'a') as f:
            f.write(target)
        return False

    result = list()
    for letter in decoded_string:
        result.append(chr(ord(letter) ^ ord(c)))

    return ''.join(result)


if __name__ == '__main__':
    '''
    '''

    hex_encoded_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

    result_list = list()
    for c in test_characters:
        result = xor_by_char(hex_encoded_string, c)
        if not result:
            break
        score = letter_frequency_scorer(result)
            
        result_list.append([score, c, result])

    result_list.sort(key=lambda x: x[0])
    for each in result_list:
        print each

