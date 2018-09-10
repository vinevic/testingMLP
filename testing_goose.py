# Importa biblioteca Goose
from goose import Goose
# Importa codecs para trabalhar com os arquivos no modo UTF-8
import codecs
# Importa biblioteca para trabalhar com xls
import xlrd

# Importa biblioteca para lidar com comandos do OS (Criar diretorios)
import os

# Abre arquivo de base para extrair os textos
book = xlrd.open_workbook("/home/vinevic/Documentos/Trabalho/base.xls", encoding_override="utf-8")
sh = book.sheet_by_index(0)

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
