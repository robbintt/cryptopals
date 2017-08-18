''' take 2 equal length buffers and produce their XOR

Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination.


Test data:

    hex decode and xor these values

    1. 1c0111001f010100061a024b53535009181c
    2. 686974207468652062756c6c277320657965

Expected Result: 746865206b696420646f6e277420706c6179

'''
import base64

t1 = '1c0111001f010100061a024b53535009181c'
t2 = '686974207468652062756c6c277320657965'
expected_result = '746865206b696420646f6e277420706c6179'.upper() # needs to be upper for comparing to actual result

t1decode = base64.b16decode(t1, True)
t2decode = base64.b16decode(t2, True)

# test: ensure xor items have equal length
if len(t1decode) != len(t2decode):
    print("xor items must have equal length")
    exit(1)

xor_result = list()
for i in range(len(t1decode)):
    xor_result.append(chr(ord(t1decode[i]) ^ ord(t2decode[i])))
xor_result = "".join(xor_result)

encoded_xor_result = base64.b16encode(xor_result)

print("decoded hex #1: {}".format(t1decode))
print("decoded hex #2: {}".format(t2decode))
print("possible result: {}".format(xor_result))
print("encoded: {}".format(encoded_xor_result))
print("expected result: {}".format(expected_result))

print("Correct result? {}".format(expected_result ==  encoded_xor_result))
