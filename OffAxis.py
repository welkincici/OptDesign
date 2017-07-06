import math
from Prepare import Upie
import Calculate


def func_tpie(t, n, npie, r, I, Ipie):
    I = math.radians(I)
    Ipie = math.radians(Ipie)
    a = npie * math.cos(Ipie) * math.cos(Ipie) * t

    return npie / (n / t + (npie - n) / r)


def func_spie(s, n, npie, r, I, Ipie):
    return npie / (n / s + (npie - n) / r)


def func_D(h1, h2, L, U, r, n, npie):
    U_pie = Upie(L, U, r, n, npie)
    sinUpie = math.sin(math.radians(U_pie))
    return (h1-h2)/sinUpie


def off_axis(lens):
    lights = Calculate.meri_limi_off()
    s = lights[0]['l'] / math.cos(math.radians(lights[0]['U']))
    t = s
    h = []
    for i in range(0, len(lens)):
        h[i] = lens[i].r * math.sin(math.radians(lights[i]['U'] + lights[i]['I']))

    for i in range(0, len(lens)):
        if i == 0:
            n = 1
        else:
            n = lens[i-1].n
        spie = func_spie(s, n, lens[i].n, lens[i].r, lights[i]['I'], lights[i]['Ipie'])
        tpie = func_tpie(s, n, lens[i].n, lens[i].r, lights[i]['I'], lights[i]['Ipie'])

        if i == len(lens) - 1:
            s = spie
            t = tpie
        else:
            # 过渡公式
            light = lights[i]
            D = func_D(h[i], h[i + 1], light[0], light[1], lens[i].r, n, lens[i].n)
            t = tpie - D
            s = spie - D

        print(t)
        print(s)

    return [s, t]

# def func_ltpie(tpie,xk,Ukpie):
#     result=tpie*(math.cos(math.radians(Ukpie)))+xk
#     return result
# def func_lspie(spie,xk,Ukpie):
#     result=spie*(math.cos(math.radians(Ukpie)))+xk
#     return result
#
# xtpie=ltpie-lpie
# xspie=lspie-lpie
