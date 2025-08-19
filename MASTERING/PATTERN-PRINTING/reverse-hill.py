'''
   *  *  *  *  *  *  *  *  *
      *  *  *  *  *  *  *
         *  *  *  *  *
            *  *  *
               *
'''

def patter(dimension):
    for row in range(dimension):

        for column in range(row + 1):
            print("  ", end=" ")

        for second_column in range(dimension - row):
            print("* ", end=" ")

        for third_column in range(dimension - (row + 1)):
            print("* ", end=" ")

        print()

patter(5)