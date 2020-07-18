#Understand
## input is list of weights int, length int and limit int

## output is a tuple that has two weights that match the limit or None if
## it does not exist

## Have to go through in linear time which means a single pass through

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # for weight_1 in weights:
    #     for weight_2 in weights:
    #         if limit - (weight_1 + weight_2) == 0:
    #             if weight_1 > weight_2:
    #                 return (weight_1, weight_2)
    #             else:
    #                 return (weight_2, weight_1)

    # return None
    # weight_cache = {key:value for value, key in enumerate(weights)}

    weight_cache = {}

    for value, key in enumerate(weights):
        if key not in weight_cache:
            weight_cache[key] = [value]
        else:
            weight_cache[key].append(value) 
    
    for weight in weight_cache:
        if limit - weight in weight_cache:
            if weight_cache[weight][0] > weight_cache[limit - weight][0]:
                return (weight_cache[weight][0], weight_cache[limit - weight][0])
            elif weight == limit - weight:
                return (weight_cache[weight][1], weight_cache[weight][0])
            else:
                return (weight_cache[limit - weight][0], weight_cache[weight][0])
    return None