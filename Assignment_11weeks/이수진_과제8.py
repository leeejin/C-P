def a(word):
    wordd = dict()
    while(word!=""):
        cnt = int()
        for i  in range(len(word)):
            if word[0] == word[i]:
                cnt = cnt +1
        wordd[word[0]] = cnt
        word = word.replace(word[0],'')
    return wordd

word = input("문자열 입력: ")
wordd = a(word)

wordk = list(wordd.keys())
for i in range(len(wordk)):
    print(wordk[i]+" : ",wordd[wordk[i]]," 회   |"+'*' * wordd[wordk[i]])
