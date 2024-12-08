vowels = ['a', 'e', 'i', 'o', 'u']
for i in range (4): #gives four tries for the user.
    word = input("Provide a word to search for unnique vowels: ") #Takes the input frpm the user.
    found =[]
    for letter in word:
        if letter in vowels:
            if letter not in found: #we are not allowing the duplicate in the list.
                found.append(letter)
    for alphabet in found: # to convert list into badic letters.
        print(alphabet, end =" ")
        print()
