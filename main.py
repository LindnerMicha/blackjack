import random

import pygame

pygame.init()
w, h = 1200, 900
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Workplace Helper")
clock = pygame.time.Clock()
fps = 60
runtime = True
option = " "
value_player = 0
value_bank = 0
state = " "

#region      -> Fonts
sys_font15 = pygame.font.SysFont(None, 15)
sys_font22 = pygame.font.SysFont(None, 22)
sys_font30 = pygame.font.SysFont(None, 30)
sys_font44 = pygame.font.SysFont(None, 44)
sys_font60 = pygame.font.SysFont(None, 60)
#endregion

def textObjekt(text, pixel_font15):
    textFlaeche = pixel_font15.render(text, True, (0, 0, 0))
    return textFlaeche, textFlaeche.get_rect()
def button(but_txt, but_x, but_y, but_laenge, but_hoehe, but_color_0, but_color_1, but_font):
    global maus_aktiv
    global option
    global r_int
    global value_player
    global value_bank
    global state

    if maus_pos[0] > but_x and maus_pos[0] < but_x + but_laenge and maus_pos[1] > but_y and maus_pos[1] < but_y+but_hoehe:
        pygame.draw.rect(screen, but_color_1, (but_x, but_y, but_laenge, but_hoehe))
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            option = but_txt

            if but_txt == "Hit":
                play_cards.append(r_int)
                value_player += cards[r_int][1]
                r_int = random.randint(0, len(cards)-1)
            elif but_txt == "Neue Karte":
                r_int = random.randint(0, len(cards)-1)
            elif but_txt == "Clear":
                play_cards.clear()
                bank_cards.clear()
                state = ""
                value_player = 0
                value_bank = 0
                bank_cards.append(r_int)
                value_bank += cards[r_int][1]
                r_int = random.randint(0, len(cards)-1)
            elif but_txt == "Ready":
                bank_cards.append(r_int)
                value_bank += cards[r_int][1]
                r_int = random.randint(0, len(cards)-1)
            elif but_txt == "Stand":
                while value_bank <= 17:
                    bank_cards.append(r_int)
                    value_bank += cards[r_int][1]
                    r_int = random.randint(0, len(cards)-1)
                    # wer gewonne hat auswertung hier hin

        if maus_klick[0] == 0:
            maus_aktiv = False
            option = " "
    else:
        pygame.draw.rect(screen, but_color_0, (but_x, but_y, but_laenge, but_hoehe))
    textGrund, textkasten = textObjekt(but_txt, but_font)
    textkasten.center = ((but_x+(but_laenge/2)),(but_y+(but_hoehe/2)))
    screen.blit(textGrund, textkasten)
def card(but_txt, but_x, but_y, but_laenge, but_hoehe, but_color_0, but_color_1, but_font):
    global maus_aktiv
    global option


    if maus_pos[0] > but_x and maus_pos[0] < but_x + but_laenge and maus_pos[1] > but_y and maus_pos[1] < but_y+but_hoehe:
        pygame.draw.rect(screen, but_color_1, (but_x, but_y, but_laenge, but_hoehe))
        if maus_klick[0] == 1 and maus_aktiv == False:
            maus_aktiv = True
            option = but_txt

            if but_txt == "Baugruppen":
                sites = "Baugruppen"
        if maus_klick[0] == 0:
            maus_aktiv = False
    else:
        pygame.draw.rect(screen, but_color_0, (but_x, but_y, but_laenge, but_hoehe))
    textGrund, textkasten = textObjekt(but_txt, but_font)
    textkasten.center = ((but_x+(but_laenge/2)),(but_y+(but_hoehe/2)))
    screen.blit(textGrund, textkasten)
def draw_text(text, sys_font15, color, screen, x , y):
    textobj = sys_font15.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)

card_x = 70
card_y = 110


cards = [
        ["II", 2, (255, 100, 100), (255, 200, 200)],
        ["III", 3, (255, 100, 100), (255, 200, 200)],
        ["IV", 4, (255, 100, 100), (255, 200, 200)],
        ["V", 5, (255, 100, 100), (255, 200, 200)],
        ["VI", 6, (255, 100, 100), (255, 200, 200)],
        ["VII", 7, (255, 100, 100), (255, 200, 200)],
        ["VIII", 8, (255, 100, 100), (255, 200, 200)],
        ["IX", 9, (255, 100, 100), (255, 200, 200)],
        ["X", 10, (255, 100, 100), (255, 200, 200)],
        ["K", 10, (255, 100, 100), (255, 200, 200)],
        ["A", 10, (255, 100, 100), (255, 200, 200)],
        ]

r_int = random.randint(0, len(cards)-1)
play_cards = []
bank_cards = []

bank_cards.append(r_int)
value_bank += cards[r_int][1]
r_int = random.randint(0, len(cards)-1)

while runtime:
    screen.fill((0, 0, 0))
    maus_pos = pygame.mouse.get_pos()
    maus_klick = pygame.mouse.get_pressed()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        runtime = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime = False


    pygame.draw.rect(screen, (255, 0, 0), [150, 50, card_x, card_y])
    button("Neue Karte", 1000, 20, 150, 70, (255, 255, 255), (255, 225, 255), sys_font30)
    button("Hit", 50, 800, 150, 70, (255, 255, 255), (255, 225, 255), sys_font30)
    button("Clear", 450, 800, 150, 70, (255, 255, 255), (255, 225, 255), sys_font30)

    play_card_x = 50
    play_card_y = 400
    for i in range(len(play_cards)):
        card(cards[play_cards[i]][0], play_card_x, play_card_y, card_x, card_y, cards[r_int][2], cards[r_int][3], sys_font44)
        play_card_x += 100

    bank_card_x = 50
    bank_card_y = 50
    for i in range(len(bank_cards)):
        card(cards[bank_cards[i]][0], bank_card_x, bank_card_y, card_x, card_y, cards[r_int][2], cards[r_int][3], sys_font44)
        bank_card_x += 100


    draw_text(f"Val Player: {value_player}", sys_font30, (255, 255, 255), screen, 50, 700)
    draw_text(f"Val Bank: {value_bank}", sys_font30, (255, 255, 255), screen, 50, 650)

    if value_player > 21:
        state = "player_lose"
        endscreen = True
    if value_bank > 21:
        state = "bank_lose"
        endscreen = True
    if value_bank == 21 and len(bank_cards) == 2:
        state = "bank_bj"
        endscreen = True
    elif value_player == 21 and len(play_cards) == 2:
        state = "player_bj"
        endscreen = True
    if value_bank <= 17:
        button("Stand", 250, 800, 150, 70, (255, 255, 255), (255, 225, 255), sys_font30)



    print(state)
    pygame.display.flip()
    clock.tick(fps)
