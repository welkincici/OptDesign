import math
import Materials
import Paraxial
import Meridional
import OffAxis
from Prepare import FAR_L


def first_para():
    if 'first_para' not in Materials.lights:
        light = Materials.Light(Materials.lens[0].d,
                                math.degrees(math.atan(Materials.stops[0].r / Materials.lens[0].d)))
        Materials.lights['first_para'] = light
    # print('first_para')
    return Paraxial.paraxial(Materials.lens, Materials.lights['first_para'])


def second_para():
    if 'second_para' not in Materials.lights:
        if 'w' in Materials.obj:
            light = Materials.Light(0, Materials.obj['w'])
        else:
            light = Materials.Light(0,
                                    math.degrees(math.atan(Materials.obj['r'] / Materials.lens[0].d)))

        Materials.lights['second_para'] = light
    return Paraxial.paraxial(Materials.lens, Materials.lights['second_para'])


def meri_infi_on():
    if Materials.lens[0].d > FAR_L:
        return

    K1 = Materials.K1

    # print('meri_infi_on')
    h1 = K1 * Materials.stops[0].r
    sin_i = h1 / Materials.lens[0].r
    sin_i_pie = sin_i / Materials.lens[0].n
    I = math.degrees(math.asin(sin_i))
    Ipie = math.degrees(math.asin(sin_i_pie))

    # print('in circle')

    U = I - Ipie
    L = Materials.lens[0].r + Materials.lens[0].r * sin_i_pie / \
                              math.sin(math.radians(U)) + Materials.lens[1].d

    Materials.lights['meri_infi_on_' + str(K1)] = Materials.Light(L, U)

    # print(Meridional.meridional(Materials.lens, Materials.lights['meri_infi_on_'+str(K1)], 1))
    return Meridional.meridional(Materials.lens, Materials.lights['meri_infi_on_'+str(K1)], 1)


def meri_infi_off():
    if Materials.lens[0].d > FAR_L:
        return

    K1 = Materials.K1
    K2 = Materials.K2

    U = K2 * Materials.obj['w']
    L = Materials.stops[0].d + K1 * Materials.stops[0].r / (math.tan(math.radians(U)))
    Materials.lights['meri_infi_off_' + str(K1) + '_' + str(K2)] = Materials.Light(L, U)

    # print(Meridional.meridional(Materials.lens, Materials.lights['meri_infi_off_'+str(K1)+'_'+str(K2)]))
    return Meridional.meridional(Materials.lens, Materials.lights['meri_infi_off_'+str(K1)+'_'+str(K2)])


def meri_limi_on():
    if Materials.lens[0].d <= FAR_L:
        return

    K1 = Materials.K1

    Umax = math.degrees(math.atan(Materials.stops[0].r / Materials.lens[0].d))
    L = Materials.lens[0].d
    sinU = K1 * (math.sin(math.radians(float(Umax))))
    U = math.degrees(math.asin(sinU))
    Materials.lights['meri_limi_on_' + str(K1)] = Materials.Light(L, U)

    # print(Meridional.meridional(Materials.lens, Materials.lights['meri_limi_on_' + str(K1)]))
    return Meridional.meridional(Materials.lens, Materials.lights['meri_limi_on_' + str(K1)])


def meri_limi_off():
    if Materials.lens[0].d <= FAR_L or 'r' not in Materials.obj:
        return

    K1 = Materials.K1
    K2 = Materials.K2

    ymax = Materials.obj['r']

    tanU = (K2 * ymax - K1 * Materials.stops[0].r) / (Materials.stops[0].d - Materials.lens[0].d)
    L = Materials.stops[0].d + K1 * Materials.stops[0].r / tanU
    U = math.degrees(math.atan(tanU))

    Materials.lights['meri_limi_off_' + str(K1) + '_' + str(K2)] = Materials.Light(L, U)

    # print(Meridional.meridional(Materials.lens, Materials.lights['meri_limi_off_' + str(K1) + '_' + str(K2)]))
    return Meridional.meridional(Materials.lens, Materials.lights['meri_limi_off_' + str(K1) + '_' + str(K2)])


def off_axis():
    Materials.K2 = 1
    Materials.K1 = 0

    return OffAxis.off_axis(Materials.lens)


def height():
    y = Materials.obj['r'] * Materials.K2
    w = math.radians(Materials.obj['w']) * Materials.K2

    return Paraxial.height(Materials.lens, y, w)