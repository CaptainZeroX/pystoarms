import pygame
import math


fileName = 'fll.rtf'               # variable fileName
myfile = open(fileName, 'w')        # define variable myfile to open the fll.rtf when used in the code


def cmpx(inp):                      # define function cmpx (inp)
    output = (inp * 12) / 2.3        # what is this equation used for ???
    return output


                      # this is to define the function count to use it later .
count = 0


quit = 0
pygame.init()
test = 0
screen = pygame.display.set_mode((1222, 693))            # so this line is to write the size of the output window
background = pygame.image.load('mat.png')                # this one is to choose the background picture
# lines

# Rotation doesn't work if the size is less than 40 * 40 ... so we need to use convert_alpha()

playerimg = pygame.image.load('Midnight.png').convert_alpha()         # image of the robot

# Keyboard control

screen.fill((0, 0, 0))

keys = [False, False, False, False]
position_array = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
angle_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Distance = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lcount = 0
conut_draw = 0
count_new = 0
counter = 0
check = [1, 1]
z = 0

running = True

while running:
    # LOOP 1
    quit = 0
    # title and icon
    pygame.display.set_caption("Graphical mapping")        # caption of the output window

    mx, my = pygame.mouse.get_pos()
    screen.blit(background, (0, 0))
    pygame.display.update()                                 # this is to apply any changes or updates that occur to code

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            z = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            z = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                while check != [0, 0]:
                    M = math.tan(angle_array[conut_draw])
                    c = position_array[conut_draw][1] - M * position_array[conut_draw][0]

                    m = math.tan(angle_array[conut_draw + 1])
                    b = position_array[conut_draw + 1][1] - m * position_array[conut_draw + 1][0]

                    x = (b - c) / (M - m)
                    y = m * x + b
                    if abs(angle_array[conut_draw] * (-1 * (180 / math.pi))) == 90:
                        x = position_array[conut_draw][0]
                        y = m * x + b

                    elif abs(angle_array[conut_draw + 1] * (-1 * (180 / math.pi))) == 90:
                        x = position_array[conut_draw + 1][0]
                        y = M * x + c

                    pygame.draw.line(background, (0, 0, 0), position_array[conut_draw], (x, y), 5)
                    pygame.draw.line(background, (0, 0, 0), (x, y), position_array[conut_draw + 1], 5)
                    Distance[count_new] = str(math.sqrt(((x - position_array[conut_draw][0]) * (x - position_array[conut_draw][0])) + ((y - position_array[conut_draw][1])*(y - position_array[conut_draw][1]))))
                    Distance[count_new + 1] = str(math.sqrt(
                        ((x - position_array[conut_draw+1][0]) * (x - position_array[conut_draw+1][0])) +
                        ((y - position_array[conut_draw+1][1]) * (y - position_array[conut_draw+1][1]))))
                    count_new += 2
                    check = position_array[conut_draw + 2]
                    conut_draw += 1



            if event.key == pygame.K_d:                       # loop for the fll.rtf file
                if event.key == pygame.K_d:
                    correction = 0
                    while Distance[counter] != 0:
                        myfile.write(str(0))
                        myfile.write('\n')
                        myfile.write(Distance[counter])
                        myfile.write('\n')

                        if counter == 0:
                            trg = '0'
                            turn = str(a[counter + 1] - a[counter])
                        else:
                            trg = turn
                            turn = str(a[counter - correction] - a[counter - correction - 1])
                            correction += 1

                        myfile.write(trg)
                        myfile.write('\n')

                        myfile.write(str(1))
                        myfile.write('\n')
                        myfile.write(turn)
                        myfile.write('\n')

                        counter += 1
                        myfile.write(str(2))
                        myfile.write('\n')
                        myfile.write(Distance[counter])
                        myfile.write('\n')
                        trg = turn
                        myfile.write(trg)
                        myfile.write('\n')
                        counter += 1

                myfile.close()

        if z == 1:
            # rotate only when Mouse button Down
            while z == 1 or quit == 0:

                if z == 1:
                    # Rotation with mouse
                    Mouse_position = pygame.mouse.get_pos()
                    angle = math.atan2(Mouse_position[1] - my, Mouse_position[0] - mx)
                    angle360 = 0 - angle * 180 / math.pi
                    angle360_string = str(angle360)
                    rotation = pygame.transform.rotate(playerimg, angle360)
                    position_new = [mx - rotation.get_rect().width / 2, my - rotation.get_rect().height / 2]

                # title = angle
                pygame.display.set_caption(angle360_string)
                # check if the mouse button is up
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        z = 0
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            keys[0] = True

                        elif event.key == pygame.K_LEFT:
                            keys[1] = True

                        elif event.key == pygame.K_DOWN:
                            keys[2] = True

                        elif event.key == pygame.K_RIGHT:
                            keys[3] = True

                        elif event.key == pygame.K_q:
                            quit = 1
                            angle_error = angle360 - math.atan2(cmpx(4.65), cmpx(3.5)) * 180 / math.pi
                            position_array[count] = [mx - math.sqrt(cmpx(4.65) * cmpx(4.65) + cmpx(3.5) * cmpx(3.5)) * math.cos(angle_error * math.pi / 180),
                                                    my + math.sqrt(cmpx(4.65) * cmpx(4.65) + cmpx(3.5) * cmpx(3.5)) * math.sin(angle_error * math.pi / 180)]

                            angle_array[count] = angle
                            a[count] = angle360
                            count += 1

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP:
                            keys[0] = False
                        elif event.key == pygame.K_LEFT:
                            keys[1] = False
                        elif event.key == pygame.K_DOWN:
                            keys[2] = False
                        elif event.key == pygame.K_RIGHT:
                            keys[3] = False
                if keys[0]:
                    position_new[1] -= 0.3
                    my -= 0.3

                elif keys[2]:
                    position_new[1] += 0.3
                    my += 0.3
                if keys[1]:
                    position_new[0] -= 0.3
                    mx -= 0.3
                elif keys[3]:
                    position_new[0] += 0.3
                    mx += 0.3
                screen.blit(background, (0, 0))
                screen.blit(rotation, position_new)
                pygame.display.update()

    try:
        background.blit(rotation, position_new)
    except:
        continue
