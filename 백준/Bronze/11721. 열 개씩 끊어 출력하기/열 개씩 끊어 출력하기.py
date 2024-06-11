word = input()
arr = []

for i in range(0,len(word),10):
    arr.append(word[i:i+10])

for i in arr:
    print(i, sep='\n')
