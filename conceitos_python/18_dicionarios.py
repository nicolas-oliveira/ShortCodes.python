# Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos,
# fazendo a leitura dos valores por meio de uma estrutura de repetição.
# Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média

# Inicializando o dicionário para armazenar nome e nota dos alunos
alunos = {}

# Fazendo a leitura dos nomes e notas dos alunos e armazenando no dicionário
for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota

# Calculando a soma das notas
soma_notas = 0
for nota in alunos.values():
    soma_notas += nota

# Calculando a média das notas
media = soma_notas / len(alunos)

# Exibindo a média das notas
print("A média das notas dos alunos é:", media)

