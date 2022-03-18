from email.policy import default
from re import I
from Grafo import Grafo
from converteJSON import converteJSON
opcao1 = 1
opcao2 = 1
opcao3 = 1
while (opcao1 != 0):
    print("\n")
    print("|----------------------------------------------------------------------|")
    print("|----------Teoria e Modelo de Grafos - Trabalho Prático I--------------|")
    print("|                                                                      |")
    print("|--------------------------BIBLIOTECA----------------------------------|")
    print("|                                                                      |")
    print("|---------------------Selecione uma opção:-----------------------------|")
    print("|                                                                      |")
    print(
        "|          [1] - Funcionalidades Trabalho Pratico I                    |")
    print(
        "|          [2] - Funcionalidades Trabalho Pratico II                   |")
    print(
        "|          [3] - Converter arquivo JSON para o formato de entrada      |")
    print(
        "|          [0] - Encerrar a Execucao                                   |")
    print("|----------------------------------------------------------------------|")
    print("Insira o numero da opcao desejada: ")
    opcao1 = int(input())

    
    if (opcao1 == 1):
        print("------------------------------------------------")
        arqInput = input("Insira o nome do arquivo de entrada: ")
        g = Grafo.leArquivo(arqInput)
        print("\n")
        nomeOut = input("Insira o nome do arquivo de saida: ")
        #print("\n")
        

        with open(nomeOut, "w") as arqOut:
            arqOut.write(
                "\n--------------------------IMPRIMINDO GRAFO--------------------------------------\n")

            g.mostra_matriz(arqOut)

            arqOut.write(
                "\n----------------------------------------------------------------------------\n")
            vertice = int(input(f'Selecione o vertice: (1 - {g.vertices})\n'))
            b = [0 for i in range(g.vertices+1)]
            a = [0 for i in range(g.vertices+1)]

            
            arqOut.write(
                "--------------------------ARQUIVO DE SAIDA--------------------------------------\n")

            while (opcao2 != 0):
                print("\n")
                print(
                    "|----------------------MENU DA BIBLIOTECA TPI--------------------------|")
                print(
                    "|                                                                      |")
                print(
                    "|          [1] - Grafo de Ordem                                        |")
                print(
                    "|          [2] - Grafo de tamanho                                      |")
                print(
                    "|          [3] - Vizinhos do vértice                                   |")
                print(
                    "|          [4] - Densidade do Grafo                                    |")
                print(
                    "|          [5] - Grau do vertice                                       |")
                print(
                    "|          [6] - Ciclo euleriano                                       |")
                print(
                    "|          [7] - BFS                                                   |")
                print(
                    "|          [8] - Componentes Conexas                                   |")
                print(
                    "|          [0] - Voltar para o Menu principal                          |")
                print(
                    "|----------------------------------------------------------------------|")
                opcao2 = int(input())

                if(opcao2 == 1):
                    arqOut.write(f'Grafo de Ordem: {g.ordemGrafo()}\n')
                    arqOut.write("\n")
                    print("Grafo de ordem exibido no arquivo de saida!")

                if(opcao2 == 2):
                    arqOut.write(f'Grafo de tamanho: {g.tamanhoGrafo()}\n')
                    arqOut.write("\n")

                if(opcao2 == 3):
                    arqOut.write(
                        f'Vizinhos do vértice {vertice}: {g.retornaVizinhos(vertice)}\n')
                    arqOut.write("\n")
                    g.AP(vertice, arqOut)

                if(opcao2 == 4):
                    arqOut.write(
                        f'Densidade do Grafo: {g.densidade_grafo()}\n')
                    arqOut.write("\n")

                if(opcao2 == 5):
                    arqOut.write(
                        f'Grau do vertice {vertice}: {g.grauVertice(vertice)}\n')

                if(opcao2 == 6):
                    arqOut.write(f'Ciclo euleriano: \n')
                    g.printEulerTour(arqOut)
                    arqOut.write("\n")
                    g.KruskalMST(arqOut)
                    grafoAux = Grafo.leArquivo(arqInput)

                if(opcao2 == 7):
                    arqOut.write("\nBFS\n")
                    g.BFS(arqOut)
                    cc = g.connectedComponents()

                if(opcao2 == 8):
                    arqOut.write(f'\nComponentes Conexas : {cc}\n')
                    if g.isCyclic() == 1:
                        arqOut.write("\nO GRAFO POSSUI CICLO\n")
                    else:
                        arqOut.write("\nO GRAFO NÃO POSSUI CICLO\n")

                if(opcao2 == 0):
                    default

    elif (opcao1 == 2):
 
        print("------------------------------------------------")
        arqInput = input("Insira o nome do arquivo de entrada: ")
        g = Grafo.leArquivo(arqInput)
        print("\n")
        nomeOut = input("Insira o nome do arquivo de saida: ")
        with open(nomeOut, "w") as arqOut:
            arqOut.write(
            "\n--------------------------IMPRIMINDO GRAFO--------------------------------------\n")

            g.mostra_matriz(arqOut)

            arqOut.write(
                "\n----------------------------------------------------------------------------\n")

            arqOut.write(
                "--------------------------ARQUIVO DE SAIDA--------------------------------------\n")
            
            while(opcao3!=0):
                print("\n")
                print(
                    "|----------------------MENU DA BIBLIOTECA------------------------------|")
                print(
                    "|                                                                      |")
                print(
                    "|          [1] - Heuristica Gulosa                                     |")
                print(
                    "|          [2] - Numero Cromatico do Grafo                             |")
                print(
                    "|          [3] - Grafo Dirigido                                        |")
                print(
                    "|          [0] - Voltar para o Menu principal                          |")
                print(
                    "|----------------------------------------------------------------------|")
                print("Insira a opcao desejada: ")
                opcao3 = int(input())
                
                if(opcao3 == 1):
                    arqOut.write("\n Heuristica Gulosa \n")
                    g.printSets(arqOut)
                    print("Heuristica Gulosa apresentada no arquivo de saida!\n")
                
                if(opcao3==2):
                   g.DSATUR_ALGORITHM(arqOut)   
                if(opcao3 == 0):
                    default
    if (opcao1 == 3): # Lê arquivo JSON
        arqJSON = input("Digite o nome do arquivo JSON: ")
        arqOut = input("Digite o nome do arquivo de saída: ")
        converteJSON(arqJSON, arqOut)
