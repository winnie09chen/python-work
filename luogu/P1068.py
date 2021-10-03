import math
people = {}

def func(dic, num):
    c = []
    dic = sorted(dic.items(), key=lambda x:x[1]*10000+10000-x[0], reverse=True)
    for i in dic:
        if i[1] >= dic[num][1]:
            c.append(i)
    return c

def output(dic):
    print(dic[1][1], len(dic))
    for i in dic:
        print(i[0], i[1])


def main():
    a = input().split(' ')
    num = int(a[0])
    p_num = math.floor(int(a[1])*1.5)
    for i in range(num):
        b = input().split(' ')
        n = int(b[0])
        m = int(b[1])
        people[n] = m
    dic = func(people, p_num)
    output(dic)

if __name__ == '__main__':
    main()