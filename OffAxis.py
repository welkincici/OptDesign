import math
from Prepare import Upie, FAR_L
import Calculate
import Materials


def func_tpie(t, n, npie, r, I, Ipie):
    I = math.cos(math.radians(I))
    Ipie = math.cos(math.radians(Ipie))
    a = npie * Ipie * Ipie * t
    b = n * I * I
    c = (npie * Ipie - n * I) * t / r

    return a / (b + c)


def func_spie(s, n, npie, r, I, Ipie):
    I = math.cos(math.radians(I))
    Ipie = math.cos(math.radians(Ipie))

    c = (npie * Ipie - n * I) * s / r

    return npie * s / (n + c)


def func_D(h1, h2, L, U, r, n, npie):
    U_pie = Upie(L, U, r, n, npie)
    sinUpie = math.sin(math.radians(U_pie))
    return (h1-h2)/sinUpie


def off_axis(lens):
    if Materials.lens[0].d > FAR_L:
        lights = Calculate.meri_limi_off()
    else:
        lights = Calculate.meri_infi_off()
    s = lights[0]['L'] / math.cos(math.radians(lights[0]['U']))
    t = s
    h = []

    for i in range(0, len(lens)):
        h.append(lens[i].r * math.sin(math.radians(lights[i]['U'] + lights[i]['I'])))

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
            D = func_D(h[i], h[i + 1], light['L'], light['U'], lens[i].r, n, lens[i].n)
            t = tpie - D
            s = spie - D

        # print(t)
        # print(s)

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
