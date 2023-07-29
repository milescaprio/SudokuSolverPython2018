import random as rand#Just in case I need these imports
import turtle as bird
change = 0
PuzzleToDecrypt = input("Give Sudoku Here. Put numbers with no spaces, ? if unknown. Read left to right, by row, starting from top left.")#Ask for puzzle
def Check1():#First check to confirm puzzle is valid
    Checkinghelper = 0
    LoopIndex5 = 0
    while LoopIndex5 < 9:
        if '?' in SudokuToSolveRows[LoopIndex5]:
            QMtestRows = 1
        else:
            QMtestRows = 0
        if '?' in SudokuToSolveColumns[LoopIndex5]:
            QMtestColumns = 1
        else:
            QMtestColumns = 0
        if '?' in SudokuToSolveSquares[LoopIndex5]:
            QMtestSquares = 1
        else:
            QMtestSquares = 0
        if len(set(SudokuToSolveRows[LoopIndex5])) != len(SudokuToSolveRows[LoopIndex5]) - SudokuToSolveRows[LoopIndex5].count('?') + QMtestRows:
            Checkinghelper = Checkinghelper + 1
        if len(set(SudokuToSolveColumns[LoopIndex5])) != len(SudokuToSolveColumns[LoopIndex5]) - SudokuToSolveColumns[LoopIndex5].count('?') + QMtestColumns:
            Checkinghelper = Checkinghelper + 1
        if len(set(SudokuToSolveSquares[LoopIndex5])) != len(SudokuToSolveSquares[LoopIndex5]) - SudokuToSolveSquares[LoopIndex5].count('?') + QMtestSquares:
            Checkinghelper = Checkinghelper + 1
        LoopIndex5 = LoopIndex5 + 1
    if Checkinghelper == 0:
        print("First Check Complete: Valid Puzzle")
    else:
        print("Invalid Puzzle.",Checkinghelper,"Errors")
        quit()
def RefreshMemosInSudokuRange():
    print("CodeHere")
def Algr1():#First algorithm: main 
    print("CodeHere")
def Algr2():#backup algorithm
    print("Codehere")
def DecryptInp():#Make lists from input
    global SudokuToSolve
    global SudokuToSolveRows
    global SudokuToSolveColumns
    global SudokuToSolveSquares
    LoopIndex1 = 0
    SudokuToSolve = [PuzzleToDecrypt[0]]#Run-on list
    while LoopIndex1 < 81:
        if LoopIndex1 == 0:
            print('working on it...')
        else:    
            SudokuToSolve = SudokuToSolve + [PuzzleToDecrypt[LoopIndex1]]
        LoopIndex1 = LoopIndex1+1
    SudokuToSolveRows = [SudokuToSolve[0:9]]#List grouped by rows
    LoopIndex2 = 0
    while LoopIndex2 < 9:
        if not LoopIndex2 == 0:
            SudokuToSolveRows = SudokuToSolveRows + [SudokuToSolve[(9*LoopIndex2):(9*LoopIndex2+9)]]
        LoopIndex2 = LoopIndex2+1
    LoopIndex2_9 = 0
    SudokuToSolveColumns = [[SudokuToSolve[0]]]#List grouped by columns
    while LoopIndex2_9 < 9:
        if not LoopIndex2_9 == 0:
            SudokuToSolveColumns = [SudokuToSolveColumns[0] + [SudokuToSolve[((9*LoopIndex2_9))]]]
        LoopIndex2_9 = LoopIndex2_9 + 1
    LoopIndex3 = 0
    LoopIndex3_1 = 0
    while LoopIndex3 < 9:
        if not LoopIndex3 == 0:
            SudokuToSolveColumns = SudokuToSolveColumns + [[SudokuToSolve[LoopIndex3]]]
            while LoopIndex3_1 < 9:
                if not LoopIndex3_1 == 0:
                    SudokuToSolveColumns[LoopIndex3] = SudokuToSolveColumns[LoopIndex3] + [SudokuToSolve[LoopIndex3 + 9*LoopIndex3_1]]
                LoopIndex3_1 = LoopIndex3_1 + 1
        LoopIndex3 = LoopIndex3 + 1
        LoopIndex3_1 = 0
    LoopIndex4 = 0
    SudokuToSolveSquares = [SudokuToSolveRows[0][0:3] + SudokuToSolveRows[1][0:3] + SudokuToSolveRows[2][0:3]]#list grouped by Squares
    while LoopIndex4 < 9:
        if not LoopIndex4 == 0:
            SudokuToSolveSquares = SudokuToSolveSquares + [SudokuToSolveRows[((LoopIndex4//3)*3)][((LoopIndex4%3)*3):((LoopIndex4%3)*3)+3] + SudokuToSolveRows[((LoopIndex4//3)*3)+1][((LoopIndex4%3)*3):((LoopIndex4%3)*3)+3] + SudokuToSolveRows[((LoopIndex4//3)*3)+2][((LoopIndex4%3)*3):((LoopIndex4%3)*3)+3]]
        LoopIndex4 = LoopIndex4 + 1
    print(SudokuToSolve)#admin & debugging
    print(SudokuToSolveRows)
    print(SudokuToSolveColumns)
    print(SudokuToSolveSquares)
DecryptInp()#actual code (behind is definitions)
Check1()
Algr1()
if change == 0:
    Algr2()



