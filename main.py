# Classe pessoa, que contem nome e idade
class pessoa:
    # inicializar o objeto pessoa
    def __init__(self, nome, idade):
        self.id = None
        self.nome = nome
        self.idade = idade

    # funcao que imprime os dados de uma pessoa
    def imprime(self):
        if self.id != None:
            print("id: ",self.id,", ",end="")
        print("nome: ",self.nome,", idade: ",self.idade)

# funcao para layout
def imprimeLinha(simb):
    if(simb != ""):
        for i in range(60):
            print(simb, end = "")
        print()

# Funcao para imprimir um array de pessoas
def imprimeVetor(pessoas, texto = "", simb="-"):
    print()
    print(texto)
    imprimeLinha(simb)
    for i in range(len(pessoas)):
        pessoas[i].imprime()

# Funcao para ordenar um array de pessoas por ordem alfabetica
def ordenaPorOrdemAlfabetica(pessoas):
    # Funcao que retorna a idade
    def key_func(pessoa):
        return pessoa.nome
    pessoas.sort(key=key_func)

# Funcao para ordenar um array de pessoas por idade
def ordenaPorIdade(pessoas):
    # Funcao que retorna o nome
    def key_func(pessoa):
        return pessoa.idade
    pessoas.sort(key=key_func)

# Array de pessoas do exercicio
pessoas = [pessoa("Fabiana Araújo", 33),
           pessoa("Gabriel Gomes", 25),
           pessoa("Fernando Henrique", 17),
           pessoa("Ana Luiza", 2),
           pessoa("Geralda do Nascimento", 93),
           pessoa("Miguel Souza", 70),
           pessoa("Antonio Miguel", 69)]

# imprimie o array inicial
imprimeVetor(pessoas, "Array inicial:")

def numeroDoExercicio(numeroAtual):
    print()
    imprimeLinha("=")
    print("\nEXERCIO NUMERO ",numeroAtual,":")
    imprimeLinha("=")
    return numeroAtual + 1

#----------------------------------------------------- NUMERO 2
numeroAtual = 2
numeroAtual = numeroDoExercicio(numeroAtual)
# ordena por idade e imprime
ordenaPorIdade(pessoas)
imprimeVetor(pessoas,"\nOrdenado por idade:")

# ordena por ordem alfabetica e imprime
ordenaPorOrdemAlfabetica(pessoas)
imprimeVetor(pessoas,"\nOrdenado por ordem alfabetica")
#--------------------------------------------------------------

#----------------------------------------------------- NUMERO 3
numeroAtual = numeroDoExercicio(numeroAtual)
def pesquisa(pessoas, pessoaDesejada):
    retorno = "Pessoa não encontrada"
    for p in pessoas:
        if(p.nome == pessoaDesejada):
            retorno = p
            break
    return retorno

pessoaTeste = pesquisa(pessoas, "Gabriel Gomes")
print("\nPessoa buscada:")
imprimeLinha("-")
pessoaTeste.imprime()
#--------------------------------------------------------------

#----------------------------------------------------- NUMERO 4
numeroAtual = numeroDoExercicio(numeroAtual)
def vetorNomes(pessoas):
    nomes = []
    for i in pessoas:
        nomes.append(i.nome)
    return nomes

def vetorPrimeirosNomes(pessoas):
    nomes = []
    for i in pessoas:
        nome = i.nome
        for j in range(len(nome)):
            if(nome[j] == " "):
                nomes.append(nome[0:j:1])
                break
    return nomes

nomes = vetorNomes(pessoas)
primeirosNomes = vetorPrimeirosNomes(pessoas)

def imprimeVetorString(vetor, texto=""):
    print()
    if(texto != ""):
        print(texto)
        imprimeLinha("-")
    print("[",end="")
    for i in range(len(vetor)):
        print('\'',vetor[i],'\'',end="")
        if(i != len(vetor) - 1):
            print(', ',end="")
            if(i % 2 == 0 and i != 0):
                print()
    print("]")

imprimeVetorString(nomes,"Vetor de nomes:")
imprimeVetorString(primeirosNomes,"Vetor dos primeiros nomes:")

#--------------------------------------------------------------

#----------------------------------------------------- NUMERO 5
numeroAtual = numeroDoExercicio(numeroAtual)
def geraId(pessoas):
    for i in range(len(pessoas)):
        pessoas[i].id = i + 1

geraId(pessoas)
imprimeVetor(pessoas, "Array com id's gerados:")
#--------------------------------------------------------------

#----------------------------------------------------- NUMERO 6
numeroAtual = numeroDoExercicio(numeroAtual)
def getIdadeParaHabilitacao(pessoas):
    suficiente = []
    for p in pessoas:
        if(p.idade > 17):
            suficiente.append(p)
    return suficiente

habilHabilitar = getIdadeParaHabilitacao(pessoas)

imprimeVetor(habilHabilitar,"\nPessoas que podem tirar habilitação:")
#--------------------------------------------------------------

#----------------------------------------------------- NUMERO 7
numeroAtual = numeroDoExercicio(numeroAtual)
def mediaIdades(pessoas):
    soma = 0
    for i in pessoas:
        soma += i.idade
    return float(soma / len(pessoas))

media = mediaIdades(pessoas)
print(f'\nA media das idades eh: {media:,.2f}')
#--------------------------------------------------------------

