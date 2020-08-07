def spiral_2(inputMatrix):
  copy_array = []
  column_num = len(inputMatrix[0])
  row_num = len(inputMatrix)
  top_row = 0
  btm_row = row_num - 1
  left_column = 0
  right_column = column_num - 1
  count = 0
  y = 1
  z = 1
  
  # every time we go across to the end of the row we have to subtract the amount columns by 1
  # do the same when we go down a column
  while (top_row <= btm_row and left_column <= right_column):
   # print("loop count", count)
    # this handles the top row
    for x in range(left_column, right_column):
      
      
      copy_array.append(inputMatrix[top_row][x])
    top_row += 1
      
      # this handles the right column
    
    for x in range(top_row - 1, btm_row):
      
      copy_array.append(inputMatrix[x][right_column])
    right_column -= 1
      
      # want handle the bottom row
    if(top_row <= btm_row):
      #we have to go in reverse
      for x in range(left_column - y, right_column):
        copy_array.append(inputMatrix[btm_row][right_column - x])
      btm_row -= 1
      y += 1
    
   # print("column", left_column, "right column", right_column)
    if(left_column <= right_column):
      for x in range(top_row - z, btm_row):
        print(inputMatrix[btm_row - x][left_column])
        copy_array.append(inputMatrix[btm_row - x][left_column])
      z += 1
      left_column +=1
      count += 1
    #  print("end of loop", "top_row :", top_row, "btm_row :", btm_row, "left_column :", left_column, "right_column :", right_column)
  return copy_array    
      
    
      
  
      
    
    
    
inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]
  
  
print(spiral_2(inputMatrix))
