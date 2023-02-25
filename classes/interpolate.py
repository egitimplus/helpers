import numpy as np


class Interpolate:
    # linear interpolation between two points
    def __init__(self, x, y):
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
        b = (self.x.size * np.sum(self.y * np.log(self.x)) - sumy * sumlogx) / (self.x.size * np.sum(np.log(self.x) ** 2) - sumlogx ** 2)
        a = (sumy - b * sumlogx) / self.x.size
        def islem(xfit):
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
