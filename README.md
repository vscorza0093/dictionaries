# &#128013; Mapping Types


## Dictionaries

* Dicionários são tipos mapeamento, suportam operador de associação in e função len(). São coleções de itens chave-valor.
* Quando iterados, tipos mapeamento fornecem seus itens de forma desordenada.
* No Python existem dois tipos de mapeamento nativos, dict e collections.defaultdict o termo comum para referí-los é dicionário

* As chaves dos dicionários só suportam objetos hashable, imutáveis
* Os valores dos dicionários suportam todo tipo de dados.

```py
class Person():
    def __init__(self) -> None:
        pass

good_dictionarie = {"key":"value",1:Person(),"numbers":[1, 2, 3, 4],"sets":{"set","inside","dictionarie"}}

tuple_is_good = {"tuple":"is good"}
frozenset_too = {"frozenset":frozenset({"is good"})}


wrong_dictionarie = {{"chave":"valor", 1:Person()}, ["list","inside","dictionarie"], {"is","forbidden"}}

^^^
TypeError: unhashable type: 'dict'
```

* Dicionários são mutáveis, então podemos adicionar e remover itens facilmente, porém, por serem desordenados, não possuem noção de posição de índice

```py
print(good_dictionarie[2])

KeyError: 2
```

* Dicionários são como funções que são chamadas e instanciam um novo objeto dicionário baseado no argumento.

* Formas de instanciar dicionários

```py
new_dict1 = dict({"id":"1234","name":"Vinicius"}) -> Literal
new_dict2 = dict(id=1234, name="Vinicius") -> Argumentos palavras-chave
new_dict3 = dict([("id",1234), ("name","Vinicius")]) -> Sequência
new_dict4 = dict(zip(("id","name"),(1234,"Vinicius))) -> Sequência
new_dict5 = {"id":1234,"name":"Vinicius"} -> Literal
```

* A função embutida zip(), retorna uma lista de tuplas; a primeira com os itens de cada argumento iterável da função zip();

* Para adicionar itens ao dicionários atribuímos um valor a uma chave com o operador =

```py
new_dict1["x"] = 200000
```
* Para remover, utilizamos del
```py
del(new_dict1["name"])
```

* Existem várias maneiras de iterar através de um dicionário. Podemos iterar por  uso de itens (chave e valor), através de valores e através de chaves

* O método items() é de grande valia nesse procedimento, pois ele retorna o item completo (chave e valor) de cada linha do dicionário, e podemos acessar esses  itens da forma que desejarmos (essa forma de trazer iterabilidade ao dicionário é conhecida como visualizações de dicionário)

```py
print ("\n---Method 1---")
for item in good_dictionarie.items():
    print(item)

print ("\n---Method 2---")
for item in good_dictionarie.items():
    print(item[0], item[1])

print("\n---Method 3---")
for key, value in good_dictionarie.items():
    print(key,value)
```

* Sem a utilização do método items() iteraremos por cada item do dicionário mas teremos como resposta apenas a sua chave

```py
print("\n---Method 1 without items()---")
print("It will return keys:\n")
for item in good_dictionarie:
    print(item)

print("\n---Method 2 without items()---")
print("It will return values:\n")
for item in good_dictionarie:
    print(good_dictionarie[item])
```        

* dict.items(), dict.keys() também são visualizações de dicionário.
* Uma visualização de dicionário é um objeto somento leitura que, aparentemente, armazena os itens, ou chaves, ou valores de um dicionário.
* Em geral, tratamos as visualizações como iteráveis, mas existem duas coisas que fazem uma visualização diferente de um iterável normal.
* A primeira é que a visualização reflete as mudanças sofridas pelo dicionário referenciado
* A segunda é que as chaves e itens da visualização suportam algumas operações do tipo set:

        * visualização_V & visualização_X -> Intersection
        * visualização_V | visualização_X -> Union
        * visualização_V - visualização_X -> Difference
        * visualização_V ^ visualização_X -> Symmetric difference

*  Além de utilizar o operador de associação in para verificar a existência de uma chave dentro de um dicionário, podemos utilizar o operador de interseção, para visualizar quais chaves de um set estão dentro de um dicionário:

```py
d = {}.fromkeys("ABCD", 3)
s = set("ACX")
matches = d.keys() & s
* {'A', 'C'}
```

* Aqui temos um programa completo que lista cada palavra e o número de vezes que ela ocorre, em ordem alfabética, para todos os arquivos listados na linha de comando

```py
import string
import sys

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
```

* Cria-se um dicionário vazio, em seguida é criada uma string que contém todos os caracteres que queremos ignorar, concatenando algumas strings úteis fornecidas pelo pacote string.
* Em seguida iteramos sobre cada linha do arquivo filename que foi recebido pelo método open()
* Então podemos passar um ou mais documentos de texto como argumento na hora que executarmos o programa via linha de comando
* Chamada com um argumento: python.exe .\uniquewords.py testdocument.txt
* Chamada com dois argumentos: python.exe .\uniquewords.py testdocument.txt testdocument2.txt
* Não é especificada nenhuma codificação pois não sabemos a codificação que cada arquivo terá, portanto, iremos deixar que o Python abra cada arquivo utilizando uma codificação loca padrão. 
* Não é possível utilizar a sintaxe words[word] += 1, uma exceção KeyError seria lançada assim que uma nova palavra fosse encontrada, não podemos incrementar o valor de um item que não existe no dicionário.
* Podemos chamar dict.get() com um valor padrão de 0. Se a palavra já estiver no dicionário, dict.get() irá retornar um número associado e este valor + 1 será configurado como sendo o novo valor do item

* Aqui temos um exemplo de como lidar com o mesmo tipo de problema, só que cada valor sendo, por si próprio, uma coleção

```py
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
```

* Começamos criando um dicionário vazio, iteramos sobre cada linha do arquivo listado na linha de comando e cada linha dentro dos limites de cada arquivo.
* Cada linha pode se referir a qualquer número de sites, por isso que é bom mantermos a chamada str.find(), até que a mesma falhe.
* Caso a string "http://" seja encontrada, incrementamos i (ou iniciamos a posição de índice) através do tamanho do "http://" e, depois, vemos cada caractere, sucessivamente, até encontrar um que não seja válido para um nome de site da Web. Se encontrarmos um site, o adicionamos para o dicionário.

* Não podemos utilizar a sintaxe sites[site].add(arquivo), pois isso lançaria uma exceção KeyError logo que um novo site fosse encontrado, depois de tudo, não podemos adicionar nada para um set que é o valor de um item que ainda não existe no dicionário. O método dict.setdefault() retorna uma referência de objeto ao item no dicionário que possui a chave dada (primeiro argumento). Caso não haja nenhum item semelhante, o método cria um novo item com a chave e configura seu valor para None, ou para o valor padrão (segundo argumento). 

* Utilizando um set, asseguramos que, ainda que um arquivo refira-se a um site repetidamente, poderemos gravar o filename somente uma vez para o site.

* Cada site é impresso com o caminho dos arquivos que se referem a ele, identados logo abaixo.

* A chamada sorted() externa ao loop for, ordena todas as chaves do dicionário -> Sempre que um dicionário é usado num contexto que requer um iterável, são as chaves que são utilizadas.

## Compreensão de dicionário

* A compreensão de dicionários é uma expressão e um loop com uma condição opicional entre chaves.
* Assim como compreensão de listas e de sets, existem duas sintaxes suportadas:
* {key_expression:value_expression for key, value in iterable}
* {key_expression:value_expression for key, value in iterable if condition}

* Exemplo de como utilizar a compreensão de dicionários a fim de criar um dicionário o qual cada chave seja o nome de um arquivo no diretório corrente e cada valor seja o tamanho do arquivo em bytes

```py
import os

file_sizes = {name: os.path.getsize(name) for name in os.listdir(".")}
```

* A função os.listdir() do módulo os retorna uma lista de arquivos e diretórios no caminho que foi passado, ainda que ele nunca inclua "." ou ".." na lista. A função os.path.getsize() retorna o tamanho de um arquivo dado em bytes. Podemos evitar diretórios e outras entradas que não são arquivos adicionando uma condição:

```py
file_sizes2 = {name: os.path.getsize(name) for name in os.listdir(".") if os.path.isfile(name)}
```

* A função isfile() do módulo os.path retorna True caso o argumento passado seja um arquivo e falso caso não seja.
* Também existem as funções islink(), isdir(), isabs() entre outas funções 

* A compreensão de dicionários também pode ser usada para criar dicionários invertidos, onde as chaves são os valores e os valores são as chaves

```py
inverted_dict = {v: k for k, v in file_sizes.items()}

for k, v in inverted_dict.items():
print(k, v)
```

## Dicionários Padrão (default dict)
