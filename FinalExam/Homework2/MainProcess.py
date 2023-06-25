from Homework2.MLPackage.MLModules import MLPackage
from Homework2.VerifyModule.Standard import VerifyPackage


@MLPackage("SVM", "RF", "CNN", "RNN")
def generate_random_data(*args):
    # 实现随机数据结构生成
    # print("Generating random data...")
    data = args
    return data


@MLPackage("SVM")
@VerifyPackage("ACC", "MCC")
def svm_classification(data):
    # 实现SVM分类算法
    # 使用data进行训练和预测
    result = "SVM result"
    return result


@MLPackage("RF")
@VerifyPackage("F1", "RECALL")
def random_forest_classification(data):
    # 实现随机森林分类算法
    # 使用data进行训练和预测
    result = "Random Forest result"
    return result


# 调用示例
data = generate_random_data(10, 20, 30)
# print("Generated data:", data)

svm_result = svm_classification(data)
# print("SVM result:", svm_result)

rf_result = random_forest_classification(data)
# print("Random Forest result:", rf_result)