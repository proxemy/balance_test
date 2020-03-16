




class Skill():

	def __init__(self, damage: int, range: int, cooldown: int, activation_time: int):

		self.damage = damage
		self.range = range
		self.cooldown = cooldown
		self.activation_time = activation_time

		self.cooldown_ticks = 0
		self.activation_ticks = 0

