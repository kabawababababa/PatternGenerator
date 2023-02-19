# Each part of a sweater
from measurements import measurements
class arm:
    length=None
    type=None
    ease=None
    def __init__(self, stype):
        print("I'm not done yet")

class neckline:
    type=None;
    thickness=None
    def __init__(self, type):
        type=type
        thickness=None

class body:
    type=None
    ease=None

    def __init__(self, type):
        print("I'm not done yet")

class sweater():
    measurements = None
    gauge = None
    def __init__(self,measure, gauge) -> None:
        self.measurements = measurements(measure)
        self.set_gauge = gauge
    
    def set_gauge(self,knitGauge):
        if not all(isinstance(gauge, int) for gauge in knitGauge):
            raise ValueError(f'"Your gauge must use integers as values for [stitch width, row height]. Value: {knitGauge} is not valid"')
        elif len(knitGauge) != 2:
            raise ValueError(f'"Your gauge must use only two values, a width and a height"')
        elif knitGauge[0] == 0 or knitGauge[1] == 0:
            raise ValueError(f'"Your gauge must use non zero values"')
        self.newGauge=knitGauge
        return 0

    def get_gauge(self):
        return self.gauge