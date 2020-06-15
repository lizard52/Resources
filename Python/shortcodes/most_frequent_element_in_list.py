def main():
    a = [1, 2, 3, 4, 4, 5, 7, 3, 4, 6, 4, 3, 6, 4, 3, 6, 7, 8]

    from collections import Counter

    count = Counter(a)
    print(count.most_common(3))
    # They will be ordered
    print(list(count.elements()))
    for letter, count in count.most_common(1):
        print(str(letter))

    new_c = Counter()
    print("Initiall :" +str(new_c))
    new_c.update('abcd')
    print("updated :" + str(new_c))
    new_c.update({'a':5, 'b':5})
    print("Second update :" + str(new_c))

    # to get the count of the value
    print(new_c['a'])

if __name__ == '__main__':
    main()
