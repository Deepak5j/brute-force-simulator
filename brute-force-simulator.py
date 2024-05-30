def bruteforce(w):
    k = 0
    sol = ''
    i = 30
    while i<=122:
        print(sol + chr(i))
        if chr(i) == w[k]:
            sol += chr(i)
            i = 30
            k += 1
            print(sol)    
        i += 1
        if k == len(w):
            break

word = input('Enter word: ')
bruteforce(word)
        
        
