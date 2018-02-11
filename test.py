class TestClass:
	def mod_dict(self, x):
	    x['attr'] = [x['attr'][0] + 1, x['attr'][1]]

test = dict()
test['attr'] = [0, 0]

func = TestClass()

for i in xrange(10):
    func.mod_dict(test)
    print test
    