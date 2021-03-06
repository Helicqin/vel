from .base_metric import BaseMetric


class SummingMetric(BaseMetric):
    """ Base class for metrics that simply calculate the sum over the epoch """
    def __init__(self, name, reset_value=True):
        super().__init__(name)

        self.reset_value = reset_value
        self.buffer = 0

    def calculate(self, data_dict):
        """ Calculate value of a metric """
        value = self._value_function(data_dict)
        self.buffer += value

    def _value_function(self, data_dict):
        raise NotImplementedError

    def reset(self):
        """ Reset value of a metric """

        if self.reset_value:
            self.buffer = 0

    def value(self):
        """ Return current value for the metric """
        return self.buffer


class SummingNamedMetric(SummingMetric):
    """ Super simple summing metric that just takes a value from dictionary and sums it over samples """
    def __init__(self, name, reset_value=True):
        super().__init__(name, reset_value=reset_value)

    def _value_function(self, data_dict):
        return data_dict[self.name].item()
