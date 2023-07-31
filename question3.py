
#calculate average word length

words = input("Please enter a sentence: ").split()
total = 0

for word in words:
    total += len(word)

print("Average word length is " + str(total / len(words)))
