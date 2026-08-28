import pygame

print("Setup start")
pygame.init()
# Define o tamanho da janela do jogo
screen = pygame.display.set_mode(size=(600, 480))
print("Setup end")

print("Loop Start")
# Mantém a janela aberta
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close window
            quit()  # End pygame
