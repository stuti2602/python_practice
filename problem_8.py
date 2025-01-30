import numpy as np
"""
day_8 : problem_8

you are given nested list representing 2D matrix of numerical values .
write a pyhton function to apply the softmax function to each row of the matrix and then return the index of highest 
value(maxmium probability) from the softmax result for each row. 

the formula for the softmax of an element xi in a row is :
softmax(xi) = e^xi/Eje^xi

input:
nested_list = [[2.0,1.0,0.1],
[1.0,3.0,0.2]]

output:
[0,1]
"""


def softmax_function(nested_list):
    output = []
    

    for list in nested_list:
        exp_val = []
        for element in list:
            exp_val.append(np.exp(element))
        # print(exp_val)

        softmax = []
        for value in exp_val:
            softmax.append(value/sum(exp_val))
        print(softmax)

        max_index = softmax.index(max(softmax))
        output.append(max_index)
    print(output)

def main():
    nested_list = [[1,2,3],[3,4,5],[5,6,7]]
    output = softmax_function(nested_list)
    output

if __name__ == "__main__":
    main()
