import pgzrun
from random import randint
WIDTH = 1000
HEIGHT = 550
player = Actor("monkey")
player.bottom = HEIGHT
player.x = WIDTH // 2
banana_y_speed = 0
missed = False
score=0
bananas = []
 
def draw():
  screen.clear()
  screen.blit("jungle.jpg" , (0,0))
  player.draw()
  draw_bananas()
  display_score()
  if missed:
    display_text()
 
def update():
  if not missed:
    move_player()
    move_bananas()
    check_collision()
    check_miss()
   
     
def move_bananas():
  global banana_y_speed
  for banana in bananas:
        banana.y += 5
 
def move_player():
   if keyboard.left:
     player.x -=10
   elif keyboard.right:
     player.x +=10
   if bananas[-1].y > 300:
          create_new_banana()
   if player.left < 0:
        player.left = 0
   elif player.right > WIDTH:
        player.right = WIDTH
 
 
def create_new_banana():
   banana = Actor("banana.png")
   banana.x = randint(100, WIDTH-100)
   banana.y += 10
   bananas.append(banana)
 
 
def draw_bananas():
   for banana in bananas:
      banana.draw()
 
def check_collision():
   global score
   for banana in bananas:
        if banana.colliderect(player):
            score += 5
            bananas.remove(banana)
            if len(bananas) == 0:
                  create_new_banana()
 
def check_miss():
    global missed
    for banana in bananas:
         if banana.bottom > HEIGHT+abs(banana_y_speed):
            print(banana.bottom)
            print(HEIGHT)
            print(HEIGHT + banana_y_speed)
            missed=True
            display_text()
 
def display_text():
    screen.draw.text(("OOPS MONKEY LEFT THE BANANA !!!"),((WIDTH//2)-300,HEIGHT//2),fontsize= 50,color="white")
 
def display_score():
    screen.draw.text("SCORE:" +str(score),(800,10),fontsize=50,color="blue")
 
create_new_banana() 
pgzrun.go()
