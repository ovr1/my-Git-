import pickle

with open('C:/Users/Ruslan/PycharmProjects/GitProject/rsavenkov/serializing/colors.pickle', 'rb') as f:
    colors = pickle.load(f)
    print(colors)