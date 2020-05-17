# Import libraries for organizing our data
# Import module for loading and saving our classifiers
import pickle
import tkinter as tk
# Import modules for our GUI
import tkinter.messagebox
# import different mathematical tools for analyzing our data
from statistics import mode

import pandas as pd
# Import module for our language processing classifiers
from nltk import ClassifierI


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    # Classify method that will take the classification of each classifier as a vote
    def predict(self, text):
        votes = []

        for classifier in (self._classifiers[0]):
            vote = int(classifier.predict(text))
            votes.append(vote)

        # Return whichever classification has the most votes with confidence
        confidence = (votes.count(mode(votes))) / len(votes)
        print(mode(votes), confidence)


def get_classifiers():
    # Load our classifiers for later classification
    load_classifier = open("BNB_classifier.pickle", "rb")
    BNB_classifier = pickle.load(load_classifier)
    load_classifier.close()

    load_classifier = open("Linear_classifier.pickle", "rb")
    Linear_classifier = pickle.load(load_classifier)
    load_classifier.close()

    load_classifier = open("LR_classifier.pickle", "rb")
    LR_classifier = pickle.load(load_classifier)
    load_classifier.close()

    load_classifier = open("MNB_classifier.pickle", "rb")
    MNB_classifier = pickle.load(load_classifier)
    load_classifier.close()

    load_classifier = open("SGD_classifier.pickle", "rb")
    SGD_classifier = pickle.load(load_classifier)
    load_classifier.close()

    load_classifier = open("SVC_classifier.pickle", "rb")
    SVC_classifier = pickle.load(load_classifier)
    load_classifier.close()

    load_classifier = open("NuSVC_classifier.pickle", "rb")
    NuSVC_classifier = pickle.load(load_classifier)
    load_classifier.close()

    classifiers = [Linear_classifier, LR_classifier, MNB_classifier]

    return classifiers


def transform_data(text):
    # Load our classifiers for later classification
    load_classifier = open("count_vector.pickle", "rb")
    count_vector = pickle.load(load_classifier)
    load_classifier.close()

    x_transform = count_vector.transform(text)
    return x_transform[0]


# Method called to get the user's input
def get_input():
    text = str(entry1.get())
    # Make sure the user has entered text before getting prediction
    if not text.strip():
        tk.messagebox.showerror("No Input", "Please Enter Headline!")
        entry1.delete(0, len(text))
    elif text is None:
        pass
    else:
        entry1.delete(0, len(text))
        df_headline = pd.DataFrame(columns=["Headlines"])
        df_headline = df_headline.append({"Headlines": text}, ignore_index=True)
        return transform_data(df_headline.iloc[0])


def get_prediction():
    # Creating a vote classifier object
    vote_classifier = VoteClassifier(get_classifiers())
    return vote_classifier.predict(get_input())


# GUI creation
root = tk.Tk()
root.title("Stock Market Prediction")

introduction = "Enter a popular headline from Reddit\n" \
               "World News to get a Dow Jones \nIndustrial " \
               "Average prediction."

label1 = tk.Label(text='Insert Headline Below').grid(padx=5, pady=5)
entry1 = tk.Entry(root, width=40)
entry1.grid(row=1, padx=5, pady=5)

label2 = tk.Label(text=introduction).grid(row=0, column=1, rowspan=3, padx=5, pady=5)

predictButton = tk.Button(text="Get Prediction", command=get_prediction).grid(row=3, padx=5, pady=5)
exitButton = tk.Button(text="Exit", width=10, command=root.quit).grid(row=3, column=1)

root.mainloop()
