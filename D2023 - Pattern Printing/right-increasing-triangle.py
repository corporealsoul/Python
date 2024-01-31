'''
               *
            *  *
         *  *  *
      *  *  *  *
   *  *  *  *  *
'''

def patter(dimension):
    for row in range(dimension):

        for column in range(dimension - row):
            print("  ", end=" ")

        for second_column in range(row + 1):
            print("* ", end=" ")

        print()

patter(5)