import datetime
import copy
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
N = int(name)
numberOfQueens = N;
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail


# Write your code here
ignoreQueenPos = [];
boardVersionsQueenPos = [];
board = []
for i in range(N):
    board.append([]);
    ignoreQueenPos.append([]);
    boardVersionsQueenPos.append([]);
    for j in range(N):
        board[i].append(0);

orgBoard = copy.deepcopy(board);
def is_attacked(board, i, j):
    # to check horizontal line
    if 1 not in board[i]:
        # to check vertical line
        for x in range(N):
            if board[x][j] == 1:
                return True;
    else:
        return True;

    # to check diagnosal line
    #print(board);
    if not attackedDiagnonally(board, i, j, -1, -1) and not attackedDiagnonally(board, i, j, -1, 1) and not attackedDiagnonally(board, i, j, 1, -1) and not attackedDiagnonally(board, i, j, 1, 1):
        return False;
    else:
        return True;

def attackedDiagnonally(board, i, j, tocheck, direction):
    if i < 0 or j < 0 or i == len(board) or j == len(board):
        return False;

    if board[i][j] == 1:
        return True;

    if attackedDiagnonally(board,i+tocheck,j+direction,tocheck,direction):
        return True;

    return False;

def countQueens(board):
    #print("countQueens");
    queens = 0;
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                queens += 1;

    return queens;

boardVersions = []
queenAssigned = False;
ignorePosition_i = [-1];
ignorePosition_j = [-1];
queenAssignedPosition_i = -1;
queenAssignedPosition_j = -1;
versionToGoBack = 0;
rolledBackVersion = -1;
print(boardVersionsQueenPos);
overallIterations = 0;
backtrackingCounter = 0;
print("Program Starts: " + str(datetime.datetime.now()));
log = open("log", "w+");
log.write("Program Starts: " + str(datetime.datetime.now()));
while numberOfQueens > 0:
    for i in range(N):
        queenAssigned = False;
        if 1 in board[i]:
            continue;
        
        for j in range(N):
            overallIterations += 1;
            # to ignore the previous Queen assigned position
            if len(ignoreQueenPos[i]) > 0 and j in ignoreQueenPos[i]:
                print("position " + str(i) + ',' + str(j) + " ignored");
                continue;
                
            if not is_attacked(board, i, j):
                print("position " + str(i) + ',' + str(j) + " not attacked - to assign a queen");
                
                board[i][j] = 1;
                boardVersions.append(copy.deepcopy(board));
                boardVersionsQueenPos[i].append(j);

                #print board
                for x in board:
                    print(x);
                
                numberOfQueens -= 1;
                queenAssigned = True;
                break;
        if not queenAssigned:
            #print("break if queen not assigned for a row");
            break;

    # not able to assign Queen
    # to go back to the previous version of the board
    if not queenAssigned:
        print("--------------------");
        print("oops! there is a mistake. not all queens could be assigned!");
        
        if len(boardVersions) > 0:
            versionToGoBack = len(boardVersions)-2;

            if versionToGoBack == -1:
                board = copy.deepcopy(orgBoard);
            elif versionToGoBack == -2:
                print("no board versions available to backtrack");
                break;
            else:
                board = copy.deepcopy(boardVersions[versionToGoBack])
                
            ignoreQueenPos[versionToGoBack+1].append(boardVersionsQueenPos[versionToGoBack+1][0]);
                
            numberOfQueens = N - countQueens(board);
            print("=============================================================================================================");
            print("Let's rollback to version: " + str(versionToGoBack));
            log.write('\n');
            log.write("Let's rollback to version: " + str(versionToGoBack));
            
            backtrackingCounter += 1;
            log.write('\n');
            log.write("Total Backtrackings: " + str(backtrackingCounter));
            log.write('\n');
            log.write("Total Iterations: " + str(overallIterations));
            
            for x in board:
                log.write('\n');
                log.write(str(x));
                print(x);
            log.write('\n');
            log.write("---");
            
            #remove unwanted board versions & queen pos tracking
            for x in range(len(boardVersions)-1, versionToGoBack, -1):
                if x > versionToGoBack:
                    boardVersions.pop(x);
                    boardVersionsQueenPos[x] = [];
                    if len(ignoreQueenPos) > x:
                        ignoreQueenPos[x+1] = []
            
            print("numberOfQueens yet to be assigned now: " + str(numberOfQueens));
            #print("Version: " + str(versionToGoBack));
            print("=============================================================================================================");
        else:
            print("no board versions available to backtrack");
            break;

print("=============================================================================================================");
print("=============================================================================================================");
print("=============================================================================================================");
#print board versions
#print("printing final board versions");
#for x in range(len(boardVersions)):
#    print("Index: " + str(x));
#    for y in boardVersions[x]:
#        print(y);
#    print("--");

print("printing final board");
log.write('\n');
log.write("=============================================================================================================");
log.write('\n');
log.write("Final Board");
for x in board:
    log.write('\n');
    log.write(str(x));
    print(x);
log.write('\n');
log.write("---");

print("----");
print("Total Backtracking: " + str(backtrackingCounter));
print("Total Iterations: " + str(overallIterations));
print("Program Ends: " + str(datetime.datetime.now()));
log.write('\n');
log.write("Total Backtracking: " + str(backtrackingCounter));
log.write('\n');
log.write("Total Iterations: " + str(overallIterations));
log.write('\n');
log.write("Program Ends: " + str(datetime.datetime.now()));
log.close();
