'''Autor: Davi Jatobá Galdino
Componente Curricular: Algoritmos I
Concluido em: 26/04/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.'''


from random import randint
from time import sleep
import keyboard
import os

# Variáveis Globais utilizadas ao longo do programa
menu_inicial = 1
linha_nave = 29
coluna_nave = 15
linha_asteroid = 0
coluna_asteroid = randint(0, 21)
linha_projetil = 27
coluna_projetil = 26
movimento_asteroid = 0
score = 0
contador_asteroid = 0
tecla_espaco = False
primeiro_score = 0
segundo_score = 0
terceiro_score = 0
quarto_score = 0
quinto_score = 0
primeiro_lugar = 'None'
segundo_lugar = 'None'
terceiro_lugar = 'None'
quarto_lugar = 'None'
quinto_lugar = 'None'


# Função para apagar inputs que eram registrados durante o jogo
def apagar_inputs():
    while True:
        for i in range(0,1):
            keyboard.press('enter')
        input('')
        break


# Função reponsável por mostrar o conteúdo do 'sobre', e também controlar os comandos dentro dele
def mostrar_sobre():
    menu_sobre = 1
    global menu_inicial
    while menu_sobre == 1:
        os.system('cls')
        print('==== Sobre ====\n\n    1 - História\n    2 - Como jogar\n    3 - Voltar')
        menu_sobre = input('\nSua opção: ').strip()
        os.system('cls')
        if menu_sobre == '1':
            print ('História:')
            print('''\nAno 3021 - d.C.  -  A colisão do Planeta Upsilon - 431 com o cometa Faye, gerou uma explosão devastadora, espalhando
detritos por toda a  Via Láctea, cientistas  terráqueos  de  plantão  observaram essa  inquientação  no  universo, e
identificaram que uma chuva de pequenos asteroids iam se aproximar da atmosfera da Terra em alguns anos. Visto isso,
todas as nações do mundo se uniram para desenvolver uma nave, com projéteis capazes de extinguir os asteroids. Com o
tempo apertado, estimaram que conseguiriam construir apenas uma nave para essa missão, e para decidir aquele que vai
definir o destino da terra, convocaram os melhores pilotos do mundo para fazerem simulações desse confronto  com  os 
asteroids, e você foi selecionado para participar desses testes. Dê o seu melhor, e seja aquele que irá salvar  todo
o ecosssistema da Terra.''')
            print('\nAperte "ESC" para voltar')
            keyboard.wait('esc')
            menu_sobre = 1
        elif menu_sobre == '2':
            print('Como jogar:')
            print('''\n- Para controlar a nave utilize os comandos "< . >" (seta para esquerda, e seta para direita), movendo
  ela sempre na horizontal.
- Os projéteis são disparados pela tecla "espaço", e surgem a partir da posicão da nave, e se locomovem até o final.
- Só pode ser disparado um projétil por vez, então, NÃO ERRE (Acertar um asteroid reinicia os tiros). 
- O jogo é encerrado quando 10 asteroids chegarem até o final sem serem destruídos, ou quando atingir a nave.
- Apertar a tecla "Esc" encerra o jogo imediatamente.
- Cada asteroid destruído vale 10 pontos que no final serão contabilizados para definir um recordista.''' )
            print('\nAperte "ESC" para voltar')
            keyboard.wait('esc')
            menu_sobre = 1
        elif menu_sobre == '3':
            menu_inicial = 1
            menu_sobre = 0
        else:
            print('Opção inválida')


# Função que printa o nome do jogador dado, e a sua respectiva pontuação
def mostrar_record():
    global primeiro_score
    global segundo_score
    global terceiro_score
    global quarto_score
    global quinto_score
    global primeiro_lugar
    global segundo_lugar
    global terceiro_lugar
    global quarto_lugar
    global quinto_lugar
    global menu_inicial
    os.system('cls')
    print('========= Recordes ==========')
    print('Jogador ============ Pontuação')
    print(f'{primeiro_lugar}   ============   {primeiro_score}')
    print(f'{segundo_lugar}   ============   {segundo_score}')
    print(f'{terceiro_lugar}   ============   {terceiro_score}')
    print(f'{quarto_lugar}   ============   {quarto_score}')
    print(f'{quinto_lugar}   ============   {quinto_score}')
    print('=============================')
    print('Aperte "ESC" para voltar para o menu principal')
    keyboard.wait('esc')
    menu_inicial = 1


# Função responsável por reiniciar o asteroid e o projétil quando entram em colisão
def pontuacao():
    global coluna_asteroid
    global linha_asteroid
    global linha_projetil
    global coluna_projetil
    global tecla_espaco
    global score
    coluna_asteroid = randint(0, 21)
    linha_asteroid = 0
    linha_projetil = 27
    coluna_projetil = 26
    tecla_espaco = False
    score += 1


# Função que adiciona o projétil a quando a tecla 'espaço' é pressionada
def gerador_projetil():
    global tecla_espaco
    global coluna_projetil
    global colisao_nave
    global linha_projetil
    if tecla_espaco == False:
        if keyboard.is_pressed('space'):
            tecla_espaco = True
            coluna_projetil = coluna_nave
    if tecla_espaco == True:
        if linha_projetil != 5:
            matriz[linha_projetil][coluna_projetil] = 'o'
            linha_projetil -= 1
        else:
            linha_projetil = 27
            tecla_espaco = False


# Print da pontuação dentro da matriz do jogo
def matriz_score():
    global score
    global contador_asteroid
    matriz[30][1] = 'Score:'
    matriz[30][2] = str(score)
    matriz[31][1] = 'Asteroids não destruídos:'
    matriz[31][3] = str(contador_asteroid)


# Menu final de jogo, pergunta se o usuário quer tentar novamente, e reinicia os dados de jogo (Score, Contador de Asteroids, ...)
def segunda_tentativa():
    global tentar_novamente
    global contador_asteroid
    global coluna_projetil
    global linha_projetil
    global tecla_espaco
    global colisao_nave
    global score
    global linha_asteroid
    global menu_inicial
    while tentar_novamente != '1' and tentar_novamente != '2':
        print('\n===== Tentar novamente? =====')
        print('== 1 - Sim ======= Não - 2 ==')
        tentar_novamente = (input('Sua opção: ')).strip()
        if tentar_novamente == '1':
            contador_asteroid = 0
            coluna_projetil = 26
            linha_projetil = 27
            tecla_espaco = False
            colisao_nave = 1
            score = 0
            linha_asteroid = 0
            print('3...')
            sleep(0.8)
            print('2...')
            sleep(0.8)
            print('1...')
            sleep(0.8)
            menu_inicial = '1'
        elif tentar_novamente == '2':
            contador_asteroid = 0
            coluna_projetil = 26
            linha_projetil = 27
            tecla_espaco = False
            colisao_nave = 1
            score = 0
            linha_asteroid = 0
            menu_inicial = 1
        else:
            print('\n===== Opção inválida =====')
            sleep(1.5)
            os.system('cls')


# Printa GAME OVER e o motivo disso ter acontecido
def mensagem_gameover():
    global colisao_nave
    if colisao_nave == 0:
        print('========= GAME OVER =========')
        print('Um asteroid atingiu sua nave!')
        sleep(2)
        os.system('cls')
    elif colisao_nave == 1:
        print('========== GAME OVER ==========')
        print(f'Você deixou passar {contador_asteroid} asteroids')
        sleep(2)
        os.system('cls')
    else:
        print('========== GAME OVER ==========')
        print('Jogo encerrado pelo comando ESC')
        sleep(2)
        os.system('cls')


# Reinicia os valores quando 'esc' é apertado para finalizar o jogo
def press_esc():
    global contador_asteroid
    contador_asteroid = 0
    global linha_projetil
    linha_projetil = 27
    global coluna_projetil 
    coluna_projetil = 26
    global tecla_espaco
    tecla_espaco = False
    global colisao_nave
    colisao_nave = 3
    global linha_asteroid
    linha_asteroid = 0


# Função para registrar o score em ordem decrescente e recever o nick do jogador
def recordes():
    global primeiro_score
    global segundo_score
    global terceiro_score
    global quarto_score
    global quinto_score
    global primeiro_lugar
    global segundo_lugar
    global terceiro_lugar
    global quarto_lugar
    global quinto_lugar
    if score >= primeiro_score:
        quinto_lugar = quarto_lugar
        quarto_lugar = terceiro_lugar
        terceiro_lugar = segundo_lugar
        segundo_lugar = primeiro_lugar
        primeiro_lugar = input('NOVO RECORDE - Digite seu nick (5 caracteres): ')
        quinto_score = quarto_score
        quarto_score = terceiro_score
        terceiro_score = segundo_score
        segundo_score = primeiro_score
        primeiro_score = score
    elif score >= segundo_score:
        quinto_lugar = quarto_lugar
        quarto_lugar = terceiro_lugar
        terceiro_lugar = segundo_lugar
        segundo_lugar = input('NOVO RECORDE - Digite seu nick (5 caracteres): ')
        quinto_score = quarto_score
        quarto_score = terceiro_score
        terceiro_score = segundo_score
        segundo_score = score
    elif score >= terceiro_score:
        quinto_lugar = quarto_lugar
        quarto_lugar = terceiro_lugar
        terceiro_lugar = input('NOVO RECORDE - Digite seu nick (5 caracteres): ')
        quinto_score = quarto_score
        quarto_score = terceiro_score
        terceiro_score = score
    elif score >= quarto_score:
        quinto_lugar = quarto_lugar
        quarto_lugar = input('NOVO RECORDE - Digite seu nick (5 caracteres): ')
        quinto_score = quarto_score
        quarto_score = score
    elif score >= quinto_score:
        quinto_lugar = input('NOVO RECORDE - Digite seu nick (5 caracteres): ')
        quinto_score = score

    
# Controle da nave pelas teclas <,> do teclado, e a reposiciona na matriz
def posicao_nave(coluna, movimento):
    if movimento == 'right':
        if coluna != 23:
            coluna += 1
            return coluna
        else:
            return 23
    if movimento == 'left':
        if coluna != 2:
            coluna -= 1
            return coluna
        else:
            return 2
 

# Reset do asteroid quando ele chega na ultima linha da matriz
def posicao_asteroid(linha):
    if linha != 29:
        linha += 1
        return linha
    else:
        return 0


# Print da nave na matriz
def formato_nave():
    matriz[linha_nave][coluna_nave - 1] = '/'
    matriz[linha_nave][coluna_nave] = '_'
    matriz[linha_nave][coluna_nave + 1] = '\\'
    matriz[linha_nave - 1][coluna_nave] = '^'
    return


# Print do asteroid na matriz
def formato_asteroid():
    matriz[linha_asteroid][coluna_asteroid + 1] = '/'      
    matriz[linha_asteroid][coluna_asteroid + 2] = '*'     
    matriz[linha_asteroid][coluna_asteroid + 3] = '\\'
    matriz[linha_asteroid + 1][coluna_asteroid] = '/'
    matriz[linha_asteroid + 1][coluna_asteroid + 1] = '*'
    matriz[linha_asteroid + 1][coluna_asteroid + 2] = '*'
    matriz[linha_asteroid + 1][coluna_asteroid + 3] = '*'
    matriz[linha_asteroid + 1][coluna_asteroid + 4] = '\\'
    matriz[linha_asteroid + 2][coluna_asteroid] = '*'
    matriz[linha_asteroid + 2][coluna_asteroid + 1] = '*'
    matriz[linha_asteroid + 2][coluna_asteroid + 2] = '*'
    matriz[linha_asteroid + 2][coluna_asteroid + 3] = '*'
    matriz[linha_asteroid + 2][coluna_asteroid + 4] = '*'
    matriz[linha_asteroid + 3][coluna_asteroid ] = '\\'
    matriz[linha_asteroid + 3][coluna_asteroid + 1] = '*'
    matriz[linha_asteroid + 3][coluna_asteroid + 2] = '*'
    matriz[linha_asteroid + 3][coluna_asteroid + 3] = '*'
    matriz[linha_asteroid + 3][coluna_asteroid + 4] = '/'
    matriz[linha_asteroid + 4][coluna_asteroid + 1] = '\\'
    matriz[linha_asteroid + 4][coluna_asteroid + 2] = '*'
    matriz[linha_asteroid + 4][coluna_asteroid + 3] = '/'
    return


# Verifica se a coordenada do projétil é a mesma coordenada do asteroid, declarando colisão
def verificar_colisao_projetil():
    coordenada_projetil = matriz[linha_projetil][coluna_projetil]
    if coordenada_projetil == matriz[linha_asteroid + 4][coluna_asteroid + 1] or \
    coordenada_projetil == matriz[linha_asteroid + 4][coluna_asteroid + 2] or \
    coordenada_projetil == matriz[linha_asteroid + 4][coluna_asteroid + 3] or \
    coordenada_projetil == matriz[linha_asteroid + 3][coluna_asteroid] or \
    coordenada_projetil == matriz[linha_asteroid + 3][coluna_asteroid + 1] or \
    coordenada_projetil == matriz[linha_asteroid + 3][coluna_asteroid + 2] or \
    coordenada_projetil == matriz[linha_asteroid + 3][coluna_asteroid + 3] or \
    coordenada_projetil == matriz[linha_asteroid + 3][coluna_asteroid + 4] or \
    coordenada_projetil == matriz[linha_asteroid + 2][coluna_asteroid] or \
    coordenada_projetil == matriz[linha_asteroid + 2][coluna_asteroid + 4]:
        return True
    else:
        return False
    

# Verifica se a coordenada da nave é a mesma coordenada do asteroid, declarando colisão
def verificar_colisao_nave():
    if matriz[linha_nave][coluna_nave - 1] == '*' or \
    matriz[linha_nave][coluna_nave] == '*' or \
    matriz[linha_nave][coluna_nave + 1] == '*' or \
    matriz[linha_nave - 1][coluna_nave] == '*':
        return True
    else:
        return False

    
# Início do menu inicial do programa, através de um loop While
while menu_inicial == 1:
    os.system('cls')
    print('==== ASTEROIDS ====\n\n    1 - Jogar\n    2 - Record\n    3 - Sobre\n    4 - Sair')
    menu_inicial = input('\nSua opção: ').strip()
    # Colisão nave = variável para identificar se a nave foi atingida
    colisao_nave = 1
    contador_asteroid = 0
    if menu_inicial == '1':
        while menu_inicial == '1':
            tentar_novamente = 0
            while contador_asteroid < 10 and colisao_nave == 1:
                os.system('cls')
                matriz = []
                for i in range(0, 32):
                    linha = []
                    for j in range(0, 27):
                        linha.append(' ')
                    matriz.append(linha)
                # Gerador Nave
                formato_nave()
                # Gerador Asteroid
                formato_asteroid()
                # Gerador Projetil
                gerador_projetil()
                matriz_score()
                # Print da matriz
                for l in matriz:
                    print(''.join(l))
                # Recebe os comando e realiza as funções respectivas
                if keyboard.is_pressed('esc'):
                    press_esc()
                    break
                if verificar_colisao_nave() == True:
                    colisao_nave = 0
                if keyboard.is_pressed('right'):
                    direcao = 'right'
                    coluna_nave = posicao_nave(coluna_nave, direcao)
                if keyboard.is_pressed('left'):
                    direcao = 'left'
                    coluna_nave = posicao_nave(coluna_nave, direcao)
                if verificar_colisao_projetil() == True:
                    pontuacao()
                if linha_asteroid + 4 == 29:
                    # Reset do asteroid
                    contador_asteroid += 1
                    linha_asteroid = 0
                    coluna_asteroid = randint(0, 21)
                if verificar_colisao_nave == True:
                    colisao_nave = 0
                linha_asteroid = posicao_asteroid(linha_asteroid)
                sleep(0.03)
            apagar_inputs()
            mensagem_gameover()
            recordes()
            segunda_tentativa()
    # Outras opções do menu principal
    elif menu_inicial == '2':
        mostrar_record()
    elif menu_inicial == '3':
        mostrar_sobre()
    elif menu_inicial == '4':
        os.system('cls')
        print('============================')
        print('==== Obrigado por jogar ====')
        print('============================')
    else:
        print('\n== Opção inválida ==')
        sleep(1.5)
        menu_inicial = 1
        os.system('cls')
