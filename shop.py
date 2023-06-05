class Shop():
    def __init__(self, shop_name,store_type):
        self.shop_name=shop_name
        self.store_type=store_type
        self.number_of_units=0
    def describe_shop(self):
        print(self.shop_name)
        print(self.store_type)
    def open_shop(self):
        print( f"{self.shop_name} ВІДЧИНЕНО")
    def set_number_of_units(self,num):
        self.number_of_units=num
    def increment_number_of_units(self,num):
        self.number_of_units+=num

shop=Shop('SinSay','clothes, footwear and household goods')
shop2=Shop('Rybna Lavka','seafood')
shop3=Shop('Tano','food')

print('№a')
shop.open_shop()
shop.describe_shop()

print('№b')
shop.describe_shop()
shop2.describe_shop()
shop3.describe_shop()

print('№c')
store=Shop('SANDALINO','footwear')
print(store.number_of_units)
store.number_of_units=7
print(store.number_of_units)

print('№d')
print(store.number_of_units)
shop.set_number_of_units(7)
print(shop.number_of_units)
shop.increment_number_of_units(15)
print(shop.number_of_units)

print('№e')
class Discount(Shop):
    def __init__(self, shop_name,store_type,discount_products):
        super().__init__(shop_name,store_type)
        self.discount_products=discount_products
    def get_discounts_ptoducts(self):
        print(f'Виводить акційні товари{self.discount_products}')
    def describe_shop(self):
        super().describe_shop()
        print(f'Зберігає акційні товари{self.discount_products}')

store_discount=Discount('Zara','clothes','T-shirt, dress, vest, sweater, suit')
store_discount.get_discounts_ptoducts()