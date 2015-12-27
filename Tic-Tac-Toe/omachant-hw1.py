def print_board():
    for i in range(0,3):
        for j in range(0,3):
            print map[2-i][j],
            if j != 2:
                print "|",
        print ""


def check_done():
    for i in range(0,3):
        if map[i][0] == map[i][1] == map[i][2] != " " \
        or map[0][i] == map[1][i] == map[2][i] != " ":
            print turn, "Won!!!"
            return True
        
    if map[0][0] == map[1][1] == map[2][2] != " " \
    or map[0][2] == map[1][1] == map[2][0] != " ":
        print turn, "Won!!!"
        return True

    if " " not in map[0] and " " not in map[1] and " " not in map[2]:
        print "Draw!!"
        return True
        

    return False

def check_for_win():
    if turn == "X":
       for i in range(0,3):
           if map[i][0] == map[i][1] == "X":
              if map[i][2] == " ":
                  map[i][2] = "X"
                  return True
           elif map[i][0] == map[i][2] == "X":
              if map[i][1] == " ":
                  map[i][1] = "X"
                  return True
           elif map[i][1] == map[i][2] == "X":
              if map[i][0] == " ":
                  map[i][0] = "X"
                  return True
           elif map[0][i] == map[1][i] == "X":
              if map[2][i] == " ":
                  map[2][i] = "X"
                  return True
           elif map[0][i] == map[2][i] == "X":
              if map[1][i] == " ":
                  map[1][i] = "X"
                  return True
           elif map[1][i] == map[2][i] == "X":
              if map[0][i] == " ":
                  map[0][i] = "X"
                  return True
           elif map[0][0] == map[1][1] == "X":
              if map[2][2] == " ":
                  map[2][2] = "X"
                  return True
           elif map[0][0] == map[2][2] == "X":
              if map[1][1] == " ":
                  map[1][1] = "X"
                  return True
           elif map[1][1] == map[2][2] == "X":
              if map[0][0] == " ":
                  map[0][0] = "X"
                  return True
           elif map[0][2] == map[1][1] == "X":
              if map[2][0] == " ":
                  map[2][0] = "X"
                  return True
           elif map[0][2] == map[2][0] == "X":
              if map[1][1] == " ":
                  map[1][1] = "X"
                  return True
           elif map[2][0] == map[1][1] == "X":
              if map[0][2] == " ":
                  map[0][2] = "X"
                  return True

    else:
        for i in range(0,3):
           if map[i][0] == map[i][1] == "O":
              if map[i][2] == " ":
                  map[i][2] = "O"
                  return True
           elif map[i][0] == map[i][2] == "O":
              if map[i][1] == " ":
                  map[i][1] = "O"
                  return True
           elif map[i][1] == map[i][2] == "O":
              if map[i][0] == " ":
                  map[i][0] = "O"
                  return True
           elif map[0][i] == map[1][i] == "O":
              if map[2][i] == " ":
                  map[2][i] = "O"
                  return True
           elif map[0][i] == map[2][i] == "O":
              if map[1][i] == " ":
                  map[1][i] = "O"
                  return True
           elif map[1][i] == map[2][i] == "O":
              if map[0][i] == " ":
                  map[0][i] = "O"
                  return True
           elif map[0][0] == map[1][1] == "O":
              if map[2][2] == " ":
                  map[2][2] = "O"
                  return True
           elif map[0][0] == map[2][2] == "O":
              if map[1][1] == " ":
                  map[1][1] = "O"
                  return True
           elif map[1][1] == map[2][2] == "O":
              if map[0][0] == " ":
                  map[0][0] = "O"
                  return True
           elif map[0][2] == map[1][1] == "O":
              if map[2][0] == " ":
                  map[2][0] = "O"
                  return True
           elif map[0][2] == map[2][0] == "O":
              if map[1][1] == " ":
                  map[1][1] = "O"
                  return True
           elif map[2][0] == map[1][1] == "O":
              if map[0][2] == " ":
                  map[0][2] = "O"
                  return True
        
    return False

# Defines machine play


def program_play():
    
#Blocks the center cell intially(when the map is empty), if program has the first turn
    for i in range(0,3):
      for j in range(0,3):
        if map[i][j] == " ":
            check = 0
        else:
            global check_there
            check_there = 1
            
            
    if check_there == 0:
            if turn == "X":
                if map[1][1] == " ":
                 map[1][1] = "X"
                 global win_win
                 win_win = True
                 return True
            else:
                if map[1][1] == " ":
                    map[1][1] = "O"
                    win_win = True
                    return True
    
    #To win if the program plays first and choses center
    if win_win == True and pos in {1,3,7,9}:
        if turn == "X":
            
            win_win = False
            if pos == 1:
                if map[2][2] == " ":
                    map[2][2] = "X"
                    return True
            if pos == 3:
                if map[2][0] == " ":
                    map[2][0] = "X"
                    return True
            if pos == 7:
                if map[0][2] == " ":
                    map[0][2] = "X"
                    return True
            if pos == 9:
                if map[0][0] == " ":
                    map[0][0] = "X"
                    return True
        else:
            win_win = False
            if pos == 1:
                if map[2][2] == " ":
                    map[2][2] = "O"
                    return True
            if pos == 3:
                if map[2][0] == " ":
                    map[2][0] = "O"
                    return True
            if pos == 7:
                if map[0][2] == " ":
                    map[0][2] = "O"
                    return True
            if pos == 9:
                if map[0][0] == " ":
                    map[0][0] = "O"
                    return True

    #if the user plays first and choses edges/corners, program blocks center
    if pos in {1,3,7,9,2,4,6,8}:
        if turn == "X":
            if map[1][1] == " ":
                map[1][1] = "X"
                return True
        else:
            if map[1][1] == " ":
                map[1][1] = "O"
                return True

    #To if the user choses center instead, program blocks the top right corner
    if pos == 5:
        global cunning_win
        cunning_win = True
        if turn == "X":
            if map[0][0] == map[0][1] == map[0][2] == map[1][0] == " " \
            and map[1][0] == map[1][2] == " "\
            and map[2][0] == map[2][1] == map[2][2] == " ":
                map[2][2] = "X"
                return True
        else:
            if map[0][0] == map[0][1] == map[0][2] == map[1][0] == " " \
            and map[1][0] == map[1][2] == " "\
            and map[2][0] == map[2][1] == map[2][2] == " ":
                map[2][2] = "O"
                return True

    #To win if the user plays first and choses center
    if cunning_win == True and pos in {1,3,7}:
        winning_chance = check_for_win()
        if winning_chance == True:
                 return True
        else:
            if turn == "X":
                cunning_win = False
                if pos == 1:
                    if map[0][2] == " ":
                        map[0][2] = "X"
                        return True
                    elif map[2][0] == " ":
                         map[2][0] = "X"
                         return True
                if pos == 3:
                    if map[0][0] == " ":
                        map[0][0] = "X"
                        return True
                    elif map[2][0] == " ":
                         map[2][0] = "X"
                         return True
                if pos == 7:
                    if map[0][0] == " ":
                        map[0][0] = "X"
                        return True
                    elif map[0][2] == " ":
                         map[0][2] = "X"
                         return True
            else:
                cunning_win = False
                if pos == 1:
                    if map[0][2] == " ":
                        map[0][2] = "O"
                        return True
                    elif map[2][0] == " ":
                         map[2][0] = "O"
                         return True
                if pos == 3:
                    if map[0][0] == " ":
                        map[0][0] = "O"
                        return True
                    elif map[2][0] == " ":
                         map[2][0] = "O"
                         return True
                if pos == 7:
                    if map[0][0] == " ":
                        map[0][0] = "O"
                        return True
                    elif map[0][2] == " ":
                         map[0][2] = "O"
                         return True
            
    #checks for similarities row wise and column wise to fill the third cell
    for i in range(0,3):
        if map[i][0] == map[i][1] == "X" \
        or map[i][0] == map[i][1] == "O" :
            winning_chance = check_for_win()
            if winning_chance == True:
                 return True
            else:
                if turn == "X":
                    if map[i][2] == " ":
                        map[i][2] = "X"
                        return True
                else:
                    if map[i][2] == " ":
                        map[i][2] = "O"
                        return True

        if map[i][0] == map[i][2] == "X" \
        or map[i][0] == map[i][2] == "O" :
            winning_chance = check_for_win()
            if winning_chance == True:
                 return True
            else:
                if turn == "X":
                    if map[i][1] == " ":
                        map[i][1] = "X"
                        return True
                else:
                    if map[i][1] == " ":
                        map[i][1] = "O"
                        return True

        if map[i][1] == map[i][2] == "X" \
        or map[i][1] == map[i][2] == "O" :
            winning_chance = check_for_win()
            if winning_chance == True:
                 return True
            else:
                if turn == "X":
                    if map[i][0] == " ":
                        map[i][0] = "X"
                        return True
                else:
                    if map[i][0] == " ":
                        map[i][0] = "O"
                        return True


        if map[0][i] == map[1][i] == "X" \
        or map[0][i] == map[1][i] == "O" :
            winning_chance = check_for_win()
            if winning_chance == True:
                 return True
            else:
                if turn == "X":
                    if map[2][i] == " ":
                        map[2][i] = "X"
                        return True
                else:
                    if map[2][i] == " ":
                       map[2][i] = "O"
                       return True

        

        if map[0][i] == map[2][i] == "X" \
        or map[0][i] == map[2][i] == "O" :
            winning_chance = check_for_win()
            if winning_chance == True:
                 return True
            else:
                if turn == "X":
                    if map[1][i] == " ":
                        map[1][i] = "X"
                        return True
                else:
                    if map[1][i] == " ":
                        map[1][i] = "O"
                        return True

               

        if map[1][i] == map[2][i] == "X" \
        or map[1][i] == map[2][i] == "O" :
            winning_chance = check_for_win()
            if winning_chance == True:
                 return True
            else:
                if turn == "X":
                    if map[0][i] == " ":
                        map[0][i] = "X"
                        return True
                else:
                    if map[0][i] == " ":
                        map[0][i] = "O"
                        return True

    # checks for similarities diagonally
    if map[0][0] == map[1][1] == "X" \
    or map[0][0] == map[1][1] == "O" :
        winning_chance = check_for_win()
        if winning_chance == True:
                 return True
        else:
                if turn == "X":
                    if map[2][2] == " ":
                        map[2][2] = "X"
                        return True
                else:
                    if map[2][2] == " ":
                        map[2][2] = "O"
                        return True

    if map[0][0] == map[2][2] == "X" \
    or map[0][0] == map[2][2] == "O" :
        winning_chance = check_for_win()
        if winning_chance == True:
                 return True
        else:
                if turn == "X":
                    if map[1][1] == " ":
                        map[1][1] = "X"
                        return True
                else:
                    if map[1][1] == " ":
                        map[1][1] = "O"
                        return True

    if map[1][1] == map[2][2] == "X" \
    or map[1][1] == map[2][2] == "O" :
        winning_chance = check_for_win()
        if winning_chance == True:
                 return True
        else:
                if turn == "X":
                    if map[0][0] == " ":
                        map[0][0] = "X"
                        return True
                else:
                    if map[0][0] == " ":
                        map[0][0] = "O"
                        return True

    if map[0][2] == map[1][1] == "X" \
    or map[0][2] == map[1][1] == "O" :
        winning_chance = check_for_win()
        if winning_chance == True:
                 return True
        else:
                if turn == "X":
                    if map[2][0] == " ":
                        map[2][0] = "X"
                        return True
                else:
                    if map[2][0] == " ":
                        map[2][0] = "O"
                        return True

    if map[0][2] == map[2][0] == "X" \
    or map[0][2] == map[2][0] == "O" :
        winning_chance = check_for_win()
        if winning_chance == True:
                 return True
        else:
                if turn == "X":
                    if map[1][1] == " ":
                        map[1][1] = "X"
                        return True
                else:
                    if map[1][1] == " ":
                        map[1][1] = "O"
                        return True

    if map[1][1] == map[2][0] == "X" \
    or map[1][1] == map[2][0] == "O" :
        winning_chance = check_for_win()
        if winning_chance == True:
                 return True
        else:
                if turn == "X":
                    if map[0][2] == " ":
                        map[0][2] = "X"
                        return True
                else:
                    if map[0][2] == " ":
                        map[0][2] = "O"
                        return True        

    # check to fill the third cell when no similar cells diagonally
    if map[0][0] != map[1][1] != " ":
        winning_chance = check_for_win()
        if winning_chance == True:
                 return True
        else:
                if turn == "X":
                    if map[2][2] == " ":
                        map[2][2] = "X"
                        return True
                else:
                    if map[2][2] == " ":
                        map[2][2] = "O"
                        return True

    if map[0][0] != map[2][2] != " ":
        winning_chance = check_for_win()
        if winning_chance == True:
                 return True
        else:
                if turn == "X":
                    if map[1][1] == " ":
                        map[1][1] = "X"
                        return True
                else:
                    if map[1][1] == " ":
                        map[1][1] = "O"
                        return True

    if map[1][1] != map[2][2] != " ":
        winning_chance = check_for_win()
        if winning_chance == True:
                 return True
        else:
                if turn == "X":
                    if map[0][0] == " ":
                        map[0][0] = "X"
                        return True
                else:
                    if map[0][0] == " ":
                        map[0][0] = "O"
                        return True

    if map[0][2] != map[1][1] != " ":
        winning_chance = check_for_win()
        if winning_chance == True:
                 return True
        else:
                if turn == "X":
                    if map[2][0] == " ":
                        map[2][0] = "X"
                        return True
                else:
                    if map[2][0] == " ":
                        map[2][0] = "O"
                        return True

    if map[0][2] != map[2][0] != " ":
        winning_chance = check_for_win()
        if winning_chance == True:
                 return True
        else:
                if turn == "X":
                    if map[1][1] == " ":
                        map[1][1] = "X"
                        return True
                else:
                    if map[1][1] == " ":
                        map[1][1] = "O"
                        return True

    if map[1][1] != map[2][0] != " ":
        winning_chance = check_for_win()
        if winning_chance == True:
                 return True
        else:
                if turn == "X":
                    if map[0][2] == " ":
                        map[0][2] = "X"
                        return True
                else:
                    if map[0][2] == " ":
                        map[0][2] = "O"
                        return True          

    # checks to fill third cell when no similar cells row/column wise
    for i in range(0,3):
        if map[i][0] != map[i][1] != " ":
            winning_chance = check_for_win()
            if winning_chance == True:
                 return True
            else:
                if turn == "X":
                    if map[i][2] == " ":
                        map[i][2] = "X"
                        return True
                else:
                    if map[i][2] == " ":
                        map[i][2] = "O"
                        return True

        if map[i][0] != map[i][2] != " ":
            winning_chance = check_for_win()
            if winning_chance == True:
                 return True
            else:
                if turn == "X":
                    if map[i][1] == " ":
                        map[i][1] = "X"
                        return True
                else:
                    if map[i][1] == " ":
                        map[i][1] = "O"
                        return True

        if map[i][1] != map[i][2] != " ":
           winning_chance = check_for_win()
           if winning_chance == True:
                 return True
           else:
                if turn == "X":
                    if map[i][0] == " ":
                        map[i][0] = "X"
                        return True
                else:
                    if map[i][0] == " ":
                        map[i][0] = "O"
                        return True


        if map[0][i] != map[1][i] != " ":
           winning_chance = check_for_win()
           if winning_chance == True:
                 return True
           else:
                if turn == "X":
                   if map[2][i] == " ":
                      map[2][i] = "X"
                      return True
                else:
                   if map[2][i] == " ":
                        map[2][i] = "O"
                        return True

        

        if map[0][i] != map[2][i] != " ":
           winning_chance = check_for_win()
           if winning_chance == True:
                 return True
           else:
                if turn == "X":
                    if map[1][i] == " ":
                        map[1][i] = "X"
                        return True
                else:
                    if map[1][i] == " ":
                        map[1][i] = "O"
                        return True

               

        if map[1][i] != map[2][i] != " ":
           winning_chance = check_for_win()
           if winning_chance == True:
                 return True
           else:
                if turn == "X":
                    if map[0][i] == " ":
                        map[0][i] = "X"
                        return True
                else:
                    if map[0][i] == " ":
                        map[0][i] = "O"
                        return True


    return False

#Takes user input and set such that X goes first

choice = raw_input("Please enter if you want to play X or O ")
if choice == "X":
   turn = choice
else:
   turn = "X"

map = [[" "," "," "],
       [" "," "," "],
       [" "," "," "]]

#variable declaration
done = False
win_win = False
cunning_win = False
global winning_chance
winning_chance = False
global check_there
check_there = 0

#
while done != True:
  
  # checks if the user or program will take X and play. 'X' always goes first.
  if turn != choice:
      print turn, "'s turn"
      result = program_play() #call to the program to play
      done = check_done()
      print_board()
      if result == True:
         if turn == "X":
            turn = "O"
         else:
            turn = "X"
            
  if done == False:
     
      print turn, "'s turn"
      moved = False
      while moved != True:
            print "Please select position by typing in a number between 1 and 9, see below for which number that is which position..."
            print "7|8|9"
            print "4|5|6"
            print "1|2|3"
            print

            try:
                pos = input("Select: ")
                if pos <=9 and pos >=1:
                    Y = pos/3
                    X = pos%3
                    if X != 0:
                        X -=1
                    else:
                         X = 2
                         Y -=1
                        
                    if map[Y][X] == " ":
                        map[Y][X] = turn
                        print_board()
                        moved = True
                        prev_pos = pos
                        done = check_done()
                    
                        if done == False:
                            if turn == "X" or turn != choice: 
                                turn = "O"
                            else:
                                turn = "X"
                    else:
                        print "Position filled. Please select an empty one!"
                                
                    
                
            except:
                print "You need to add a numeric value"
