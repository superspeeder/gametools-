import pygame

class EquilateralTriangle:
  def __init__(self, side_length):
    self.sl = side_length
    self.pregenSurf(self)
   
  def pregenSurf(self):
    self.surf = pygame.Surface((self.sl,self.sl))
    pygame.draw.line(self.surf, (0,0,0), (0, self.sl), (self.sl, self.sl), 1)
    pygame.draw.line(self.surf, (0,0,0), (0, self.sl), (self.sl/2, 0), 1)
    pygame.draw.line(self.surf, (0,0,0), (self.sl, self.sl), (self.sl/2, 0), 1)
    
   
  def draw_to(self, surf, tl_pos):
    surf.blit(self.surf, tl_pos)
    
class Layer:
  def __init__(self, size):
    self.surf = pygame.Surface(size)
    self.memory = []
  
  def save(self):
    self.memory.append(self.surf.copy())
    if len(self.memory) == 50:
      self.memory.popleft()
    
  def rollback(self, save_ind):
    self.surface = self.memory[save_ind].copy()

  
