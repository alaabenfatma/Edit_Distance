import pandas as pd
import dynamic_programming_ED as dp
import greedy_approach as ga
import k_stripes_dynamic_programming as ksp
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score
from math import sqrt
from sklearn import preprocessing, decomposition

def edit_distance(database):
    protein = database.values
    n = protein.shape[0]
    tab = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            if i != j:
                #tab[i, j] = tab[j, i] = dp.dynamic_programming(protein[i, 3], protein[j, 3])[0]
                tab[i, j] = tab[j, i] = ksp.K_stripes_DP_ED(protein[i, 3], protein[j, 3], 3)[0]

    np.savetxt('edit_distance_branch_and_bound.txt', tab, fmt='%i')
    return tab

def knn(protein):
    n = 500
    target = protein['class'][:n]
    features = np.loadtxt('edit_distance_500.txt')
    features = pca(features)
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=13)
    k = int(sqrt(n / 22))
    if k % 2 == 0:
        k += 1
    neigh = KNeighborsClassifier(n_neighbors=k)
    neigh.fit(X_train, y_train)
    accuracy_score = neigh.score(X_test, y_test)
    y_predict = neigh.predict(X_test)
    labels = [i for i in range(1, 22)] + [99]
    f1_score_value = pd.DataFrame(f1_score(y_test, y_predict, average=None, labels=labels, zero_division=0), index=labels)
    return accuracy_score, f1_score_value, neigh

def pca(tab_ed):
    # calcul des composantes principales
    pca = decomposition.PCA(n_components=5)
    std_scale = preprocessing.StandardScaler().fit(tab_ed)  # normaliation des données
    X = std_scale.transform(tab_ed)
    pca.fit_transform(X)
    print(X[0])
    #print(pca.explained_variance_ratio_)
    #print(pca.explained_variance_ratio_.sum())
    return X



if __name__ == '__main__':
    database = pd.read_csv('protein_database.csv', header=None, names=['nom', 'length', 'class', 'chain'])
    print(database[:500].groupby('class').size())
    #knn(database)