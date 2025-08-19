'''
               *
            *  *  *
         *  *  *  *  *
      *  *  *  *  *  *  *
   *  *  *  *  *  *  *  *  *
      *  *  *  *  *  *  *
         *  *  *  *  *
            *  *  *
               *
'''

def patter(dimension):
    for t_row in range(dimension - 1):

        for t_column in range(dimension - t_row):
            print("  ", end=" ")

        for t_second_column in range(t_row + 1):
            print("* ", end=" ")

        for t_third_column in range(t_row):
            print("* ", end=" ")

        print()

    for b_row in range(dimension):

        for b_column in range(b_row + 1):
            print("  ", end=" ")

        for b_second_column in range(dimension - b_row):
            print("* ", end=" ")

        for b_third_column in range(dimension - (b_row + 1)):
            print("* ", end=" ")

        print()

patter(5)