#  knapsack_problem.py Using a bottom up approach of dynamic programming, solving the famous knapsack problem.
#  Assume that the data is given in list of list, with the index being the item number. The first element is weight
#  second is the value of the respective item.

def max_value(lofl, c):
    number_of_items = len(lofl)
    array_of_weights = []
    dict_of_weights = dict()
    dict_of_values = dict()
    for n in range(number_of_items):  # Fills in the values for each respective item's weight and value
        dict_of_values[n] = lofl[n][1]
        dict_of_weights[n] = lofl[n][0]
        #  Creating an array of sets and respective max value. Index indicates weight, first element is the set of
        #  items it contains, second element is the value.
    for x in range(c+1):
        array_of_weights.append([set(), 0])
    for weight in range(c+1):  # Iterates once through all the weights leading up to the constraint
        tmp_max = 0
        for item in range(number_of_items):  # Iterates through the possible items
            tmp_value = 0
            weight_of_item = dict_of_weights[item]
            value_of_item = dict_of_values[item]
            #  If the item is light enough to be considered, it's weight is subtracted from the current weight and
            #  its value is added to the previously solved weights. Note that using a set allows items to not be double
            #  counted.
            if weight_of_item <= weight:
                tmp_set = array_of_weights[weight - weight_of_item][0].copy()
                tmp_set.add(item)
                tmp_value = [dict_of_values[x] for x in tmp_set]
                tmp_value = sum(tmp_value)
            #  The max value and its respective set is added to the array for the given weight
            if tmp_value > tmp_max:
                tmp_max = tmp_value
                array_of_weights[weight][0] = tmp_set.copy()
                array_of_weights[weight][1] = tmp_max
    print(f"The Max value of items is {array_of_weights[c][1]} and its contains items {array_of_weights[c][0]}")

max_value([[1,5], [10,2], [5,1], [11,15]], 30)



