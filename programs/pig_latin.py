pyg = 'ay'

def pig_latin():

    original = raw_input('Enter a word:')
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]

    if len(original) > 0 and original.isalpha():
        print new_word
        pig_latin()
    else:
        print 'characters only! Try Again'
        pig_latin()

pig_latin()
