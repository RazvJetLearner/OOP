
class Phone():
    shape = 'square'
    camera = 2
    screen = "3 by 9"
    charging_port = 'USBC'

    def Photo(self):
        print("phone took picture")

    def Call(self):
        print('phone is calling')



samsung = Phone()
Iphone = Phone()

print(samsung.shape)
print(Iphone.screen)

samsung.Photo()
Iphone.Call()