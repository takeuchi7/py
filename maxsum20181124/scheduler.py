import sys, os, json
from datetime import datetime

class Scheduler:
	def __init__(self, fg, agents, ms, opt):
		self.fg = fg
		self.agents = agents
		self.opt = opt
		self.ms = ms

	def initialize(self):
        #ms = MessageServer(opt)
        #ms.load #ms.send #ms.printer #ms.logger
        #このmsってマックスサムの略か
		self.ms.load(self.agents)

	def run(self):
		terminated = False
        #terminated = False の間はループがつづく
		while not terminated:
			terminated = True
			for a in self.agents:
                #{v0:関数 v1:関数 v2:関数 v3:関数 v4:関数 f1:関数 f2:関数}
                #変数ノードにはVariable関数、因子ノードにはfunction関数
				self.agents[a].run()
                #variableの場合
                    #self.agents[a].run()... 
                    #VariableAgent/run... 
                        #VariableAgent/read_r_messages... 
                        #VariableAgent/send_q_messages...Agent/send_message...MessageServer/send
                            #self.agentLog[sender] += 1
                            #self.timeLog[sender] += 1
                            #self.clients[receiver].receive(sender, content)を得る感じか？？
                        #VariableAgent/self.calculate_z()
                        #VariableAgent/self.check_convergence()
				terminated = terminated and self.agents[a].is_terminated

				if terminated:
					print('agent %s terminated' % a)

	def terminate(self):
		for v in self.fg.variables:
			print('variable %s = %f' % (v, self.agents[v].get_solution()))