#write_function_to_calculate_accumulated_products_to_list.py
def accumulating_product(numbers):
    product = 1
    product_list = []

    for index in range(len(numbers)):
        product *= numbers[index]
        product_list.append(product)

    return product_list