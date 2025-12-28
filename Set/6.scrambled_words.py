word_set={'leap','medical','listen','pale','silent','plea','enlist'}
print(word_set)

result=set()

for word1 in word_set:
    for word2 in word_set:
        #print(word1,word2)
        if word1 != word2 and sorted(word1) == sorted(word2):
            pair=tuple(sorted(word1,word2))
            result.add(pair)
for word in result:
    print(word)