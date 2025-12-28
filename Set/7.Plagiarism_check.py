import re
str1="Time is the most valuable thing we have and once it is lost, it never returns"
str2="We never get time back once it's gone -it's truly the most valuable resource."
words1=re.findall(r'\w+',str1)
#print(words1)
words2=re.findall(r'\w+',str2)
#print(words2)

swords1=set(words1)
swords2=set(words2)

#print(swords1)
#print(swords2)

common_words=swords1&swords2
#print(common_words)

unique_words=swords1|swords2
#print(unique_words)

ratio=len(common_words)/len(unique_words)
print(f"Jaccard Similarity is :{ratio:.2f}")