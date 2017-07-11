import math
import Materials
import Paraxial
import Meridional
import OffAxis
from Prepare import FAR_L


def first_para():

    name = 'first_para'

    if name not in Materials.lights:
        light = {'L': Materials.lens[0]['d'],
                 'U': math.degrees(math.atan(Materials.stops[0]['r'] / Materials.lens[0]['d']))}
        Materials.lights[name] = [light]
        Materials.lights[name].append({'L': Paraxial.paraxial(Materials.lens, light)})

    Materials.basic['ideal spot'] = Materials.lights[name][-1]['L']

    return Materials.lights[name]


def second_para():

    name = 'second_para'

    if name not in Materials.lights:
        if 'w' in Materials.obj:
            light = {'L': 0, 'U': Materials.obj['w']}
        else:
            light = {'L': 0,
                     'U': math.degrees(math.atan(Materials.obj['r'] / Materials.lens[0]['d']))}

        Materials.lights[name] = [light]
        Materials.lights[name].append({'L': Paraxial.paraxial(Materials.lens, light)})

    return Materials.lights[name]


def meri_infi_on():

    if Materials.lens[0]['d'] > FAR_L:
        return

    K1 = Materials.K1

    name = 'meri_infi_on_' + str(K1) + Materials.extend

    if name not in Materials.lights:
        h1 = K1 * Materials.stops[0]['r']
        sin_i = h1 / Materials.lens[0]['r']
        sin_i_pie = sin_i / Materials.lens[0]['n']
        I = math.degrees(math.asin(sin_i))
        Ipie = math.degrees(math.asin(sin_i_pie))
        U = I - Ipie
        L = Materials.lens[0]['r'] + Materials.lens[0]['r'] * sin_i_pie / \
                                     math.sin(math.radians(U)) + Materials.lens[1]['d']

        Materials.lights[name] = [{'L': L, 'U': U}]
        Meridional.meridional(Materials.lens, Materials.lights[name], 1)

    return Materials.lights[name]


def meri_infi_off():
    if Materials.lens[0]['d'] > FAR_L:
        return

    K1 = Materials.K1
    K2 = Materials.K2

    name = 'meri_infi_off_' + str(K1) + '_' + str(K2) + Materials.extend

    if name not in Materials.lights:
        U = K2 * Materials.obj['w']
        L = Materials.stops[0]['d'] + K1 * Materials.stops[0]['r'] / (math.tan(math.radians(U)))
        Materials.lights[name] = [{'L': L, 'U': U}]

        Meridional.meridional(Materials.lens, Materials.lights[name])

    return Materials.lights[name]


def meri_limi_on():
    if Materials.lens[0]['d'] <= FAR_L:
        return

    K1 = Materials.K1

    name = 'meri_limi_on_' + str(K1) + Materials.extend

    if name not in Materials.lights:
        Umax = math.atan(Materials.stops[0]['r'] / Materials.lens[0]['d'])
        L = Materials.lens[0]['d']
        sinU = K1 * math.sin(Umax)
        U = math.degrees(math.asin(sinU))
        Materials.lights[name] = [{'L': L, 'U': U}]

        Meridional.meridional(Materials.lens, Materials.lights[name])

    return Materials.lights[name]


def meri_limi_off():
    if Materials.lens[0]['d'] <= FAR_L or 'r' not in Materials.obj:
        return

    K1 = Materials.K1
    K2 = Materials.K2

    name = 'meri_limi_off_' + str(K1) + '_' + str(K2) + Materials.extend

    if name not in Materials.lights:
        ymax = Materials.obj['r']

        tanU = (K2 * ymax - K1 * Materials.stops[0]['r']) / (Materials.stops[0]['d'] - Materials.lens[0]['d'])
        L = Materials.stops[0]['d'] + K1 * Materials.stops[0]['r'] / tanU
        U = math.degrees(math.atan(tanU))
        Materials.lights[name] = [{'L': L, 'U': U}]

        Meridional.meridional(Materials.lens, Materials.lights[name])

    return Materials.lights[name]


def off_axis():
    return OffAxis.off_axis(Materials.lens)


def height():
    if 'height' not in Materials.basic:
        y = Materials.obj['r']
        w = math.radians(Materials.obj['w'])

        Materials.basic['height'] = Paraxial.height(Materials.lens, y, w)

    return Materials.basic['height']


def focal():
    if 'focal' not in Materials.basic:
        Materials.basic['focal'] = Paraxial.focal(Materials.lens)

    return Materials.basic['focal']


def lp():
    if 'lp'not in Materials.basic:
        light = {'L': 0,
                 'U': math.degrees(math.atan(Materials.stops[0]['r'] / Materials.lens[0]['d']))}
        Materials.basic['lp'] = Paraxial.paraxial(Materials.lens, light)

    return Materials.basic['lp']


def all_parameters():
    first_para()
    height()
    focal()
    lp()