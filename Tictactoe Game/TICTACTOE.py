#Importing necessary libraries
import cv2
import numpy as np
#Declaring varibles
clicked = False  #clicked function is to check when the user clicks
x1 = 0           #x1 and y1 are used for drawing the cross and circles
y1 = 0           
co = 0           #co is used for calculating the centre of o
cx = 0           #cx is used for calculating the centre of x
eo = 0           #eo is odd even counter of clicked which helps to decide which shape to draw on a particular  click 
w1 = 0           #w1 and w2 decide player 1 will win or player 2  
w2 = 0
cl = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) # for storing the numeric values corresponding to cross and circle             
bg = 255*np.ones((700, 600, 3), np.uint8)        # blank white window
cv2.line(bg, (200, 0), (200, 600), (0, 0, 0), 3) # generating the tictactoe frame
cv2.line(bg, (400, 0), (400, 600), (0, 0, 0), 3)
cv2.line(bg, (0, 200), (600, 200), (0, 0, 0), 3)
cv2.line(bg, (0, 400), (600, 400), (0, 0, 0), 3)
cv2.line(bg, (0, 600), (600, 600), (0, 0, 0), 3)
cv2.imshow("criss_cross", bg)


def func(event, x, y, flags, param): # this function stores values in c1 corresponding to the square clicked in tictactoe frame
    global clicked, x1, y1, eo, cx, co, c1, c2, c3, c4, c5, c6, c7, c8, c9, w1, w2
    if event == cv2.EVENT_LBUTTONDOWN:
        eo += 1                      # event-odd count  
        if eo % 2 == 0:              # if eo is even then x is printed else o 
            cx += 1
        else:
            co += 1
        clicked = True
        if(x < 200 and y < 200):     # first box
            x1 = 100
            y1 = 100
            if eo % 2 == 0:
                cl[0, 0] = 1
            else:
                cl[0, 0] = 4

        if((x > 200 and x < 400) and y < 200): # first row second box 
            x1 = 300
            y1 = 100
            if eo % 2 == 0:
                cl[0, 1] = 1
            else:
                cl[0, 1] = 4

        if(x > 400 and y < 200):  # each box is covered like this..
            x1 = 500
            y1 = 100
            if eo % 2 == 0:
                cl[0, 2] = 1
            else:
                cl[0, 2] = 4

        if((y > 200 and y < 400) and x < 200):
            x1 = 100
            y1 = 300
            if eo % 2 == 0:
                cl[1, 0] = 1
            else:
                cl[1, 0] = 4

        if((x > 200 and x < 400) and y > 200 and y < 400):
            x1 = 300
            y1 = 300
            if eo % 2 == 0:
                cl[1, 1] = 1
            else:
                cl[1, 1] = 4

        if(x > 400 and (y > 200 and y < 400)):
            x1 = 500
            y1 = 300
            if eo % 2 == 0:
                cl[1, 2] = 1
            else:
                cl[1, 2] = 4

        if(x < 200 and (y > 400 and y < 600)):
            x1 = 100
            y1 = 500
            if eo % 2 == 0:
                cl[2, 0] = 1
            else:
                cl[2, 0] = 4

        if((x > 200 and x < 400) and (y > 400 and y < 600)):
            x1 = 300
            y1 = 500
            if eo % 2 == 0:
                cl[2, 1] = 1
            else:
                cl[2, 1] = 4

        if((x > 400 and x < 600) and (y>400 and y < 600)): # last row last box
            x1 = 500
            y1 = 500
            if eo % 2 == 0:
                cl[2, 2] = 1
            else:
                cl[2, 2] = 4


def win(cl):   # this function checks whether first player wins or second
    global w1, w2
    if (cl[0, 0]+cl[1, 1]+cl[2, 2]) == 12: # if the sum is 12 then o wins or 2nd player wins 
        w2 = 1
        return
    if (cl[0, 0]+cl[1, 1]+cl[2, 2]) == 3:  # if the sum is 12 then o wins or 2nd player wins
        w1 = 1
        return
    if (cl[0, 0]+cl[0, 1]+cl[0, 2]) == 12: # the same condition is checked for different forms a player can win in tictactoe 
        w2 = 1
        return
    if (cl[0, 0]+cl[0, 1]+cl[0, 2]) == 3:
        w1 = 1
        return
    if (cl[1, 0]+cl[1, 1]+cl[1, 2]) == 12:
        w2 = 1
        return
    if (cl[1, 0]+cl[1, 1]+cl[1, 2]) == 3:
        w1 = 1
        return
    if (cl[2, 0]+cl[2, 1]+cl[2, 2]) == 12:
        w2 = 1
        return
    if (cl[2, 0]+cl[2, 1]+cl[2, 2]) == 3:
        w1 = 1
        return
    if (cl[2, 0]+cl[1, 1]+cl[0, 2]) == 12:
        w2 = 1
        return
    if (cl[2, 0]+cl[1, 1]+cl[0, 2]) == 3:
        w1 = 1
        return
    if (cl[0, 1]+cl[1, 1]+cl[2, 1]) == 12:
        w2 = 1
        return
    if (cl[0, 2]+cl[1, 2]+cl[2, 2]) == 12:
        w2 = 1
        return
    if (cl[0, 0]+cl[1, 0]+cl[2, 0]) == 12:
        w2 = 1
        return
    if (cl[0, 1]+cl[1, 1]+cl[2, 1]) == 3:
        w1 = 1
        return
    if (cl[0, 2]+cl[1, 2]+cl[2, 2]) == 3:
        w1 = 1
        return
    if (cl[0, 0]+cl[1, 0]+cl[2, 0]) == 3:
        w1 = 1
        return


while 1:
    cv2.imshow("criss_cross", bg)
    cv2.setMouseCallback('criss_cross', func) # when mouse button is clicked on criss_cross window 'func' is called 
    if clicked == True:
        if eo % 2 == 0: # if eo is even then x is drawn on the box which is clicked
            cv2.line(bg, (x1-70, y1-70), (x1+60, y1+60), (0, 0, 0), 3)
            cv2.line(bg, (x1-70, y1+60), (x1+60, y1-70), (0, 0, 0), 3)
        else:
            cv2.circle(bg, (x1, y1), 70, (0, 0, 0), 3) # if eo is odd then x is drawn on the box which is clicked
        win(cl) # win function is called
        if w1 == 1: # if w1 = 1 that means x wins
            cv2.putText(bg, "X WINS", (280, 680),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break  
        if w2 == 1: # if w2 = 1 that means o wins
            cv2.putText(bg, "O WINS", (280, 680),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)
            if cv2.waitKey(1) & 0xFF == ord('q'):            
                break
        if w1!=1 and w2!=1 and eo==9: # if both of them are not 1 but all the boxes are filled so its a draw
            cv2.putText(bg, "Draw", (280, 680),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)
            if cv2.waitKey(1) & 0xFF == ord('q'):            
                break
        
    if cv2.waitKey(1) & 0xFF == ord('q'): # player can exit the window by clicking 'q' after the game ends
        break   
            
if cv2.waitKey(1) & 0xFF == ord('q'):   
    cv2.destroyAllWindows()               # destroying all windows