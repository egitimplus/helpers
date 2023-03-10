import numpy as np


class Interpolate:
    # linear interpolation between two points
    def __init__(self, x, y):
        self.x = np.array(x[:2])
        self.y = np.array(y[:2])

    # linearly
    def lin(self):
        m = (self.y[1]-self.y[0])/(self.x[1]-self.x[0])
        def execute(x_fit):
            return self.result(m * (x_fit - self.x[0]) + self.y[0])
        return execute

    # logarithmically
    def log(self):
        sumy = np.sum(self.y)
        sumlogx = np.sum(np.log(self.x))
        b = (self.x.size * np.sum(self.y * np.log(self.x)) - sumy * sumlogx) / (self.x.size * np.sum(np.log(self.x) ** 2) - sumlogx ** 2)
        a = (sumy - b * sumlogx) / self.x.size
        def execute(xfit):
            return self.result(a + b * np.log(xfit))
        return execute

    # exponentially
    def exp(self):
        curve_fit = np.polyfit(self.x, np.log(self.y), 1)
        def execute(x_fit):
            return self.result(np.exp(curve_fit[1]) * np.exp(curve_fit[0] * x_fit))
        return execute

    # Increases the variable by percentage
    def min(self):
        def execute(x_fit):
            if self.y[0] > self.y[1]:
                return self.result(self.y[1] + self.y[1] * x_fit /100)
            else:
                return self.result(self.y[0] + self.y[0] * x_fit /100)
        return execute

    # Decreases the variable by percentage
    def max(self):
        def execute(x_fit):
            if self.y[0] > self.y[1]:
                return self.result(self.y[0] - self.y[0] * x_fit /100)
            else:
                return self.result(self.y[1] - self.y[1] * x_fit /100)
        return execute

    # manipulate fitted value
    def result(self, y_fit):
        if self.y[0] < self.y[1]:
            return self.y[1] if y_fit > self.y[1] else self.y[0] if y_fit < self.y[0] else y_fit
        else:
            return self.y[0] if y_fit > self.y[0] else self.y[1] if y_fit < self.y[1] else y_fit
