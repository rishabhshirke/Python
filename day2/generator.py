# def test_sequence():
#     num = 0
#     while num < 10:
#         yield num
#         num += 1
# for i in test_sequence():
#        print(i, end=",")

# print()
# def reverse_str(test_str):
#     length = len(test_str)
#     for i in range(length - 1, -1, -1):
#         yield test_str[i]
# for char in reverse_str("Trojan"):
#     print(char,end =" ")


# def generator_function(arg):

#     yield #somevalue


def gen_func(n):
    value=0

    while(value<n):
        yield value #yield is used to produce value from generator function
        value+=1

# g=gen_func(3)
# print(next(g))
# for i in gen_func(5):
#     print(i)


#Generator Expressions
#produces the values of expression for each item in the 
#iterable, one at a time, when iterated over.

# list1=[1,2,3,4,5,6]

# x=(x for x in list1)
# for i in x:
#     print(i)