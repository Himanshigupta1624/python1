# def sum(a,b,c):
#     return a+b+c
# def board(xstate,ystate):
#     zero='X' if xstate[0] else ('"0"' if ystate[0] else 0)
#     one='X' if xstate[1] else ('"0"' if ystate[1] else 1)
#     two='X' if xstate[2] else ('"0"' if ystate[2] else 2)
#     three='X' if xstate[3] else ('"0"' if ystate[3] else 3)
#     four='X' if xstate[4] else ('"0"' if ystate[4] else 4)
#     five='X' if xstate[5] else ('"0"' if ystate[5] else 5)
#     six='X' if xstate[6] else ('"0"' if ystate[6] else 6)
#     seven='X' if xstate[7] else ('"0"' if ystate[7] else 7)
#     eight='X' if xstate[8] else ('"0"' if ystate[8] else 8)
    
    
#     print(f"{zero} | {one} | {two}")
#     print("---------")
#     print(f"{three} | {four} | {five} ")
#     print("---------")
#     print(f"{six} | {seven} | {eight} ")
    
    
# def checkwin(xstate,ystate):
#         states=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        
#         for win in states:
#             if (sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
#                 board(xstate,ystate)
#                 print('x wins')
#                 return 1
#             if (sum(ystate[win[0]],ystate[win[1]],ystate[win[2]])==3):
#                 board(xstate,ystate)
#                 print('0 wins')
#                 return 0
#         return -1
    
# if __name__=='__main__':
#      xstate=[0,0,0,0,0,0,0,0,0]   
#      ystate=[0,0,0,0,0,0,0,0,0]  
#      turn=1
#      print("welcome to the tic-tac-toe baby")
#      while True:
#          board(xstate,ystate)
#          if(turn==1):
#              print("X's turn") 
#              value=int(input("please enter the position:- "))
#              xstate[value]=1 
#          else:
#              print("0's turn")
#              value=int(input("please enter the position:- "))
#              ystate[value]=1
         
         
#          cwin=checkwin(xstate,ystate) 
#          if(cwin!=-1):
#              print("GAME OVER")
#              break
#          turn=1-turn       


# def sum(a,b,c):
#     return a+b+c


# def board(xstate,ystate):
#     zero='X' if xstate[0] else('"0"' if ystate[0] else 0)
#     one='X' if xstate[1] else('"0"' if ystate[1] else 1)            
#     two='X' if xstate[2] else('"0"' if ystate[2] else 2)
#     three='X' if xstate[3] else('"0"' if ystate[3] else 3)
#     four='X' if xstate[4] else('"0"' if ystate[4] else 4)
#     five='X' if xstate[5] else('"0"' if ystate[5] else 5)
#     six='X' if xstate[6] else('"0"' if ystate[6] else 6)
#     seven='X' if xstate[7] else('"0"' if ystate[7] else 7)
#     eight='X' if xstate[8] else('"0"' if ystate[8] else 8)
    
#     print(f"{zero} | {one} | {two}")    
#     print("---------")
#     print(f"{three} | {four} | {five}")
#     print("---------")
#     print(f"{six} | {seven} | {eight}")
    
# def checkwin(xstate,ystate):
#     states= [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    
#     for win in states:
#         if (sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
#             board(xstate,ystate)
#             print('X wins')
#             return 1
#         if (sum(ystate[win[0]],ystate[win[1]],ystate[win[2]])==3):
#             board(xstate,ystate)
#             print('0 wins')
            
#             return 1
#         return -1
    


# if __name__=='__main__':
#     xstate=[0,0,0,0,0,0,0,0,0]
#     ystate=[0,0,0,0,0,0,0,0,0]
#     turn=1
#     print("welcome to the tic-tac-toe baby")    
#     while True:
#         board(xstate,ystate)
#         if (turn==1):
#             print("X's turn")
#             value=int(input("please enter the position:- "))
#             xstate[value]=1
#         else:
#             print("0's turn")
#             value=int(input("please enter the position:- "))
#             ystate[value]=1
            
#         cwin=checkwin(xstate,ystate)
        
#         if (cwin!=-1):
#             print("GAME OVER")
#             break
#         turn=1-turn         
            
def display_board(xstate, ystate):
    board= [
        'X' if xstate[i] else('0' if ystate[i] else int(i))
        for i in range(9)
    ] 
    print(f"{board[0]} | {board[1]} | {board[2] }")      
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5] }")      
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8] }")  
    
def checkwin(xstate, ystate):
    states=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in states:
        if all(xstate[i] for i in win ):
            return 'X'
        if all(ystate[i] for i in win ):
            return '0'
    return None   

def ttt():
   xstate=[0,0,0,0,0,0,0,0,0]
   ystate=[0,0,0,0,0,0,0,0,0]
   turn=1
   print("welcome to the tic-tac-toe baby")  
   
   for y in range(9):
       display_board(xstate,ystate)
       
       if turn==1:
           print("X's turn")
       else: 
          print("0's turn")  
        
       value=int(input("please enter the position:- "))     
       
       if turn==1:
           xstate[value]=1
       else:
           ystate[value]=1
       cwin=checkwin(xstate,ystate)
       
       if cwin:
           display_board(xstate,ystate)
           print(f"Player {cwin} wins!")  
           return
       
       turn=1-turn
       
       display_board(xstate,ystate)
       print("It's a tie!")                
if __name__=="__main__":
    ttt()       