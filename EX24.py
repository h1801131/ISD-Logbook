sent1=input("Enter the sentence one:")
sent2=input("Enter the sentence two:")

#concatenate
longSent=sent1 + " " +sent2
print(longSent)

#split sentence into words
words=longSent.split(" ")

#created sorted words
words=sorted(words)
print("Sorted words are:")
print(words)

#count number of words
print("Total number of words are: ", len(words))

#created emty dictionary
dict={}
#here take index of each item 
for i  in range(len(words)):
    dict[i]=words[i]
print(words)



