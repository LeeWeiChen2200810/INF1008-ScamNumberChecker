# Text checker
# obtain input from user
texttocheck = [input("Enter paragraph here: ")]

# suspicious words to check for
suswords = ["work", "easy", "money", "reliable", "licensed", "licenced", "repayment"]

# Array for making each word an index in the array
splittext = []
finalarray = []
# count the number of suspicious words
suswordscounter = 0

# split the text into individual indexes
for i in texttocheck:
    splittext = [i for string in texttocheck for i in string.split()]

# make the split text lowercase
lowersplittext = [i.lower() for i in splittext]

# remove any commas and such
for i in lowersplittext:
    clearedindex = i.replace(",", "").replace(":", "").replace("\n", "")
    finalarray.append(clearedindex)

# debugging purposes
print(texttocheck)
print(finalarray)

# check if the index i is the same as the suspicious words in array "j"
for i in finalarray:
    for j in suswords:
        if i == j:
            suswordscounter += 1


# print results based on outcome
if suswordscounter == 0:
    print("No suspicious text was found. However, exercise caution fi you think it is a scam.")
elif 0 < suswordscounter <= 2:
    print("There are", suswordscounter, "word(s) which are concerning. Exercise caution.")
elif 2 < suswordscounter <= 4:
    print("There are", suswordscounter, "suspicious word(s) in the message. There is a good probability it is a scam.")
elif suswordscounter >= 5:
    print("There are", suswordscounter, "suspicious words in this text. It is a scam.")
