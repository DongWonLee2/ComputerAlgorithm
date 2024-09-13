def gcd(a, b):
    alist = [i for i in range(1, a) if a % i == 0]
    print("{}의 약수 = {}".format(a, alist))
    blist = [i for i in range(1, b) if b % i == 0]
    print("{}의 약수 = {}".format(b, blist))
    
    for i in range(len(alist)-1, 0, -1):
        if alist[i] in blist:
            print("{}와 {}의 최대공약수 = {}".format(a, b, alist[i]))
            break

gcd(60, 28)