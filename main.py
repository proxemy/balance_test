



from agent import Agent



class Arena():

	def __init__(self, agents: list, num_matches: int):

		if num_matches % 2 != 0:
			raise Exception("'num_matches' must be an even number.")

		self.num_matches = num_matches


	def fight(self):
		pass







if __name__ == "__main__":

	print("Start")

	arena = Arena(
		[
			Agent("Melee",[]),
			Agent("Ranged",[]),
		],
		50
	)

	arena.fight()


	print("Done")
