



from agent import Agent



class Arena():

	def __init__(self, agents: list):
		self.agents = agents


	def reset(self):

		self.agents = list(reversed(self.agents))

		for i, agent in enumerate(self.agents):

			pos_offset = i%2 * 1000

			agent.position = -500 + pos_offset
			agent.health = 1000



	def fight(self, num_rounds: int):

		if num_rounds % 2 != 0:
			raise Exception("'num_matches' must be an even number.")
	
		for r in range(num_rounds):
			self.reset()

			for i, agent in enumerate(self.agents):

				opponent_idx = (i+1)%2

				agent.fight(self.agents[opponent_idx])

	def print_result(self):
		pass









if __name__ == "__main__":

	print("Start")

	arena = Arena([
		Agent("Melee",[]),
		Agent("Ranged",[]),
	])

	arena.fight(50)

	arena.print_result()


	print("Done")
