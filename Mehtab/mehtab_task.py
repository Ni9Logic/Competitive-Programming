def sum():
    a = input("A: ")
    b = input("B: ")

    a = int(a, 2)
    b = int(b, 2)
    return a + b

def main():
    add = sum()

    if add > 9:
        add = str(add)
        add = list(add)
        
        store_bin = []
        for i in range(len(sum)):
            zero_one = bin(int(sum[i]))
            zero_one = zero_one.replace('0b', '')
            num_zero = 4 - len(zero_one)
            for i in range(num_zero):
                zero_one = '0' + zero_one
                
            store_bin.append(zero_one)
            
        print("Sum is: ", end = '')
        for b in store_bin:
            print(b, end = ' ')
        
        return
    
    binaryy = bin(sum)
    binaryy = binaryy.replace('0b', '')
    num_zero = 4 - len(binaryy)
    for i in range(num_zero):
        binaryy = '0' + binaryy
    
    print("Y: ", binaryy)
    
if __name__ == '__main__':
    main()