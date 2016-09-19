class Bird:
	def __init__(self, kind, call):
		self.call = call
		self.kind = kind

	def do_call(self):
		print "a %s goes %s" % (self.kind, self.call);

class Parrot(Bird):
	def__init__(self):
		Bird.__init__(self, "Parrot"' "kah!")

class Cuckoo(Bird):
	def__init__(self):
		Bird.__init__(self, "cuckoo", "cuckoo!")

if __name__ == "__main__":
	parrot = Parrot()
	cuckoo = Cuckoo()

	parrot.do_call()
	cuckoo.do_call()

