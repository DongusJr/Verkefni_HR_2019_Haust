def get_list(vector_size):
    dot_product_list = []
    for i in range(2):
        dot_product_inner_list = []
        for j in range(vector_size):
            element = float(input("Element no {}: ".format(j+1)))
            dot_product_inner_list.append(element)
        dot_product_list.append(dot_product_inner_list)
    return dot_product_list

def get_sum(dot_product, vector_size):
    dot_sum = 0
    for i in range(vector_size):
        dot_sum += dot_product[0][i]*dot_product[1][i]
    return dot_sum

# Main program starts here
# Should only be a sequence of function calls
vector_size = int(input("Input vector size: "))
dot_product_list = get_list(vector_size)
dot_sum = get_sum(dot_product_list, vector_size)
print("Dot product is: {}".format(dot_sum))
