"""
Affiche une chaine de caractère avec une certaine identation
"""


def afficher(s, indent=0):
    print(" " * indent + s)


class lire:
    def __init__(self):
        pass

    def afficher(self, indent=0):
        afficher("<lire>", indent)
        afficher("</lire>", indent)


class Programme:
    def __init__(self, listeInstructions,listeFonctions=None):
        self.listeInstructions = listeInstructions
        self.listeFonctions = listeFonctions

def afficher(self, indent=0):
        afficher("<programme>", indent)
        self.listeInstructions.afficher(indent + 1)
        afficher("</programme>", indent)


class ListeInstructions:
    def __init__(self):
        self.instructions = []

    def afficher(self, indent=0):
        afficher("<listeInstructions>", indent)
        for instruction in reversed(self.instructions):
            instruction.afficher(indent + 1)
        afficher("</listeInstructions>", indent)

class ListeFonctions:
    def __init__(self):
        self.fonctions = []

    def afficher(self, indent=0):
        afficher("<listeFonctions>", indent)
        for fonction in reversed(self.fonctions):
            fonction.afficher(indent + 1)
        afficher("</listeFonctions>", indent)


class Affectation:
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

    def afficher(self, indent=0):
        afficher("<affectation>", indent)
        self.variable.afficher(indent + 1)
        self.expression.afficher(indent + 1)
        afficher("</affectation>", indent)

class Declaration:
    def __init__(self, type_, identifiant):
        self.type_ = type_
        self.identifiant = identifiant

    def afficher(self, indent=0):
        afficher("<declaration>", indent)
        self.type_.afficher(indent + 1)
        self.identifiant.afficher(indent + 1)
        afficher("</declaration>", indent)

class DeclarationAffectation:
    def __init__(self, type_, identifiant, expression):
        self.type_ = type_
        self.identifiant = identifiant
        self.expression = expression

    def afficher(self, indent=0):
        afficher("<declaration_affectation>", indent)
        self.type_.afficher(indent + 1)
        self.identifiant.afficher(indent + 1)
        self.expression.afficher(indent + 1)
        afficher("</declaration_affectation>", indent)

class InstructionConditionnelle:
    def __init__(self, condition, instructions_si, instructions_sinsi, instructions_sinon):
        self.condition = condition
        self.instructions_si = instructions_si
        self.instructions_sinsi = instructions_sinsi
        self.instructions_sinon = instructions_sinon

    def afficher(self, indent=0):
        afficher("<instruction_conditionnelle>", indent)
        self.condition.afficher(indent + 1)
        self.instructions_si.afficher(indent + 1)
        self.instructions_sinsi.afficher(indent + 1)
        self.instructions_sinon.afficher(indent + 1)
        afficher("</instruction_conditionnelle>", indent)



class InstructionRetour:
    def __init__(self, expression):
        self.expression = expression

    def afficher(self, indent=0):
        afficher("<instruction_retour>", indent)
        self.expression.afficher(indent + 1)
        afficher("</instruction_retour>", indent)

class AppelFonctionIgnoreRetour:
    def __init__(self, nom, arguments):
        self.nom = nom
        self.arguments = arguments

    def afficher(self, indent=0):
        afficher("<appel_fonction_ignore_retour>", indent)
        self.nom.afficher(indent + 1)
        self.arguments.afficher(indent + 1)
        afficher("</appel_fonction_ignore_retour>", indent)



class Ecrire:
    def __init__(self, exp):
        self.exp = exp

    def afficher(self, indent=0):
        afficher("<ecrire>", indent)
        self.exp.afficher(indent + 1)
        afficher("</ecrire>", indent)




class Operation:
    def __init__(self, op, exp1, exp2):
        self.exp1 = exp1
        self.op = op
        self.exp2 = exp2

    def afficher(self, indent=0):
        afficher('<operation "' + self.op + '">', indent)
        self.exp1.afficher(indent + 1)
        self.exp2.afficher(indent + 1)
        afficher('</operation "' + self.op + '">', indent)


class Entier:
    def __init__(self, valeur):
        self.valeur = valeur

    def afficher(self, indent=0):
        afficher("[Entier:" + str(self.valeur) + "]", indent)


class Variable:
    def __init__(self, valeur):
        self.valeur = valeur

    def afficher(self, indent=0):
        afficher("[Variable:" + str(self.valeur) + "]", indent)

class Type:
    def __init__(self, valeur):
        self.valeur = valeur

    def afficher(self, indent=0):
        afficher("[Type:" + str(self.valeur) + "]", indent)


class AppelFonction:
    def __init__(self, nom, arguments):
        self.nom = nom
        self.arguments = arguments

    def afficher(self, indent=0):
        afficher("<Appel fonction:" + str(self.nom) + ">", indent)
        self.arguments.afficher(indent + 1)
        afficher("</Appel fonction:" + str(self.nom) + ">", indent)


class ExprList:
    def __init__(self, expr, exprList=None):
        self.expr = expr
        self.exprList = exprList

    def afficher(self, indent=0):
        self.expr.afficher(indent + 2)
        if self.exprList:
            self.exprList.afficher(indent)

class Boolean:
    def __init__(self, valeur):
        self.valeur = valeur

    def afficher(self, indent=0):
        afficher("[Boolean:" + str(self.valeur) + "]", indent)


class BooleanOperation:
    def __init__(self, operator, operand1, operand2=None):
        self.op = operator
        self.exp1 = operand1
        self.exp2 = operand2

    def afficher(self, indent=0):
        afficher("<BooleanOperation: \"" + self.op + "\">", indent)
        self.exp1.afficher(indent + 1)
        if(self.exp2):
            self.exp2.afficher(indent + 1)
        afficher("</BooleanOperation: \"" + self.op + "\">", indent)


class InstructionBoucle:
    def __init__(self, condition, instructions):
        self.condition = condition
        self.instructions = instructions

    def afficher(self, indent=0):
        afficher("<instruction_boucle>", indent)
        self.condition.afficher(indent + 1)
        self.instructions.afficher(indent + 1)
        afficher("</instruction_boucle>", indent)

class Si:
    def __init__(self, condition, instructions, sinon=None):
        self.condition = condition
        self.instructions = instructions
        self.sinon = sinon

    def afficher(self, indent=0):
        afficher("<si>", indent)
        self.condition.afficher(indent + 1)
        self.instructions.afficher(indent + 1)
        afficher("</si>", indent)
        if self.sinon:
            self.sinon.afficher(indent)


class SinonSi:
    def __init__(self, condition, instructions, sinon=None):
        self.condition = condition
        self.instructions = instructions
        self.sinon = sinon

    def afficher(self, indent=0):
        afficher("<sinon_si>", indent)
        self.condition.afficher(indent + 1)
        self.instructions.afficher(indent + 1)
        afficher("</sinon_si>", indent)
        if self.sinon:
            self.sinon.afficher(indent)


class Sinon:
    def __init__(self, instructions):
        self.instructions = instructions

    def afficher(self, indent=0):
        afficher("<sinon>", indent)
        self.instructions.afficher(indent + 1)
        afficher("</sinon>", indent)


