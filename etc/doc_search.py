docs = input()
word = input()

runner = 0
answer = 0
while runner <= len(docs)-len(word):
    if docs[runner:runner+len(word)] == word:
        answer += 1
        runner += len(word)
    else:
        runner += 1
    
print(answer)
        