'''
*  *  *  *  *
*  *  *  *
*  *  *
*  *
*
'''


# def patter(dimension):
#     for row in range(dimension):
#         for column in range(row, dimension):
#             print("* ", end=" ")
#         print()
#
# patter(5)


def patter(dimension):
    for row in range(dimension):
        for column in range(dimension - row):
            print("* ", end=" ")
        print()

patter(5)