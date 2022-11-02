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

#----------------------------------------------------- NUMERO 7
numeroDoExercicio(7)
def mediaIdades(pessoas):
    soma = 0
    for i in pessoas:
        soma += i.idade
    return float(soma / len(pessoas))

media = mediaIdades(pessoas)
print(f'\nA media das idades eh: {media:,.2f}')
#--------------------------------------------------------------

