from numpy import mean

#set the value_X Variable to a list
Value_X = [0, 0]
#define the
def my_average_function(Value_X):

    x = mean(Value_X)
    print(x)

print(my_average_function([1,2,3,4,5,6]))