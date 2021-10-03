import sys

def func(a, num):
    win = 0
    lose = 0
    a = [a[i:i+num] for i in range(0, len(a), num)]
    for i in a:
        for j in i:
            if j == 'W':
                win += 1
            elif j == 'L':
                lose += 1
        print(f'{win}:{lose}')
        win = 0
        lose = 0

def main():
    a = ''
    for line in sys.stdin.readlines():
        a += line
        if 'E' in a:
            a = a[:a.find('E')]
            break 
    func(a, 11)
    print('\n')
    func(a, 21)

if __name__ == '__main__':
    main()