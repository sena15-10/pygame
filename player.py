import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, img_player, wrd_width, wrd_height, screen, pos, speed=20):
        super().__init__()
        self.images = img_player
        self.world_width, self.world_height = wrd_width, wrd_height
        self.image = self.images['down'][0]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.speed = speed
        self.direction = 'down'
        self.frame = 10
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
        self.font = pygame.font.Font(None, 36)
        self.font_color = (0, 0, 0)
        self.screen = screen
        self.show_choice = False
        self.show_choice_index = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if not self.show_choice:
            if keys[pygame.K_DOWN]:
                self.rect.y += self.speed
                self.direction = 'down'
            elif keys[pygame.K_UP]:
                self.rect.y -= self.speed
                self.direction = 'up'
            elif keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
                self.direction = 'left'
            elif keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
                self.direction = 'right'
            now = pygame.time.get_ticks()
            if (keys[pygame.K_DOWN] or keys[pygame.K_UP] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame = (self.frame + 1) % len(self.images[self.direction])
                self.image = self.images[self.direction][self.frame]
            else:
                self.frame = 0
                self.image = self.images[self.direction][self.frame]
        
        self.atari_judg()

    def atari_judg(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.world_width:
            self.rect.right = self.world_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.world_height:
            self.rect.bottom = self.world_height

    def player_select(self, x, y):
        keys = pygame.key.get_pressed()
        enter_text = self.font.render("Push on ENTER", True, self.font_color)
        text_position = (self.rect.x -350 + x, self.rect.y - 20 + y)
        if self.rect.x > 3690 and 860 <= self.rect.y <= 960:
            print(f"Playre:{self.rect.x},Player{self.rect.y}\nTEXT POS:{text_position[0]},{text_position[1]}")
            self.screen.blit(enter_text, text_position)
            if keys[pygame.K_RETURN]:
                print("エンターキーが押されました")
                self.show_choice = True
                return self.handle_choice(keys, text_position)
        return None

    def player_push_enter_event(self, text_position):
        enter_text = self.font.render("Do you press the bell? yes/no g to go back", True, (0, 0, 0))
        yes_text = self.font.render("YES", True, (0, 0, 0) if self.show_choice_index == 0 else (100, 100, 100))
        no_text = self.font.render("NO", True, (0, 0, 0) if self.show_choice_index == 1 else (100, 100, 100))
        self.screen.blit(enter_text, (text_position[0], text_position[1] + 50))
        self.screen.blit(yes_text, (text_position[0], text_position[1] + 100))
        self.screen.blit(no_text, (text_position[0], text_position[1] + 150))

    def handle_choice(self, keys, text_position):
        while self.show_choice:
            self.screen.fill((255, 255, 255))  # 画面を白で塗りつぶす
            self.player_push_enter_event(text_position)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.show_choice_index = 0
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.show_choice_index = 1
                    elif event.key == pygame.K_g:
                        self.show_choice = False
                        return None
                    elif event.key == pygame.K_RETURN:
                        if self.show_choice_index == 0:
                            self.show_choice = False
                            return True
                        else:
                            self.show_choice = False
                            print("ああ")
                            return False
        return None
