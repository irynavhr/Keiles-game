# Developed by Iryna Hrytsenko

import pygame as pg
import random
import time

# printinng game going
def printinng_game_going(lablabla):
    dell_text = pg.Surface(size=(wnd_w,70),depth=32)
    dell_text.fill(DARK_GRAY)
    # очистити поверхню під текст
    work_window.blit(dell_text,(0, 150))
    # друкуємо текст 
    text = bigText.render(lablabla,0, WHITE)
    sizeT = text.get_rect()
    work_window.blit(text,((wnd_w-sizeT[2])/2, 150)) 
    # відображуємо
    surface.blit(work_window, (0, 0))
    pg.display.update()

def print_game_erorr(blabla):
    dell_text = pg.Surface(size=(wnd_w,40),depth=32)
    dell_text.fill(DARK_GRAY)
    # очистити поверхню під текст
    work_window.blit(dell_text,(0, 490))
    # друкуємо текст 
    text = smallText.render(blabla,0, RED)
    sizeT = text.get_rect()
    work_window.blit(text,((wnd_w-sizeT[2])/2, 500)) 
    # відображуємо
    surface.blit(work_window, (0, 0))
    pg.display.update()
    # чекаємо
    time.sleep(1.2)
    # стираємо напис
    work_window.blit(dell_text,(0, 490))
    # відображуємо
    surface.blit(work_window, (0, 0))
    pg.display.update()


# match definer
def define_match_id(x):
    global AxORleft
    return (x - AxORleft)//60


# print matches
def fire_it(id):
    match_firing = pg.image.load('burning-match.png')
    match_none = pg.Surface(size=(60,250),depth=32)
    match_none.fill(DARK_GRAY)
    # # знебарвлення + запалення сірника
    work_window.blit(match_none,(AxORleft+id*60, AyORtop))
    work_window.blit(match_firing,(AxORleft+id*60, AyORtop))
    surface.blit(work_window, (0, 0))
    pg.display.update()

def make_match_fired():
    global matches_existing, work_window
    match_on = pg.image.load('match.png')
    match_firing = pg.image.load('burning-match.png')
    match_off = pg.image.load('burned-match.png')
    match_none = pg.Surface(size=(60,250),depth=32)
    match_none.fill(DARK_GRAY)
    for id in range(len(matches_existing)):
        if matches_existing[id] == 0:
            # знебарвлення + спалення сірника
            work_window.blit(match_none,(AxORleft+id*60, AyORtop))
            work_window.blit(match_off,(AxORleft+id*60, AyORtop))
            surface.blit(work_window, (0, 0))
            pg.display.update()
            # time.sleep(0.1)

def computer_make_match_fired():
    global compyter_choice_list
    global matches_existing, work_window
    match_on = pg.image.load('match.png')
    match_firing = pg.image.load('burning-match.png')
    match_off = pg.image.load('burned-match.png')
    match_none = pg.Surface(size=(60,250),depth=32)
    match_none.fill(DARK_GRAY)
    for id in compyter_choice_list:
        # # знебарвлення + запалення сірника
        work_window.blit(match_none,(AxORleft+id*60, AyORtop))
        work_window.blit(match_firing,(AxORleft+id*60, AyORtop))
        surface.blit(work_window, (0, 0))
        pg.display.update()
    time.sleep(1.2)    
    for id in compyter_choice_list:
        # знебарвлення + спалення сірника
        work_window.blit(match_none,(AxORleft+id*60, AyORtop))
        work_window.blit(match_off,(AxORleft+id*60, AyORtop))
        surface.blit(work_window, (0, 0))
        pg.display.update()
    time.sleep(0.3)    

def print_start_matches():  
    global work_window
    # знебарвлення попередніх сірників
    match_none = pg.Surface(size=(60*len(matches_existing),250),depth=32)
    match_none.fill(DARK_GRAY)
    work_window.blit(match_none,(AxORleft, AyORtop))
    # малюємо заново за списком
    match_on = pg.image.load('match.png')
    match_off = pg.image.load('burned-match.png')
    for id in range(len(matches_existing)):
        if matches_existing[id] == 1:
            work_window.blit(match_on,(AxORleft+id*60, 200)) 
        elif matches_existing[id] == 0:
            work_window.blit(match_off,(AxORleft+id*60, 200))
    # відображуємо
    surface.blit(work_window, (0, 0))
    # pg.display.update()


# funcs for displaying winds:
def display_start_wind():
    global currentWind, start_window
    global buttonToStart_w, buttonToStart_h
    start_window = pg.Surface(size=(wnd_w,wnd_h),depth=32)
    start_window.fill(DARK_BLUE)
    # button
    buttonToStart_h = 100
    buttonToStart_w = 200
    buttonToStart = pg.Rect((wnd_w-buttonToStart_w)/2, (wnd_h-buttonToStart_h)/2,\
                    buttonToStart_w, buttonToStart_h)
    pg.draw.rect(start_window,      WHITE,      buttonToStart, border_radius=20, )
    pg.draw.rect(start_window, (240, 240, 240), buttonToStart, border_radius=20, width=3)
    pg.draw.rect(start_window, (220, 220, 220), buttonToStart, border_radius=20, width=2)
    pg.draw.rect(start_window, (200, 200, 200), buttonToStart, border_radius=20, width=1)
    # button-text
    button_text = bigText.render("Play!",0, DARK_BLUE)
    sizeT = button_text.get_rect()  
    start_window.blit(button_text,((wnd_w-sizeT[2])/2, (wnd_h-sizeT[3])/2)) 
    # display
    currentWind = startWind
    print(f"currentWind = {currentWind}")
    surface.blit(start_window, (0, 0))
    pg.display.update()
  
def display_menu_wind():
    global currentWind, menu_window
    global buttonToPlay_h, buttonToPlay_w, but_1play_left, but_2play_left, buts_play_top
    menu_window = pg.Surface(size=(wnd_w,wnd_h),depth=32)
    menu_window.fill(DARK_GRAY)
    # label
    label = bigText.render("Keiles game",0, DARK_BLUE)  
    sizeT = label.get_rect() 
    menu_window.blit(label,((wnd_w-sizeT[2])/2 + 2, 160)) 
    label = bigText.render("Keiles game",0, WHITE)  
    menu_window.blit(label,((wnd_w-sizeT[2])/2, 157)) 
    # text
    text = smallText.render("or 2 neighboring ones from the row. Whoever takes the last match wins.",0, WHITE)
    sizeT = text.get_rect()
    menu_window.blit(text,((wnd_w-sizeT[2])/2, 251))
    text = smallText.render("The matches are placed in one row. Two players take turns taking 1 match",0, WHITE) 
    sizeT = text.get_rect() 
    menu_window.blit(text,((wnd_w-sizeT[2])/2, 221))
    # line
    pg.draw.line(menu_window,DARK_BLUE,(192,322),(910,322),width=3)
    pg.draw.line(menu_window,WHITE,(190,320),(908,320),width=2)
    # label
    label = bigText.render("Chose",0, WHITE)
    sizeT = label.get_rect()
    menu_window.blit(label,((wnd_w-sizeT[2])/2, 391))
    # label
    label = mediumText.render("or",0, WHITE)
    sizeT = label.get_rect()
    menu_window.blit(label,((wnd_w-sizeT[2])/2, 494))
    # buttons
    but_1play_left = 210
    but_2play_left = 618
    buts_play_top = 478

    buttonToPlay_h = 65
    buttonToPlay_w = 270
    buttonToPlay = pg.Rect(but_1play_left, buts_play_top,\
                    buttonToPlay_w, buttonToPlay_h)
    pg.draw.rect(menu_window, DARK_BLUE,  buttonToPlay, border_radius=20, )
    pg.draw.rect(menu_window, (0, 0, 40), buttonToPlay, border_radius=20, width=3)
    pg.draw.rect(menu_window, (0, 0, 30), buttonToPlay, border_radius=20, width=2)
    pg.draw.rect(menu_window, (0, 0, 20), buttonToPlay, border_radius=20, width=1)
    buttonToPlay = pg.Rect(but_2play_left, buts_play_top,\
                    buttonToPlay_w, buttonToPlay_h)
    pg.draw.rect(menu_window, DARK_BLUE,  buttonToPlay, border_radius=20, )
    pg.draw.rect(menu_window, (0, 0, 40), buttonToPlay, border_radius=20, width=3)
    pg.draw.rect(menu_window, (0, 0, 30), buttonToPlay, border_radius=20, width=2)
    pg.draw.rect(menu_window, (0, 0, 20), buttonToPlay, border_radius=20, width=1)
    # buttons text
    text = smallText.render("Play with friend",0, WHITE)
    sizeT = text.get_rect()
    menu_window.blit(text,((wnd_w-138-buttonToPlay_w-sizeT[2])/2, 500))
    text = smallText.render("Play with computer",0, WHITE) 
    sizeT = text.get_rect() 
    menu_window.blit(text,((wnd_w+138+buttonToPlay_w-sizeT[2])/2, 500))

    # display
    currentWind = menuWind
    print(f"currentWind = {currentWind}")
    surface.blit(menu_window, (0, 0))
    pg.display.update()

def display_work_wind(lable):
    global currentWind
    global buts_SUBMIT_top, buttonToSUBMIT_h, buttonToSUBMIT_w
    surface.blit(work_window,(0, 0))
    pg.display.update()
    # label
    label = bigText.render(lable,0, WHITE)
    sizeT = label.get_rect()  
    work_window.blit(label,((wnd_w-sizeT[2])/2, 150))

    # SUBMIT BUTTON
    buts_SUBMIT_top = 550
    buttonToSUBMIT_h = 65
    buttonToSUBMIT_w = 180
    buttonToPlay = pg.Rect((wnd_w-buttonToSUBMIT_w)/2, buts_SUBMIT_top,\
                    buttonToSUBMIT_w, buttonToSUBMIT_h)
    pg.draw.rect(work_window, DARK_BLUE,  buttonToPlay, border_radius=20, )
    pg.draw.rect(work_window, (0, 0, 40), buttonToPlay, border_radius=20, width=3)
    pg.draw.rect(work_window, (0, 0, 30), buttonToPlay, border_radius=20, width=2)
    pg.draw.rect(work_window, (0, 0, 20), buttonToPlay, border_radius=20, width=1)
    # buttons text
    text = smallText.render("SUBMIT",0, WHITE)
    sizeT = text.get_rect()
    work_window.blit(text,((wnd_w-sizeT[2])/2, buts_SUBMIT_top+2+((buttonToSUBMIT_h-sizeT[3])/2))) 
    currentWind = workWind
    print(f"currentWind = {currentWind}")
    surface.blit(work_window, (0, 0))
    pg.display.update()

def display_resolt_wind(who):
    global currentWind
    resolt_window = pg.Surface(size=(wnd_w,wnd_h),depth=32)
    resolt_window.fill(DARK_BLUE)
    # label
    label = bigText.render(who+" win!!!",0, WHITE)
    sizeT = label.get_rect()  
    resolt_window.blit(label,((wnd_w-sizeT[2])/2, (wnd_h-sizeT[3])/2)) 
    # display
    currentWind = resoltWind
    print(f"currentWind = {currentWind}")
    surface.blit(resolt_window, (0, 0))
    pg.display.update()


# bool funcs
def corsor_in_play_button(x, y):
    global buttonToStart_w, buttonToStart_h
    return (wnd_w+buttonToStart_w)/2>x>(wnd_w-buttonToStart_w)/2 \
        and (wnd_h+buttonToStart_h)/2>y>(wnd_h-buttonToStart_h)/2

def corsor_in_play_with_friend_button(x, y):
    global buttonToPlay_h, buttonToPlay_w, but_1play_left, but_2play_left, buts_play_top
    return but_1play_left < x < (but_1play_left + buttonToPlay_w) \
        and buts_play_top < y < buts_play_top + buttonToPlay_h

def corsor_in_play_with_computer_button(x, y):
    global buttonToPlay_h, buttonToPlay_w, but_1play_left, but_2play_left, buts_play_top
    return but_2play_left < x < (but_2play_left + buttonToPlay_w) \
        and buts_play_top < y < buts_play_top + buttonToPlay_h

def cursor_in_match_block(x, y):
    return  AxORleft < x < Bx and AyORtop < y < By

def corsor_in_submit_button(x, y):
    global buts_SUBMIT_top, buttonToSUBMIT_h, buttonToSUBMIT_w
    return (wnd_w - buttonToSUBMIT_w)/2 < x < (wnd_w + buttonToSUBMIT_w)/2 \
        and  buts_SUBMIT_top < y < buts_SUBMIT_top + buttonToSUBMIT_h

# computer make choice
def computerMakeTurn():
    global compyter_choice_list
    global qeue, choice, choice_list
    computer_choice = 3 - choice
    compyter_choice_list =[]
    mixed_id_list = [i for i in range(len(matches_existing)-1)]
    random.shuffle(mixed_id_list)
    print(mixed_id_list)
    # computer desision
    if computer_choice == 2:
        # for i in range(len(mixed_id_list)-1):
        for i in mixed_id_list:
            if matches_existing[i] == 1 and matches_existing[i+1] == 1:
                compyter_choice_list.append(i)
                compyter_choice_list.append(i+1)
                break
    if len(compyter_choice_list) == 0:
        mixed_id_list = [i for i in range(len(matches_existing))]
        for i in mixed_id_list:
            if matches_existing[i] == 1:
                compyter_choice_list.append(i)
                break
    # del choosen matches 
    for i in compyter_choice_list:
        matches_existing[i] = 0
    # підпалюємо сірники
    computer_make_match_fired()
    # якщо виграв
    if sum(matches_existing) == 0:
        display_resolt_wind(str("Computer"))
        # time.sleep(1)
    else:
        # змінюємо чергу на чергу гравця
        qeue*=-1
        turn = qeue_dict_с[qeue]
        print(turn)
        printinng_game_going(turn)

# processing...
def processingEvents():
    global current_mod, currentWind, menu_window, matches_existing, start_window
    global choice, qeue, choice_list
    save_mod = 0
    while True:
        # взяти подію
        event = pg.event.wait()
        print(event)
        # взяти координати курсора
        x, y = pg.mouse.get_pos()


        # закрити вікно
        if event.type == pg.QUIT or ((event.type == pg.KEYUP) and ((event.scancode == 41) and \
        (event.key == 27) or (event.scancode == 20) and (event.key == 113))):
            print('Bye!!!')
            quit()

        # почати гру заново                            and (event.scancode == 22)
        elif  (event.type == pg.KEYUP) and (event.key == 115):
            print("start")
            surface.blit(start_window, (0, 0))
            pg.display.update()
            current_mod = 0
            currentWind = startWind
            matches_existing = [1, 1, 1,
                                1, 1, 1,
                                1, 1, 1,]
            choice = 0
            choice_list = []
            qeue = 1
            work_window.fill(DARK_GRAY)
            print_start_matches()


        # перемикач режиму гри при натисненні 'м'      and (event.scancode == 16)
        elif (event.type == pg.KEYUP) and (event.key == 109):
            if current_mod == c:
                pg.display.set_caption("Keiles " + p)
                current_mod = p
            elif current_mod == p:
                pg.display.set_caption("Keiles " + c)
                current_mod = c
            
        # перемикач режиму гри при натисненні 'o'      and (event.scancode == 18)
        elif (event.type == pg.KEYUP) and (event.key == 111):
            surface.blit(menu_window, (0, 0))
            pg.display.update()
            currentWind = menuWind
            save_mod = current_mod
            current_mod = 0
        
        # перемикач режиму гри при натисненні 'p'       and (event.scancode == 19)
        elif (event.type == pg.KEYUP) and (event.key == 112):
            surface.blit(work_window, (0, 0))
            pg.display.update()
            currentWind = work_window
            current_mod = save_mod
        

        # computer_play_mod 
        elif current_mod == c:
            print("current_mod == p!!!!!!!")
            # поки є сірники:
            if sum(matches_existing) > 0 :
                # якщо натиснуто submit
                if ((event.type == pg.MOUSEBUTTONUP) and (event.button == 1))\
                and corsor_in_submit_button(x, y):
                    print("tou tap submit")

                    # actions if any erorr
                    if choice == 0:
                        # erorr declaration
                        print("Виберіть хочаб 1 сірник!")
                        print_game_erorr("Choose at least 1 match!")
                        # display prev
                        print_start_matches()
                        pg.display.update()
                    elif choice > 2:
                        # erorr declaration
                        print("Виберіть не більше 2-ох сірників!")
                        print_game_erorr("Choose no more than 2 matches!")
                        # обнулення вибору користувача
                        choice = 0
                        choice_list = []
                        # display prev
                        print_start_matches()
                        pg.display.update()
                    elif choice == 2 and int(abs(choice_list[0]-choice_list[1])) != 1:
                        # erorr declaration
                        print("Виберіть  2 СУСІДНІ сірники!")
                        print_game_erorr("Choose 2 neighboring matches!")
                        # обнулення вибору користувача
                        choice = 0
                        choice_list = []
                        # display prev
                        print_start_matches()
                        pg.display.update()

                    # actions if all correct
                    else:
                        for i in choice_list:
                            matches_existing[i] = 0
                        make_match_fired()
                        qeue*=-1
                        # check if it was the last match
                        if sum(matches_existing) == 0:
                            winner = "Player" if qeue == -1 else "Computer"
                            display_resolt_wind(str(winner))
                            choice = 0
                            choice_list = []
                            continue

                        turn = qeue_dict_с[qeue]
                        print(turn)
                        printinng_game_going(turn)
                        computerMakeTurn() # черга комп'ютера
                        choice = 0
                        choice_list = []
                        
                        
                # якщо натиснуто лівою кнопкою миші у блоці сірників
                if ((event.type == pg.MOUSEBUTTONUP) and (event.button == 1))\
                    and cursor_in_match_block(x, y):
                    # визначаємо сірник
                    id = define_match_id(x)
                    print(f"you tap on a match № {id+1}!")
                    # запалюємо та зберігаємо
                    fire_it(id)
                    choice +=1
                    choice_list.append(id)               
                 

        # 2_players_play_mod 
        elif current_mod == p:
            print("current_mod == p!!!!!!!")
            # поки є сірники:
            if sum(matches_existing) > 0 :
                # якщо натиснуто submit
                if ((event.type == pg.MOUSEBUTTONUP) and (event.button == 1))\
                and corsor_in_submit_button(x, y):
                    print("tou tap submit")

                    # actions if any erorr
                    if choice == 0:
                        # erorr declaration
                        print("Виберіть хочаб 1 сірник!")
                        print_game_erorr("Choose at least 1 match!")
                        # display prev
                        print_start_matches()
                        pg.display.update()
                    elif choice > 2:
                        # erorr declaration
                        print("Виберіть не більше 2-ох сірників!")
                        print_game_erorr("Choose no more than 2 matches!")
                        # обнулення вибору користувача
                        choice = 0
                        choice_list = []
                        # display prev
                        print_start_matches()
                        pg.display.update()
                    elif choice == 2 and int(abs(choice_list[0]-choice_list[1])) != 1:
                        # erorr declaration
                        print("Виберіть  2 СУСІДНІ сірники!")
                        print_game_erorr("Choose 2 neighboring matches!")
                        # обнулення вибору користувача
                        choice = 0
                        choice_list = []
                        # display prev
                        print_start_matches()
                        pg.display.update()

                    # actions if all correct
                    else:
                        for i in choice_list:
                            matches_existing[i] = 0
                        make_match_fired()
                        qeue*=-1
                        # check if it was the last match
                        if sum(matches_existing) == 0:
                            winner = "First player" if qeue == -1 else "Second player"
                            display_resolt_wind(str(winner))
                            choice = 0
                            choice_list = []
                            continue

                        turn = qeue_dict_p[qeue]
                        print(turn)
                        printinng_game_going(turn)
                        choice = 0
                        choice_list = []
                        
                        
                # якщо натиснуто лівою кнопкою миші у блоці сірників
                if ((event.type == pg.MOUSEBUTTONUP) and (event.button == 1))\
                    and cursor_in_match_block(x, y):
                    # визначаємо сірник
                    id = define_match_id(x)
                    print(f"you tap on a match № {id+1}!")
                    # запалюємо та зберігаємо
                    fire_it(id)
                    choice +=1
                    choice_list.append(id)               
                
    
        # none-mod
        elif current_mod == 0:
            print(f"currentWind - {currentWind}")
            
            print(f"mouse.get_pos = {x} and {y}")
            # якщо натиснуто лівою кнопкою миші на кнопці 'play' у стартовому вікні
            if  ((event.type == pg.MOUSEBUTTONUP) and (event.button == 1))\
                and currentWind==startWind and corsor_in_play_button(x, y):
                display_menu_wind()
                currentWind = menuWind

            # якщо натиснуто лівою кнопкою миші на кнопці 'Play with friend' у  вікні-меню
            if  ((event.type == pg.MOUSEBUTTONUP) and (event.button == 1))\
                and currentWind==menuWind and corsor_in_play_with_friend_button(x, y):
                current_mod = p
                pg.display.set_caption("Keiles " + p)
                display_work_wind("First player turn...")
                print("corsor_in_play_with_friend_button")
                currentWind = workWind

            # якщо натиснуто лівою кнопкою миші на кнопці 'Play with computer' у  вікні-меню
            if  ((event.type == pg.MOUSEBUTTONUP) and (event.button == 1))\
                and currentWind==menuWind and corsor_in_play_with_computer_button(x, y):
                current_mod = c
                pg.display.set_caption("Keiles " + c)
                display_work_wind("Player turn...")
                print("corsor_in_play_with_computer_button")
                currentWind = workWind

            print("let`s play!")  



# ІНІЦІАЛІЗАЦІЯ
# colors
BLACK = (0, 0, 0)
DARK_BLUE = (0,0,50)
DARK_GRAY = (44,44,44)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# ініціалізація графіки 
wnd_h = 700
wnd_w = 1100
pg.init()
surface = pg.display.set_mode(size=(wnd_w,wnd_h),depth=32)
surface.fill(DARK_GRAY)
pg.display.set_caption("Keiles")
pg.display.update()
# зміна іконки вікна
wnd_icon = pg.image.load('game-icon.png')
pg.display.set_icon(wnd_icon)

# text 
bigText = pg.font.SysFont("inter", 50)
mediumText = pg.font.SysFont("inter", 36)
smallText = pg.font.SysFont("inter", 30)

# налаштування режимів гри
c = "with computer"
p = "with another player"
zero = 0
current_mod = zero

# відслідкування вікон
startWind = 0
menuWind = 1
workWind = 2
resoltWind = 3
currentWind = startWind


# data about matches
# координати лівої верхньої та правої нижньої точок блоку сірників
AyORtop = 200
AxORleft = 280
By = 450
Bx = 910
matches_existing = [1, 1, 1,
                    1, 1, 1,
                    1, 1, 1,]
choice = 0
choice_list = []
qeue = 1
qeue_dict_p = {1:"First player turn...", \
            -1:"Second player turn..."}

qeue_dict_с = {1:"Player turn...", \
            -1:"Computer turn..."}


# підготовка ігрової поверхні
work_window = pg.Surface(size=(wnd_w,wnd_h),depth=32)
work_window.fill(DARK_GRAY)
print_start_matches()

# відображення стартового вікна
display_start_wind()

# обробка подій миші та клавіатури
processingEvents()