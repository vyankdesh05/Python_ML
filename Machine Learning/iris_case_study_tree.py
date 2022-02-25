from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def Train_data_Decision_tree():

    iris=load_iris()

    data=iris.data
    target=iris.target

    train_data,test_data,train_target,test_target=train_test_split(data,target,test_size=0.5)
    obj=tree.DecisionTreeClassifier()
    obj1=obj.fit(train_data,train_target)
    result=obj1.predict(test_data)
    print(result)

    Accuracy=accuracy_score(test_target,result)
    print(Accuracy*100)

def main():

    print("---- Iris case study Decision tree -----")
    Train_data_Decision_tree()

if __name__ == "__main__":
    main()
