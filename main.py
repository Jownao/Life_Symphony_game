import pygame
from elements import Tree, River, Building

# Inicializar o Pygame
pygame.init()

# Configurar a resolução da janela do jogo
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Configurar o título da janela do jogo
pygame.display.set_caption('Life Symphony')

# Criação dos elementos
tree = Tree((100, 100), 50, (0, 255, 0))
river = River((200, 200), 100, (0, 0, 255))
building = Building((300, 300), 150, (255, 0, 0))

# Loop principal do jogo
running = True
while running:
    # Preencher a tela com a cor preta
    screen.fill((0, 0, 0))

    # Desenhar os elementos
    tree.draw(screen)
    river.draw(screen)
    building.draw(screen)

    # Lidar com os eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o Pygame
pygame.quit()
