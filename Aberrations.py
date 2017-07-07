import Materials
import Calculate
from Prepare import FAR_L
import math


def spherical():
    aber = {}
    Materials.K2 = 0
    if Materials.lens[0].d > FAR_L:
        for k in Materials.K['spherical']:
            Materials.K1 = k
            aber[str(Materials.K1)] = Calculate.meri_limi_on()[-1]['L'] - Calculate.first_para()
    else:
        for k in Materials.K['spherical']:
            Materials.K1 = k
            aber[str(Materials.K1)] = Calculate.meri_infi_on()[-1]['L'] - Calculate.first_para()

    print(aber)
    return aber


def coma():
    aber = {}
    gauss = Calculate.first_para()
    if Materials.lens[0].d > FAR_L:
        for k in Materials.K['coma']:
            Materials.K2 = k[1]
            Materials.K1 = 0
            light = Calculate.meri_limi_off()
            y = (light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

            Materials.K1 = -k[0]
            light = Calculate.meri_limi_off()
            y_b = (light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

            Materials.K1 = k[0]
            light = Calculate.meri_limi_off()
            y_a = (light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

            aber[str(Materials.K1) + '_' + str(Materials.K2)] = (y_a + y_b) / 2 - y
    else:
        for k in Materials.K['coma']:
            Materials.K2 = k[1]

            Materials.K1 = 0
            light = Calculate.meri_infi_off()
            y = (light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))
            print(y)

            Materials.K1 = -k[0]
            light = Calculate.meri_infi_off()
            y_b = (light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

            Materials.K1 = k[0]
            light = Calculate.meri_infi_off()
            y_a = (light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

            aber[str(Materials.K1) + '_' + str(Materials.K2)] = y - (y_a + y_b) / 2

    print(aber)
    return aber


def astigmatism():
    print('astigmatism')

    out = Calculate.off_axis()
    if Materials.lens[0].d > FAR_L:
        light = Calculate.meri_limi_off()[-1]
    else:
        light = Calculate.meri_infi_off()[-1]
    cos_u = math.cos(math.radians(light['U']))

    aber = - out[0] * cos_u + out[1] * cos_u
    print(aber)


def curvature():
    print('curvature')
    gauss = Calculate.first_para()
    aber = {}
    out = Calculate.off_axis()
    if Materials.lens[0].d > FAR_L:
        light = Calculate.meri_limi_off()[-1]
    else:
        light = Calculate.meri_infi_off()[-1]
    cos_u = math.cos(math.radians(light['U']))

    aber['s'] = out[0] * cos_u - gauss
    aber['t'] = out[1] * cos_u - gauss

    print(aber)

    return aber


def distortion():
    print('distortion')
    gauss = Calculate.first_para()
    aber = {}

    if Materials.lens[0].d > FAR_L:
        for k in Materials.K['distortion']:
            Materials.K2 = k
            Materials.K1 = 0
            light = Calculate.meri_limi_off()
            y = (light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))
            y0 = -Calculate.height()
            aber[str(k)] = -y - y0
    else:
        for k in Materials.K['distortion']:
            Materials.K2 = k
            Materials.K1 = 0
            light = Calculate.meri_infi_off()
            y = (light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))
            y0 = -Calculate.height()
            aber[str(k)] = - y + y0

    print(aber)
    return aber


def mag_chromatism():
    # print('magnification chromatism')

    lens = Materials.lens.copy()
    gauss = Calculate.first_para()
    Materials.K1 = 0

    aber = {}

    y_d = {}
    if Materials.lens[0].d > FAR_L:
        # BUG!!
        for k in Materials.K['mag_chromatism']:
            Materials.K2 = k
            light = Calculate.meri_limi_off()
            y_d[str(k)] = -(light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

    else:
        for k in Materials.K['mag_chromatism']:
            Materials.K2 = k
            light = Calculate.meri_infi_off()
            y_d[str(k)] = -(light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

    for item in range(0, len(lens)):
        Materials.lens[item].n = Materials.nf[item]

    y_f = {}
    if Materials.lens[0].d > FAR_L:
        # BUG!!
        for k in Materials.K['mag_chromatism']:
            Materials.K2 = k
            light = Calculate.meri_limi_off()
            y_f[str(k)] = -(light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

    else:
        for k in Materials.K['mag_chromatism']:
            Materials.K2 = k
            light = Calculate.meri_infi_off()
            y_f[str(k)] = -(light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

    for item in range(0, len(lens)):
        Materials.lens[item].n = Materials.nc[item]

    y_c = {}
    if Materials.lens[0].d > FAR_L:
        # BUG!!
        for k in Materials.K['mag_chromatism']:
            Materials.K2 = k
            light = Calculate.meri_limi_off()
            y_c[str(k)] = -(light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

    else:
        for k in Materials.K['mag_chromatism']:
            Materials.K2 = k
            light = Calculate.meri_infi_off()
            y_c[str(k)] = -(light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

    for k in Materials.K['mag_chromatism']:
        aber[str(k)] = y_f[str(k)] - y_c[str(k)]

    Materials.lens = lens
    print('d', y_d)
    print('c', y_c)
    print('f', y_f)
    print(aber)
    return aber


def trans_chromatism():
    print('transverse chromatism')

    lens = Materials.lens.copy()
    Materials.K2 = 0

    for item in range(0, len(lens)):
        Materials.lens[item].n = Materials.nf[item]

    aber_f = {}
    if Materials.lens[0].d > FAR_L:
        for k in Materials.K['trans_chromatism']:
            Materials.K1 = k
            aber_f[str(Materials.K1)] = Calculate.meri_limi_on()[-1]['L']
    else:
        for k in Materials.K['trans_chromatism']:
            Materials.K1 = k
            aber_f[str(Materials.K1)] = Calculate.meri_infi_on()[-1]['L']

    for item in range(0, len(lens)):
        Materials.lens[item].n = Materials.nc[item]

    aber_c = {}
    if Materials.lens[0].d > FAR_L:
        for k in Materials.K['trans_chromatism']:
            Materials.K1 = k
            aber_c[str(Materials.K1)] = Calculate.meri_limi_on()[-1]['L']
    else:
        for k in Materials.K['trans_chromatism']:
            Materials.K1 = k
            aber_c[str(Materials.K1)] = Calculate.meri_infi_on()[-1]['L']

    aber = {}
    for k in Materials.K['trans_chromatism']:
        aber[str(k)] = aber_f[str(k)] - aber_c[str(k)]
    print(aber)
    Materials.lens = lens

