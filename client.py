import pygame
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
#Window size
width = 800
height = 600
#Create a window
window = pygame.display.set_mode((width, height))
#Set the windows title
pygame.display.set_caption("Hyper Sandbox")

clientNumber = 0

#Create a player class
class Player():
  #
  def __init__(self, x, y, width, height, color):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color
    self.rect = (x,y,width,height)
    self.vel = 3

  def draw(self,window):
      pygame.draw.rect(window, self.color, self.rect)

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
      self.rect = (self.x, self.y, self.width, self.height)

def stateWindow(bgcolor,text,color):
    window.fill(bgcolor)
    text_surface = myfont.render(text, False, color)
    window.blit(text_surface,(0,0))

def deathWindow(window):
  bgcolor = (0,0,0)
  text = 'You died.'
  color = (255,0,0)
  stateWindow(bgcolor,text,color)

def redrawWindow(window,player):
  window.fill((255,255,255))
  #Fill the windows before drawing the player otherwise it doesn't work
  player.draw(window)
  pygame.display.update()

#Main loop
def main():
  run = True
  #Instantiate the object, from the class Player
  p = Player(50,50,100,100,(180,0,240))
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()
    p.move()
    #Update the window and player
    redrawWindow(window,p)
    deathWindow(window)
#execute the main loop
main()
