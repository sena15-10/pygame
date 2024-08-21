import pygame

def load_images():
    image_paths = {
        ##プレイヤーの宣言
        'player': {
            'down': [
                'img/player/bottomplayer1.png',
                'img/player/bottomplayer2.png'
            ],
            'left': [
                'img/player/left_player1.png',
                'img/player/left_player2.png'
            ],
            'up': [
                'img/player/player_top.png',
                'img/player/player_top2.png'
            ],
            'right': [
                'img/player/player_right.png',
                'img/player/player_right2.png'
            ]
        },
        #ここから異変のない置物の宣言(左側)
        'okimono':'img/okiren.png',
        'wall':'img/wall.png',
        'oki1':'img/oki1.png',
        'char':'img/char.png',
        'knight':'img/knight.png',
        'defalutetile':'img/defalute_yuka.png',
        'mado':'img/mado.png',      
        'richtable_set':'img/table_set.png',
        'hachi':'img/hachi.png',
        'carpet':'img/carpet.png',
        'table_set':'img/table_set.png',
        'doll_char':'img/dollchar.png',
        'piano':'img/piano.png',
        'plant':'img/plant.png',
        'plantset':'img/plant_set.png',
        'paper_set':'img/paper_set.png',
        'yokowall':'img/yoko_wall.png',
        'yoko_guiter':'img/yoko_guiter.png',
        'humen':'img/humen.png',
        'paper_set':'img/paper_set.png',
        #右側の宣言
        'tansu':'img/tansu.png',
        'zou':'img/zou.png',
        'cupdai':'img/cupdai.png',
        'sofa':'img/sofa.png',
        'rev_sofa':'img/sofa_revr.png',
        'teacup_set':'img/teacup_set.png',
        'clock':'img/clock.png',
        'doll_char':'img/dollchar.png',
        'dai_flower':'img/daiflower.png',
        'bookshelf':'img/bookshelf.png',
        'bookshelf_right':'img/bookshelf_right2.png',
        'bed':'img/bed.png',
        'tubo_Set':'img/tubo_set.png',
        'wood_table':'img/wood_tableSet.png',
        'brown_carpet':'img/Brown_carpet.png',
        'book_table':'img/bookEria_table.png',
        'book_set':'img/book_set.png',
        'light':'img/light.png',
        'rev_char':'img/rev_char.png',
        #バグシステムの読み込み
        'bug_yuka':'img/bugSystem/bug_yuka.png', #床
        'bug_bed':'img/bugSystem/bug_bed.png',
        'bug_bookset':'img/bugSystem/Bug_book_set.png',
        'bug_bookshelf':'img/bugSystem/bug_bookshelf.png',
        #アプデ
        'bug_bookshelf2':'img/bugSystem/bug_bookshelf2.png',
        'bug_book_set':'img/bugSystem/bug_bookEria_table.png',
        'bug_woodTableset':'img/bugSystem/bugwood_tableSet.png',
        'bug_yoko_wall':'img/bugSystem/bug_yoko_wall.png',
        'bugtable_set':'img/bugSystem/bug_table_set.png',
        'bugtable_set2':'img/bugSystem/bugtable_set.png',
        'bug_clock':'img/bugSystem/bug_clock.png',
        'bug_plantSet':'img/bugSystem/bug_plant_set.png',        
        'bug_char':'img/bugSystem/notdollchar.png',#血の椅子
        #
        'bug_daiflower':'img/bugSystem/bug_daiflower.png',
        'bug_paperSet':'img/bugSystem/bug_paperSet.png',
        'bug_revchar':'img/bugSystem/bug_revchar.png',
        'bug_tansu':'img/bugSystem/bug_tansu.png',
        'bug_tuboset':'img/bugSystem/Bug_tuboset.png',
        'Bug_guiter':'img/bugSystem/Bug_yoko_guiter.png',
        'bug_zou':'img/bugSystem/bug_zou.png',
        'bug_dollchar':'img/bugSystem/bugdollchar.png',
        'bug_knight':'img/bugSystem/bugknight.png',#ナイト
        'bug_light':'img/bugSystem/buglight.png',#ライト
        'bug_wall':'img/bugSystem/wallbug.png', #壁
        
        # 'bug_cup':{
        #             'img/bugSystem/bugcup1.png', #カップ
        #             'img/bugSystem/bugcup2.png',
        #             'img/bugSystem/bugcup3.png',
        #             'img/bugSystem/bugcup4.png',
        #             'img/bugSystem/bugcup5.png',
        #             'img/bugSystem/bugcup6.png',
        #             'img/bugSystem/bugcup7.png'
        #             }
    }

    def load_image(path):
        return pygame.image.load(path)#ここでkey:'img/path'の'pathを返してロード'

    def load_image_dict(image_dict):
        for key, value in image_dict.items():
            if isinstance(value, dict):
                image_dict[key] = load_image_dict(value) 
            elif isinstance(value, list):
                image_dict[key] = [load_image(v) for v in value] ##ここでアニメーション用の画像のパスを返す
            else:
                image_dict[key] = load_image(value)
        return image_dict

    images = load_image_dict(image_paths)
    return images
