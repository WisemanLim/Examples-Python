#-*- coding: utf-8 -*-
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pandas as pd

def  main() :
    # iris 데이터 로드 (1)
    dataset = datasets.load_iris()
    features = dataset.data
    targets = dataset.target

    df = pd.DataFrame(data=dataset['data'], columns=dataset['feature_names'])
    df.to_csv('03iris.csv', sep=',', index=False)

    # 꽃잎의 길이와 넓이 정보만 특징으로 사용 (2)
    petal_features = features[:, 2:]

    # 의사결정 모델 클래스 생성 (3)
    cIris = DecisionTreeClassifier (criterion = 'entropy', max_depth = 3)
    #모델을 훈련 (4)
    cIris.fit(petal_features, targets)

    # DOT 언어의 형식으로 결정 나무의 형태를 출력한다.
    filename = '03iris-dtree.dot'
    with open(filename, mode = 'w') as f:
        tree.export_graphviz(cIris, out_file = f)
    f.close()

    # DOT 형태를 이미지로 출력
    import graphviz
    with open(filename) as f:
        dot_graph = f.read()
    f.close()
    graphviz.Source(dot_graph)

if __name__ == '__main__':
    main()
