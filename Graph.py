from numpy import linspace
from matplotlib.pyplot import figure, gca, xlabel, ylabel, plot, show, annotate
import Materials
import Aberrations
import copy


def spherical():
    figure('Spherical')
    name = 'spherical'
    x = linspace(0, 1, 51)

    k_copy = copy.deepcopy(Materials.K)
    aber_copy = copy.deepcopy(Materials.aber)
    lights_copy = copy.deepcopy(Materials.lights)

    Materials.K[name] = []
    for item in x:
        if item == 0:
            continue
        Materials.K[name].append([item, 0])

    Materials.aber[name] = {}
    Aberrations.spherical()

    aber= []
    for key in x:
        if key == 0:
            aber.append(0)
        else:
            aber.append(Materials.aber[name][str(key) + '_0'])

    Materials.K = k_copy
    Materials.aber = aber_copy
    Materials.lights = lights_copy

    xlabel('spherical aberration')
    ylabel('K1')
    ax = gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    plot(aber, x)
    show()


def distortion():
    figure('Distortion')
    name = 'distortion'
    x = linspace(0, 1, 51)

    k_copy = copy.deepcopy(Materials.K)
    aber_copy = copy.deepcopy(Materials.aber)
    lights_copy = copy.deepcopy(Materials.lights)

    Materials.K[name] = []
    for item in x:
        if item == 0:
            continue
        Materials.K[name].append([0, item])

    Materials.aber[name] = {}
    Aberrations.distortion()

    aber = []
    for key in x:
        if key == 0:
            aber.append(0)
        else:
            aber.append(Materials.aber[name]['0_' + str(key)])

    Materials.K = k_copy
    Materials.aber = aber_copy
    Materials.lights = lights_copy

    xlabel('distortion')
    ylabel('K2')
    ax = gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    plot(aber, x)
    show()


def mag_chromatism():
    figure('Mag_chromatism')
    name = 'mag_chromatism'
    x = linspace(0, 1, 51)
    k_copy = copy.deepcopy(Materials.K)
    aber_copy = copy.deepcopy(Materials.aber)
    lights_copy = copy.deepcopy(Materials.lights)

    Materials.K[name] = []
    for item in x:
        if item == 0:
            continue
        Materials.K[name].append([0, item])

    Materials.aber[name] = {}
    Aberrations.mag_chromatism()

    aber = []
    for key in x:
        if key == 0:
            aber.append(0)
        else:
            aber.append(Materials.aber[name]['0_' + str(key)])

    Materials.K = k_copy
    Materials.aber = aber_copy
    Materials.lights = lights_copy

    xlabel('lateral chromatic aberration')
    ylabel('K2')
    ax = gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    plot(aber, x)
    show()


def trans_chromatism():
    figure('Trans_chromatism')
    x = linspace(0, 1, 51)
    x.put(0, 0.001)

    k_copy = copy.deepcopy(Materials.K)
    aber_copy = copy.deepcopy(Materials.aber)
    lights_copy = copy.deepcopy(Materials.lights)

    Materials.K['spherical'] = []
    for item in x:
        Materials.K['spherical'].append([item, 0])
        Materials.K['trans_chromatism'].append([item, 0])

    Materials.aber['spherical'] = {}

    Aberrations.spherical()
    Aberrations.trans_chromatism()
    aber = []
    for key in x:
        aber.append(Materials.aber['spherical'][str(key) + '_0'])
    aber_f = []
    for key in x:
        aber_f.append(Materials.aber['spherical_f'][str(key) + '_0'])
    aber_c = []
    for key in x:
        aber_c.append(Materials.aber['spherical_c'][str(key) + '_0'])

    Materials.K = k_copy
    Materials.aber = aber_copy
    Materials.lights = lights_copy

    xlabel('spherical aberration')
    ylabel('K1')
    ax = gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    plot(aber, x)
    plot(aber_f, x)
    plot(aber_c, x)
    annotate('d', xy=(aber[-1], x[-1]), xytext=(aber[-1], x[-1] - 0.1))
    annotate('F', xy=(aber_f[-1], x[-1]), xytext=(aber_f[-1], x[-1] - 0.1))
    annotate('C', xy=(aber_c[-1], x[-1]), xytext=(aber_c[-1], x[-1] - 0.1))
    show()


def curvature():
    figure('Curvature')
    name = 'curvature'
    x = linspace(0, 1, 51)
    k_copy = copy.deepcopy(Materials.K)
    aber_copy = copy.deepcopy(Materials.aber)
    lights_copy = copy.deepcopy(Materials.lights)

    Materials.K[name] = []
    for item in x:
        if item == 0:
            continue
        Materials.K[name].append([0, item])

    Materials.aber[name + '_s'] = {}
    Materials.aber[name + '_t'] = {}
    Aberrations.curvature()

    abers = []
    abert = []
    for key in x:
        if key == 0:
            abers.append(0)
            abert.append(0)
        else:
            abers.append(Materials.aber[name + '_s']['0_' + str(key)])
            abert.append(Materials.aber[name + '_t']['0_' + str(key)])

    Materials.K = k_copy
    Materials.aber = aber_copy
    Materials.lights = lights_copy

    xlabel('curvature')
    ylabel('K2')
    ax = gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    plot(abers, x)
    plot(abert, x)
    annotate('s', xy=(abers[-1], x[-1]), xytext=(abers[-1], x[-1] - 0.1))
    annotate('t', xy=(abert[-1], x[-1]), xytext=(abert[-1], x[-1] - 0.1))
    show()


def all_aberrations():
    spherical()
    curvature()
    distortion()
    trans_chromatism()
    mag_chromatism()