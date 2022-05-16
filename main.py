from funkcje import text_tokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn.svm import LinearSVC
from sklearn import metrics
import pandas as pd

fake = pd.read_csv('Fake.csv', usecols=['title', 'text'])
true = pd.read_csv('True.csv', usecols=['title', 'text'])
true['flag'] = 1
fake['flag'] = 0
joined = pd.concat([fake, true], ignore_index=True)


def main():
    vectorizer_count = CountVectorizer(tokenizer=text_tokenizer)
    news = vectorizer_count.fit_transform(joined['title'])
    x_train, x_test, y_train, y_test = train_test_split(news, joined['flag'], test_size=0.25, random_state=13)

    # Decision tree
    model_tree = DecisionTreeClassifier().fit(x_train, y_train)
    y_pred = model_tree.predict(x_test)
    print("\nDecision tree model accuracy: ", round(metrics.accuracy_score(y_test, y_pred), 3))

    # Random forest
    model_rf = RandomForestClassifier().fit(x_train, y_train)
    y_pred = model_rf.predict(x_test)
    print("\nRandom forest model accuracy: ", round(metrics.accuracy_score(y_test, y_pred), 2))

    # SVM
    model_svm = LinearSVC().fit(x_train, y_train)
    y_pred = model_svm.predict(x_test)
    print("\nSVM model accuracy: ", round(metrics.accuracy_score(y_test, y_pred), 3))

    # AdaBoost
    model_adaboost = AdaBoostClassifier().fit(x_train, y_train)
    y_pred = model_adaboost.predict(x_test)
    print("\nAdaBoost model accuracy: ", round(metrics.accuracy_score(y_test, y_pred), 3))

    # Bagging
    model_bag = BaggingClassifier().fit(x_train, y_train)
    y_pred = model_bag.predict(x_test)
    print("\nBagging model accuracy: ", round(metrics.accuracy_score(y_test, y_pred), 3))


main()
