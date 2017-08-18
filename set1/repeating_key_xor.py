''' Given a set of strings, and an input, perform repeating key XOR on the input

''' 
import base64

def repeating_key_xor(target, keys):
    ''' use repeating key xor

    target  => encoded hex string as python string
    keys       => list of characters as python list of strings
    '''
    result = list()
    k = 0
    for letter in target:
        # instead of resetting to zero later, we can modulo an increment counter
        result.append(chr(ord(letter) ^ ord(keys[k % len(keys)])))
        k += 1

    return ''.join(result)


if __name__ == '__main__':
    '''
    '''

    input1 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

    # also could use a string and split it later. Might make more sense for later problems.
    repeating_keys = ['I', 'C', 'E']

    result1 = base64.b16encode(repeating_key_xor(input1, repeating_keys))

    expected_result = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

    # check result against expected_result
    print result1 == expected_result.upper()

