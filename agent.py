from skill import Skill

from pdb import set_trace as BP


class Agent():
	"""
	The Agent class represents a basic Agent in combat.
	"""

	def __init__(self, name: str, skills: list):
		self.name = name
		self.skills = skills
		self.health = 1000
		self.move_speed = 10
		self.position = None
	
	def colored(self, var: str):
		
		color_map = \
		{
			"name" :	"\033[4m",	# underlined
			"health" :	"\033[92m",	# green
			"position":	"\033[94m"	# blue
		}

		if var not in vars(self).keys():
			raise Exception("Can't get colored variable '{}' for agent.".format(var))

		val_str = str(vars(self)[var])
		
		if var in color_map.keys():
			return color_map[var] + val_str + "\033[0m"

		return val_str


	def __repr__(self):
		return \
			self.colored("name") +": " +\
			"HP(" + self.colored("health") + "), "\
			"Pos(" + self.colored("position") + ")"


	def fight(self, target) -> bool:

		if not self.in_range_to(target):
			self.move_to(target)

		else:
			self.attack(target)

		return target.health <= 0


	def get_distance_to(self, target):
		return abs(self.position - target.position)


	def in_range_to(self, target) -> bool:
		#TODO: check all skill ranges for further actions
		return self.get_distance_to(target) <= self.skills[0].range

	def move_to(self, target):
		direction = 0
		
		if self.position < target.position:
			direction = 1
		elif self.position > target.position:
			direction = -1

		dist = self.get_distance_to(target)

		if dist >= self.move_speed:
			dist = self.move_speed

		self.position += dist * direction

	def attack(self, target):
		#TODO: determine best skill to use
		target.health -= self.skills[0].damage

