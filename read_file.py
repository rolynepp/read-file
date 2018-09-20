import os #operating system

def read_file(filename):
    products = []
    with open(filename, 'r') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q': #quit
            break
        price = input('請輸入價格: ')
        price = int(price)
    #p = []
    #p.append(name)
    #p.append(price) 下方為清單簡化
        p = [name, price]
        products.append(p)
    print(products)
    return products


#印出所有的購買紀錄

def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])


#寫入檔案:
def write_file(filename,products):
    with open(filename, 'w') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ','+ str(p[1]) + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):#檢查檔案   
        print('有此檔案')
        products = read_file(filename) #執行檔案   
    else:
        print('無此檔案')

    products = user_input(products) #又把products存進去
    print_products(products)
    write_file(filename, products)

main()