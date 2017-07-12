import Materials
import Calculate
import OffAxis
import math
import copy


def spherical():
    name = 'spherical'
    if name + Materials.extend not in Materials.aber:
        Materials.aber[name + Materials.extend] = {}

    gauss = Calculate.first_para()[-1]['L']

    for k in Materials.K[name]:
        if str(k[0]) + '_' + str(k[1]) not in Materials.aber[name + Materials.extend]:
            Materials.K1 = k[0]
            Materials.K2 = k[1]
            Materials.aber[name + Materials.extend][str(k[0]) + '_' + str(k[1])] = \
                Calculate.meri_on()[-1]['L'] - gauss


def coma():
    name = 'coma'

    if name not in Materials.aber:
        Materials.aber[name] = {}

    gauss = Calculate.first_para()[-1]['L']

    for k in Materials.K[name]:
        if str(k[0]) + '_' + str(k[1]) not in Materials.aber[name]:
            Materials.K2 = k[1]
            Materials.K1 = 0
            light = Calculate.meri_off()
            y = (light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

            Materials.K1 = -k[0]
            light = Calculate.meri_off()
            y_b = (light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

            Materials.K1 = k[0]
            light = Calculate.meri_off()
            y_a = (light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

            Materials.aber[name][str(k[0]) + '_' + str(k[1])] = y - (y_a + y_b) / 2


def curvature():
    name = 'curvature'

    if name not in Materials.aber:
        Materials.aber[name + '_s'] = {}
        Materials.aber[name + '_t'] = {}
        Materials.aber['astigmatism'] = {}

    for k in Materials.K[name]:
        if str(k[0]) + '_' + str(k[1]) not in Materials.aber[name + '_s']:
            Materials.K1 = k[0]
            Materials.K2 = k[1]
            gauss = Calculate.first_para()[-1]['L']
            out = OffAxis.off_axis()
            light = Calculate.meri_off()[-1]
            cos_u = math.cos(math.radians(light['U']))

            Materials.aber[name + '_s'][str(k[0]) + '_' + str(k[1])] = out[0] * cos_u - gauss
            Materials.aber[name + '_t'][str(k[0]) + '_' + str(k[1])] = out[1] * cos_u - gauss
            Materials.aber['astigmatism'][str(k[0]) + '_' + str(k[1])] = \
                Materials.aber[name + '_t'][str(k[0]) + '_' + str(k[1])] - \
                Materials.aber[name + '_s'][str(k[0]) + '_' + str(k[1])]


def distortion():
    name = 'distortion'
    if name not in Materials.aber:
        Materials.aber[name] = {}

    for k in Materials.K[name]:
        if str(k[0]) + '_' + str(k[1]) not in Materials.aber[name]:
            Materials.K1 = k[0]
            Materials.K2 = k[1]
            gauss = Calculate.first_para()[-1]['L']
            light = Calculate.meri_off()
            yp = -(light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))
            y = Materials.obj['r'] * k[1]
            w = math.radians(Materials.obj['w']) * k[1]
            y0 = -Calculate.height(y, w)

            Materials.aber[name][str(k[0]) + '_' + str(k[1])] = yp - y0


def mag_chromatism():
    name = 'mag_chromatism'

    if name not in Materials.aber:
        Materials.aber[name] = {}

    for k in Materials.K[name]:
        if str(k[0]) + '_' + str(k[1]) not in Materials.aber[name]:
            Materials.K1 = k[0]
            Materials.K2 = k[1]
            gauss = Calculate.first_para()[-1]['L']
            light = Calculate.meri_off()
            y_d = -(light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

            for item in range(0, len(Materials.lens)):
                Materials.lens[item]['n'] = Materials.nf[item]
            Materials.extend = '_f'
            light = Calculate.meri_off()
            y_f = -(light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

            for item in range(0, len(Materials.lens)):
                Materials.lens[item]['n'] = Materials.nc[item]
            Materials.extend = '_c'
            light = Calculate.meri_off()
            y_c = -(light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

            Materials.aber[name][str(k[0]) + '_' + str(k[1])] = y_f - y_c
            Materials.basic['d height'] = y_d
            Materials.basic['F height'] = y_f
            Materials.basic['C height'] = y_c

    for item in range(0, len(Materials.lens)):
        Materials.lens[item]['n'] = Materials.nd[item]

    Materials.extend = ''


def trans_chromatism():
    name = 'trans_chromatism'

    if name not in Materials.aber:
        Materials.aber[name] = {}

    if 'spherical' in Materials.K:
        ks_copy = copy.deepcopy(Materials.K['spherical'])
    else:
        ks_copy = []

    Materials.K['spherical'] = copy.deepcopy(Materials.K[name])

    for item in range(0, len(Materials.lens)):
        Materials.lens[item]['n'] = Materials.nf[item]
    Materials.extend = '_f'
    spherical()

    for item in range(0, len(Materials.lens)):
        Materials.lens[item]['n'] = Materials.nc[item]
    Materials.extend = '_c'
    spherical()

    for item in range(0, len(Materials.lens)):
        Materials.lens[item]['n'] = Materials.nd[item]
    Materials.extend = ''

    Materials.K['spherical'] = ks_copy

    for k in Materials.K[name]:
        if str(k[0]) + '_' + str(k[1]) not in Materials.aber[name]:
            Materials.aber[name][str(k[0]) + '_' + str(k[1])] = \
                Materials.aber['spherical_f'][str(k[0]) + '_' + str(k[1])] -\
                Materials.aber['spherical_c'][str(k[0]) + '_' + str(k[1])]


def all_aberrations():
    spherical()
    coma()
    curvature()
    distortion()
    trans_chromatism()
    mag_chromatism()

