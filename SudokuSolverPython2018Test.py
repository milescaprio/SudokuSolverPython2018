import sys
sys.modules[__name__].__dict__.clear()
global change
change = 0
global set1to9                  #The standard reference set of 1 thru 9
global SudokuToSolve            #This 1x81 List is the Sudoku input by user to solve 1x81 elements, gets updated throughout the routine
global SudokuToSolveRows        #This 9x9 Matrix is the working copy of the ROWS of the sudoku, gets updated throughout the routine 
global SudokuToSolveColumns     #This 9x9 Matrix is the working copy of the COLUMNS of the sudoku, gets updated throughout the routine 
global SudokuToSolveSquares     #This 9x9 Matrix is the working copy of the SQUARES of the sudoku, gets updated throughout the routine 
global SudokuToSolveCopy        #This 1x81 List is a temporary working copy of SudokuToSolve, gets updated throughout the routine
global SudokuToSolveRowsCopy
global SudokuToSolveColumnsCopy
global SudokuToSolveSquaresCopy
global loopcount
global BreakoutHelper
global loopcount2
global change2
global TryCell
global SaveElement
global CheckingElementRequirement
global RowRequirements
global SaveCell
global TryCellColumns
global SaveElementColumns
global CheckingElementRequirementColumns
global ColumnRequirements
global SaveCellColumns
change2 = 0
BreakoutHelper = 0
loopcount = 0
loopcount2 = 0
set1to9 = {'1','2','3','4','5','6','7','8','9'}
PuzzleToDecrypt = input("Give Sudoku Here. Put numbers with no spaces, ? if unknown. Read left to right, by row, starting from top left.\n")#81-Character String Ask for puzzle
SAS = input("Show Advanced Scripting? y\\n\n")
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
        print("This puzzle contains", SudokuToSolve.count('?'), "Unknowns and", (81-SudokuToSolve.count('?')),"Hints.")
    else:
        print("Invalid Puzzle.",Checkinghelper,"Errors")
        quit()
def RefreshMemosInSudokuRange():
    print("CodeHere")
def Algr1():#First algorithm: main 
    global set1to9
    global SudokuToSolve
    global SudokuToSolveRows
    global SudokuToSolveColumns
    global SudokuToSolveSquares
    global SudokuToSolveCopy
    global SudokuToSolveRowsCopy
    global SudokuToSolveColumnsCopy
    global SudokuToSolveSquaresCopy
    CheckingCell = 0
    change = 1
    loopcount = 0
    while change == 1 and '?' in SudokuToSolve:
        change = 0
        CheckingCell = 0
        while CheckingCell < 81:
            CheckingColumn = CheckingCell%9
            CheckingRow = CheckingCell//9
            CheckingSquare = CheckingColumn//3 + (CheckingRow//3)*3
            if SudokuToSolve[CheckingCell] == '?': #incomplete 
                if len(set1to9 - set(SudokuToSolveRows[CheckingRow]) - set(SudokuToSolveColumns[CheckingColumn]) - set(SudokuToSolveSquares[CheckingSquare])) == 1:
                    SudokuToSolveCopy = SudokuToSolve#Just to replace ONE "?" to a number? Kind of extensive! But worth it.
                    SudokuToSolveRowsCopy = SudokuToSolveRows
                    SudokuToSolveColumnsCopy = SudokuToSolveColumns
                    SudokuToSolveSquaresCopy = SudokuToSolveSquares
                    SudokuToSolveCopy[CheckingCell] = list(set1to9 - set(SudokuToSolveRows[CheckingRow]) - set(SudokuToSolveColumns[CheckingColumn]) - set(SudokuToSolveSquares[CheckingSquare]))[0]
                    SudokuToSolveRowsCopy[CheckingRow][CheckingColumn] = list(set1to9 - set(SudokuToSolveRows[CheckingRow]) - set(SudokuToSolveColumns[CheckingColumn]) - set(SudokuToSolveSquares[CheckingSquare]))[0]
                    SudokuToSolveColumnsCopy[CheckingColumn][CheckingRow] = SudokuToSolveRowsCopy[CheckingRow][CheckingColumn]#list(set1to9 - set(SudokuToSolveRows[CheckingRow]) - set(SudokuToSolveColumns[CheckingColumn]) - set(SudokuToSolveSquares[CheckingSquare]))[0]
                    SudokuToSolveSquaresCopy[CheckingSquare][((CheckingCell%27)//9)*3+((CheckingCell%27)%3)] = SudokuToSolveColumnsCopy[CheckingColumn][CheckingRow]
                    SudokuToSolveSquares = SudokuToSolveSquaresCopy
                    SudokuToSolveColumns = SudokuToSolveColumnsCopy
                    SudokuToSolveRows = SudokuToSolveRowsCopy
                    SudokuToSolve = SudokuToSolveCopy
                    change = 1
            CheckingCell = CheckingCell + 1
        loopcount = loopcount + 1
    print("Ran through algorithm1",loopcount,"Times.")
def Algr2():#Second Algorithm: backup, but common use.
    global set1to9
    global SudokuToSolve
    global SudokuToSolveRows
    global SudokuToSolveColumns
    global SudokuToSolveSquares
    global SudokuToSolveCopy
    global SudokuToSolveRowsCopy
    global SudokuToSolveColumnsCopy
    global SudokuToSolveSquaresCopy
    global change2
    global loopcount2
    global RowRequirements
    global TryCell
    global SaveElement
    global CheckingElementRequirement
    global SaveCell
    global SaveCellColumns
    global CheckingElementRequirementColumns
    global SaveElementColumns
    global TryCellColumns
    global ColumnRequirements
    global CheckingColumns2
    change2 = 1
    CheckingColumns2 = 0
    loopcount2 = 0
    SudokuToSolveCopy = SudokuToSolve
    SudokuToSolveRowsCopy = SudokuToSolveRows
    SudokuToSolveColumnsCopy = SudokuToSolveColumns
    SudokuToSolveSquaresCopy = SudokuToSolveSquares
    CheckingRow2 = 0
    CheckingElementRequirement = 0
    TryCell = 0
    TryCellColumns = 0
    CheckingColumns2 = 0
    CheckingElementRequirementColumns = 0
    AmountOfPlacesRows = 0
    global RowRequirements
    global ColumnRequirements
    RowRequirements = list(set1to9 - set(SudokuToSolveRows[CheckingRow2]))
    RowRequirements = sorted(RowRequirements)
    while change2 == 1 and '?' in SudokuToSolve:
        change2 = 0
        CheckingRow2 = 0
        while CheckingRow2 < 9: #which row(
            SudokuToSolveCopy = SudokuToSolve
            SudokuToSolveRowsCopy = SudokuToSolveRows
            SudokuToSolveColumnsCopy = SudokuToSolveColumns
            SudokuToSolveSquaresCopy = SudokuToSolveSquares
            RowRequirements = list(set1to9 - set(SudokuToSolveRows[CheckingRow2]))
            RowRequirements = sorted(RowRequirements)
            CheckingElementRequirement = 0
            while CheckingElementRequirement < len(RowRequirements):#Which requirement(
                TryCell = 0
                AmountOfPlacesRows = 0
                SaveElement = 0
                SudokuToSolveCopy = SudokuToSolve
                SudokuToSolveRowsCopy = SudokuToSolveRows
                SudokuToSolveColumnsCopy = SudokuToSolveColumns
                SudokuToSolveSquaresCopy = SudokuToSolveSquares
                RowRequirements = list(set1to9 - set(SudokuToSolveRows[CheckingRow2]))
                RowRequirements = sorted(RowRequirements)
                RowRequirements = RowRequirements + ['-1','-1','-1','-1','-1']
                while TryCell < 9: #Which trying cell(
                    SudokuToSolveCopy = SudokuToSolve
                    SudokuToSolveRowsCopy = SudokuToSolveRows
                    SudokuToSolveColumnsCopy = SudokuToSolveColumns
                    SudokuToSolveSquaresCopy = SudokuToSolveSquares
##                    RowRequirements = list(set1to9 - set(SudokuToSolveRowsCopy[CheckingRow2]))
##                    RowRequirements = sorted(RowRequirements)
                    if SudokuToSolveRows[CheckingRow2][TryCell] == '?':
                        if RowRequirements[CheckingElementRequirement] in list(set1to9 - set(SudokuToSolveColumns[TryCell]) - set(SudokuToSolveSquares[TryCell//3 + (CheckingRow2//3)*3])):
                            AmountOfPlacesRows = AmountOfPlacesRows + 1
                            SaveCell = TryCell
                            SaveElement = CheckingElementRequirement#)
                        else:
                            SaveElement = 0
                    TryCell = TryCell + 1
                if AmountOfPlacesRows == 1:
                    SudokuToSolveRowsCopy[CheckingRow2][SaveCell] = RowRequirements[SaveElement]
                    SudokuToSolveCopy[CheckingRow2*9 + SaveCell] = SudokuToSolveRowsCopy[CheckingRow2][SaveCell]
                    SudokuToSolveColumnsCopy[SaveCell][CheckingRow2] = RowRequirements[SaveElement]
                    #breakpoint()
                    WeirdGlitchHelper = RowRequirements[SaveElement]# never mind, figured out glitch, but code stays :D
                    SudokuToSolveSquaresCopy[SaveCell//3 + (CheckingRow2//3)*3][(((CheckingRow2*9 + SaveCell)%27)//9)*3+(((CheckingRow2*9 + SaveCell)%27)%3)] = WeirdGlitchHelper
                    SudokuToSolveSquares = SudokuToSolveSquaresCopy
                    SudokuToSolveColumns = SudokuToSolveColumnsCopy
                    SudokuToSolveRows = SudokuToSolveRowsCopy
                    SudokuToSolve = SudokuToSolveCopy
                    change2 = 1
                CheckingElementRequirement = CheckingElementRequirement + 1
            CheckingRow2 = CheckingRow2 + 1
        loopcount2 = loopcount2 + 1
    print("Ran through algorithm2",loopcount2,"Times.")
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
    if SAS == 'y': 
        print("PuzzleList:",SudokuToSolve)#admin & debugging
        print("PuzzleList By Rows:",SudokuToSolveRows)
        print("PuzzleList BY Columns:",SudokuToSolveColumns)
        print("PuzzleList By Squares:",SudokuToSolveSquares)
def FinalCheck():
    CheckingHelper2 = 0
    LoopIndex7 = 0
    while LoopIndex7 < 9:
        if len(set(SudokuToSolveRows[LoopIndex7]) - set('?')) != len(SudokuToSolveRows[LoopIndex7]) - SudokuToSolveRows.count('?'):
            CheckingHelper2 = CheckingHelper2 + 1
        if len(set(SudokuToSolveColumns[LoopIndex7]) - set('?')) != len(SudokuToSolveColumns[LoopIndex7]) - SudokuToSolveColumns.count('?'):
            CheckingHelper2 = CheckingHelper2 + 1
        if len(set(SudokuToSolveSquares[LoopIndex7]) - set('?')) != len(SudokuToSolveSquares[LoopIndex7]) - SudokuToSolveSquares.count('?'):
            CheckingHelper2 = CheckingHelper2 + 1
        LoopIndex7 = LoopIndex7 + 1
    if CheckingHelper2 != 0:
        print("Error(s) in code.",CheckingHelper2,"Errors.")
        print(SudokuToSolve.count('?'),"remaining unknowns.")
    else:
        print("Solution Verified.")
DecryptInp()    #Receives user input string and makes the Sudoku Lists and matrices "SudokuToSolve..." for coding ease
Check1()        #Checks to make sure the user input a valid Sudoku puzzle before proceeding with algorithm
Algr1()         #Explicit Solver Algorithm -- Executes a loop of algorithm to solve the puzzle. SUMMARY: takes cell, finds possibilities, if one, takes that.
Algr2()        #Explicit Solver Algorithm -- Executes a loop of algorithm to solve the puzzle -- but in a different way. SUMMARY: takes columns/row/square, finds requirements, finds amount of requirement possible positions for each req, if one, takes that.
while '?'in SudokuToSolve and BreakoutHelper != 1:
    SudokuToSolveBreakout = SudokuToSolve
    Algr1()
    Algr2()
    if SudokuToSolveBreakout == SudokuToSolve:
        BreakoutHelper = 1
for x in range(1,20): # this could be for overriding loop breakout; needed for debugging
    Algr1()
    Algr2()
print("Final Solution:",SudokuToSolve)
if SAS == 'y': 
    print("Final Solution by Rows:",SudokuToSolveRows)
    print("Final Solution by Columns:",SudokuToSolveColumns)
    print("Final Solution by Squares:",SudokuToSolveSquares)
FinalCheck()
