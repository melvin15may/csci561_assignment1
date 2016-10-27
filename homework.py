
try:
	input_file = open("input.txt","r")
	input_lines = input_file.readlines()
	input_lines = [l.strip("\n") for l in input_lines]

	input_file.close()

	algo = input_lines.pop(0)
	start = input_lines.pop(0)
	end = input_lines.pop(0)
	no_paths = int(input_lines.pop(0))

	realtime_traffic = []

	realtime_tree = {}

	"""
		realtime_tree= {
			<parent - node> : [{
				<child - node> : <time - taken>
			}]
		}
		e.g
		for
			A B 5
			A C 3
			B D 1
			C D 2

		realtime_tree = {
			A : [{
					B: 5
				},{
					C: 3
			}],
			B: [{
				D: 1
			}],
			C: [{
				D: 2
			}]
		}
	"""

	for i in range(no_paths):
		path = input_lines.pop(0).split(" ")
		if path[0] not in realtime_tree:
			realtime_tree[path[0]] = []
		realtime_tree[path[0]].append({})
		realtime_tree[path[0]][-1][path[1]] = int(path[2])

	sunday_travel = {}

	"""
		sunday_travel = {
			<node> : <time to destination>
		}
	"""
	no_paths = int(input_lines.pop(0))


	for i in range(no_paths):
		path=input_lines.pop(0).split(" ")
		sunday_travel[path[0]] = path[1]

	print start
	print end
	print algo
	print sunday_travel
	print realtime_tree

	""" 
		Back tracing for correct parent-child linking 
	"""

	def back_tracing(parent,start,end):
		trace = [end]
		while trace[0] != start:
			trace = [parent[trace[0]]] + trace
		return trace

	"""
		BFS
	"""

	def bfs(realtime_tree,start,end):
		current = start
		queue = []
		path = []
		parent = {}
		discovered = []
		while True:
			if current == end:
				path = back_tracing(parent,start,end)
				break

			for ch in realtime_tree.get(current,[]):
				try:
					nn = ch.keys()[0]
					if nn not in discovered:
						if nn not in parent:
							parent[nn] = current
						queue.append(nn)
				except IndexError:
					pass
			try:
				discovered.append(current)
				current = queue.pop(0)
			except IndexError:
				break

		return path
	

	def is_present(List,node,key="n"):
		for i,nn in enumerate(List):
			if nn[key] == node:
				return i
		return -1

	"""
		DFS
	"""

	def dfs(realtime_tree,start,end):
		opened=[{"n":start, "g":0}]
		closed = []
		while True:
			if len(opened) <= 0:
				return []
			current = opened.pop(0)
			if current["n"] == end:
				closed.append(current)
				break
			children = realtime_tree.get(current["n"],[])
			children_nodes = []
			for ch in children:
				ch_node = ch.keys()[0]
				if (is_present(closed,ch_node)==-1) and (is_present(opened,ch_node) == -1):
					children_nodes.append({"n": ch_node, "g": (current["g"] + 1), "p": current["n"]})
				else:
					open_index = is_present(opened,ch_node)
					close_index= is_present(closed,ch_node)
					if open_index != -1:
						if(current["g"]+1) < opened[open_index]["g"]:
							opened.pop(open_index)
							children_nodes.append({"n":ch_node,"g":(current["g"]+1),"p": current["n"]})
					elif close_index != -1:
						if(current["g"]+1) < closed[close_index]["g"]:
							closed.pop(close_index)
							children_nodes.append({"n":ch_node,"g":(current["g"]+1),"p": current["n"]})
			closed.append(current)
			opened = children_nodes + opened

		def create_path(curr_node,path=[]):
			for i,n in enumerate(closed):
				if n["n"] == curr_node:
					path = [n] + path
					closed.pop(i) 
					try:
						return create_path(n["p"],path)
					except KeyError:
						return path

		return create_path(end) 


	"""
		UCS
	"""

	def ucs(realtime_tree,start,end):
		opened = [{"n": start, "g": 0}]
		closed = []

		while True:
			if len(opened) <= 0:
				return []
			current = opened.pop(0)
			if current["n"] == end:
				closed.append(current)
				break
			children = realtime_tree.get(current["n"],[])
			for ch in children:
				ch_node = ch.keys()[0]
				if (is_present(closed,ch_node) == -1) and (is_present(opened,ch_node) == -1):
					opened.append({"n": ch_node,"g":(current["g"]+ch[ch_node]),"p": current["n"] })
				else:
					open_index = is_present(opened,ch_node)
					close_index = is_present(closed,ch_node)
					if open_index != -1:
						if (current["g"]+ch[ch_node]) < opened[open_index]["g"]:
							opened.pop(open_index)
							opened.append({"n": ch_node,"g":(current["g"]+ch[ch_node]),"p": current["n"] })
					elif close_index != -1:
						if (current["g"]+ch[ch_node]) < closed[close_index]["g"]:
							closed.pop(close_index)
							opened.append({"n": ch_node,"g":(current["g"]+ch[ch_node]),"p": current["n"] })
			closed.append(current)
			opened = sorted(opened, key=lambda k: k['g']) 

		def create_path(curr_node,path=[]):
			for i,n in enumerate(closed):
				if n["n"] == curr_node:
					path = [n] + path
					closed.pop(i) 
					try:
						return create_path(n["p"],path)
					except KeyError:
						return path

		return create_path(end) 

	"""
		A*
	"""

	def is_present(List,node,key="n"):
		for i,nn in enumerate(List):
			if nn[key] == node:
				return i
		return -1

	def a_star(realtime_tree,start,end):
		opened = [{"n": start, "g": 0}]
		closed = []

		while True:
			if len(opened) <= 0:
				return []
			current = opened.pop(0)
			current["fn"] = current["g"] + int(sunday_travel[current["n"]])
			if current["n"] == end:
				closed.append(current)
				break
			children = realtime_tree.get(current["n"],[])
			for ch in children:
				ch_node = ch.keys()[0]
				fn = current["g"] + ch[ch_node] + int(sunday_travel[ch_node])
				if (is_present(closed,ch_node) == -1) and (is_present(opened,ch_node) == -1):
					opened.append({"n": ch_node,"g":(current["g"]+ch[ch_node]),"p": current["n"], "fn": fn })
				else:
					open_index = is_present(opened,ch_node)
					close_index = is_present(closed,ch_node)
					if open_index != -1:
						if (current["fn"] + ch[ch_node]) < opened[open_index]["fn"]:
							opened.pop(open_index)
							opened.append({"n": ch_node,"g":(current["g"]+ch[ch_node]),"p": current["n"] , "fn": fn})
					elif close_index != -1:
						if (current["fn"] + ch[ch_node]) < closed[close_index]["fn"]:
							closed.pop(close_index)
							opened.append({"n": ch_node,"g":(current["g"]+ch[ch_node]),"p": current["n"] , "fn": fn})
			closed.append(current)
			opened = sorted(opened, key=lambda k: k['fn']) 

		def create_path(curr_node,path=[]):
			for i,n in enumerate(closed):
				if n["n"] == curr_node:
					path = [n] + path
					closed.pop(i) 
					try:
						return create_path(n["p"],path)
					except KeyError:
						return path

		return create_path(end) 

	"""
		Write to output file

	"""

	def write_file(string, file_name="output.txt"):
		target = open(file_name,"w")
		target.write(string)
		target.close()


	if algo == "BFS":
		bfs_path = bfs(realtime_tree,start,end)
		string = ""
		for i,n in enumerate(bfs_path[:-1]):
			string = string + "{0} {1}\n".format(n,i)
		string = string + "{0} {1}".format(bfs_path[-1],(len(bfs_path)-1))
		write_file(string)
		print string

	elif algo == "DFS":
		dfs_path = dfs(realtime_tree,start,end)

		print dfs_path

		string = ""
		for n in dfs_path[:-1]:
			string = string + "{0} {1}\n".format(n["n"],n["g"])
		string = string + "{0} {1}".format(dfs_path[-1]["n"],dfs_path[-1]["g"])
		write_file(string)
		print string
	elif algo == "UCS":
		ucs_path = ucs(realtime_tree,start,end)

		print ucs_path


		string = ""
		for n in ucs_path[:-1]:
			string = string + "{0} {1}\n".format(n["n"],n["g"])
		string = string + "{0} {1}".format(ucs_path[-1]["n"],ucs_path[-1]["g"])
		write_file(string)
		print string

	elif algo == "A*":
		a_path = a_star(realtime_tree,start,end)

		print a_path


		string = ""
		for n in a_path[:-1]:
			string = string + "{0} {1}\n".format(n["n"],n["g"])
		string = string + "{0} {1}".format(a_path[-1]["n"],a_path[-1]["g"])
		write_file(string)
		print string


except IOError:
	print "IO Error"