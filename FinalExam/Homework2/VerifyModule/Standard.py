
# Modules decorator
class VerifyPackage:
    def __init__(self, *args):
        self.metrics = args

    def __call__(self, func):
        def wrapper(result):
            # 进行验证指标操作
            # print("Calculating performance metrics: ", *self.metrics)
            metrics = self.calculate_metrics(result)

            return metrics

        return wrapper

    def calculate_metrics(self, result):
        # 根据验证指标进行相应的计算
        metrics = []
        for metric in self.metrics:
            if metric == "ACC":
                acc = self.calculate_accuracy(result)
                metrics.append((metric, acc))
            elif metric == "MCC":
                mcc = self.calculate_mcc(result)
                metrics.append((metric, mcc))
            elif metric == "F1":
                f1 = self.calculate_f1(result)
                metrics.append((metric, f1))
            elif metric == "RECALL":
                recall = self.calculate_recall(result)
                metrics.append((metric, recall))
        return metrics

    def calculate_accuracy(self, result):
        # 计算准确率
        # 实现具体的计算逻辑
        return 0.85

    def calculate_mcc(self, result):
        # 计算MCC
        # 实现具体的计算逻辑
        return 0.72

    def calculate_f1(self, result):
        # 计算F1
        # 实现具体的计算逻辑
        return 0.78

    def calculate_recall(self, result):
        # 计算召回率
        # 实现具体的计算逻辑
        return 0.92