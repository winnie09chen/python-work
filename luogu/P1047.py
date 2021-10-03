def main():
    road = {}
    tree = 0
    a = input().split(' ')
    length = int(a[0])
    num = int(a[1])

    for i in range(length+1):
        road[i] = 0

    for i in range(num):
        b = input().split(' ')
        begin = int(b[0])
        end = int(b[1])
        for j in range(begin, end+1):
            road[j] += 1

    for i in range(length+1):
        if road[i] == 0:
            tree += 1
    
    print(tree)


if __name__ == '__main__':
    main()