import numpy as np
import pygame
import sys

#Initializing
pygame.init()
screen = pygame.display.set_mode((1200,690))
clock = pygame.time.Clock()

#Outside loop
x = np.linspace(-10,10,100)     #coordinate space
t = np.linspace(-10,10,100)     #time space ---> ct

#Sliderset up:
slider_x = 50
slider_y = 400
slider_width = 3
handle_x = 50
handle_y = 400
handle = (handle_x,handle_y)
slider_end = slider_x + 400
dragging = False

#Slider conversion:
def slider_to_velocity(handle_x,slider_x):
    slider_length = 400
    velocity_window = 0.9999999999
    slider_scale = velocity_window / slider_length

    velocity = (handle_x - slider_x) * slider_scale

    return(velocity)

def math_to_pixel(x, t):
    math_width = 20     #max(x) - min(x)
    math_height = 20    #max(t) - min(t)

    pixel_width = 650       #Defining the right square(worldline plot) graph
    pixel_height = 650

    scale_x = (pixel_width / math_width)
    scale_y = (pixel_height / math_height)

    pixel_x = 855 + (x * scale_x)   #Defining the origin of that graph
    pixel_y = 345 - (t * scale_y)   #(855,345) is the position of origin of that graph

    return(pixel_x,pixel_y)

#Setting up font
heading = pygame.font.SysFont('Times New Roman', 30)
norm_text =pygame.font.SysFont('Times New Roman', 20)
labelling = pygame.font.SysFont('Times New Roman', 15)

#Inside loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Slider
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (abs((event.pos[0]) - handle_x) < 10):
                if (abs((event.pos[1]) - handle_y) < 10):
                    dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False

        if event.type == pygame.MOUSEMOTION:
            if dragging:
                 handle_x = max(slider_x, min((slider_end),event.pos[0]))

    v = slider_to_velocity(handle_x, slider_x)     #in terms of c  

    screen.fill((255,255,255))
    pygame.draw.rect(screen, "#d3d3d4", (530,20,650,650))
    pygame.draw.rect(screen, '#d3d3d4', (20,20,490,650))
    pygame.draw.rect(screen, 'white', (550,30,200,80))
    pygame.draw.rect(screen, '#ff0029', (600,60,10,10))
    pygame.draw.rect(screen, '#00a5ff', (600,80,10,10))


    #World line:
    theta = np.arctan(v)
    x_new = (np.tan(theta)) * x
    t_new = (np.tan(theta)) * t

    #Length contraction:
    #def lorentz_transformation(x,v,t):  
    gama = 1 / (np.sqrt(1 - np.square(v)))
    c = 299792458
    x_r = gama * (x - (v*t))
    t_r = gama * (t - ((v*x)/c))

    length_cont = x_r[99] - x_r[0]
    length_cont_str = str(round(length_cont,5))

    time_dil = t_r[99] - t[0]
    time_dil_str = str(round(time_dil,5))

    lorentz_f = str(round(gama,5))

    #Change in distance:
    delta_distance = (max(x) - min(x)) - length_cont
    delta_distance_str = str(round(delta_distance,5))

    #Change in time:
    delta_time = abs((max(t) - min(t)) - time_dil)
    delta_time_str = str(round(delta_time,5))

    #X-axis
    for i in range(0,99):
        start = math_to_pixel(x[i],t[49])
        end = math_to_pixel(x[i+1], t[49])
        pygame.draw.line(screen, 'black', start, end, 1)
    
    #Y-axis
    for j in range(0,99):
        start = math_to_pixel(x[49],t[j])
        end = math_to_pixel(x[49], t[j+1])
        pygame.draw.line(screen, 'black', start, end, 1)

    #New world line
    for i in range(0,99):
        start = math_to_pixel(x[i],x_new[i])
        end = math_to_pixel(x[i+1],x_new[i+1])
        pygame.draw.line(screen,'#ff0029',start,end,2)

    for j in range(0,99):
        start = math_to_pixel(t_new[j],t[j])
        end = math_to_pixel(t_new[j+1], t[j+1])
        pygame.draw.line(screen, '#00a5ff', start, end, 2)

    #Drawing slider
    pygame.draw.line(screen,'white',(slider_x,slider_y),((slider_end),slider_y),slider_width)
    pygame.draw.circle(screen,'#026115',(handle_x,(slider_y+1)),8)

    #Displaying texts
    text_topic = heading.render('Lorentz Transformation:',True,(0,0,0))
    screen.blit(text_topic, (120, 20))

    title_length = norm_text.render('Length Contraction:', True, (0,0,0))
    screen.blit(title_length,(25,90))
    text_length = norm_text.render(length_cont_str,True,(0,0,0))
    screen.blit(text_length,(200,90))

    title_time = norm_text.render('Time dilation:', True, (0,0,0))
    screen.blit(title_time,(25,130))
    text_time = norm_text.render(time_dil_str,True,(0,0,0))
    screen.blit(text_time,(200,130))
    
    title_gama = norm_text.render('Lorentz factor:', True, (0,0,0))
    screen.blit(title_gama,(25,170))
    text_gama = norm_text.render(lorentz_f,True,(0,0,0))
    screen.blit(text_gama,(200,170))

    title_change_dist = norm_text.render('Change in distance:',True,(0,0,0))
    screen.blit(title_change_dist,(25,210))
    text_change_dist = norm_text.render(delta_distance_str,True,(0,0,0))
    screen.blit(text_change_dist,(200,210))

    title_change_time = norm_text.render('Dilation in time:',True,(0,0,0))
    screen.blit(title_change_time,(25,250))
    text_change_time = norm_text.render(delta_time_str,True,(0,0,0))
    screen.blit(text_change_time,(200,250))

    title_velocity = norm_text.render('Velocity (in terms of c):', True, (0,0,0))
    screen.blit(title_velocity,(50,370))
    text_velocity = norm_text.render(str(round(v,5)), True, (0,0,0))
    screen.blit(text_velocity,(250,370))

    legend = labelling.render('Legend:', True, (0,0,0))
    screen.blit(legend,(555,35))
    x_axis = labelling.render('x-axis:',True,(0,0,0))
    screen.blit(x_axis,(555,55))
    y_axis = labelling.render('y-axis:',True,(0,0,0))
    screen.blit(y_axis,(555,75))

    space_label = labelling.render('Space coordinates (x)',True,(0,0,0))
    screen.blit(space_label,(615,55))
    time_label = labelling.render('Time coordinates (ct)',True,(0,0,0))
    screen.blit(time_label,(615,75))

    pygame.display.flip()
    clock.tick(60)



