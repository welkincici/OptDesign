import numpy as np
import matplotlib.pyplot as plt
import Materials
import Aberrations
import copy


def spherical():
    plt.figure('Spherical')
    name = 'spherical'
    x = np.linspace(0, 1, 52)
    if name in Materials.K:
        k_copy = copy.deepcopy(Materials.K[name])
    else:
        k_copy = []
    if name in Materials.aber:
        aber_copy = copy.deepcopy(Materials.aber[name])
    else:
        aber_copy = {}

    Materials.K[name] = []
    for item in x:
        if item == 0:
            continue
        Materials.K[name].append([item, 0])

    Materials.aber[name] = {}
    Aberrations.spherical()

    aber = list(Materials.aber[name].values())
    aber.insert(0, 0)

    Materials.K[name] = k_copy
    Materials.aber[name] = aber_copy

    plt.xlabel('spherical aberration')
    plt.ylabel('K1')
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    plt.plot(aber, x)
    plt.show()


def distortion():
    plt.figure('Distortion')
    name = 'distortion'
    x = np.linspace(0, 1, 52)

    if name in Materials.K:
        k_copy = copy.deepcopy(Materials.K[name])
    else:
        k_copy = []
    if name in Materials.aber:
        aber_copy = copy.deepcopy(Materials.aber[name])
    else:
        aber_copy = {}

    Materials.K[name] = []
    for item in x:
        if item == 0:
            continue
        Materials.K[name].append([0, item])

    Materials.aber[name] = {}
    Aberrations.distortion()

    aber = list(Materials.aber[name].values())
    aber.insert(0, 0)

    Materials.K[name] = k_copy
    Materials.aber[name] = aber_copy

    plt.xlabel('distortion')
    plt.ylabel('K2')
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    plt.plot(aber, x)
    plt.show()


def mag_chromatism():
    plt.figure('Mag_chromatism')
    name = 'mag_chromatism'
    x = np.linspace(0, 1, 52)
    if name in Materials.K:
        k_copy = copy.deepcopy(Materials.K[name])
    else:
        k_copy = []
    if name in Materials.aber:
        aber_copy = copy.deepcopy(Materials.aber[name])
    else:
        aber_copy = {}

    Materials.K[name] = []
    for item in x:
        if item == 0:
            continue
        Materials.K[name].append([0, item])

    Materials.aber[name] = {}
    Aberrations.mag_chromatism()

    aber = list(Materials.aber[name].values())
    aber.insert(0, 0)

    Materials.K[name] = k_copy
    Materials.aber[name] = aber_copy

    plt.xlabel('lateral chromatic aberration')
    plt.ylabel('K2')
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    plt.plot(aber, x)
    plt.show()


def trans_chromatism():
    plt.figure('Trans_chromatism')
    x = np.linspace(0, 1, 52)
    x.put(0, 0.001)

    if 'spherical' in Materials.K:
        ks_copy = copy.deepcopy(Materials.K['spherical'])
    else:
        ks_copy = []

    if 'spherical' in Materials.aber:
        abers_copy = copy.deepcopy(Materials.aber['spherical'])
    else:
        abers_copy = {}

    lights = copy.deepcopy(Materials.lights)

    Materials.K['spherical'] = []
    for item in x:
        Materials.K['spherical'].append([item, 0])

    Materials.aber['spherical'] = {}
    Materials.aber['trans_chromatism'] = {}

    Aberrations.spherical()
    aber = list(Materials.aber['spherical'].values())

    for item in range(0, len(Materials.lens)):
        Materials.lens[item]['n'] = Materials.nf[item]
    Materials.extend = '_f'
    Aberrations.spherical()
    aber_f = list(Materials.aber['spherical' + Materials.extend].values())

    for item in range(0, len(Materials.lens)):
        Materials.lens[item]['n'] = Materials.nc[item]
    Materials.extend = '_c'
    Aberrations.spherical()
    aber_c = list(Materials.aber['spherical' + Materials.extend].values())

    for item in range(0, len(Materials.lens)):
        Materials.lens[item]['n'] = Materials.nd[item]
    Materials.extend = ''

    Materials.K['spherical'] = ks_copy
    Materials.aber['spherical'] = abers_copy
    Materials.lights = lights

    plt.xlabel('spherical aberration')
    plt.ylabel('K1')
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    plt.plot(aber, x)
    plt.plot(aber_f, x)
    plt.plot(aber_c, x)
    plt.annotate('d', xy=(aber[-1], x[-1]), xytext=(aber[-1], x[-1] - 0.1))
    plt.annotate('F', xy=(aber_f[-1], x[-1]), xytext=(aber_f[-1], x[-1] - 0.1))
    plt.annotate('C', xy=(aber_c[-1], x[-1]), xytext=(aber_c[-1], x[-1] - 0.1))
    plt.show()


def curvature():
    plt.figure('Curvature')
    name = 'curvature'
    x = np.linspace(0, 1, 52)
    if name + '_s' in Materials.K:
        k_copy = copy.deepcopy(Materials.K[name])
    else:
        k_copy = []
    if name + '_s' in Materials.aber:
        abers_copy = copy.deepcopy(Materials.aber[name + '_s'])
        abert_copy = copy.deepcopy(Materials.aber[name + '_t'])
    else:
        abers_copy = []
        abert_copy = {}

    Materials.K[name] = []
    for item in x:
        if item == 0:
            continue
        Materials.K[name].append([0, item])

    Materials.aber[name + '_s'] = {}
    Materials.aber[name + '_t'] = {}
    Aberrations.curvature()

    abers = list(Materials.aber[name + '_s'].values())
    abers.insert(0, 0)
    abert = list(Materials.aber[name + '_t'].values())
    abert.insert(0, 0)

    Materials.K[name] = k_copy
    Materials.aber[name + '_s'] = abers_copy
    Materials.aber[name + '_t'] = abert_copy

    plt.xlabel('curvature')
    plt.ylabel('K2')
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    plt.plot(abers, x)
    plt.plot(abert, x)
    plt.annotate('s', xy=(abers[-1], x[-1]), xytext=(abers[-1], x[-1] - 0.1))
    plt.annotate('s', xy=(abert[-1], x[-1]), xytext=(abert[-1], x[-1] - 0.1))
    plt.show()


def all_aberrations():
    spherical()
    curvature()
    distortion()
    trans_chromatism()
    mag_chromatism()