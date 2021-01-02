import random
lista = ["Ler um livro", "Descansar 15 minutos", "Criar um projetinho em python", "Estudar uma materia da faculdade"] 
concluida = [] 
class Decididor():
    def adicionarMeta(self):
        lista.append(str(input("\nAdicionar meta: ")))

    def escolherMeta(self):
        cont = 0
        for i in lista:
            cont += 1
        num = random.randint(0, cont)
        print(num)
        metaAtual = lista.pop(num-1)
        print("\nMinha escolha foi: {}".format(metaAtual))
        concluida.append(metaAtual)
    
    def verTodasAsMetas(self):
        cont = 0
        for i in lista:
            cont +=1
            print("{}- {}".format(cont, i))
            
    def metasConcluidas(self):
        cont = 0
        print("\nMETAS CONCLUIDAS!!!\n")
        for i in concluida:
            cont +=1
            print("{}- {}".format(cont, i))
            
    def removerMeta():
        pass
    
    def removerMetaConcluida():
        pass


print("""1-Adicionar meta. 
2-Escolher meta.
3-Ver Todas as metas.
4-Metas Concluidas.
5-Remover meta.
         """)
var = 0
teste = Decididor()
while var != 5:
    var = int(input("Opção: "))
    if var == 1:
        teste.adicionarMeta()
    elif var == 2:
        teste.escolherMeta()
    elif var == 3:
        teste.verTodasAsMetas()
    elif var == 4:
        teste.metasConcluidas()
    elif var == 5:
        print("Você saiu")
        break
    else:
        print('[ERROR] Você digitou errado!!!')
