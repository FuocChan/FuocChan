with open('input.txt', 'r') as FileInp:
    n = FileInp.readline().rstrip('\n')
    lst = []
    for i in range(0, len(n)):
        lst.append(n[i:i + 1])
    answer = ", ".join(lst)
        
FileOut = open('output', 'w')
FileOut.write(answer)

