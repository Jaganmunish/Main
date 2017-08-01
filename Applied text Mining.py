# Applied Text Mining with Python

#Ex.1

text1 = "Ethics are buit right into the ideals and objective of the United Nations"
len(text1)

text2 = text1.split(" ") # Tockenization

len(text2)

text2

#Ex.2

# Finding specfic words

longwrd = [x for x in text2 if len(x) >3] # Long Word

capwrd = [i for i in text2 if i.istitle()] # Capitalized words

wrds = [a for a in text2 if a.endswith("s")]  #Words ends with 'S'

# Finding unique words

text3 = 'To be or not to be'

text4 = text3.split(" ")
text4
set(text4) # This will give the unique words. But, it will not filter the UPPER and lower case

len(set([w.lower() for w in text4]))

#Ex.5
# String Operations
#From words to char



