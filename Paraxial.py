import math


def func1(n1, n, r, d, l1, u):
    d = l1+d
    i = (d - r)* u / r
    i1 = n1*i/n
    u1 = i + u - i1
    return u1


def func2(n1, n, r, d, l1, u, u1):
    d = l1 + d
    i = (d - r) * u / r
    i1 = n1 * i / n
    u1 = i + u - i1
    l1 = r + r*i1/u1
    return l1


def func3(n):
    n1=n
    return n1


def func4(n1, n, r, d, l1):
    d=l1+d
    l1=(n*r*d)/((n-n1)*d+n1*r)
    return l1


def func5(n1, n, r, d, l1, f):
    d = l1 + d
    l1 = (n*r*d)/((n-n1)*d+n1*r)
    f = (f*l1)/d
    return f


def paraxial(lens, light):

    light.u = math.radians(light.u)

    n1 = 1
    l1 = 0

    number = len(lens)
    n = lens[0].n
    r = lens[0].r
    d = light.l
    u1 = func1(n1, n, r, d, l1, light.u)
    l1 = func2(n1, n, r, d, l1, light.u, u1)
    n1 = func3(n)
    u = u1

    for item in range(1, number):
        n = lens[item].n
        r = lens[item].r
        d = lens[item].d
        u1 = func1(n1, n, r, d, l1, u)
        l1 = func2(n1, n, r, d, l1, u, u1)
        n1 = func3(n)
        u = u1
    print('像距：', l1)
    return l1


def focal(lens):
    number = len(lens)
    f = lens[0].n * lens[0].r / (lens[0].n - 1)
    n1 = lens[0].n
    l1 = f
    for item in range(1, number):
        n = lens[item].n
        r = lens[item].r
        d = lens[item].d
        f = func5(n1, n, r, d, l1, f)
        l1 = func4(n1, n, r, d, l1)
        n1 = func3(n)
    print('焦距：', f)