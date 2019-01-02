sentence1 = input("Enter the first sentence:")
sentence2 = input("Enter the second sentence:")

sentence3 = sentence1 + " " + sentence2
wordsList = sentence3.split()

wordsList.sort()
print("The sorted words from this sentence are:\n", wordsList)
#total numbers words
print("Total number of words is: %d" %(len(wordsList)))

wordsDictionary = {}
for words in wordsList:
    wordsDictionary[words] = wordsList.count(words)
print("The dictionary occuresce is:")
#prints elements of dictionary
for element in wordsDictionary:
    print(element, ":\t",wordsDictionary[element])
    

