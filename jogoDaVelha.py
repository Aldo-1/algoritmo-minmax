import math

matriz = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

jogador_1 = 'x'
jogador_2 = 'o'

opcoes = {
  'x': (+1), #vitoria
  'o': (-1), #derrota
  'empate': 0, #empate
}

def melhorMovimento():
  pontuacao = -(math.inf)
  quemJoga = 0
  
  iMovimento = 0
  jMovimento = 0
  for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
      if(matriz[i][j] == ' '):
        #IA
        matriz[i][j] = jogador_1
        resultado = minimax(matriz, False)
        matriz[i][j] = ' '
        if(resultado > pontuacao):
          pontuacao = resultado
          iMovimento = i
          jMovimento = j

  matriz[iMovimento][jMovimento] = jogador_1
  quemJoga =+ 1
  return matriz,quemJoga 

def minimax(matriz, minOrMax):
  
  resultadoWinner = checarGanhador() 
 
  if(resultadoWinner != None):
    
    return opcoes[resultadoWinner]

  if(minOrMax):
    valorMaximo = -(math.inf)
    
    for i in range(0,len(matriz)):
      for j in range(0,len(matriz)):
        if(matriz[i][j] == ' '):
          ##ia
          matriz[i][j] = jogador_1
          valor = minimax(matriz, False)
          matriz[i][j] = ' '
          valorMaximo = max(valor, valorMaximo)
    return valorMaximo
  else:
    valorMinimo = (math.inf)
    for i in range(0,len(matriz)):
      for j in range(0,len(matriz)):
        if(matriz[i][j] == ' '):
          ##humano
          matriz[i][j] = jogador_2
          valor = minimax(matriz, True)
          matriz[i][j] = ' '
          valorMinimo = min(valor, valorMinimo)
    return valorMinimo

def printJogo():
  for i in range(0,len(matriz)):
    print('|'.join(matriz[i]))
    if(i != (len(matriz) - 1)):
      print('--' * len(matriz))

def checarGanhador():
  ganhador = None

  for i in range(0, len(matriz)):
    if(matriz[i][0] == matriz[i][1] == matriz[i][2] and matriz[i][0] != ' '):
      ganhador = matriz[i][0]
      

  for i in range(0, len(matriz)):    
    if(matriz[0][i] == matriz[1][i]  == matriz[2][i] and matriz[0][i] != ' '):
      ganhador = matriz[0][i]

  if(matriz[0][0] == matriz[1][1] == matriz[2][2] and matriz[0][0] != ' '):
      ganhador = matriz[1][1]
    
  if(matriz[0][2] == matriz[1][1] == matriz[2][0] and matriz[0][2] != ' '):
      ganhador = matriz[1][1]

  contadorAreaAberta = 0
  
  for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
      if(matriz[i][j] == ' '):
        contadorAreaAberta += 1
  
  if(ganhador != None and contadorAreaAberta != 0):
    return ganhador
  elif(ganhador == None and contadorAreaAberta == 0):
    return 'empate'
  else:
    return ganhador
  
def jogada(quemJoga):
  
  whoIsPlaying = jogador_1 if quemJoga == 0 else jogador_2

  jogador = 'Jogador 1' if whoIsPlaying == 'x' else 'Jogador 2'

  alguemGanhou = False
  while(True):
    jogada = input(jogador + ' Onde deseja jogar (Coloque o - Posição x e a posição y)?')
    jogadas = jogada.split(',')
    jogadas = [int(elem) for elem in jogadas]
          
    jogadaX = jogadas[0]
    jogadaY = jogadas[1]
          
    if(matriz[jogadaX][jogadaY] != ' '):
      print('Lugar ocupado!, escolha outra posicao')
    else:
      matriz[jogadaX][jogadaY] = whoIsPlaying
      break

  if(checarGanhador() == None and quemJoga == 1):
    quemJoga -= 1
  elif(checarGanhador() == None and quemJoga == 0):
    quemJoga += 1
  else:
    printJogo()
    if(checarGanhador() == 'x'):
      print('Ganhador jogador 1')
    else:
      print('Ganhador jogador 2')

    alguemGanhou = True
    

  return matriz, alguemGanhou, quemJoga

def startGame():
  quemJoga = 0
  while(True):
      if(quemJoga == 0):
        matriz , quemJoga = melhorMovimento()
        if(checarGanhador() == 'x'):
          printJogo()
          print('maquina Ganhou')
          return False
      elif(quemJoga == 1):
        printJogo()
        matriz,alguemGanhou, quemJoga = jogada(1)
        if(alguemGanhou == True):
          return False
        
if __name__ == "__main__":
    startGame()

