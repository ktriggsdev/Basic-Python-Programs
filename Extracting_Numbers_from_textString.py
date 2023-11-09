# Given  Sentence
sentence="Ramu have 150 Apples and 10 bananas"
sentence2="Ramu Sell 1 Apple at 15.5 Rupees"

sum=0
sum2=0
# split is used to split sentence
# This code is not fit for Decimal Nos.

print("---------------EXTRACTING NUMBER FROM STRING---------------\n")
list1 = [word for word in sentence.split() if word.isdigit()]
print("New List",list1)



# Calculating the SUM
for i in list1:
    sum=sum+int(i)

print("No. without Fraction \nsum=",sum,"\n")

list2 = [word2 for word2 in sentence2.split() if not word2.isalpha()]
print("New List",list2)

# Calculating the SUM
for j in list2:
    sum2=sum2+float(j)

print("No. with Fraction \nsum=",sum2)
print("-----------------------------------------------------------")