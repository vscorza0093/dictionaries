# Dicionários são tipos mapeamento, suportam operador de associação in e função len(). São coleções de itens chave-valor.
# Quando iterados, tipos mapeamento fornecem seus itens de forma desordenada.
# No Python existem dois tipos de mapeamento nativos, dict e collections.defaultdict o termo comum para referí-los é dicionário

# As chaves dos dicionários só suportam objetos hashable, imutáveis
# Os valores dos dicionários suportam todo tipo de dados.

class Person():
    def __init__(self) -> None:
        pass

good_dictionarie = {"key":"value",1:Person(),"numbers":[1, 2, 3, 4],"sets":{"set","inside","dictionarie"}}

tuple_is_good = {"tuple":"is good"}
frozenset_too = {"frozenset":frozenset({"is good"})}


# wrong_dictionarie = {{"chave":"valor", 1:Person()}, ["list","inside","dictionarie"], {"is",#"forbidden"}}

#^^^
#TypeError: unhashable type: 'dict'

# Dicionários são mutáveis, então podemos adicionar e remover itens facilmente, porém, por serem desordenados, não possuem noção de posição de índice

# print(good_dictionarie[2])
#
# KeyError: 2

# Dicionários são como funções que são chamadas e instanciam um novo objeto dicionário baseado no argumento.
#
# Formas de instanciar dicionários
#
new_dict1 = dict({"id":"1234","name":"Vinicius"}) # Literal
# new_dict2 = dict(id=1234, name="Vinicius") # Argumentos palavras-chave
# new_dict3 = dict([("id",1234), ("name","Vinicius")]) # Sequência
# new_dict4 = dict(zip(("id","name"),(1234,"Vinicius))) # Sequência
# new_dict5 = {"id":1234,"name":"Vinicius"} # Literal

# A função embutida zip(), retorna uma lista de tuplas; a primeira com os itens de cada argumento iterável da função zip();

# Para adicionar itens ao dicionários atribuímos um valor a uma chave com o operador =
new_dict1["x"] = 200000

# Para remover, utilizamos del
del(new_dict1["name"])

# Existem várias maneiras de iterar através de um dicionário. Podemos iterar por  uso de itens (chave e valor), através de valores e através de chaves

# O método items() é de grande valia nesse procedimento, pois ele retorna o item completo (chave e valor) de cada linha do dicionário, e podemos acessar esses  itens da forma que desejarmos (essa forma de trazer iterabilidade ao dicionário é conhecida como visualizações de dicionário)

print ("\n---Method 1---")
for item in good_dictionarie.items():
    print(item)

print ("\n---Method 2---")
for item in good_dictionarie.items():
    print(item[0], item[1])

print("\n---Method 3---")
for key, value in good_dictionarie.items():
    print(key,value)

# Sem a utilização do método items() iteraremos por cada item do dicionário mas teremos como resposta apenas a sua chave

print("\n---Method 1 without items()---")
print("It will return keys:\n")
for item in good_dictionarie:
    print(item)

print("\n---Method 2 without items()---")
print("It will return values:\n")
for item in good_dictionarie:
    print(good_dictionarie[item])
    
print("\n")

# dict.items(), dict.keys() também são visualizações de dicionário.
# Uma visualização de dicionário é um objeto somento leitura que, aparentemente, armazena os itens, ou chaves, ou valores de um dicionário.
# Em geral, tratamos as visualizações como iteráveis, mas existem duas coisas que fazem uma visualização diferente de um iterável normal.
# A primeira é que a visualização reflete as mudanças sofridas pelo dicionário referenciado
# A segunda é que as chaves e itens da visualização suportam algumas operações do tipo set:

# visualização_V & visualização_X -> Intersection
# visualização_V | visualização_X -> Union
# visualização_V - visualização_X -> Difference
# visualização_V ^ visualização_X -> Symmetric difference

#  Além de utilizar o operador de associação in para verificar a existência de uma chave dentro de um dicionário, podemos utilizar o operador de interseção, para visualizar quais chaves de um set estão dentro de um dicionário:

d = {}.fromkeys("ABCD", 3)
s = set("ACX")
matches = d.keys() & s
# {'A', 'C'}
