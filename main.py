#! /usr/bin/env python3.8


import os

from pdb import set_trace as BP
from time import sleep

from agent import Agent
from skill import Skill



class Arena():

	def __init__(self, agents: list):
		self.agents = agents
		self.result = dict()


	def reset(self):
		self.agents = list(reversed(self.agents))

		for i, agent in enumerate(self.agents):

			distance = 1000

			pos_offset = i%2 * distance

			agent.position = -0.5 * distance + pos_offset
			agent.health = 1000


	def fight(self, num_rounds: int):
		if num_rounds % 2 != 0:
			raise Exception("'num_matches' must be an even number.")
	
		for r in range(num_rounds):

			print(" --- Round: {}".format(r))
			self.reset()

			is_winner = False

			while not is_winner:

				for i, agent in enumerate(self.agents):
					opponent_idx = (i+1)%2

					is_winner = agent.fight(self.agents[opponent_idx])

					if is_winner:
						break

				self.print_agents()

			self.print_winner()
			self.collect_stats()

		self.print_stats()


	def collect_stats(self):
		winner = self.get_winner()

		if winner.name not in self.result.keys():
			self.result.update({winner.name : 0})

		self.result[winner.name] += 1


	def print_stats(self):
		print(
			" --- Result:\n" + \
			"\n".join(str(i) for i in self.result.items())
		)


	def get_winner(self):
		winner = [ a for a in self.agents if a.health > 0 ]

		if len(winner) > 1:
			raise Exception("More than one agent alive")
		elif len(winner) == 0:
			raise Exception("No agents alive")

		return winner[0]


	def print_agents(self):
		s = " --- ".join((str(a) for a in self.agents))
		print(s + (len(s)//4) * " " + "\r", end="")


	def print_winner(self):
		print("\n\033[31mWinner\033[00m: " + self.get_winner().colored("name"))









if __name__ == "__main__":

	print("Start")

	arena = Arena([
		Agent("Melee",
			[Skill(damage=100, range=0, cooldown=5, activation_time=1)]
		),
		Agent("Ranged",
			[Skill(damage=50, range=100, cooldown=5, activation_time=1)]
		)
	])

	arena.fight(50)

	print("Done")
