from skill import Skill




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


	def fight(self, target) -> bool:

		if not self.in_range_to(target):
			self.move_to(target)

		else:
			self.attack(target)

		return target.health <= 0


	def in_range_to(self, target) -> bool:
		#TODO: check all skill ranges for further actions
		return abs(self.position - target.position) < self.skills[0].range

	def move_to(self, target):
		
		if self.position < target.position:
			direc

	def attack(self, target):
		#TODO
		pass

