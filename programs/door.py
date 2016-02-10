def matrix():
    print "You've entered the matrix"
    print "Do you pick the red pill or the blue pill?"
    answer = raw_input("Do you pick the red pill or the blue one. type then press enter: ").lower()
    if answer == 'red' or answer == 'r':
        print "you picked the red pill"
    elif answer == 'blue' or answer == 'b':
        print "you picked the blue pill, idiot"
    else:
        print "Thats not an option, try again"
        matrix()

matrix()