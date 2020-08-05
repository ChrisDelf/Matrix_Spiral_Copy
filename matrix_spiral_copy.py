def spiral_copy(inputMatrix):
  copy_array = []
  first_array = inputMatrix[0]
  number_of_columns = len(inputMatrix[0])
  number_of_rows = len(inputMatrix)
  bottom_array = inputMatrix[number_of_rows - 1]
  
  columns = 0
  y = 0
  z = 0

  for x in first_array:
    copy_array.append(x)
    
  for x in range(1, number_of_columns - 1):
    
    copy_array.append(inputMatrix[x][number_of_columns-1])
  
  for x in range(0, number_of_columns - 1):
    copy_array.append(bottom_array[(number_of_columns - 2) - y])
    y += 1
    
  for x in range(1, number_of_rows - 1):
    copy_array.append(inputMatrix[(number_of_rows - 2) - z][0])
    z += 1
  for x in range(1, number_of_columns - 1):
    copy_array.append(inputMatrix[1][x])
  
  for x in range(2, number_of_columns - 2):
    copy_array.append(inputMatrix[x][ number_of_columns-2])
    
  for x in range(2, number_of_columns - 1):
    copy_array.append(inputMatrix[number_of_rows - 2][(number_of_columns - 1)- x])
    z += 1 
  
  return copy_array      
  
      
    
    
    
inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]
  
  
print(spiral_copy(inputMatrix))
