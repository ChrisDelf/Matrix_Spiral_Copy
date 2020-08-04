def spiral_copy(inputMatrix):
  copy_array = []
  first_array = inputMatrix[0]
  number_of_columns = len(inputMatrix[0])
  columns = 0
  y = 1
  print("number of columns", number_of_columns)
  for x in first_array:
    copy_array.append(x)
    
  for columns in inputMatrix[y]:
    copy_array.append(columns[number_of_columns - 1])
    y += 1
    
  return copy_array
  
    
  
      
  
      
    
    
    
inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]
  
  
print(spiral_copy(inputMatrix))
