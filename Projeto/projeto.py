import numpy as np
import random as rd

# Gerando mapa 5x5 com valores aleatórios de 1 a 10
mapa = np.random.randint(1,10, size=(5,5)) 

# Posicionando o Tesouro em uma posição do mapa
while True:
   tesouro_linha, tesouro_coluna = np.random.randint(0, 5, size=2)
   if(tesouro_coluna, tesouro_linha) != (0,0):
      break

# Declaração de pósição inicial do jogador
posicao_inicial_jogador = (0, 0)

# Declaração de pontuação do jogador
pontuacao = 0

# Criando Função para printar o mapa com o jogador
def mostrar_mapa(mapa, posicao_jogador):
   copia_mapa_original = mapa.copy()
   linha, coluna = posicao_jogador
   copia_mapa_original[linha, coluna] = -1

   mapa_joagador_toStr = np.char.mod('%2d', copia_mapa_original)
   copia_mapa_original[copia_mapa_original == '-1']== 'J1'

   print(f'\nMapa Atual:')
   for linha in copia_mapa_original:
      print(' '.join(linha))
    

