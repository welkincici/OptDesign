import math
FAR_L = -9999999999


def sinI(L, U, r):                                                                        # L,U,r→sinI
    return (L-r)*(math.sin(math.radians(U)))/r


def sinIpie(L, U, r, n, npie):                                                              # L,U,r,n,n’→sinI
    return n*sinI(L,U,r)/npie


def Upie(L, U, r, n, npie):                                                                # L,U,r,n,n’→U'
    I = math.degrees(math.asin(sinI(L,U,r)))
    Ipie = math.degrees(math.asin(sinIpie(L,U,r,n,npie)))
    return U+I-Ipie


def Lpie(L, U, r, n, npie):                                                                # L,U,r,n,n’→L'
    return r+r*sinIpie(L, U, r, n, npie)/math.sin(math.radians(Upie(L, U, r, n, npie)))