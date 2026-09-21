print (" 1 - Sim")
print (" 2 - Não")
Baixo = 0
Medio = 0
Alto = 0
Total = 0
Outro = int( input("Deseja registrar um novo chamado?"))
while Outro != 2:
    Nome = input("Digite o nome do funcionário ")
    print ("1 - Computador 2 - Internet 3 - Sistema 4- Impressora")
    Problema = int( input("Qual o tipo de problema? "))
    while Problema < 1 or Problema > 4:
        print ("Opção inválida")
    Descrição = input("Descreva o problema.")
    print ("1 - Baixa 2 - Média 3 - Alta")
    Grau = int( input("Qual o grau de prioridade do problema?"))
    while Grau < 1 or Grau > 3:
        print ("Opção inválida")
    if Grau == 1:
        Grau = "Baixo"
        Baixo = Baixo + 1
        Total = Total + 1
        print ("Quantidade total de chamados:", Total)
        print ("Quantidade de chamados de baixa prioridade:", Baixo)
        print ("Quantidade de chamados de média prioridade:", Medio)
        print ("Quantidade de chamados de Alta prioridade:", Alto)
    elif Grau == 2:
        Grau = "Medio"
        Medio = Medio + 1
        Total = Total + 1
        print ("Quantidade total de chamados:", Total)
        print ("Quantidade de chamados de baixa prioridade:", Baixo)
        print ("Quantidade de chamados de média prioridade:", Medio)
        print ("Quantidade de chamados de Alta prioridade:", Alto)
    elif Grau == 3:
        Grau = "Alto"
        Alto = Alto + 1
        Total = Total + 1
        print ("Quantidade total de chamados:", Total)
        print ("Quantidade de chamados de baixa prioridade:", Baixo)
        print ("Quantidade de chamados de média prioridade:", Medio)
        print ("Quantidade de chamados de Alta prioridade:", Alto)
    Outro = int( input("Deseja registrar um novo chamado?"))
