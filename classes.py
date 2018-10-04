class Dog:
	species = "Mammal"
	def _init_(self,name,age):
		self.name = name
		self.age = age
	
	def description(self):
		return "{} is {} years old ".format(self.name,self.age)
	
	def speak(self, sound):
		return "{} says {} years old ".format(self.name, sound)
		
class RusselTerrier(Dog):
	def run(self,speed):
		return "{} runs {} ".format(self.name, speed)

jim = RusselTerrier.main("Jim",15)
#print (jim.description())
#print (jim.run("Slowly"))
print ("completed")