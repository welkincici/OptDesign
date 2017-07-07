class Stop:
    def __init__(self, r, d):
        self.d = d
        self.r = r

lens = []
stops = []
obj = {}
K = {
    'spherical': [0.7, 1],
    'coma': [[0.7, 0.7], [0.7, 1], [1, 0.7], [1, 1]],
    'trans_chromatism': [0.7, 1],
    'mag_chromatism': [0.7, 1],
    'distortion': [0.7, 1]
}
K1 = 1
K2 = 1
nf = [1.52237092, 1.68751548, 1, 1]
nc = [1.51432267, 1.66661041, 1, 1]
nd = []


lights = {}
aber = {}
basic = {}
extend = ''


def add_len(row):
    lens.append({'n': row[0], 'v': row[1], 'r': row[2], 'd': row[3]})


# d是到第一面距离
def add_stop(r, d):
    stops.append(Stop(r, d))
    stops.sort(key=lambda stop: stop.d)


def show():
    print(lens)

    for item in stops:
        print(item.__dict__)

    print('obj', obj)
