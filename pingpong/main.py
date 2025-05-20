from pygame import *

back = (200, 255, 255)
win_width = 1000
win_height = 1200
window = display.set_mode((win_width, win_height))

# Load background image
background = transform.scale(image.load("image.png"), (win_width, win_height))
winrlose = transform.scale(image.load("win or lose.jpg"), (500, 500))

# Inisialisasi font
font.init()
font_win = font.SysFont("Arial", 70)
win_text_p1 = font_win.render("NEKO 1 WINS!", True, (0, 200, 0))
win_text_p2 = font_win.render("NEKO 2 WINS!", True, (0, 0, 200))

class GameSprite(sprite.Sprite):  
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (wight, height)) 
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
 
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 
 
class Player(GameSprite): 
    def update_r(self): 
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < win_height - 80: 
            self.rect.y += self.speed 
    def update_l(self): 
        keys = key.get_pressed() 
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

p1 = Player("racket1.png", 5, 200, 10, 150, 150)
p2 = Player("racket.png", 850, 200, 10, 150, 150)
ball = GameSprite("ball.png", 200, 200, 4, 50, 50)

game = True 
finish = False 
clock = time.Clock() 
fps = 60

speed_x = 5
speed_y = 5

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))

        # Gerakkan bola
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        # Pantulan atas dan bawah
        if ball.rect.top <= 0 or ball.rect.bottom >= win_height:
            speed_y *= -1

        # Pantulan paddle
        if sprite.collide_rect(p1, ball) or sprite.collide_rect(p2, ball):
            speed_x *= -1

        # Deteksi menang/kalah
        if ball.rect.left <= 0:
            finish = True
        elif ball.rect.right >= win_width:
            finish = True

        # Update dan tampilkan objek
        p1.update_l()
        p2.update_r()
        p1.reset()
        p2.reset()
        ball.reset()
    else:
        # Posisi gambar win/lose
        win_img_x = 250
        win_img_y = 350
        window.blit(winrlose, (win_img_x, win_img_y))

        # Posisi teks di dalam gambar
        text_x = win_img_x + 60
        text_y = win_img_y + 370

        if ball.rect.left <= 0:
            window.blit(win_text_p2, (text_x, text_y))  # NEKO 2 WINS!
        elif ball.rect.right >= win_width:
            window.blit(win_text_p1, (text_x, text_y))  # NEKO 1 WINS!

    display.update()
    clock.tick(fps)
