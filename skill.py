

from pdb import set_trace as BP


class Skill():

	def __init__(self, damage: int, range: int, cooldown: int, cast_time: int):
		self.damage = damage
		self.range = range
		self.cooldown = cooldown
		self.cast_time = cast_time

		self.cooldown_ticks = 0


	def update(self, tick: float):
		self.cooldown_ticks -= tick
		if self.cooldown_ticks < 0:
			self.cooldown_ticks = 0

	def in_range_to(self, distance):
		return self.range >= distance


	def is_ready(self):
		return self.cooldown_ticks <= 0


	def cast_on(self, target):
		if not self.is_ready():
			raise Exception("Can't cast non-ready skill!")

		#TODO: handle more diverse skills
		target.health -= self.damage

		self.cooldown_ticks = self.cooldown


	def __repr__(self):
		return "[DMG:{},Range:{}]".format(self.damage, self.range)
