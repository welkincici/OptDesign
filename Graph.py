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

    plt.plot(aber, x)
    plt.show()


def trans_chromatism():
    plt.figure('Trans_chromatism')
    name = 'trans_chromatism'
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
    Aberrations.trans_chromatism()

    aber = list(Materials.aber[name].values())
    aber.insert(0, 0)

    Materials.K[name] = k_copy
    Materials.aber[name] = aber_copy

    plt.plot(aber, x)
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

    plt.plot(abers, x)
    plt.plot(abert, x)
    plt.show()


def all_aberrations():
    spherical()
    curvature()
    distortion()
    trans_chromatism()
    mag_chromatism()