import sklearn
import spacy
from sklearn import datasets
from sklearn.neural_network import MLPClassifier
dataset = sklearn.datasets.load_files("/home/vinevic/anaconda3/envs/test_mlp/files")

nlp=spacy.load('pt')

textos = []
for i in dataset.target:
    doc = nlp(dataset.data[1].decode("utf-8"))
    tokens = [token.orth_ for token in doc if not token.is_punct]
    textos.append(tokens)

print(textos[0])

x = textos
y = dataset.target

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(x, y)

