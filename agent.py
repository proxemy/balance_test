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

	def __repr__(self):

		name = lambda n : "\033[4m" + str(n) + "\033[0m"
		hp = lambda h : "\033[92m" + str(h) + "\033[0m"
		pos = lambda p : "\033[94m" + str(p) + "\033[0m"


		return \
			name(self.name) +": " +\
			"HP(" + hp(self.health) + "), "\
			"Pos(" + pos(self.position) + ")"


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

