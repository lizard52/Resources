def main():
    a = 'asdasdsadghtghjjlkl'
    # reversing string with special case of slice step param
    print(a[::-1])

    # iterating over string

    for char in reversed(a):
        print(char)

    num = 123124565466
    print(int(str(num)[::-1]))
    
    # reversing a list 
    b = [1,2,5,7,8,3,6,8,3]
    print(b[::-1])
    
    for item in reversed(b):
        print item

if __name__ == "__main__":
    main()
