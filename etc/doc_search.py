docs = input()
word = input()

runner = 0
answer = 0
while runner <= len(docs)-len(word):
    found = True
    last_loc = runner
    for w in word:
        if docs[runner] != w:
            found = False
            break;
        runner += 1
        
    if found:
        answer += 1
    else:
        runner = last_loc+1
    
print(answer)
        