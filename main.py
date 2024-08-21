import pygame
import sys
from pygame.locals import *
from resources import load_images
from player import Player
from map import default_map, draw_map

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def init_game():
    pygame.init()
    pygame.display.set_caption("異変")
    
    display_info = pygame.display.Info()
    screen_width = display_info.current_w
    screen_height = display_info.current_h
    print(f"{screen_width}:{screen_height}")
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    num = 0
    font = pygame.font.Font(None, 50)
    return screen, clock, screen_width, screen_height, num, font

def reset(player):
    if player:
        player.rect.x, player.rect.y = 10, 800  # 位置をpos=(10,800)にまた入れなおす
    map_data, flag = default_map()  # 新しいマップを表示する
    return map_data, flag

def main():
    screen, clock, screen_width, screen_height, game_clear_num, font = init_game()
    images = load_images()
    if not images:
        print("Error loading images")
        sys.exit()
    
    world_width, world_height = screen_width * 2, screen_height * 2
    player = Player(images["player"], world_width, world_height, screen, pos=(10, 800), speed=20)
    if not player:
        print("Error initializing player")
        sys.exit()
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    map_data, flag = default_map()
    if map_data is None:
        print("Error loading map data")
        sys.exit()

    switch = None

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_r:  # 'r'キーが押されたらリセット
                    map_data, flag = reset(player)

        all_sprites.update()

        # game_clear_numを文字列に変換して描画
        text = font.render(str(game_clear_num), True, (0, 0, 0))

        player_center_x = player.rect.centerx
        player_center_y = player.rect.centery

        camera_x = min(0, max(screen_width - world_width, -player_center_x + screen_width // 2))
        camera_y = min(0, max(screen_height - world_height, -player_center_y + screen_height // 2))

        screen.fill(BLACK)
        draw_map(screen, images, map_data, camera_x, camera_y)
        for sprite in all_sprites:
            screen.blit(sprite.image, (sprite.rect.x + camera_x, sprite.rect.y + camera_y))
        
        switch = player.player_select(camera_x, camera_y)
        if switch is not None:
            if flag and switch:  # 両方とも True の場合
                game_clear_num += 1
            elif not flag and not switch:  # 両方とも False の場合
                game_clear_num += 1
            map_data, flag = reset(player)
            switch = None  # ベルを押された時だけ判定するためswitchにはNoneが入ります

        if game_clear_num == 8:
            sys.exit()  # GameClear
        
        screen.blit(text, (camera_x + 0, camera_y + 0))
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
