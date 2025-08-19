'''
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *
'''

def patter(dimension):
    for row in range(dimension):
        for column in range(dimension):
            print("* ", end=" ")
        print()

patter(5)