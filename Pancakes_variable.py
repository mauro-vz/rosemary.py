# import chef, untensiles and ingredients necessary
from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Egg, Salt, Flour, Milk

# create variable for number of pancakes desired 

n_pancakes = 50
n_eggs = int(n_pancakes/4)
g_flour = int(n_pancakes*31.25)
ml_milk = int(n_pancakes*62.5)

# make the batter by adding and mixing the ingredients
bowl = Bowl.use(name = 'batter')
for i in range(n_eggs):
    egg = Egg.take()
    egg.crack()
    bowl.add(egg)
bowl.mix()
bowl.add(Salt.take('dash'))
for i in range(g_flour):
    flour_batch = Flour.take(grams=50)
    bowl.add(flour_batch)
bowl.mix()
for i in range(2):
    bowl.add(Milk.take(ml=ml_milk/2))
    bowl.mix()

# cook the batter on a pan and don't forget to flip the pancakes
pan = Pan.use(name='Pancakes')
plate = Plate.use()
for i in range(n_pancakes):
    pan.add(bowl.take(f'1/{n_pancakes}'))
    pan.cook(minutes=1)
    pan.flip()
    pan.cook(minutes=1)
    pancake = pan.take()
    plate.add(pancake)

Rosemary.serve(plate)