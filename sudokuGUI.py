from Tkinter import *
import sudoku
entries = []
secs = 0
mins=0


def initialize(top,board):

    E = entries[0]
    m=1
    for i in range(9):
        for j in range(9):
            if(not E.get()):
                board[i][j] = 0
            else:
                board[i][j] = int(E.get())
            if(m<=80):
                E = entries[m]
                m+=1
           
def printBoardOnGUI(board):
    cleanBoard()
    E = entries[0]
    m=1
    for i in range(9):
        for j in range(9):
            E.insert(m,board[i][j])
            if(m<=80):
                E = entries[m]
                m+=1
        
def createGUI(board):
    top = Tk()
    top.title("Sudoku Solver")
    canvas = Canvas(top, height=330, width =350)
    createRow(canvas)
    createCol(canvas)
    createEntry(top)
    createButtons(top,board)
    printBoardOnGUI(board)
    canvas.pack(side = 'top')
    top.mainloop()  

def newBoardOnGUI():
    newboard = sudoku.createNewBoard()
    printBoardOnGUI(newboard)
    global secs,mins
    secs=0
    mins=0


def createButtons(top,board):
    button_solve = Button(top, text="Solve", justify='left', bg = 'green', font="Helvetica 10 bold",default='active', command = lambda: solveBoard(top,board))
    button_reset = Button(top, text="Reset", justify='right',bg = 'red' , font="Times 10 bold",command = lambda: resetBoard())
    button_new = Button(top, text="Generate New Puzzle", justify='right',bg = 'yellow' , font="Times 10 bold",command = lambda: newBoardOnGUI())
    button_solve.place(x=180, y=275, height=30, width=60)
    button_reset.place(x=255, y=275, height=30, width=60)
    button_new.place(x=35, y=275, height=30, width=130)
    label =Label(top, text="0 : 0", fg="blue", font="Verdana 18 bold")
    label.place(x=35, y=0)
    def startClock(label):
        def count() : 
            global secs,mins
            if mins < 10:
                if secs < 10 :
                    display= '0' + str(mins) + ' : ' + '0' + str(secs) 
                else : 
                    display= '0' + str(mins) + ' : ' + str(secs)
            else:
                display=  str(mins) + ' : ' + str(secs) 
            label['text']=display
            label.after(1000, count) 
            secs += 1
            if secs == 60 : 
                secs=0
                mins+=1
        count()
    startClock(label)
    
def cleanBoard():
    for e in entries:
        e.delete(0, END)

def resetBoard():
    for e in entries:
        e.delete(0, END)
    global secs,mins
    secs=0
    mins=0

def solveBoard(top,board):
    initialize(top,board)
    if(sudoku.solveSudoku(board)):
        printBoardOnGUI(board)
    else:
        print ("No solution found")
    
def createEntry(top):
    p,q=41.4,41.4
    for i in range(9):
        for j in range(9):
            E = Entry(top, width=3, font = 'BOLD')
            E.grid(row=i, column=j)
            E.place(x=p, y=q, height=20, width=25)
            entries.append(E)
            p+=30.0
        q+=24.5
        p=41.2
    
def createRow(canvas):
    i,j=40,40
    p=40
    q=260
    for m in range(10):
        if(m%3==0):
            canvas.create_line(i,j,p,q,width=4)
        else:
            canvas.create_line(i,j,p,q,width=2)
        i+=30
        p+=30
    
def createCol(canvas):
    i,j=40,40
    p,q=310,40
    for m in range(10):
        if(m%3==0):
            canvas.create_line(i,j,p,q,width=4)
        
        else:
            canvas.create_line(i,j,p,q,width=2)
        j+=24.5
        q+=24.5

    
if __name__=="__main__":
    
    board = sudoku.createNewBoard()
    createGUI(board)