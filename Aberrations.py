import Materials
import Calculate
import Paraxial
from Prepare import FAR_L
import math


def spherical():
    name = 'spherical'
    if name not in Materials.aber:
        Materials.aber[name] = {}

    Materials.K2 = 0
    gauss = Calculate.first_para()[-1]['L']

    for k in Materials.K[name]:
        if k not in Materials.aber[name]:
            Materials.K1 = k
            if Materials.lens[0]['d'] > FAR_L:
                Materials.aber[name][str(k)] = Calculate.meri_limi_on()[-1]['L'] - gauss
            else:
                Materials.aber[name][str(k)] = Calculate.meri_infi_on()[-1]['L'] - gauss

    print(Materials.aber)


def coma():
    name = 'coma'

    if name not in Materials.aber:
        Materials.aber[name] = {}

    gauss = Calculate.first_para()[-1]['L']

    for k in Materials.K[name]:
        if str(k[0]) + '_' + str(k[1]) not in Materials.aber[name]:
            Materials.K2 = k[1]
            if Materials.lens[0]['d'] > FAR_L:
                Materials.K1 = 0
                light = Calculate.meri_limi_off()
                y = (light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

                Materials.K1 = -k[0]
                light = Calculate.meri_limi_off()
                y_b = (light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

                Materials.K1 = k[0]
                light = Calculate.meri_limi_off()
                y_a = (light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))
            else:
                Materials.K1 = 0
                light = Calculate.meri_infi_off()
                y = (light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

                Materials.K1 = -k[0]
                light = Calculate.meri_infi_off()
                y_b = (light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

                Materials.K1 = k[0]
                light = Calculate.meri_infi_off()
                y_a = (light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

            Materials.aber[name][str(k[0]) + '_' + str(k[1])] = \
                y - (y_a + y_b) / 2

    print(Materials.aber)


def astigmatism():
    name = 'astigmatism'

    if name not in Materials.aber:
        Materials.K2 = 1
        Materials.K1 = 0
        out = Calculate.off_axis()
        if Materials.lens[0]['d'] > FAR_L:
            light = Calculate.meri_limi_off()[-1]
        else:
            light = Calculate.meri_infi_off()[-1]
        cos_u = math.cos(math.radians(light['U']))

        Materials.aber[name] = - out[0] * cos_u + out[1] * cos_u

    print(Materials.aber)


def curvature():
    # print('curvature')
    name = 'curvature'

    if name not in Materials.aber:
        Materials.K2 = 1
        Materials.K1 = 0
        gauss = Calculate.first_para()[-1]['L']
        Materials.aber[name] = {}
        out = Calculate.off_axis()
        if Materials.lens[0]['d'] > FAR_L:
            light = Calculate.meri_limi_off()[-1]
        else:
            light = Calculate.meri_infi_off()[-1]
        cos_u = math.cos(math.radians(light['U']))

        Materials.aber[name] = {}

        Materials.aber[name]['s'] = out[0] * cos_u - gauss
        Materials.aber[name]['t'] = out[1] * cos_u - gauss

    print(Materials.aber)


def distortion():
    # print('distortion')
    name = 'distortion'
    if name not in Materials.aber:
        Materials.aber[name] = {}

    gauss = Calculate.first_para()[-1]['L']
    Materials.K1 = 0

    for k in Materials.K[name]:
        if str(k) not in Materials.aber[name]:
            Materials.K2 = k
            if Materials.lens[0]['d'] > FAR_L:
                light = Calculate.meri_limi_off()
                yp = (light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))
                y = Materials.obj['r'] * k
                w = math.radians(Materials.obj['w']) * k
                y0 = -Paraxial.height(Materials.lens, y, w)
            else:
                light = Calculate.meri_infi_off()
                yp = (light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))
                y = Materials.obj['r'] * k
                w = math.radians(Materials.obj['w']) * k
                y0 = -Paraxial.height(Materials.lens, y, w)

            Materials.aber[name][str(k)] = - yp + y0
    print(Materials.aber)


def mag_chromatism():
    # print('magnification chromatism')
    name = 'mag_chromatism'

    if name not in Materials.aber:
        Materials.aber[name] = {}

    gauss = Calculate.first_para()[-1]['L']
    Materials.K1 = 0

    for k in Materials.K[name]:
        if str(k) not in Materials.aber[name]:
            Materials.K2 = k
            if Materials.lens[0]['d'] > FAR_L:
                light = Calculate.meri_limi_off()
                y_d = -(light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

                for item in range(0, len(Materials.lens)):
                    Materials.lens[item]['n'] = Materials.nf[item]
                Materials.extend = '_f'
                light = Calculate.meri_limi_off()
                y_f = -(light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

                for item in range(0, len(Materials.lens)):
                    Materials.lens[item]['n'] = Materials.nc[item]
                Materials.extend = '_c'
                light = Calculate.meri_limi_off()
                y_c = -(light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))
            else:
                light = Calculate.meri_infi_off()
                y_d = -(light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

                for item in range(0, len(Materials.lens)):
                    Materials.lens[item]['n'] = Materials.nf[item]
                Materials.extend = '_f'
                light = Calculate.meri_infi_off()
                y_f = -(light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

                for item in range(0, len(Materials.lens)):
                    Materials.lens[item]['n'] = Materials.nc[item]
                Materials.extend = '_c'
                light = Calculate.meri_infi_off()
                y_c = -(light[-1]['L'] - gauss) * math.tan(math.radians(light[-1]['U']))

            Materials.aber[name][str(k)] = y_f - y_c

    for item in range(0, len(Materials.lens)):
        Materials.lens[item]['n'] = Materials.nd[item]

    Materials.extend = ''

    Materials.show()
    Materials.change_flag = 0
    print(Materials.aber)


def trans_chromatism():
    # print('transverse chromatism')
    name = 'trans_chromatism'

    if name not in Materials.aber:
        Materials.aber[name] = {}

    Materials.K2 = 0
    Materials.change_flag = 1

    for k in Materials.K[name]:
        if str(k) not in Materials.aber[name]:
            Materials.K1 = k
            if Materials.lens[0]['d'] > FAR_L:
                for item in range(0, len(Materials.lens)):
                    Materials.lens[item]['n'] = Materials.nf[item]
                Materials.extend = '_f'
                aber_f = Calculate.meri_limi_on()[-1]['L']

                for item in range(0, len(Materials.lens)):
                    Materials.lens[item]['n'] = Materials.nc[item]
                Materials.extend = '_c'
                aber_c = Calculate.meri_limi_on()[-1]['L']
            else:
                for item in range(0, len(Materials.lens)):
                    Materials.lens[item]['n'] = Materials.nf[item]
                Materials.extend = '_f'
                aber_f = Calculate.meri_infi_on()[-1]['L']

                for item in range(0, len(Materials.lens)):
                    Materials.lens[item]['n'] = Materials.nc[item]
                Materials.extend = '_c'
                aber_c = Calculate.meri_infi_on()[-1]['L']

            Materials.aber[name][str(k)] = aber_f - aber_c

    for item in range(0, len(Materials.lens)):
        Materials.lens[item]['n'] = Materials.nd[item]

    Materials.extend = ''
    Materials.show()
    print(Materials.aber)

