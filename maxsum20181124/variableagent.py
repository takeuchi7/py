from agent import Agent

class VariableAgent(Agent):
	def __init__(self, name, fg, ms, opt):
        #name = v0など変数ノード１つ１つ
		Agent.__init__(self, name, fg, ms, opt)
        #self.name = name
		#self.fg = fg
		#self.ms = ms
		#self.opt = opt
		#self.is_terminated = False
		#self.neighbors = []
		#self.message_queue = queue.Queue()

		self.v = self.fg.variables[self.name]
        #self.variables[v0] = Variable(v0,[-1~1], [f1], ['v2', 'v1'])
        #fg=FactorGraph(opt)
		self.neighbors = self.v.functions
		self.domain = self.v.domain
		self.z = {value:0 for value in self.domain}
		self.r = {f:{value:0 for value in self.domain} for f in self.neighbors}
		self.z_queue = []

	def run(self):
        #self.is_terminated は false
        #terminated = False の間はループがつづく
		if not self.is_terminated:
			self.read_r_messages()
			self.send_q_messages()
			self.calculate_z()
			self.check_convergence()

	def read_r_messages(self):
        #queue.Queue()がemptyではないときループする
        #キューが空の場合TRUEを返す
        #多分self.message_queue.empty()はTRUE?
		#print('queue',self.message_queue)#massage_queueは関数？？
        #なんだか釈然とはしないけどキューの中身はみれない．
		#print('queue.empty()',self.message_queue.empty())
		while not self.message_queue.empty():
			#print('AAAAAAAAAAAAAAAAAAAA')
            #やっぱり確信。今回このループは機能していない
			sender, r = self.message_queue.get()
			for value in r:
				self.r[sender][value] = r[value]

	def send_q_messages(self):
		#print('self.neighbors', self.neighbors)
        #self.variables[v0] = Variable(v0,[-1~1], [f1], ['v2', 'v1'])
        #self.variables[v1] = Variable(v1,[-1~1], [f1], ['v0', 'v2'])
        #self.variables[v2] = Variable(v2,[-1~1], [f1,f2], ['v4', 'v0', 'v1', 'v3'])
        #self.variables[v3] = Variable(v3,[-1~1], [f2], ['v4', 'v2'])
        #self.variables[v4] = Variable(v4,[-1~1], [f2], ['v2', 'v3'])
        #v0のとき[f1],v1のとき[f1],v2のとき[f1,f2],v3のとき[f2],v4のとき[f2]
		for f in self.neighbors:
			q = {value:0 for value in self.domain}
			#print('q',q)それぞれのドメインに対して、０をあてる
            #{-1:0, -0.8:0, -0.6:0, -0.4:0, -0.2:0, 0.0:0, 0.2:0, 0.4:0, 0.6:0, 0.8:0, 1.0:0}
			for value in self.domain:
				#print('value',value){-1, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0}
				for ff in self.neighbors:
					#print('ff',ff)
                    #変数ノードに対する対応因子ノード
					if f != ff:
                        #異なる因子ノードに対する処理？
						q[value] += self.r[ff][value]
						#print('f,value,ff,q[value],self.r[ff][value]',f,value,ff,q[value],self.r[ff][value])
                        #f1,-1.0,f2,0,0　というように何の変化もなし
			self.send_message(f, {'header':'q', 'content':q})
            #多分Agentにつながる
            #self.send_message(f1, {
            #'header':'q', 
            #'content':{-1:0, -0.8:0, -0.6:0, -0.4:0, -0.2:0, 0.0:0, 0.2:0, 0.4:0, 0.6:0, 0.8:0, 1.0:0}})

	def calculate_z(self):
		for value in self.domain:
			self.z[value] = sum(self.r[f][value] for f in self.neighbors)

	def get_solution(self):
		max_z = None
		solution = None

		for value in self.domain:
			if max_z is None or max_z < self.z[value]:
				max_z = self.z[value]
				solution = value

		return solution

	def check_convergence(self):#収束の確認
		self.z_queue.append(self.z)
		if len(self.z_queue) == self.opt['lambda']:
			converged = True
			for value in self.z:
				value_converged = True

				const_value = self.z_queue[0][value]
				for z in self.z_queue:
					value_converged = z[value] == const_value
					if not value_converged:
						break

				if not value_converged:
					converged = False
					break

			self.is_terminated = converged
			if self.is_terminated:
				for f in self.neighbors:
					self.send_message(f, {'header':'termination', 'content':None})
			else:
				del self.z_queue[0]