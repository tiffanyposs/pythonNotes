def anti_vowel(text):
    string = ""
    for c in text:
    	vowel = False
        for char in "aeiouAEIOU":
            if c == char:
            	vowel = True
        else:
        	if vowel == False:
        		string = string+c
    return string

        
print anti_vowel("Hello world of mine")