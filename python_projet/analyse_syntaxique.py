import sys
from sly import Parser
from analyse_lexicale import FloLexer
import arbre_abstrait

class FloParser(Parser):
	# On récupère la liste des lexèmes de l'analyse lexicale
	tokens = FloLexer.tokens

	# Règles gramaticales et actions associées

	@_('listeInstructions')
	def prog(self, p):
		return arbre_abstrait.Programme(p[0])

	@_('listeFonctions listeInstructions')
	def prog(self, p):
		return arbre_abstrait.Programme(p[0],p[1])

	@_('instruction')
	def listeInstructions(self, p):
		l = arbre_abstrait.ListeInstructions()
		l.instructions.append(p[0])
		return l

	@_('instruction listeInstructions')
	def listeInstructions(self, p):
		p[1].instructions.append(p[0])
		return p[1]

	@_('ecrire')
	def instruction(self, p):
		return p[0]

	@_("fonction")
	def listeFonctions(self, p):
		f = arbre_abstrait.ListeFonctions()
		f.fonctions.append(p.fonction)
		return f

	@_("fonction listeFonctions")
	def listeFonctions(self, p):
		p.listeFonctions.fonctions.append(p.fonction)
		return p.listeFonctions


	@_('appel_fonction')
	def instruction(self, p):
		return p[0]

	@_('declaration')
	def instruction(self, p):
		return p[0]

	@_('affectation')
	def instruction(self,p):
		return p[0]

	@_('declaration_affectation')
	def instruction(self,p):
		return p[0]

	@_('tant_que')
	def instruction(self,p):
		return p[0]

	@_('retourner')
	def instruction(self, p):
		return p[0]

	@_('ID "(" exprList ")" ";"')
	def appel_fonction(self, p):
		return arbre_abstrait.AppelFonction(p[0], p[2])
	@_('si')
	def instruction(self,p):
		return p[0]

	@_('SI "(" expr ")" "{" listeInstructions "}" sinon')
	def si(self, p):
		return arbre_abstrait.Si(p.expr, p.listeInstructions,p.sinon)

	@_('')
	def sinon(self,p):
		return None

	@_('SINON SI "(" expr ")" "{" listeInstructions "}" sinon')
	def sinon(self,p):
		return arbre_abstrait.SinonSi(p.expr,p.listeInstructions,p.sinon)

	@_('SINON "{" listeInstructions "}"')
	def sinon(self,p):
		return arbre_abstrait.Sinon(p.listeInstructions)

	@_('TANTQUE "(" expr ")" "{" listeInstructions "}"')
	def tant_que(self, p):
		return arbre_abstrait.InstructionBoucle(p.expr, p.listeInstructions)

	@_('RETOURNER expr ";"')
	def retourner(self,p):
		return arbre_abstrait.InstructionRetour(p[1])

	@_('type variable "=" expr ";"')
	def declaration_affectation(self, p):
		return arbre_abstrait.DeclarationAffectation(p[0], p[1], p[3])

	@_('variable "=" expr ";"')
	def affectation(self, p):
		return arbre_abstrait.Affectation(p[0], p[2])

	@_('type id ";"')
	def declaration(self, p):
		return arbre_abstrait.Declaration(p[0], p[1])

	@_('TYPE')
	def type(self,p):
		return arbre_abstrait.Type(p[0])

	@_('variable')
	def id(self,p):
		return p[0]

	@_('ID')
	def variable(self,p):
		return arbre_abstrait.Variable(p[0])



	@_('ECRIRE "(" expr ")" ";"')
	def ecrire(self, p):
		return arbre_abstrait.Ecrire(p.expr) #p.expr = p[2]

	@_('expr "+" produit')
	def expr(self, p):
		return arbre_abstrait.Operation('+',p[0],p[2])


	@_('expr "-" produit')
	def expr(self, p):
		return arbre_abstrait.Operation('-',p[0],p[2])

	@_('"-" expr "+" produit')
	def expr(self, p):
		return arbre_abstrait.Operation('-', p[3], p[1])

	@_('"-" facteur')
	def produit(self, p):
		return arbre_abstrait.Operation('*', arbre_abstrait.Entier(-1), p[1])

	@_('produit')
	def expr(self,p):
		return p[0]

	@_('facteur')
	def produit(self,p):
		return p[0]

	@_('produit "*" facteur')
	def produit(self, p):
		return arbre_abstrait.Operation('*',p[0],p[2])

	@_('produit "/" facteur')
	def produit(self, p):
		return arbre_abstrait.Operation('/',p[0],p[2])

	@_('produit "%" facteur')
	def produit(self, p):
		return arbre_abstrait.Operation('%',p[0],p[2])

	@_('"(" expr ")"')
	def facteur(self, p):
		return p.expr #ou p[1]

	@_('ENTIER')
	def facteur(self, p):
		return arbre_abstrait.Entier(p.ENTIER)

	@_('ID')
	def facteur(self, p):
		return arbre_abstrait.Variable(p.ID)

	@_('LIRE "(" ")"')
	def facteur(self, p):
		return arbre_abstrait.lire()

	@_('ID "(" exprList ")"')
	def facteur(self, p):
		return arbre_abstrait.AppelFonction(p.ID, p.exprList)

	@_('expr')
	def exprList(self, p):
		return arbre_abstrait.ExprList(p.expr)

	@_('expr "," exprList')
	def exprList(self, p):
		return arbre_abstrait.ExprList(p.expr,p.exprList)

	@_('ID "(" ")"')
	def facteur(self, p):
		return arbre_abstrait.AppelFonction(p.ID, [])

	@_('ID "(" exprList ")"')
	def boolean(self, p):
		return arbre_abstrait.AppelFonction(p.ID, p.exprList)

	@_('boolean')
	def expr(self, p):
		return p[0]

	@_('BOOLEAN')
	def boolean(self, p):
		return arbre_abstrait.Boolean(p.BOOLEAN)

	@_('expr OPERATEUR expr')
	def boolean(self, p):
		return arbre_abstrait.BooleanOperation(p[1],p[0],p[2])

	@_('boolean ET boolean')
	def boolean(self, p):
		return arbre_abstrait.BooleanOperation(p[1], p[0], p[2])

	@_('boolean OU boolean')
	def boolean(self, p):
		return arbre_abstrait.BooleanOperation(p[1], p[0], p[2])

	@_('NON boolean')
	def boolean(self, p):
		return arbre_abstrait.BooleanOperation(p[0], p[1])






if __name__ == '__main__':
	lexer = FloLexer()
	parser = FloParser()
	if len(sys.argv) < 2:
		print("usage: python3 analyse_syntaxique.py NOM_FICHIER_SOURCE.flo")
	else:
		with open(sys.argv[1],"r") as f:
			data = f.read()
			try:
				arbre = parser.parse(lexer.tokenize(data))
				arbre.afficher()
			except EOFError:
				exit()
