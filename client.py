import pygame

width = 800
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
  def __init__(self, x, y, width, height, color):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color


def redrawWindow():

  window.fill((255,255,255))
  pygame.display.update()


def main():
  run = True

  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()

    redrawWindow()

main()
