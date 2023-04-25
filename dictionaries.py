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

# Podemos iterar pelos dicionários através de itens (chave e valor), através de valores e através de chaves

print ("---Method 1---")
for key in good_dictionarie.items():
    print(key[0], key[1])

print("\n---Method 2---")
for key, value in good_dictionarie.items():
    print(key,value)