




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
