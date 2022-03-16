from email.policy import default
from Grafo import Grafo
from converteJSON import converteJSON

opcaoMenuPrincipal = 1
opcaoMenuSecundario = 1 
while (opcaoMenuPrincipal!=0):
    print("\n")
    print("|----------------------------------------------------------------------|")
    print("|----------Teoria e Modelo de Grafos - Trabalho Prático I--------------|")
    print("|                                                                      |")
    print("|--------------------------BIBLIOTECA----------------------------------|")
    print("|                                                                      |")
    print("|---------------------Selecione uma opção:-----------------------------|")
    print("|                                                                      |")
    print("|          [1] - Ler grafo a partir de um arquivo                      |")
    print("|          [2] - Converter arquivo JSON para o formato de entrada      |")
    print("|          [0] - Encerrar a Execucao                                   |")
    print("|----------------------------------------------------------------------|")
    opcaoMenuPrincipal = int(input())

    if (opcaoMenuPrincipal == 1): 
        print("\n")
        print("------------------------------------------------")
        arqInput = input("Insira o nome do arquivo de entrada: ")
        g = Grafo.leArquivo(arqInput)
        nomeOut = input("Insira o nome do arquivo de saida: ")

        with open(nomeOut, "w") as arqOut:
            arqOut.write("\n--------------------------IMPRIMINDO GRAFO--------------------------------------\n")

            g.mostra_matriz(arqOut)
        
            arqOut.write("\n----------------------------------------------------------------------------\n")
            vertice = int(input(f'Selecione o vertice: (1 - {g.vertices})\n'))
            b = [0 for i in range(g.vertices+1)]
            a = [0 for i in range(g.vertices+1)]

            arqOut.write("--------------------------ARQUIVO DE SAIDA--------------------------------------\n")

            while (opcaoMenuSecundario!=0):
                print("\n")
                print("|----------------------MENU DA BIBLIOTECA------------------------------|")
                print("|                                                                      |")
                print("|          [1] - Grafo de Ordem                                        |")
                print("|          [2] - Grafo de tamanho                                      |")
                print("|          [3] - Vizinhos do vértice                                   |")
                print("|          [4] - Densidade do Grafo                                    |")
                print("|          [5] - Grau do vertice                                       |")
                print("|          [6] - Ciclo euleriano                                       |")
                print("|          [7] - BFS                                                   |")
                print("|          [8] - Componentes Conexas                                   |")
                print("|          [0] - Voltar para o Menu principal                          |")
                print("|----------------------------------------------------------------------|")
                opcaoMenuSecundario = int(input())

                if(opcaoMenuSecundario == 1):
                    arqOut.write(f'Grafo de Ordem: {g.ordemGrafo()}\n')
                    arqOut.write("\n")
                    print("Grafo de ordem exibido no arquivo de saida!")
                
                if(opcaoMenuSecundario == 2):
                    arqOut.write(f'Grafo de tamanho: {g.tamanhoGrafo()}\n')
                    arqOut.write("\n")
                
                if(opcaoMenuSecundario == 3):
                    arqOut.write(f'Vizinhos do vértice {vertice}: {g.retornaVizinhos(vertice)}\n')
                    arqOut.write("\n")
                    g.AP(vertice,arqOut)
                
                if(opcaoMenuSecundario == 4):
                    arqOut.write(f'Densidade do Grafo: {g.densidade_grafo()}\n')
                    arqOut.write("\n")
                
                if(opcaoMenuSecundario == 5):
                    arqOut.write(f'Grau do vertice {vertice}: {g.grauVertice(vertice)}\n')

                if(opcaoMenuSecundario == 6):
                    arqOut.write(f'Ciclo euleriano: \n')
                    g.printEulerTour(arqOut)
                    arqOut.write("\n")
                    g.KruskalMST(arqOut)
                    grafoAux = Grafo.leArquivo(arqInput)
                    
                if(opcaoMenuSecundario == 7):
                    arqOut.write("\nBFS\n")
                    g.BFS(arqOut)
                    cc=g.connectedComponents()
                
                if(opcaoMenuSecundario == 8):
                    arqOut.write(f'\nComponentes Conexas : {cc}\n')
                    if g.isCyclic() == 1:
                        arqOut.write("\nO GRAFO POSSUI CICLO\n")
                    else:
                        arqOut.write("\nO GRAFO NÃO POSSUI CICLO\n")
                
                if(opcaoMenuSecundario == 0):
                    default

