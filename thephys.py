import sys, pygame

'''Define constantes do programa'''
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

def pygame_init(screen_size: tuple) -> tuple:
    ''' Configuração inicial do PyGame.'''
    
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(screen_size)
    print(type(clock), type(screen))
    return clock, screen

def main_loop():
    ''' Ponto de entrada no loop principal'''

    global paused
    while True:
        clock.tick(FPS)
        check_events()
        if not paused:
            pass
            
def check_events():
    ''' Todos os eventos são verificados nessa função.'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
clock, screen = pygame_init(screen_size)
paused = False
main_loop()