import math
import Materials
import Paraxial
import Meridional
from Prepare import FAR_L


def first_para():

    name = 'first_para'

    if name not in Materials.lights:
        light = {'L': Materials.lens[0]['d'],
                 'U': math.degrees(math.atan(Materials.stops[0]['r'] / Materials.lens[0]['d']))}
        Materials.lights[name] = [light]
        Paraxial.paraxial(Materials.lens, Materials.lights[name])

    if 'ideal spot' not in Materials.basic:
        if 'first_para' in Materials.lights:
            Materials.basic['ideal spot'] = Materials.lights['first_para'][-1]['L']

    print(Materials.lights[name])

    return Materials.lights[name]


def second_para():

    name = 'lp'

    if name not in Materials.lights:
        if 'w' in Materials.obj:
            light = {'L': 0, 'U': Materials.obj['w']}
        else:
            light = {'L': 0,
                     'U': math.degrees(math.atan(Materials.obj['r'] / Materials.lens[0]['d']))}

        Materials.lights[name] = [light]
        Paraxial.paraxial(Materials.lens, Materials.lights[name])

        Materials.basic[name] = Materials.lights[name][-1]['L']


def meri_on():
    K1 = Materials.K1
    K2 = Materials.K2

    if Materials.lens[0]['d'] < FAR_L:

        name = 'infi_on_' + str(K1) + '_' + str(K2) + Materials.extend

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
    else:

        name = 'limi_on_' + str(K1) + '_' + str(K2) + Materials.extend

        if name not in Materials.lights:
            Umax = math.atan(Materials.stops[0]['r'] / Materials.lens[0]['d'])
            L = Materials.lens[0]['d']
            sinU = K1 * math.sin(Umax)
            U = math.degrees(math.asin(sinU))
            Materials.lights[name] = [{'L': L, 'U': U}]

            Meridional.meridional(Materials.lens, Materials.lights[name])

    return Materials.lights[name]


def meri_off():
    K1 = Materials.K1
    K2 = Materials.K2

    if Materials.lens[0]['d'] < FAR_L:
        name = 'infi_off_' + str(K1) + '_' + str(K2) + Materials.extend

        if name not in Materials.lights:
            U = K2 * Materials.obj['w']
            L = Materials.stops[0]['d'] + K1 * Materials.stops[0]['r'] / (math.tan(math.radians(U)))
            Materials.lights[name] = [{'L': L, 'U': U}]

    else:
        name = 'limi_off_' + str(K1) + '_' + str(K2) + Materials.extend

        if name not in Materials.lights:
            ymax = Materials.obj['r']

            tanU = (K2 * ymax - K1 * Materials.stops[0]['r']) / (Materials.stops[0]['d'] - Materials.lens[0]['d'])
            L = Materials.stops[0]['d'] + K1 * Materials.stops[0]['r'] / tanU
            U = math.degrees(math.atan(tanU))
            Materials.lights[name] = [{'L': L, 'U': U}]

    Meridional.meridional(Materials.lens, Materials.lights[name])

    return Materials.lights[name]


def height(y=0, w=0):
    if 'height' not in Materials.basic:
        if y == 0 and w == 0:
            y = Materials.obj['r']
            w = math.radians(Materials.obj['w'])

        Materials.basic['height'] = Paraxial.height(Materials.lens, y, w)

    return Paraxial.height(Materials.lens, y, w)


def focal():
    if 'focal' not in Materials.basic:
        Materials.basic['focal'] = Paraxial.focal(Materials.lens)

    return Materials.basic['focal']


def all_parameters():
    first_para()
    second_para()
    height()
    focal()