import pygame
#Window size
width = 800
height = 600
#Create a window
window = pygame.display.set_mode((width, height))
#Set the windows title
pygame.display.set_caption("Hyper Sandbox")

clientNumber = 0

class Player():
  def __init__(self, x, y, width, height, color):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color
    self.rect = (x,y,width,height)

  def draw(self,win):
      pygame.draw.rect(win, self.color, self.rect)

  def move(self):
      keys = pygame.key.get_pressed()

      if keys[pygame.K_LEFT]:
          self.x -= self.vel

      if keys[pygame.K_RIGHT]:
          self.x += self.vel

      if keys[pygame.K_UP]:
          self.y -= self.vel

      if keys[pygame.K_DOWN]:
          self.y += self.vel

def redrawWindow(window,player):
  player.draw(window)
  window.fill((255,255,255))
  pygame.display.update()


def main():
  run = True
  p = Player(50,50,100,100,(255,0,0))
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()
    p.move()
    redrawWindow(window,p)

main()
