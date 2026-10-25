class Dog():
    eyes = 2
    legs = 4
    tail = 'wavy'
    body = 'oval'

    def Bark(self):
        print('dog barked')

    def run(self):
        print('dog is running')

labradoodle = Dog()
husky = Dog()

print(labradoodle.tail)
print(husky.legs)

husky.run()
labradoodle.Bark()