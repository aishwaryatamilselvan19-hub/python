while True:
    value=input('Enter a number: ')
    if value =='done':
        break
    try:
        int=int(value)
        print(int)
    except ValueError:
        print('Invalid input')
        continue
    total=0
    count=0
    total = total+int
    count = count+1
    if count>0:
        average=total/count
        print('Average: ', average) 
        print('Total: ', total)
        print('Count: ', count)
    else:
            print('Average: 0')
        