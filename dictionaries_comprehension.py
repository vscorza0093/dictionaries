# A compreensão de dicionários é uma expressão e um loop com uma condição opicional entre chaves.
# Assim como compreensão de listas e de sets, existem duas sintaxes suportadas:
# {key_expression:value_expression for key, value in iterable}
# {key_expression:value_expression for key, value in iterable if condition}

# Exemplo de como utilizar a compreensão de dicionários a fim de criar um dicionário o qual cada chave seja o nome de um arquivo no diretório corrente e cada valor seja o tamanho do arquivo em bytes

import os

file_sizes = {name: os.path.getsize(name) for name in os.listdir(".")}


# A função os.listdir() do módulo os retorna uma lista de arquivos e diretórios no caminho que foi passado, ainda que ele nunca inclua "." ou ".." na lista. A função os.path.getsize() retorna o tamanho de um arquivo dado em bytes. Podemos evitar diretórios e outras entradas que não são arquivos adicionando uma condição:

file_sizes2 = {name: os.path.getsize(name) for name in os.listdir(".") if os.path.isfile(name)}


# A função isfile() do módulo os.path retorna True caso o argumento passado seja um arquivo e falso caso não seja.
# Também existem as funções islink(), isdir(), isabs() entre outas funções 

# A compreensão de dicionários também pode ser usada para criar dicionários invertidos, onde as chaves são os valores e os valores são as chaves

inverted_dict = {v: k for k, v in file_sizes.items()}

for k, v in inverted_dict.items():
    print(k, v)


