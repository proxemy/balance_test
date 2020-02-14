
import os

from pdb import set_trace as BP
from time import sleep

from agent import Agent
from skill import Skill



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

			print("\nRound: {}".format(r))
			self.reset()

			is_winner = False

			while not is_winner:

				for i, agent in enumerate(self.agents):

					opponent_idx = (i+1)%2

					is_winner = agent.fight(self.agents[opponent_idx])

					if is_winner:
						break

				self.print_agents()
	
				if is_winner:
					print("\nWinner")

				self.render_battlefield()

				sleep(0.1)


	def print_result(self):
		pass


	def print_agents(self):

		s = " --- ".join((str(a) for a in self.agents))

		print(s + (len(s)//4) * " " + "\r", end="")


	def render_battlefield(self):
		pass








if __name__ == "__main__":

	print("Start")

	arena = Arena([
		Agent("Melee",[Skill(100, 0)]),
		Agent("Ranged",[Skill(10, 100)]),
	])

	arena.fight(50)

	arena.print_result()


	print("Done")
