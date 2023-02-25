import numpy as np


class Interpolate:
    # linear interpolation between two points
    def __init__(self, x, y):
        self._ld = 2
        self.x = x[:2]
        self.y = y[:2]

    # linearly
    def linear(self):
        m = (self.y[1]-self.y[0])/(self.x[1]-self.x[0])

        def islem(x_fit):
            return m * (x_fit - self.x[0]) + self.y[0]

        return islem

    # logarithmically
    def log(self):
        sumy = np.sum(self.y)
        sumlogx = np.sum(np.log(self.x))

        b = (self.x.size * np.sum(self.y * np.log(self.x)) - sumy * sumlogx) / (self.x.size * np.sum(np.log(self.x) ** self._ld) - sumlogx ** self._ld)
        a = (sumy - b * sumlogx) / self.x.size
        print('log')
        def islem(xfit):
            print('mog')
            return a + b * np.log(xfit)

        return islem

    # exponentially
    def exp(self):
        curve_fit = np.polyfit(self.x, np.log(self.y), 1)
        def islem(x_fit):
            return np.exp(curve_fit[1]) * np.exp(curve_fit[0] * x_fit)
        return islem

    # Increases the variable by percentage
    def min(self):
        def islem(x_fit):
            return y[0] + y[0] * x_fit /100
        return islem

    # Decreases the variable by percentage
    def max(self):
        def islem(x_fit):
            return y[1] - y[1] * x_fit /100
        return islem

    # manipulate fitted value
    def result(self, y_fit):
        return self.y[1] if y_fit > self.y[1] else self.y[0] if y_fit < self.y[0] else y_fit

    # set, get
    @property
    def log_degree(self):
        return self._ld

    @log_degree.setter
    def log_degree(self, a):
        self._ld = a
