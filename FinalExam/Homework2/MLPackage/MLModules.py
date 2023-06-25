
# Modules decorator
class MLPackage():
    def __init__(self, func, *args):
        self._func = func
        self._methods = args

    def __call__(self,func, *args, **kwargs):

        def wrapper(*data):
            # 进行机器学习方法操作
            # print("Applying machine learning method: ", *self._methods)
            result = func(*data)

            return result

        return wrapper
        self._func(*args, **kwargs)
        results = list()
        for model in self._methods:
            if model == "SVM":
                results = self.SVM(data='')
            elif model == "RF":
                results = self.RF(data='')
            elif model == "CNN":
                results = self.CNN(data='')
            elif model == "RNN":
                results = self.RNN(data='')

        return results

    def SVM(*args, data):
        results = list()
        #Calculation
        return results

    def RF(*args, data):
        results = list()
        # Calculation
        return results

    def CNN(*args, data):
        results = list()
        # Calculation
        return results

    def RNN(*args, data):
        results = list()
        # Calculation
        return results

