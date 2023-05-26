"""
Affiche une chaine de caractère avec une certaine identation
"""
def afficher(s,indent=0):
	print(" "*indent+s)

class lire:
	def __init__(self):
		pass

	def afficher(self, indent=0):
		afficher("<lire>", indent)
		afficher("</lire>", indent)


class Programme:
	def __init__(self,listeInstructions):
		self.listeInstructions = listeInstructions
	def afficher(self,indent=0):
		afficher("<programme>",indent)
		self.listeInstructions.afficher(indent+1)
		afficher("</programme>",indent)

class ListeInstructions:
	def __init__(self):
		self.instructions = []
	def afficher(self,indent=0):
		afficher("<listeInstructions>",indent)
		for instruction in self.instructions:
			instruction.afficher(indent+1)
		afficher("</listeInstructions>",indent)

class Ecrire:
	def __init__(self,exp):
		self.exp = exp
	def afficher(self,indent=0):
		afficher("<ecrire>",indent)
		self.exp.afficher(indent+1)
		afficher("</ecrire>",indent)

class Operation:
	def __init__(self,op,exp1,exp2):
		self.exp1 = exp1
		self.op = op
		self.exp2 = exp2
	def afficher(self,indent=0):
		afficher('<operation "'+self.op+'">',indent)
		self.exp1.afficher(indent+1)
		self.exp2.afficher(indent+1)
		afficher('</operation "'+self.op+'">',indent)
class Entier:
	def __init__(self,valeur):
		self.valeur = valeur
	def afficher(self,indent=0):
		afficher("[Entier:"+str(self.valeur)+"]",indent)

class Variable:
	def __init__(self,valeur):
		self.valeur = valeur
	def afficher(self,indent=0):
		afficher("[Variable:"+str(self.valeur)+"]",indent)

class AppelFonction:
	def __init__(self, nom, arguments):
		self.nom = nom
		self.arguments = arguments

	def afficher(self, indent=0):
		afficher("<Fonction:"+str(self.nom)+">", indent)
		self.arguments.afficher(indent+1)
		afficher("</Fonction:"+str(self.nom)+">", indent)

class ExprList:
	def __init__(self, expr, exprList=None):
		self.expr = expr
		self.exprList = exprList

	def afficher(self, indent=0):
		afficher("[Argument]", indent+1)
		self.expr.afficher(indent+2)
		if self.exprList:
			self.exprList.afficher(indent)

class Boolean:
	def __init__(self,valeur):
		self.valeur = valeur
	def afficher(self,indent=0):
		afficher("[Boolean:"+str(self.valeur)+"]",indent)

class BooleanOperation:
	def __init__(self, operator, operand1, operand2):
		self.operator = operator
		self.operand1 = operand1
		self.operand2 = operand2

	def afficher(self, indent=0):
		afficher("<BooleanOperation: " + self.operator + ">", indent)
		self.operand1.afficher(indent+1)
		self.operand2.afficher(indent+1)
		afficher("</BooleanOperation: " + self.operator + ">", indent)
