import numpy as np
import pygame
import sys 

#Initializing
pygame.init()
screen = pygame.display.set_mode((1200,750))
clock = pygame.time.Clock()

#Outside Loop
#Defining space and time:
x = np.linspace(-50,50,100)    
v = 0.000001
c = 1 #natural units
t = np.linspace(-50,50,100) 

#Relativity effects: 
ruler = 30      #units
watch = 60      #seconds

#Slider set up:
slider_x = 424
slider_y = 100
slider_width = 3
handle_x = 424
handle_y = 100
handle = (handle_x,handle_y)
slider_end = slider_x + 350
dragging = False

#Hovering mechanism
l_graph = pygame.Rect(10,270,585,470)
l_hovering = False

r_graph = pygame.Rect(605,270,585,470)
r_hovering = False

p_x, p_y = 0, 0

#Slider conversion:
def slider_to_velocity(handle_x,slider_x):
    slider_length = 350
    velocity_window = 0.9999999999
    slider_scale = velocity_window / slider_length

    velocity = (handle_x - slider_x) * slider_scale
    velocity = max(0.0000000001, velocity) 

    return(velocity)

def lorentz_graph(x,t):
    max_length = 100
    max_width = 100

    pixel_length = 585
    pixel_width = 470

    scale_x = pixel_length / max_length
    scale_y = pixel_width / max_width

    pixel_x_l = 303 + (x * scale_x)
    pixel_y_l = 505 - (t * scale_y)

    return(pixel_x_l,pixel_y_l)

def simultaneity_graph(x ,t):
    max_length = 100 
    max_width = 100

    pixel_length = 585
    pixel_width = 470

    scale_x = pixel_length / max_length
    scale_y = pixel_width / max_width

    pixel_x_s = 898 + (x * scale_x)
    pixel_y_s = 505 - (t * scale_y)

    return(pixel_x_s,pixel_y_s)
     
#Simultaneous events in rest frame:
event_1_x, event_1_t = -25,25
event_2_x, event_2_t = 0,25
event_3_x, event_3_t = 25,25
event_1 = lorentz_graph(event_1_x,event_1_t)
event_2 = lorentz_graph(event_2_x,event_2_t)
event_3 = lorentz_graph(event_3_x,event_3_t)

#Text:
heading = pygame.font.SysFont('Times New Roman',30)
norm_text =pygame.font.SysFont('Times New Roman', 20)
legend = pygame.font.SysFont('Times New Roman', 15)


#Inside Loop
while True : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT : 
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_ESCAPE :
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

        #Lorentz Hovering:
        if event.type == pygame.MOUSEMOTION :
            if l_graph.collidepoint(event.pos[0],event.pos[1]):
                l_hovering = True
                p_x, p_y = event.pos[0], event.pos[1]

            else:
                l_hovering = False

        if event.type == pygame.MOUSEMOTION : 
            if r_graph.collidepoint(event.pos[0], event.pos[1]):
                r_hovering = True
                p_x, p_y = event.pos[0], event.pos[1]

            else:
                r_hovering = False
                    
    v = slider_to_velocity(handle_x, slider_x)     #in terms of c  

    #Drawing User Interface
    pygame.draw.rect(screen,'#0f121e',(0,0,1200,750))
    pygame.draw.rect(screen, '#6b6b6b',(10,10,1180,250), border_radius=15)
    pygame.draw.rect(screen,'#6b6b6b',(10,270,585,470), border_radius=15)
    pygame.draw.rect(screen,'#6b6b6b',(605,270,585,470), border_radius=15)
    pygame.draw.line(screen,'white',(393,20),(393,240),2)
    pygame.draw.line(screen,'white',(806,20),(806,240),2)
    pygame.draw.line(screen,'white',(30,55),(1170,55),2)
    pygame.draw.rect(screen,"#3c3c3c",(400,115,400,130), border_radius=15)
    pygame.draw.rect(screen, "#3c3c3c",(40,65,343,180), border_radius=15)
    pygame.draw.rect(screen, "#3c3c3c",(816,70,344,175), border_radius=15)

    #Drawing slider
    pygame.draw.line(screen,'white',(slider_x,slider_y),((slider_end),slider_y),slider_width)
    pygame.draw.circle(screen,"#01F531",(handle_x,(slider_y+1)),8)

    #Length contraction:
    #def lorentz_transformation(x,v,t):  
    gama = 1 / (np.sqrt(1 - np.square(v)))
    x_r = 100 * (np.sqrt((1 + (v**2)) / (1 - (v**2))))
    t_r = 100 * (np.sqrt((1 + (v**2)) / (1 - (v**2))))

    x_r_h = gama * (x - (v*t))
    t_r_h = gama * (t - ((v*x)/c))


    length_cont = abs(x_r)
    length_cont_str = str(round(length_cont,5))

    time_dil = abs(t_r)
    time_dil_str = str(round(time_dil,5))

    lorentz_f = str(round(gama,5))

    #Change in distance:
    delta_distance = abs((max(x) - min(x)) - length_cont)
    delta_distance_str = str(round(delta_distance,5))

    #Change in time:
    delta_time = abs((max(t) - min(t)) - time_dil)
    delta_time_str = str(round(delta_time,5))

    #Special relativity effects:
    new_ruler = ruler / gama
    new_watch = watch * gama

    length_x, pix_length = 100, 585
    scale = pix_length / length_x
    pix_ruler = round((ruler * scale),0)
    pix_new_ruler = round((new_ruler * scale))
    
    
    #Plotting:
    pygame.draw.line(screen, "#c800ffff", (333,455),((333 + pix_ruler),455), 5)
    pygame.draw.line(screen, '#c800ffff', (928,455),((928 + pix_new_ruler),455), 5)

    #Simultaneity of the events:
    transformed_event1_x,transformed_event1_t = (gama * (event_1_x - (v * event_1_t))) , (gama * (event_1_t - ((v * event_1_x) / c)))
    transformed_event2_x, transformed_event2_t = (gama * (event_2_x - (v * event_2_t))) , (gama * (event_2_t - ((v * event_2_x) / c)))
    transformed_event3_x, transformed_event3_t = (gama * (event_3_x - (v * event_3_t))) , (gama * (event_3_t - ((v * event_3_x) / c)))

    transformed_event1 = simultaneity_graph(transformed_event1_x, transformed_event1_t)
    transformed_event2 = simultaneity_graph(transformed_event2_x, transformed_event2_t)
    transformed_event3 = simultaneity_graph(transformed_event3_x, transformed_event3_t)

    #Graphing:
    #Lorentz Y axis grid
    for j in range(-50 , 50 , 10):
        for i in range(0, 99):
            start = lorentz_graph(j,t[i])
            end = lorentz_graph(j, t[i + 1])
            pygame.draw.line(screen, "#a8a8a8", start, end, 1)

    #Lorentz x axis grid
    for i in range(-50, 50,10):
        for j in range(-50,50):
            start = lorentz_graph(x[j],i)
            end = lorentz_graph(x[j +1], i)
            pygame.draw.line(screen, "#a8a8a8", start, end, 1)

    #Lorentz y-axis
    for i in range(0, 99):
            start = lorentz_graph(x[49],t[i])
            end = lorentz_graph(x[49], t[i + 1])
            pygame.draw.line(screen, "white", start, end, 3)

    #Lorentz x-axis
    for j in range(-50,50):
            start = lorentz_graph(x[j],t[49])
            end = lorentz_graph(x[j+1], t[49])
            pygame.draw.line(screen, "white", start, end, 3)

    #Simultaneity  y axis grid
    for j in range(-50 , 50 , 10):
        for i in range(0, 99):
            start = simultaneity_graph(j,t[i])
            end = simultaneity_graph(j, t[i + 1])
            pygame.draw.line(screen, "#a8a8a8", start, end, 1)

    #Simultaneity x axis grid
    for i in range(-50, 50,10):
        for j in range(-50,50):
            start = simultaneity_graph(x[j],i)
            end = simultaneity_graph(x[j +1], i)
            pygame.draw.line(screen, "#a8a8a8", start, end, 1)

    #Simultaneity y-axis
    for i in range(0, 99):
            start = simultaneity_graph(x[49],t[i])
            end = simultaneity_graph(x[49], t[i + 1])
            pygame.draw.line(screen, "#00a5ff", start, end, 3)

    #Simultaneity x-axis
    for j in range(-50,50):
            start = simultaneity_graph(x[j],t[49])
            end = simultaneity_graph(x[j+1], t[49])
            pygame.draw.line(screen, "#ff0029", start, end, 3)

    #Events in Rest frame
    pygame.draw.circle(screen,"#3DFFFF",event_1,4)
    pygame.draw.circle(screen,'#3DFFFF',event_2,4)
    pygame.draw.circle(screen,'#3DFFFF',event_3,4)

    #Transformed events:
    screen.set_clip(pygame.Rect(605,270,585,470))
    pygame.draw.circle(screen, '#3DFFFF', transformed_event1, 4)
    pygame.draw.circle(screen, '#3DFFFF', transformed_event2, 4)
    pygame.draw.circle(screen, '#3DFFFF', transformed_event3, 4)
    screen.set_clip(None)

    #Patching
    pygame.draw.line(screen, (0,0,0),(10,270),(10,740) ,2)
    pygame.draw.line(screen, (0,0,0),(10,740),(595,740) ,2)
    pygame.draw.line(screen, (0,0,0),(605,270),(605,740) ,2)
    pygame.draw.line(screen, (0,0,0),(605,740),(1190,740) ,2)

    #Hovering mechanism
    if l_hovering:
        max_length, max_width = 100, 100
        pixel_length, pixel_width = 585, 470

        scale_x = pixel_length / max_length 
        scale_y = pixel_width / max_width 

        h_x = (p_x - 303) / scale_x
        h_y = (505 - p_y) / scale_y

        pygame.draw.rect(screen, 'white',(p_x + 10 ,p_y - 20,110,30), border_radius=15)
        l_coordinates = legend.render(f'({round(h_x,2)}, {round(h_y,2)})', True, (0,0,0))
        screen.blit(l_coordinates, (p_x + 15, p_y - 15))

    if r_hovering:
        max_length = round(abs(x_r_h[99] - x_r_h[0]), 0)
        max_width  = round(abs(t_r_h[99] - t_r_h[0]), 0)
        pixel_length, pixel_width = 585, 470

        scale_x = pixel_length / max_length 
        scale_y = pixel_width / max_width 

        h_x = (p_x - 898) / scale_x
        h_y = (505 - p_y) / scale_y

        pygame.draw.rect(screen, 'white',(p_x + 10 ,p_y - 20,110,30), border_radius=15)
        l_coordinates = legend.render(f'({round(h_x,2)}, {round(h_y,2)})', True, (0,0,0))
        screen.blit(l_coordinates, (p_x + 15, p_y - 15))

    #Lorentz Transformation of Minkowski Digrams:
    theta = np.arctan(v)
    x_new = (np.tan(theta)) * x
    t_new = (np.tan(theta)) * t

    #New world line
    for i in range(0,99):
        start = lorentz_graph(x[i],x_new[i])
        end = lorentz_graph(x[i+1],x_new[i+1])
        screen.set_clip(pygame.Rect(10,270,585,470))
        pygame.draw.line(screen,'#ff0029',start,end,2)
        screen.set_clip(None)

    for j in range(0,99):
        start = lorentz_graph(t_new[j],t[j])
        end = lorentz_graph(t_new[j+1], t[j+1])
        screen.set_clip(pygame.Rect(10,270,585,470))
        pygame.draw.line(screen, '#00a5ff', start, end, 2)
        screen.set_clip(None)

    #Legend:
    pygame.draw.rect(screen, '#3c3c3c', (17,597,256,136), border_radius=15)
    pygame.draw.rect(screen,'white', (20,600,250,130),border_radius = 15)

    #Text Display:
    #Headings:
    lorentz_heading = heading.render("Lorentz Transformation",True,(0,0,0))
    screen.blit(lorentz_heading,(55,15))

    velocity_heading = heading.render("Velocity & its Effects",True,(0,0,0))
    screen.blit(velocity_heading,(473,15))

    simultaneity_heading = heading.render("Simultaneity",True,(0,0,0))
    screen.blit(simultaneity_heading,(926,15))

    title_length = norm_text.render('Transformed space axis:', True, 'white')
    screen.blit(title_length,(60,80))
    text_length = norm_text.render(length_cont_str,True,'white')
    screen.blit(text_length,(270,80))

    title_time = norm_text.render('Transformed time axis:', True, 'white')
    screen.blit(title_time,(60,105))
    text_time = norm_text.render(time_dil_str,True,'white')
    screen.blit(text_time,(270,105))
    
    title_gama = norm_text.render('Lorentz factor:', True, 'white')
    screen.blit(title_gama,(60,130))
    text_gama = norm_text.render(lorentz_f,True,'white')
    screen.blit(text_gama,(270,130))

    title_change_dist = norm_text.render('Change in space axes:',True,'white')
    screen.blit(title_change_dist,(60,155))
    text_change_dist = norm_text.render(delta_distance_str,True,'white')
    screen.blit(text_change_dist,(270,155))

    title_change_time = norm_text.render('Change in time axes:',True,'white')
    screen.blit(title_change_time,(60,180))
    text_change_time = norm_text.render(delta_time_str,True,'white')
    screen.blit(text_change_time,(270,180))

    title_velocity = norm_text.render('Velocity (in terms of c):', True, (0,0,0))
    screen.blit(title_velocity,(418,70))
    text_velocity = norm_text.render(str(round(v,5)), True, (0,0,0))
    screen.blit(text_velocity,(618,70))

    title_now_length = norm_text.render('Length contraction: Ruler', True, "#e8e8e8")
    screen.blit(title_now_length, (490, 120))
    title_now_length_2 = norm_text.render(f'Rest frame: {ruler} m', True, '#e8e8e8')
    screen.blit(title_now_length_2, (410, 147))
    title_now_length_3 = norm_text.render(f'Moving frame: {round(new_ruler, 2)} m', True, '#e8e8e8')
    screen.blit(title_now_length_3, (565, 147))

    title_now_watch = norm_text.render('Time dilation: Watch', True, '#e8e8e8')
    screen.blit(title_now_watch, (510,185))
    title_now_watch_2 = norm_text.render(f'Rest frame: {watch} s', True, '#e8e8e8')
    screen.blit(title_now_watch_2, (410,212))
    title_now_watch_3 = norm_text.render(f'Moving frame: {round(new_watch, 2)} s', True, '#e8e8e8')
    screen.blit(title_now_watch_3, (565,212))

    event1_title = norm_text.render('Event 1:', True, '#e8e8e8')
    screen.blit(event1_title, (886,120))
    event2_title = norm_text.render('Event 2:', True, '#e8e8e8')
    screen.blit(event2_title, (886,160))
    event2_title = norm_text.render('Event 3:', True, '#e8e8e8')
    screen.blit(event2_title, (886,200))

    event_heading = norm_text.render('Rest frame coordinates:', True, '#e8e8e8')
    screen.blit(event_heading, (881,85))
    event1_title_val = norm_text.render(str(round(transformed_event1_t, 4)) +' s', True, '#e8e8e8')
    screen.blit(event1_title_val, (976,120))
    event2_title_val = norm_text.render(str(round(transformed_event2_t, 4)) + ' s', True, '#e8e8e8')
    screen.blit(event2_title_val, (976,160))
    event2_title_val = norm_text.render(str(round(transformed_event3_t, 4)) + ' s', True, '#e8e8e8')
    screen.blit(event2_title_val, (976,200))

    event1_label = legend.render('Event 1', True, 'white')
    screen.blit(event1_label, ((event_1[0]-20),(event_1[1]+5)))
    event2_label = legend.render('Event 2', True, 'white')
    screen.blit(event2_label, ((event_2[0]-20),(event_2[1]+5)))
    event3_label = legend.render('Event 3', True, 'white')
    screen.blit(event3_label, ((event_3[0]-20),(event_3[1]+5)))

    screen.set_clip(pygame.Rect(605,270,585,470))
    t_event1_label = legend.render('Event 1', True, 'white')
    screen.blit(t_event1_label, ((transformed_event1[0]-20),(transformed_event1[1]+5)))
    t_event2_label = legend.render('Event 2', True, 'white')
    screen.blit(t_event2_label, ((transformed_event2[0]-20),(transformed_event2[1]+5)))
    t_event3_label = legend.render('Event 3', True, 'white')
    screen.blit(t_event3_label, ((transformed_event3[0]-20),(transformed_event3[1]+5)))
    screen.set_clip(None)

    #Lorentz graph legend:
    lorentz_graph_title = norm_text.render('Lorentz Transfromation of axes', True, 'white')
    screen.blit(lorentz_graph_title, (20,280))
    simultaneity_graph_title = norm_text.render('Moving frame', True, 'white')
    screen.blit(simultaneity_graph_title, (615,280))
    legend_title = norm_text.render("Legend", True, (0,0,0))
    screen.blit(legend_title, (110,605))

    pygame.draw.line(screen,'black',(25,630),(265,630))
    pygame.draw.rect(screen, '#ff0029',(30,640,10,10))
    pygame.draw.rect(screen, '#00a5ff',(30,660,10,10))
    pygame.draw.rect(screen, '#3DFFFF',(30,680,10,10))
    pygame.draw.rect(screen, '#c800ffff',(30,700,10,10))

    space = legend.render('Space axis (metres)', True, (0,0,0))
    screen.blit(space,(50,636))
    time = legend.render('Time axis (seconds)', True, (0,0,0))
    screen.blit(time,(50,656))
    event_title = legend.render('Simultaneous events', True, (0,0,0))
    screen.blit(event_title,(50,676))
    ruler_title = legend.render('Ruler', True, (0,0,0))
    screen.blit(ruler_title,(50,696))

    pygame.display.flip()
    clock.tick(60)