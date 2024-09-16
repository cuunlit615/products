products = []
while True:
    name = input('Product name:')
    if name == 'q':
        break
    price = input('Products price:')
    # A
    # p = []
    # p.append(name)
    # p.append(price)
    # products.append(p)
    # B
    # p = [name, price]
    #C
    products.append([name, price])
print(products)