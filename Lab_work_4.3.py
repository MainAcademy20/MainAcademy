dict = {'Elsa' : 24 , 'John' : 23 , 'Louise' : 20 , 'Trixi' : 26 , 'Brandon' : 18 , 'Emilie' : 5 }
word = 'Found Name'

def name_age (word , **name   , age = () ) :
    for name in dict.keys() :
        print( word , name )
        print(age)
    return

name_age(word , name = dict.get('Elsa')  )
name_age(word , name = dict.get('Elsa'), age = (0,1,2,3,4,5,6,7,8,9))
