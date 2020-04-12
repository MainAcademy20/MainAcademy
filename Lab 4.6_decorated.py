from Lab_4_6_decorators import bread, ingredients

@bread
@ingredients

def sandwich(food="--ветчина--"):
    print (food)

sandwich()