class Len:
    def __init__(self, n, v, r, d):
        self.n = n
        self.v = v
        self.r = r
        self.d = d


class Stop:
    def __init__(self, r, d):
        self.d = d
        self.r = r


class Light:
    def __init__(self, l, u):
        self.l = l
        self.u = u

lens = []
stops = []
lights = {}
obj = {}

K = {
    'spherical': [0.7, 1],
    'coma': [[0.7, 0.7], [0.7, 1], [1, 0.7], [1, 1]],
    'trans_chromatism': [0.7, 1],
    'mag_chromatism': [0.7, 0.1]
}
K1 = 1
K2 = 0

nf = [1.52237092, 1.68751548, 1, 1]
nc = [1.51432267, 1.66661041, 1, 1]


def add_len(row):
    lens.append(Len(row[0], row[1], row[2], row[3]))


# d是到第一面距离
def add_stop(r, d):
    stops.append(Stop(r, d))
    stops.sort(key=lambda stop: stop.d)


def show():
    for item in lens:
        print(item.__dict__)

    for item in stops:
        print(item.__dict__)

    print('obj', obj)
