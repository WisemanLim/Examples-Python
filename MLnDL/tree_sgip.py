#-*- coding: utf-8 -*-
# Ref : https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pandas as pd
import numpy as np
from sklearn import svm, metrics, model_selection

def  main() :
    # iris 데이터 로드 (1)
    # dataset = datasets.load_iris()
    # features = dataset.data
    # targets = dataset.target
    # df = pd.DataFrame(data=dataset['data'], columns=dataset['feature_names'])
    # df.to_csv('03iris.csv', sep=',', index=False)
    csv = pd.read_csv('./sgip/form_vn2020f_v22.2.csv')
    feature_names = csv.columns.tolist() # ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"]
    # print(feature_names)
    # print(csv.head())
    # print(csv.columns)
    # print(csv.shape)
    class_names = ['Dry', 'Neutral', 'Combination', 'Oily'] # 건성/중성/복합/지성
    features = csv[feature_names].to_numpy()
    # print(features)
    ''' targets = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2] # iris targets '''
    # targets = np.where(csv['AdoptionSpeed']==4, 0, 1)
    csv['bq1'] = csv['bq1'] - 1
    targets = (csv['bq1'])

    # label = targets # csv["Name"]
    # clf = svm.SVC()
    # scores = model_selection.cross_val_score(clf, features, targets, cv=5)
    # print("각각의 정답률 =", scores)
    # print("평균 정답률 =", scores.mean())

    # 꽃잎의 길이와 넓이 정보만 특징으로 사용 (2)
    # target_features = features[:, 2:]
    ''' target_feature_names = ['sq1', 'sq2', 'sq3', 'sq4open', 'sq4', 'sq5', 'sq6', 'sq7', 'aq11', 'aq12', 'aq13', 'aq14', 'aq15', 'aq16', 'aq17', 'aq18', 'aq19'
        , 'aq3', 'aq41', 'aq42', 'aq43', 'aq44', 'aq45', 'aq46', 'aq47', 'aq48', 'aq51', 'aq52', 'aq53', 'aq54', 'aq55', 'aq56', 'aq57', 'aq58', 'aq59'
        , 'aq61', 'aq62', 'aq63', 'aq64', 'aq65', 'aq66', 'aq67', 'aq68', 'aq69', 'aq610', 'aq611', 'aq612', 'aq613', 'aq614', 'aq615', 'aq616', 'aq617'] '''
    target_feature_names = ['sq1', 'sq2', 'sq3', 'sq4open', 'sq4', 'sq5', 'sq7', 'aq11', 'aq12', 'aq13', 'aq14', 'aq15', 'aq16', 'aq17', 'aq18', 'aq19'
        , 'aq41', 'aq42', 'aq43', 'aq44', 'aq45', 'aq46', 'aq47', 'aq48', 'aq51', 'aq52', 'aq53', 'aq54', 'aq55', 'aq56', 'aq57', 'aq58', 'aq59'
        , 'aq61', 'aq62', 'aq63', 'aq64', 'aq65', 'aq66', 'aq67', 'aq68', 'aq69', 'aq610', 'aq611', 'aq612', 'aq613', 'aq614', 'aq615', 'aq616', 'aq617']
    # target_features = features[:, target_feature_names]
    # target_features = features[:, 0:6]
    target_features = csv.loc[:, target_feature_names]
    # criterion(분류기준) : gini(Gini impurity), entropy/log_loss(Shannon information gain)
    criterion = 'log_loss' # gini(default), entropy, log_loss

    # 의사결정 모델 클래스 생성 (3)
    dtSGIP = DecisionTreeClassifier(criterion=criterion, max_depth=3)
    #모델을 훈련 (4)
    dtSGIP.fit(target_features, targets)

    filename = 'sgip-dtree_' + criterion
    """
    # DOT 언어의 형식으로 결정 나무의 형태를 출력한다.
    with open(filename + ".dot", mode = 'w') as f:
        tree.export_graphviz(cIris, out_file = f)
    f.close() """
    import graphviz
    """
    # DOT 형태를 이미지로 출력
    with open(filename + ".dot") as f:
        dot_graph = f.read()
    f.close()
    graph = graphviz.Source(dot_graph)
    graph.format = "png"
    graph.render(filename)
    """
    # Print text
    dot_data = tree.export_text(dtSGIP)
    print(dot_data)

    # graphviz
    dot_data = tree.export_graphviz(dtSGIP, out_file=None
                                    , feature_names=target_feature_names, class_names=class_names
                                    , filled=True, rounded=True, special_characters=True)
    graph = graphviz.Source(dot_data)
    graph.format = "png"
    graph.render(filename)

    # dtreeviz
    from dtreeviz.trees import dtreeviz  # remember to load the package
    viz = dtreeviz(dtSGIP, target_features, targets, target_name="target"
                   , feature_names=target_feature_names, class_names=list(class_names))
    viz.save(filename + ".svg")
    # delete temporary file : filename, i.e 03iris-dtress
    import os
    os.system("rm -Rf " + filename)

if __name__ == '__main__':
    main()
