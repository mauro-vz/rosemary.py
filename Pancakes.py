# import chef, untensiles and ingredients necessary
from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Egg, Salt, Flour, Milk

# make the batter by adding and mixing the ingredients
bowl = Bowl.use(name = 'batter')
for i in range(2):
    egg = Egg.take()
    egg.crack()
    bowl.add(egg)
bowl.mix()
bowl.add(Salt.take('dash'))
for i in range(5):
    flour_batch = Flour.take(grams=50)
    bowl.add(flour_batch)
bowl.mix()
for i in range(2):
    bowl.add(Milk.take(ml=250))
    bowl.mix()

# cook the batter on a pan and don't forget to flip the pancakes
pan = Pan.use(name='Pancakes')
plate = Plate.use()
for i in range(8):
    pan.add(bowl.take('1/8'))
    pan.cook(minutes=1)
    pan.flip()
    pan.cook(minutes=1)
    pancake = pan.take()
    plate.add(pancake)

Rosemary.serve(plate)