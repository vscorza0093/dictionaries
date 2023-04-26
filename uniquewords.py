import string
import sys

# Aqui temos um programa completo que lista cada palavra e o número de vezes que ela ocorre, em ordem alfabética, para todos os arquivos listados na linha de comando

words = {}
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word) > 1:
                words[word] = words.get(word, 0) + 1
for word in sorted(words):
    print("'{0}' occurs {1} times".format(word, words[word]))

print(words)

# Cria-se um dicionário vazio, em seguida é criada uma string que contém todos os caracteres que queremos ignorar, concatenando algumas strings úteis fornecidas pelo pacote string.
# Em seguida iteramos sobre cada linha do arquivo filename que foi recebido pelo método open()
# Então podemos passar um ou mais documentos de texto como argumento na hora que executarmos o programa via linha de comando
# Chamada com um argumento: python.exe .\uniquewords.py testdocument.txt
# Chamada com dois argumentos: python.exe .\uniquewords.py testdocument.txt testdocument2.txt
# Não é especificada nenhuma codificação pois não sabemos a codificação que cada arquivo terá, portanto, iremos deixar que o Python abra cada arquivo utilizando uma codificação loca padrão. 
# Não é possível utilizar a sintaxe words[word] += 1, uma exceção KeyError seria lançada assim que uma nova palavra fosse encontrada, não podemos incrementar o valor de um item que não existe no dicionário.
# Podemos chamar dict.get() com um valor padrão de 0. Se a palavra já estiver no dicionário, dict.get() irá retornar um número associado e este valor + 1 será configurado como sendo o novo valor do item

# Aqui temos um exemplo de como lidar com o mesmo tipo de problema, só que cada valor sendo, por si próprio, uma coleção

sites = {}
for filename in sys.argv[1:]:
    for line in open(filename):
        i = 0
        while True:
            site = None
            i = line.find("http://", i)
            if i > -1:
                i += len("http://")
                for j in range(i, len(line)):
                    if not (line[j].isalnum() or line[j] in ".-"):
                        site = line[i:j].lower()
                        break
                if site and "." in site:
                    sites.setdefault(site, set()).add(filename)
                i = j
            else:
                break

for site in sorted(sites):
    print("{0} is referred to in:".format(site))
    for filename in sorted(sites[site], key=str.lower):
        print("     {0}".format(filename))

# Começamos criando um dicionário vazio, iteramos sobre cada linha do arquivo listado na linha de comando e cada linha dentro dos limites de cada arquivo.
# Cada linha pode se referir a qualquer número de sites, por isso que é bom mantermos a chamada str.find(), até que a mesma falhe.
# Caso a string "http://" seja encontrada, incrementamos i (ou iniciamos a posição de índice) através do tamanho do "http://" e, depois, vemos cada caractere, sucessivamente, até encontrar um que não seja válido para um nome de site da Web. Se encontrarmos um site, o adicionamos para o dicionário.

# Não podemos utilizar a sintaxe sites[site].add(arquivo), pois isso lançaria uma exceção KeyError logo que um novo site fosse encontrado, depois de tudo, não podemos adicionar nada para um set que é o valor de um item que ainda não existe no dicionário. O método dict.setdefault() retorna uma referência de objeto ao item no dicionário que possui a chave dada (primeiro argumento). Caso não haja nenhum item semelhante, o método cria um novo item com a chave e configura seu valor para None, ou para o valor padrão (segundo argumento). 

# Utilizando um set, asseguramos que, ainda que um arquivo refira-se a um site repetidamente, poderemos gravar o filename somente uma vez para o site.

# Cada site é impresso com o caminho dos arquivos que se referem a ele, identados logo abaixo.

# A chamada sorted() externa ao loop for, ordena todas as chaves do dicionário -> Sempre que um dicionário é usado num contexto que requer um iterável, são as chaves que são utilizadas.

# Dicionário Padrão (default dict)

