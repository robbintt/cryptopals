''' XOR hunt with a bigger dataset

answer: [10231.933333333334, '5', 'Now that the party is jumping\n']

Issue: python readlines() was giving me a '\n' making each string not ascii
Response: I stripped the lines after importing them before processing them.
'''
from xor_hunting import xor_by_char, letter_frequency_scorer, test_characters


if __name__ == '__main__':
    '''
    '''

    result_list = list()

    with open("data/4.txt") as f:
        for line in f.readlines():
            line = line.strip() # strip the newline from readlines() function
            for c in test_characters:
                result = xor_by_char(line, c)
                if not result:
                    break

                score = letter_frequency_scorer(result)
                    
                result_list.append([score, c, result])

    result_list.sort(key=lambda x: x[0])
    for each in result_list:
        print each
