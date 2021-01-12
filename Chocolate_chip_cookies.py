from kitchen import Rosemary
from kitchen.utensils import BakingTray, Bowl, Oven, Plate
from kitchen.ingredients import Egg, Salt, Flour, Butter, Sugar, ChocolateChips, BakingPowder

bowl = Bowl.use(name = 'batter')
butter = Butter.take('one part')
bowl.add(butter)
sugar = Sugar.take(grams=200)
bowl.add(sugar)
bowl.mix()
for i in range(2):
    egg = Egg.take()
    egg.crack()
    bowl.add(egg)
    bowl.mix()
bowl.add(Salt.take('pinch'))
for i in range(5):
    bowl.add(Flour.take(grams=60))
    bowl.add(ChocolateChips.take(grams=50))
    bowl.mix()
bowl.add(BakingPowder.take('a bit'))
bowl.mix()

oven = Oven.use()
oven.preheat(degrees=175)

tray = BakingTray.use(name='cookies')
for i in range(15):
    tray.add(bowl.take('1/15'))

oven.add(tray)
oven.bake(minutes=10)

plate = Plate.use()

cookie = tray.take()
plate.add(cookie)

Rosemary.serve(plate)

