import math
from Prepare import Upie, FAR_L
import Calculate
import Materials


def func_tpie(t, n, npie, r, I, Ipie):
    cos_I = math.cos(math.radians(I))
    cos_Ipie = math.cos(math.radians(Ipie))
    a = (npie * cos_Ipie - n * cos_I) / r

    if Materials.lens[0]['d'] < FAR_L:
        c = a
    else:
        c = n * cos_I * cos_I / t + a

    b = npie * cos_Ipie * cos_Ipie

    return b / c


def func_spie(s, n, npie, r, I, Ipie):
    cos_I = math.cos(math.radians(I))
    cos_Ipie = math.cos(math.radians(Ipie))

    a = (npie * cos_Ipie - n * cos_I) / r

    if Materials.lens[0]['d'] < FAR_L:
        k = a
    else:
        k = n / s + a

    return npie / k


def func_D(h1, h2, L, U, r, n, npie):
    U_pie = Upie(L, U, r, n, npie)
    sinUpie = math.sin(math.radians(U_pie))
    return (h1-h2)/sinUpie


def off_axis(lens):
    if Materials.lens[0]['d'] > FAR_L:
        lights = Calculate.meri_limi_off()
    else:
        lights = Calculate.meri_infi_off()
    s = Materials.lens[0]['d'] / math.cos(math.radians(lights[0]['U']))
    t = s
    h = []

    for i in range(0, len(lens)):
        h.append(lens[i]['r'] * math.sin(math.radians(lights[i]['U'] + lights[i]['I'])))

    for i in range(0, len(lens)):
        if i == 0:
            n = 1
        else:
            n = lens[i-1]['n']

        spie = func_spie(s, n, lens[i]['n'], lens[i]['r'], lights[i]['I'], lights[i]['Ipie'])
        tpie = func_tpie(t, n, lens[i]['n'], lens[i]['r'], lights[i]['I'], lights[i]['Ipie'])
        # print('spie', spie, 'tpie', tpie)

        if i == len(lens) - 1:
            s = spie
            t = tpie
        else:
            # 过渡公式
            light = lights[i]
            D = func_D(h[i], h[i + 1], light['L'], light['U'], lens[i]['r'], n, lens[i]['n'])
            t = tpie - D
            s = spie - D

    return [s, t]
