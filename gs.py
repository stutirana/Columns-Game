#STUTIRANA
#ID:85039361
FROZEN= 0
FALLING=1
LANDED=2
MATCHED=3
NONE=4
EMPTY = ' '
class gameState():

    def __init__(self,rows:int,cols:int):
        self._ROWS = rows
        self._COLS = cols
        self.board = []
        self.game_over = False
        self.faller = faller(0,0,0,' ',' ',' ')
    def advance(self):#this function will drop,update and check state and game over
        if self.check_game_over()== False:
            if self.get_state() == FALLING:
                faller.drop(self.faller)
                faller.update_turn(self.faller)
                j1=self._drop_board()
                self.land_faller(j1)
            elif self.get_state() == LANDED:
                b=self.freeze_faller()
                if not b:
                    self.faller._start_faller()
                else:
                    faller.update_turn(self.faller)
    def update_turn(self):#will add one to the turn for faller attribute 
        faller.update_turn(self.faller)
    def shift_faller(self,direction:int):#will shift the faller
        if self._able_shift(direction)==True:
            faller._shift(self.faller,direction)
            if direction == 0:
                self._erase_right()
            elif direction ==1:
                self._erase_left()
    def rotate_faller(self):#rotate the faller
        if (self.get_state() != FROZEN and self.get_state() !=NONE) and self.faller._turn>1:
            faller.rotate(self.faller)
    def check_game_over(self):#check if game is over by looking at the faller state and if it fits in the board
        if self.get_turn() <=3 and (self.get_state() == FROZEN):
            self.game_over = True
        if self._board_full() == True:
            self.game_over = True
        return self.game_over
    def empty_board(self):#this will make an empty board
        for col in range(self._COLS):
            self.board.append([])
            for row in range(self._ROWS):
                self.board[-1].append(EMPTY)
    def changeState_adv(self):#function drops the elements in the rows if there is a match and spaces are mad
        if self.check_matched():
            new_al=[]
            block = []
            al=[]
            for i in range(self._COLS):
                for el in self.board[i]:
                    if el != EMPTY:
                        block.append(el)
                al.append(block)
                block=[]
            for el in al:
                while len(el)<self._ROWS:
                    el = [EMPTY]+el
                new_al.append(el)
            self.board=new_al

            
    def create_faller(self,currentCOL:int,jewl_block:list):#will create and update the self.faller attribute
        self.faller = faller(currentCOL-1,self._COLS,self._ROWS,jewl_block[0],jewl_block[1],jewl_block[2])
        faller._start_faller(self.faller)
    def _drop_board(self):#will update the board to the most recent coordinates
        j1c,j2c,j3c,turn=faller.get_faller_pos(self.faller)
        if turn ==1:
            self._clear_previous()
            self.board[j1c[1]][j1c[0]] = j1c[2]
        elif turn == 2:
            self._clear_previous()
            self.board[j1c[1]][j1c[0]] = j1c[2]
            self.board[j2c[1]][j2c[0]] = j2c[2]
        elif turn == 3:
            self._clear_previous()
            self.board[j1c[1]][j1c[0]] = j1c[2]
            self.board[j2c[1]][j2c[0]] = j2c[2]
            self.board[j3c[1]][j3c[0]] = j3c[2]
        elif turn >3:
            self._clear_previous()
            self.board[j1c[1]][j1c[0]] = j1c[2]
            self.board[j2c[1]][j2c[0]] = j2c[2]
            self.board[j3c[1]][j3c[0]] = j3c[2]
        return j1c
    def _clear_previous(self):#will clear the previous steps the faller has taken
        j1c,j2c,j3c,turn=faller.get_faller_pos(self.faller)
        if turn <= 1:
            pass
        elif turn == 2:
            self.board[j1c[1]][j1c[0]-1] = EMPTY
        elif turn == 3:
            self.board[j1c[1]][j1c[0]-1] = EMPTY
            self.board[j2c[1]][j2c[0]-1] = EMPTY
        elif turn >3:
            self.board[j1c[1]][j1c[0]-1] = EMPTY
            self.board[j2c[1]][j2c[0]-1] = EMPTY
            self.board[j3c[1]][j3c[0]-1] = EMPTY
    def _able_shift(self,direction:int)->bool:#will see if you can shift 1eft or right
        j1c,j2c,j3c,turn=faller.get_faller_pos(self.faller)
        if direction == 0:
            if self.get_turn() >=1 and j1c[1]+1 <self._COLS and faller.get_state(self.faller)!=FROZEN and self.board[j1c[1]+1][j1c[0]]==EMPTY:
                return True
        if direction == 1:
            if self.get_turn() >=1 and j1c[1]-1 >= 0 and faller.get_state(self.faller)!=FROZEN and self.board[j1c[1]-1][j1c[0]]==EMPTY:
                return True
        return False
    def _erase_right(self):#given you can shift it will earse the previous position faller was in
        j1c,j2c,j3c,turn=faller.get_faller_pos(self.faller)
        if turn == 1:
            self.board[j1c[1]][j1c[0]] = j1c[2]
            self.board[j1c[1]-1][j1c[0]] = EMPTY
        elif turn == 2:
            self.board[j1c[1]][j1c[0]] = j1c[2]
            self.board[j1c[1]-1][j1c[0]] = EMPTY
            self.board[j2c[1]][j2c[0]] = j2c[2]
            self.board[j2c[1]-1][j2c[0]] = EMPTY
        elif turn >2:
            self.board[j1c[1]][j1c[0]] = j1c[2]
            self.board[j1c[1]-1][j1c[0]] = EMPTY
            self.board[j2c[1]][j2c[0]] = j2c[2]
            self.board[j2c[1]-1][j2c[0]] = EMPTY
            self.board[j3c[1]][j3c[0]] = j3c[2]
            self.board[j3c[1]-1][j3c[0]] = EMPTY
        self.land_faller(j1c)
    def _erase_left(self):#given you can shift it will earse the previous position faller was in
        j1c,j2c,j3c,turn=faller.get_faller_pos(self.faller)
        if turn == 1:
            self.board[j1c[1]+1][j1c[0]] = EMPTY
            self.board[j1c[1]][j1c[0]] = j1c[2]
        elif turn == 2:
            self.board[j1c[1]][j1c[0]] = j1c[2]
            self.board[j1c[1]+1][j1c[0]] = EMPTY
            self.board[j2c[1]][j2c[0]] = j2c[2]
            self.board[j2c[1]+1][j2c[0]] = EMPTY
        elif turn >2:
            self.board[j1c[1]][j1c[0]] = j1c[2]
            self.board[j1c[1]+1][j1c[0]] = EMPTY
            self.board[j2c[1]][j2c[0]] = j2c[2]
            self.board[j2c[1]+1][j2c[0]] = EMPTY
            self.board[j3c[1]][j3c[0]] = j3c[2]
            self.board[j3c[1]+1][j3c[0]] = EMPTY    
        self.land_faller(j1c)   
    def _board_full(self):#if the board is full he game is over
        for col in self.board:
            if EMPTY in col:
                return False
        return True
    def check_matches(self):#this will iterate through all the rows and columns
        winner = EMPTY
        for col in range((self._COLS)):
            for row in range((self._ROWS)):
                self._winning_sequence_begins_at(self.board, col, row)
    def _check_match(self,board: [[int]], col: int, row: int, coldelta: int, rowdelta: int)->bool:#this will check if there are matched jewels and erase them
        jwl_list=[]
        if self._ROWS > self._COLS:
            comp = self._COLS
        else:
            comp = self._ROWS
        start_cell = board[col][row]
        if start_cell == EMPTY:
            return jwl_list
        else:  
            for i in range(0, comp+1):
                if self.is_valid_column_number(col + coldelta * i) and self.is_valid_row_number(row + rowdelta * i) and\
                   board[col + coldelta *i][row + rowdelta * i]!= EMPTY and\
                   jewel.get_color(board[col + coldelta *i][row + rowdelta * i]) == jewel.get_color(start_cell):
                    if board[col + coldelta *i][row + rowdelta * i] not in jwl_list and board[col + coldelta *i][row + rowdelta * i]!=EMPTY:
                        jwl_list.append(board[col + coldelta *i][row + rowdelta * i])
                else:
                    return jwl_list

    def _change_jwl_state(self,jwl_list):
        if len(jwl_list)>=3:
            for el in jwl_list:
                jewel._match_jewel(el)
        else:
            return False
        return True
    def _winning_sequence_begins_at(self,board: [[int]], col: int, row: int):#checks the different possiblities of winning sequences
        return self._change_jwl_state(self._check_match(board,col,row,0,1))\
            or self._change_jwl_state(self._check_match(board,col,row,1,1)) \
            or self._change_jwl_state(self._check_match(board,col,row,1,0)) \
            or self._change_jwl_state(self._check_match(board,col,row,1,-1)) \
            or self._change_jwl_state(self._check_match(board,col,row,0,-1)) \
            or self._change_jwl_state(self._check_match(board,col,row,-1,-1))\
            or self._change_jwl_state(self._check_match(board,col,row,-1,0))\
            or self._change_jwl_state(self._check_match(board,col,row,-1,1))
    def check_matched(self):#it cheks if there are mathced jewels and erases them
        a= False
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                
                if self.board[i][j]!= EMPTY and self.board[i][j]._get_state()== MATCHED:
                    self.board[i][j]= EMPTY
                    a = True
        return a
    def valid_contents(self,cont):#checks if the contents are valid
        return True in [c in cont for c in COLORS]
        return False    
    def get_jwl_state(self,jwl):
        return jewel._get_state(jwl)
    def get_game_over(self):
        return self.game_over
    def get_state(self):
        return faller.get_state(self.faller)
    def get_turn(self):
        return faller.get_turn(self.faller)
    def freeze_faller(self):
        j1c,j2c,j3c,turn=faller.get_faller_pos(self.faller)
        if not self.is_valid_row_number(j1c[0]+1):
            faller._freeze_faller(self.faller)
            return True
        elif self.board[j1c[1]][j1c[0]+1]!=EMPTY:
            faller._freeze_faller(self.faller)
            return True
        return False
    def land_faller(self,j1):#this advances the faller attribute of position by 1
        if j1[0] == self._ROWS-1 or self.board[j1[1]][j1[0]+1] != EMPTY:
            faller._land_faller(self.faller)         
    def is_valid_column_number(self,num:int)->bool:
        if num >=0 and num < self._COLS:
            return True
        return False
    def is_valid_row_number(self,num:int)->bool:
        if num >=0 and num < self._ROWS:
            return True
        return False
    def quit(self):
        self.game_over = True
class faller():#this is a faller object
    def __init__(self,current_col:int,col:int,row:int,j1:str,j2:str,j3:str):
        self._j1 = jewel(j1,current_col,col,row)
        self._j2 = jewel(j2,current_col,col,row)
        self._j3 = jewel(j3,current_col,col,row)
        self._turn = 0
        self._state = NONE
    def drop(self):#it adds one to the current row it is in
        self._start_faller()
        if self._state == FALLING:
            if self._turn ==0:
                jewel.drop(self._j1)
            elif self._turn == 1:
                jewel.drop(self._j1)
                jewel.drop(self._j2)
            else:
                jewel.drop(self._j1)
                jewel.drop(self._j2)
                jewel.drop(self._j3)
    
    def get_faller_pos(self):#returns the attributes of fller
        col1=' '
        col2 = ' '
        col3 = ' '
        row1 = ' '
        row2 = ' '
        row3=' '
        if self._turn == 0:
            col1,row1,colr1 = jewel.get_jwl_info(self._j1)
        elif self._turn == 1:
            col1, row1,colr1 = jewel.get_jwl_info(self._j1)
            col2, row2,colr2 = jewel.get_jwl_info(self._j2)
        else:
            col1, row1,colr1 = jewel.get_jwl_info(self._j1)
            col2, row2,colr2 = jewel.get_jwl_info(self._j2)
            col3, row3,colr3 = jewel.get_jwl_info(self._j3)
        
        return [row1,col1,self._j1],[row2,col2,self._j2],[row3,col3,self._j3],self._turn

    def update_turn(self):#iterates the turn attribute
        self._turn+=1
    
    def rotate(self):#rotates the faller
        temp1 = jewel.get_color(self._j1)
        temp2 = jewel.get_color(self._j2)
        temp3 = jewel.get_color(self._j3)
        jewel.change_color(self._j2,temp3)
        jewel.change_color(self._j1,temp2)
        jewel.change_color(self._j3,temp1)

    def _freeze_faller(self):#changes the state to frozen
        self._state = FROZEN
        jewel._freeze_jwl(self._j1)
        jewel._freeze_jwl(self._j2)
        jewel._freeze_jwl(self._j3)

    def _land_faller(self):#chnages the state to land
        self._state= LANDED
        jewel._land_jwl(self._j1)
        jewel._land_jwl(self._j2)
        jewel._land_jwl(self._j3)

    def _shift(self,direction:int):#moves the current col position left or right
        if direction == 1:
            jewel.shift_left(self._j1)
            jewel.shift_left(self._j2)
            jewel.shift_left(self._j3)
        elif direction == 0:
            jewel.shift_right(self._j1)
            jewel.shift_right(self._j2)
            jewel.shift_right(self._j3)
    
    def _start_faller(self):#it changes the state to fall
        self._state = FALLING
        jewel._fall_jwl(self._j1)
        jewel._fall_jwl(self._j2)
        jewel._fall_jwl(self._j3)
    def get_state(self):
        return self._state
    
    def get_turn(self):
        return self._turn
        
            
class jewel():
    
    def __init__(self,color:str,cc:int,col:int,row:int):
        self._cc= cc
        self._cr=''
        self._row=row
        self._col=col
        self._color = color
        self._state = NONE
    def _match_jewel(self):#changes the state of the jewel to matched
        self._state = MATCHED
    def get_jwl_info(self):#it returns certain attributes of the jewwl
        return self._cc,self._cr,self._color
    def _freeze_jwl(self):
        self._state = FROZEN
    def _land_jwl(self):
        self._state = LANDED
    def _fall_jwl(self):
        self._state = FALLING
    def change_color(self,color:str):
        self._color = color
    def get_color(self):
        return self._color
    def _get_state(self):
        return self._state
    def drop(self):#it adds one to the jewels row position
        if self._cr == '':
            self._cr=0
        elif self._cr<self._row:
            self._cr+=1
    def shift_left(self):#it subtracts one from the jewel's coloumn position
        if self._cc!=0 or self._cc <=self._col:
            self._cc-=1
    def shift_right(self):#it adds one to the jewel's column position
        if self._cc!=0 or self._cc <=self._col:
            self._cc+=1
