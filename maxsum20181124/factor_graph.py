#coding:utf-8
from functions import Functions
import json

class FactorGraph:
	def __init__(self, opt):
		self.variables = {}
		self.functions = {}
		self.constants = {}
		self.opt = opt
        #現在は{lambda:10}が入っている

	def load(self, graph):
		self.fg = json.load(open(graph, 'r'))
		#print('A')
        #self.fg = json.load(open(graph, 'r').read())
        #f = open('fg.json', 'r')
        #self.fg = json.load(f)
		#self.fg=graph
		#print(self.fg)
        
		# loading functions
		for f in self.fg['functions']:#2roop
            #1:{'name': 'f1', 'variables': ['v0', 'v1', 'v2']}
            #2:{'name': 'f2', 'variables': ['v2', 'v3', 'v4']}
			self.functions[f['name']] = Function(f['name'], f['variables'], self)
			#print('self',self) Object at 0x00になった
            #function(f1)=Function(f1,[v0,v1,v2],self)とfunction(f2)=Function(f2,[v0,v1,v2],self)を定義
            #関数として定義

		# loading variables
		for v in self.fg['variables']:#5roop
			#print('v',v)ループは以下のとおり
            #１回目{'name': 'v0', 'domain': {'min': -1, 'max': 1, 'step': 0.2}}
            #２回目{'name': 'v1', 'domain': {'min': -1, 'max': 1, 'step': 0.2}}
            #３回目{'name': 'v2', 'domain': {'min': -1, 'max': 1, 'step': 0.2}}
            #４回目{'name': 'v3', 'domain': {'min': -1, 'max': 1, 'step': 0.2}}
            #５回目{'name': 'v4', 'domain': {'min': -1, 'max': 1, 'step': 0.2}}
			functions = []
			neighbours = set()
            #set([1,2,3,4,5])変わらずset([1,2,3,4,5]) 
            #set([1,1,2,2,3,3])重複するものは除去set([1,2,3])
            #set({'dog':'inu', 'cat':'neko', 'bird':'tori'}) で定義するとset(['dog', 'cat', 'bird']) 
			for f in self.functions:#2roop
                #self.functions…{f1:関数　f2:関数}
				#1:f1 
                #2:f2
				#self.functions[f1].variables = ['v0', 'v1', 'v2'] 
                #self.functions[f2].variables = ['v2', 'v3', 'v4']
				if v['name'] in self.functions[f].variables:
                    #もし、self.functions[f].variablesの中に、v['name']と同じものがあるのであれば
					#print(v['name']) #1回目v0 #2回目v1 #3回目v2 #4回目v2 #5回目v3 #6回目v4
					functions.append(f)
                    #1roop(このときv[name]=v0):functions ['f1'] 被った 
                    #2roop(このときv[name]=v0):被らなかった                    
                    #3roop(このときv[name]=v1):functions ['f1'] 被った 
                    #4roop(このときv[name]=v1):被らなかった
                    #5roop(このときv[name]=v2):functions ['f1'] 被った 
                    #6roop(このときv[name]=v2):functions ['f1', 'f2'] 被った
                    #7roop(このときv[name]=v3):被らなかった 
                    #8roop(このときv[name]=v3):functions ['f2'] 被った                   
                    #9roop(このときv[name]=v4):被らなかった 
                    #10roop(このときv[name]=v4):functions ['f2'] 被った
					for n in self.functions[f].variables:#3roop
						#print(n)
                        #つまり対象の変数ノードと因子ノードの要素に被りがあったときに実行
                        #v[name]=v0 #1:v0 #2:v1 #3:v2 
                        #v[name]=v1 #4:v0 #5:v1 #6:v2 
                        #v[name]=v2 #7:v0 #8:v1 #9:v2 
                        #v[name]=v2 #10:v2 #11:v3 #12:v4 
                        #v[name]=v3 #13:v2 #14:v3 #15:v4 
                        #v[name]=v4 #16:v2 #17:v3 #18:v4
						if n != v['name']:
							neighbours.add(n)
                        #nとv[name]でノットイコールであれば追加
			neighbours = list(neighbours)
			#print(neighbours)
            #1roop['v2', 'v1'] #2roop['v0', 'v2'] #3roop['v4', 'v0', 'v1', 'v3'] #4roop['v4', 'v2'] #5roop['v2', 'v3']

			value = v['domain']['min']
            #1roop:v=v0のとき、-1
            #2roop:v=v1のとき、-1
            #3roop:v=v2のとき、-1
            #4roop:v=v3のとき、-1
            #5roop:v=v4のとき、-1
            
			domain = []
			while value <= v['domain']['max']:
				domain.append(value)
				value += v['domain']['step']
            #domain:[-1, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0]    
    
			self.variables[v['name']] = Variable(v['name'], domain, functions, neighbours)
			#各変数ごとに、v0~v4まで、それぞれドメインとfunction,隣接を関数として定義
            #self.variables[v0] = Variable(v0,[-1~1], [f1], ['v2', 'v1'])
            #self.variables[v1] = Variable(v1,[-1~1], [f1], ['v0', 'v2'])
            #self.variables[v2] = Variable(v2,[-1~1], [f1,f2], ['v4', 'v0', 'v1', 'v3'])
            #self.variables[v3] = Variable(v3,[-1~1], [f1], ['v4', 'v2'])
            #self.variables[v4] = Variable(v4,[-1~1], [f1], ['v2', 'v3'])
            #関数として定義
        #つまり現時点では以下の関数を持つことになる
        #function(f1)=Function(f1,[v0,v1,v2],self)
        #function(f2)=Function(f2,[v0,v1,v2],self)
        #self.variables[v0] = Variable(v0,[-1~1], [f1], ['v2', 'v1'])
        #self.variables[v1] = Variable(v1,[-1~1], [f1], ['v0', 'v2'])
        #self.variables[v2] = Variable(v2,[-1~1], [f1,f2], ['v4', 'v0', 'v1', 'v3'])
        #self.variables[v3] = Variable(v3,[-1~1], [f1], ['v4', 'v2'])
        #self.variables[v4] = Variable(v4,[-1~1], [f1], ['v2', 'v3'])
		
        # loading constants
		for c in self.fg['constants']:
			self.constants[c['name']] = c['value']
            #関数として定義

class Variable:
	def __init__(self, name, domain, functions, neighbours):
		self.name = name
		self.domain = domain
		self.functions = functions
		self.value_index = 0
		self.neighbours = neighbours
		self.domain_size = len(domain)

	def get_value(self):
		return self.domain[self.value_index]

	def set_value(self, value):
		self.value_index = self.domain.index(value)

class Function:
	def __init__(self, name, variables, fg):
		self.name = name
		self.variables = variables
		self.fg = fg

	def get_value(self, values):
		function = Functions(self.fg)
		return function.calculate(self.name, values)
