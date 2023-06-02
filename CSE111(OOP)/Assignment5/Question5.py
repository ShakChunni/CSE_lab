#question5

class Pokemon:
    def __init__(self,n1,n2,n3,n4,n5):
        self.pokemon1_name=n1
        self.pokemon2_name=n2
        self.pokemon1_power=n3
        self.pokemon2_power=n4
        self.damage_rate=n5

team_pika = Pokemon('pikachu', 'charmander', 90, 60, 10)
print('=======Team 1=======')
print('Pokemon 1:',team_pika.pokemon1_name,
team_pika.pokemon1_power)
print('Pokemon 2:',team_pika.pokemon2_name,
team_pika.pokemon2_power)
pika_combined_power = (team_pika.pokemon1_power +
team_pika.pokemon2_power) * team_pika.damage_rate
print('Combined Power:', pika_combined_power)

team_bulb=Pokemon("bulbasaur","squirtle",80,70,9)
print("=======Team 2=======")
print("Pokemon1:", team_bulb.pokemon1_name, team_bulb.pokemon1_power)
print("Pokemon2:", team_bulb.pokemon2_name, team_bulb.pokemon2_power)
bulb_combined_power=(team_bulb.pokemon1_power+team_bulb.pokemon2_power)*team_bulb.damage_rate
print("Combined Power:", bulb_combined_power)

