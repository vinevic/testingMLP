# Importa goose para extrair textos da URL
from goose3 import Goose
# Importa codecs para trabalhar com os arquivos no modo UTF-8
import codecs
# Importa biblioteca para trabalhar com xls
import xlrd
# Importa biblioteca para lidar com comandos do OS (Criar diretorios)
import os
# SKLearn para Rede Neural Artificial
import sklearn
from sklearn import datasets
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.neural_network import MLPClassifier

def pre_process():

    # Abre arquivo de base para extrair os textos
    book = xlrd.open_workbook("/home/vinevic/Documentos/Trabalho/01_treino.xls", encoding_override="utf-8")
    sh = book.sheet_by_index(0)

    ini_dir = os.getcwd()

    # Obtem diretorio atual
    current_catgc = "null"

    # Criar diretorio para os textos
    os.mkdir('files')   # Cria diretorio files
    os.chdir('files')   # Altera o diretorio atual para files
    actual_dir = os.getcwd()

    # Realiza a leitura da base para extrair os textos.
    for rx in range(sh.nrows):
        # obtem o nome a categoria 1
        cat1 = sh.cell_value(rx, 0)

        if not cat1:
            cat1 = "None"

        if cat1 != current_catgc:
            os.chdir(actual_dir)
            os.mkdir(cat1)
            os.chdir(cat1)
            current_catgc = cat1

        # obtem a URL do texto
        url = sh.cell_value(rx, 3)

        if not url:
            exit("Nao ha URL para leitura"+str(rx))

        filename = "arq_news_" + str(rx) + ".txt"
        g = Goose()
        article = g.extract(url=url)
        farq = codecs.open(filename, 'w', 'utf-8')
        farq.write(article.title)
        farq.write(article.cleaned_text)
        farq.close()

    os.chdir(ini_dir)

def process():

    dataset = sklearn.datasets.load_files("/home/vinevic/PycharmProjects/test_mlp/files")
    count_vect = CountVectorizer()
    x_train_counts = count_vect.fit_transform(dataset.data)
    x_train_counts.shape

    tfidf_transformer = TfidfTransformer()
    x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)
    x_train_tfidf.shape

    x = x_train_tfidf
    y = dataset.target

    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    clf.fit(x, y)

    return clf, count_vect, tfidf_transformer

def predict(clf, vect, tfidf):

    """# Abre arquivo de base para extrair os textos
    book = xlrd.open_workbook("/home/vinevic/Documentos/Trabalho/02_testes.xls", encoding_override="utf-8")
    sh = book.sheet_by_index(0)

    # Obtem diretorio atual
    current_catgc = "null"

    # Criar diretorio para os textos
    os.mkdir('fteste')   # Cria diretorio files
    os.chdir('fteste')   # Altera o diretorio atual para files
    actual_dir = os.getcwd()

    # Realiza a leitura da base para extrair os textos.
    for rx in range(sh.nrows):
        # obtem o nome a categoria 1
        cat1 = sh.cell_value(rx, 0)

        if not cat1:
            cat1 = "None"

        if cat1 != current_catgc:
            os.chdir(actual_dir)
            os.mkdir(cat1)
            os.chdir(cat1)
            current_catgc = cat1

        # obtem a URL do texto
        url = sh.cell_value(rx, 3)

        if not url:
            exit("Nao ha URL para leitura"+str(rx))

        filename = "arq_news_" + str(rx) + ".txt"
        g = Goose()
        article = g.extract(url=url)
        farq = codecs.open(filename, 'w', 'utf-8')
        farq.write(article.title)
        farq.write(article.cleaned_text)
        farq.close()
"""
    dataset = sklearn.datasets.load_files("/home/vinevic/PycharmProjects/test_mlp/fteste")
    #count_vect = CountVectorizer()
    x_train_counts = vect.transform(dataset.data)
    x_train_counts.shape

    #tfidf_transformer = TfidfTransformer()
    x_train_tfidf = tfidf.transform(x_train_counts)
    x_train_tfidf.shape

    x = x_train_counts
    y = dataset.target

    p = clf.predict(x)
    print("Resultado p: " + str(p))
    print("Resultado y: " + str(y))
    print("Labels:" + str(dataset.target) + str(dataset.target_names))

    z = clf.score(x,y)
    print("Resultado z:" + str(z))

print("Iniciando o pre-processamento..")
# pre_process()

print("Iniciando o treinamento..")
rede, vetor, tfidf = process()

print("Inicio da predicao..")
predict(rede, vetor, tfidf)