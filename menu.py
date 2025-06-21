import pygame
import sys

pygame.init()
# Tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogos da cobrinha")
# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AMARELO = (255, 255, 0)
CINZA = (100, 100, 100)
# Fontes
fonte_titulo = pygame.font.Font(None, 60)
fonte_opcao = pygame.font.Font(None, 40)
# Opções
opcoes = ["Jogar", "Opções", "Sair"]
opcao_selecionada = 0
# Retângulos dos botões
botoes = [
    pygame.Rect(largura // 2 - 100, 220, 200, 50),
    pygame.Rect(largura // 2 - 100, 300, 200, 50),
    pygame.Rect(largura // 2 - 100, 390, 200, 50),
]
# Clock
clock = pygame.time.Clock()
rodando = True
#LOOP PRINCIPAL
while rodando:
    tela.fill(PRETO)
    # Título
    titulo = fonte_titulo.render("Jogos da corinha",True,BRANCO)
    tela.blit(titulo, (largura //
                        2 - titulo.get_width() //
                          2, 100))
    # POSICIONA O MOUSE
    mouse = pygame.mouse.get_pos()
    clicando = pygame.mouse.get_pressed()[0]
    # FORMATA O BOTÃO
    for i in range(len(botoes)):
        botao = botoes[i]
        # COR PADRÃO
        cor = BRANCO
        # HOVER DO MOUSE PARA PROVOCAR ANIMAÇÃO
        if botao.collidepoint(mouse):
            cor = AMARELO
            if clicando:
                cor = CINZA
                opcao_selecionada = i  
        # SELEÇÃO VIA TECLADO
        if i == opcao_selecionada:
            cor = AMARELO
        pygame.draw.rect(tela, cor, botao, border_radius=8)
        # TEXTO DO BOTÃO
        texto = fonte_opcao.render(opcoes[i], True, PRETO)
        tela.blit(texto, (botao.centerx - texto.get_width() // 2,
                           botao.centery - texto.get_height() // 2))
    # EVENTOS
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    #EVENTO DO BOTÃO DO MOUSE 
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for i in range(len(botoes)):
                if botoes[i].collidepoint(mouse):
                    if i == 0:
                        print("Vai para a sala de modos")
                    elif i == 1:
                        print("Configurações...")
                    elif i == 2:
                        rodando = False
    #EVENTO DO BOTÃO DO TECLADO(setinha pra cima,baixo e ENTER)
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:
                opcao_selecionada = (opcao_selecionada + 1) % len(opcoes)
            if evento.key == pygame.K_UP:
                opcao_selecionada = (opcao_selecionada - 1) % len(opcoes)
            if evento.key == pygame.K_RETURN:
                if opcao_selecionada == 0:
                    print("Vai para a sala de modos")
                elif opcao_selecionada == 1:
                    print("Configurações...")
                elif opcao_selecionada == 2:
                    rodando = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
