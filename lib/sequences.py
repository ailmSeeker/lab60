def print_fibonacci(length):
    current = []
      
    if(length == 0):
        print(current)
        return
    
    for i in range(length):
        if i == 0 or i == 1:
            current.append(i)
        else:
            current.append(current[i - 2] + current[i-1])
       
    print(current)
