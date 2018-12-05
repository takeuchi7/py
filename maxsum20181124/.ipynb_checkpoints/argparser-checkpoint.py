class ArgParser:
	def __init__(self, args, pattern):
    #２つ目の引数とパターンを引数にする
		self.args = args
		self.pattern = pattern

	def read(self):
		opt = {}
		for p in self.pattern:# self.pattern={'-l': {'name': 'lambda', 'type': 'int', 'default': 10}}
			#print('aa',p) #-l という一つだけ．もしこれが「optionが存在する」を表した記号ならば？
			if p in self.args:
            #リストpatternとリストargsとの共有する要素に着目する
				if self.pattern[p]["type"] == "bool":
                #もし共通要素のtypeが"bool"であればoptのリストにTrueを代入
					opt[self.pattern[p]["name"]] = True
				elif self.pattern[p]["type"] == "int":
                #もし共通要素のtypeが"int"であればoptのリストに演算を代入
					opt[self.pattern[p]["name"]] = int(self.args[self.args.index(p) + 1])
				elif self.pattern[p]["type"] == "float":
                #もし共通要素のtypeが"float"であればoptのリストに演算を代入
					opt[self.pattern[p]["name"]] = float(self.args[self.args.index(p) + 1])
				elif self.pattern[p]["type"] == "str":
                #もし共通要素のtypeが"str"であればoptのリストに演算を代入
					opt[self.pattern[p]["name"]] = self.args[self.args.index(p) + 1]
			else:
            #もし共有リストがなければデフォルトを代入
				opt[self.pattern[p]["name"]] = self.pattern[p]["default"]

		return opt
