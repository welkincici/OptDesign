import math

from Prepare import sinI, sinIpie, Upie, Lpie


def meridional(lens, light, start=0):

    record = []

    L = light.l
    U = light.u

    for i in range(start, len(lens)):
        if i == 0:
            n = 1
        else:
            n = lens[i-1].n

        A = sinI(L, U, lens[i].r)
        B = sinIpie(L, U, lens[i].r, n, lens[i].n)
        # print('sinI:', A)
        # print('sinIpie:', B)
        if A < -1 or A > 1:
            print("over")  # 入射光线超半轴
            break
        elif B < -1 or B > 1:
            print("total reflection")  # 发生全反射
            break

        record.append({'L': L, 'U': U, 'I': math.degrees(math.asin(A)),
                       'Ipie': math.degrees(math.asin(B))})

        Lpie_i = Lpie(L, U, lens[i].r, n, lens[i].n)
        Upie_i = Upie(L, U, lens[i].r, n, lens[i].n)

        # 过渡公式
        if i == len(lens) - 1:
            L = Lpie_i
            U = Upie_i
        else:
            L = Lpie_i + lens[i + 1].d
            U = Upie_i

    record.append({'L': L, 'U': U})

    return record
