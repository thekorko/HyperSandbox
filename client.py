import pygame
pygame.font.init()
myfont = pygame.font.SysFont('Consolas', 30)
#Window size
width = 800
height = 600
#Create a window
window = pygame.display.set_mode((width, height))
#Set the windows title
pygame.display.set_caption("Hyper Sandbox")

clientNumber = 0
fullScreen = False

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
    self.death = []
    self.vel = 3
    self.isAlive = True

  def draw(self,window):
      if self.isAlive:
        pygame.draw.rect(window, self.color, self.rect)
      else:
        #if the player is death it stays in the death location, suffering endlessly lol
        pygame.draw.rect(window, (0,0,0), self.rect)
        self.x = self.death[0]
        self.y = self.death[1]


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

class Monster():
  def __init__(self, x, y, width, height, color):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color
    self.rect = (x,y,width,height)
    self.vel = 3
    self.isAlive = True

  def draw(self,window):
      if self.isAlive:
        pygame.draw.rect(window, self.color, self.rect)
      else:
        pygame.draw.rect(window, (0,0,0), self.rect)
        i = 0;
        #Make the monster bigger and smaller
        #Move the monster out of the screen(Like running away)
        while i<60:
            self.x += 0.5
            i+=i

def stateWindow(window,bgcolor,text,color):
    window.fill(bgcolor)
    text_surface = myfont.render(text, False, color)
    window.blit(text_surface,(0,0))

def deathWindow(window):
  bgcolor = (50,50,50)
  text = 'You died.'
  color = (255,0,0)
  stateWindow(window,bgcolor,text,color)

def redrawWindow(window,player):
  if player.isAlive:
    window.fill((255,255,255))
  else:
    deathWindow(window)
  #Fill the windows before drawing the player otherwise it doesn't work
  player.draw(window)
  pygame.display.update()

def screenControl():
  keys = pygame.key.get_pressed()

  if keys[pygame.K_F11]:
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


  elif keys[pygame.K_F10]:
    pygame.display.set_mode((width, height))


  print("itIsInFullScreen", fullScreen)

def playerDeath(player):
  # Screen sizes
  w, h = pygame.display.get_surface().get_size()
  if player.x < 0 or player.y < 0:
    player.isAlive = False

  elif player.x > w or player.y > h:
    player.isAlive = False

  if not player.death and not player.isAlive:
    #save death location, to use on draw()
    player.death = [player.x, player.y]

#Main loop
def main():
  run = True
  #Instantiate the object, from the class Player
  p = Player(50,50,100,100,(180,0,240))
  m = Monster(-15,25,50,50,(0,190,230))
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()
    p.move()

    playerDeath(p)
    redrawWindow(window,p)
    # screenControl()

main()
