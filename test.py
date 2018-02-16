class TestClass:
	def __init__ (self, x, y):
		self.x = x
		self.y = y

def generate_class(x, y):
	return TestClass(x, y)

def mod_mapping(mapping):
	mapping['1'].x = 10

class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):
    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.Name())
print(y.GetEmployee())

mapping = dict()
mapping['1'] = generate_class(1, 2)
mapping['2'] = generate_class(4, 5)

test = mapping['1']
test.x = 1222
print mapping['1'].x

x = Employee("asdf", "asdfd", 220)
print x.Name()