def sapxep(x):
    output = len(input)*['A']
    
    for i in range(len(input)):
        output[i] = ord(input[i]) # chuyển data chữ sang số
        
    output.sort() # sắp xếp từ bé đến lớn
    
    for i in range(len(input)):
        output[i]=chr(output[i]) # chuyển data từ số sang chữ
    
    FileOut = open('OUTPUT.TXT', 'w') # write file output
    FileOut.write("".join(output))

input = open('INPUT.TXT', 'r').readline().rstrip('\n') # read file input
sapxep(input) # gọi hàm