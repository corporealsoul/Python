# print ("Hey world !")


# def myfunc(name):
#     print('Hello {}'.format(name))
#
# myfunc('Name')


# def myfunc(*args):
#     return list(args)
#
# result = myfunc(5,6,7,8)
# print(result)

def myfunc(input_string):
    result_string = ""
    for index, char in enumerate(input_string):
        if index % 2 == 0:
            result_string += char.lower()
        else:
            result_string += char.upper()
    return result_string

print(myfunc('Anthropomorphism'))  # Output: 'aNtHrOpOmOrPhIsM'
