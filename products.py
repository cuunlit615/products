products = []
while True:
    name = input('Product name:')
    if name == 'q':
        break
    price = input('Products price:')
    price = int(price)
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

for p in products:
    print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')