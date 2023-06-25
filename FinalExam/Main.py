from Homework1 import dataSampling
from Homework2 import MainProcess
from Homework3.Factory import Factory

if __name__ == '__main__':


    while(True):
        print("输入要选择的作业展示(输入exit退出)\n"
              "1.Homework1\n"
              "2.homework2\n"
              "3.homework3")
        choice = input()
        if choice == '1':
            print(dataSampling.dataSampling(tuple=3))
        elif choice == '2':
            data = MainProcess.generate_random_data(10, 20, 30)
            print("Generated data:", data)

            svm_result = MainProcess.svm_classification(data)
            print("SVM result:", svm_result)

            rf_result = MainProcess.random_forest_classification(data)
            print("Random Forest result:", rf_result)
        elif choice == '3':
            data = Factory.data_sampling.generate_data()
            print(data)
            Factory.ml_package.execute(data)
            Factory.verify_package.evaluate(data)
        elif choice == "exit":
            exit()
        else:
            print("输入有误，请重新输入！\n")
