
#from pdb import set_trace as BP




class Position():
	def __init__(self, x=None, y=None, z=None):
		self.x, self.y, self.z = (x, y, z)


	def distance_to(self, pos):
		return abs(self.x - pos.x)


	def direction_to(self, pos):
		if pos.x == self.x:
			return 0
		return (pos.x - self.x) / abs(pos.x - self.x)


	def __repr__(self):
		return "(" + \
			",".join(str(p) for p in (self.x, self.y, self.z) if p is not None) + \
			")"



class Agent():
	"""
	The Agent class represents a basic Agent in combat.
	"""


	def __init__(self, name: str, skills: list):
		self.name = name
		self.skills = skills
		self.health = 1000
		self.move_speed = 10
		self.pos = Position() 

		self.cast_target = None
		self.cast_skill = None
		self.cast_time = None


	def colored(self, var: str):
		color_map = {
			"name" :	"\033[4m",	# underlined
			"health" :	"\033[92m",	# green
			"pos":		"\033[94m"	# blue
		}

		if var not in vars(self).keys():
			raise Exception("Can't get colored variable '{}' for agent.".format(var))

		val_str = str(vars(self)[var])
		
		if var in color_map.keys():
			return color_map[var] + val_str + "\033[0m"

		return val_str


	def __repr__(self):
		return "{}: HP({}) Pos{}".format(
			self.colored("name"),
			self.colored("health"),
			self.colored("pos")
		) 


	def act(self, opponent, tick: float):
		"""
		This function is the main action handle for any agent.
		It will determine which skill to use or to fight or flight.
		"""

		if self.cast_skill is None:
			self.cast_skill, self.cast_target = \
				self.determine_skill_to_use(opponent)

		if self.cast_skill is not None:

			if self.cast_time is None:
				self.cast_time = self.cast_skill.cast_time

			elif self.cast_time <= 0:
				self.cast_skill.cast_on(self.cast_target)

				self.cast_target = None
				self.cast_skill = None
				self.cast_time = None

		else:
			pos = self.determine_position_to_move(opponent)

			if pos:
				self.move_to(pos, tick)

		self.update(tick)


	def determine_skill_to_use(self, opponent):
		skill = None
		distance = self.pos.distance_to(opponent.pos)

		#TODO: determine optimal skills
		for skl in self.skills:
			if skl.in_range_to(distance) and skl.is_ready():
				skill = skl
				break

		return (skill, opponent)


	def determine_position_to_move(self, opponent):
		#TODO: determine aggressive or defensive positioning
		return opponent.pos


	def move_to(self, position, tick: float):
		dist = self.pos.distance_to(position)

		if dist >= self.move_speed:
			dist = self.move_speed

		self.pos.x += dist * self.pos.direction_to(position) * tick


	def update(self, tick: float):
		if self.cast_time is not None:
			self.cast_time -= tick

		for skill in self.skills:
			skill.update(tick)


	def get_distance_to(self, position):
		return abs(self.position - position)


