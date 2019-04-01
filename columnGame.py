#STUTIRANA
#ID:85039361
import pygame
import gs
import random
ROWS=13
COLS=6
FROZEN= 0
FALLING=1
LANDED=2
MATCHED=3
NONE=4
EMPTY=' '
BACKGROUND = pygame.Color(255,255,255)
GRAY=pygame.Color(142, 138, 141)
BLACK=pygame.Color(5,5,5)
R=pygame.Color(238,44,44)#red
O=pygame.Color(255,153,18)#orange
Y=pygame.Color(255,215,0)#yellow
G=pygame.Color(34,139,34)#green
B=pygame.Color(0,154,154)#blue
P=pygame.Color(159,121,238)#purple
X=pygame.Color(108, 12, 140)#greenishblue
COLORS= ['R','O','Y','G','B','P','X']
COLORS_DICT={'R':R,
             'O':O,
             'Y':Y,
             'G':G,
             'B':B,
             'P':P,
             'X':X}
class Columns_Game():
    def __init__(self):
        self._running = True
        self._gameState = gs.gameState(ROWS,COLS)
        self.num_faller =0
        
    def run(self) -> None:
        '''
        this will loop and make a resizable surface that initializes a white background
        '''
        pygame.init()#initial pygame
        pygame.display.set_mode((360,780), pygame.RESIZABLE)#this will allow the window to be resiazable
        surface = pygame.display.get_surface()
        surface.fill(BACKGROUND)
        clock = pygame.time.Clock()
        time_counter = 0
        self._gameState.empty_board()
        while self._running:
            self._gameState.changeState_adv()
            time_counter += clock.tick()
            self._generate_faller()
            surface = pygame.display.get_surface()
            surface.fill(BACKGROUND)     
            if time_counter >1000:
                self._gameState.advance()
                time_counter=0
            if self._gameState.faller._state == FROZEN:
                self._gameState.check_matches()
            self._print_board()
            self._running = not self._gameState.check_game_over()
            self._process_move()
        pygame.quit()
    
    def _generate_faller(self):
        '''
        in case we haven't made a faller, make one. If we have made a faller, check if the last is frozen and then make a faller

        '''
        if self.num_faller ==0:
            cols = random.randint(1,COLS)
            block = [random.choice(COLORS),random.choice(COLORS),random.choice(COLORS)]
            self._gameState.create_faller(cols,block)
            self.num_faller+=1
        elif self._gameState.get_turn()>1 and self._gameState.faller.get_state()==FROZEN:
            cols = random.randint(1,COLS)
            block = [random.choice(COLORS),random.choice(COLORS),random.choice(COLORS)]
            self._gameState.create_faller(cols,block)
            self.num_faller+=1
    def _quit_game(self)->None:
        '''
        it makes running false which quits the game
        '''
        self._running = False
    def _move_jewel(self,event)->None:
        '''
        given a certain key is pressed it shifts or rotates
        '''
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self._gameState.shift_faller(1)
        if keys[pygame.K_RIGHT]:
            self._gameState.shift_faller(0)
        if keys[pygame.K_SPACE]:
            self._gameState.rotate_faller()
            self._gameState._drop_board()
    def _process_move(self)->None:
        '''
        This function quits or moves the jewels
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_game()
            elif event.type == pygame.KEYDOWN:
                self._move_jewel(event)
                
    def _block_coord(self,cc,cr)->None:
        '''
        this coverts the coordinates into the width and height of the jewel to draw a rectangle
        '''
        x=60*cc
        y=60*cr
        return x,y
    def _get_color(self,jwl)->None:
        '''
        this gets the jewel color
        '''
        return COLORS_DICT[jwl.get_color()]
    def _print_board(self)->None:
        '''
        this prints the game board and resets it
        '''
        surface = pygame.display.get_surface()
        for row in range(ROWS):
            for col in range(COLS):
                if type(self._gameState.board[col][row])!=str:
                    x,y=self._block_coord(col,row)
                    if self._gameState.board[col][row]._get_state() == FROZEN:
                        pygame.draw.rect(surface, self._get_color(self._gameState.board[col][row]), (x,y,60,60), 0)
                        pygame.draw.rect(surface, BLACK, (x,y,60,60), 2)
                    elif self._gameState.board[col][row]._get_state() == LANDED:
                        pygame.draw.rect(surface, self._get_color(self._gameState.board[col][row]), (x,y,60,60), 0)
                        pygame.draw.rect(surface, GRAY, (x,y,60,60), 3)
                    elif self._gameState.board[col][row]._get_state() == FALLING:
                        pygame.draw.rect(surface, self._get_color(self._gameState.board[col][row]), (x,y,60,60), 0)
                        pygame.draw.rect(surface, BACKGROUND, (x,y,60,60), 2)
                    elif self._gameState.board[col][row]._get_state() == MATCHED:
                        pygame.draw.rect(surface, self._get_color(self._gameState.board[col][row]), (x,y,60,60), 0)
                        pygame.draw.rect(surface, R, (x,y,60,60), 9)
        pygame.display.flip()
                   
if __name__ =="__main__":
    x = Columns_Game()
    x.run()
