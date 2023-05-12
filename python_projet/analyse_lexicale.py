from ast import Not
from pickle import FALSE, TRUE
import sys
from sly import Lexer

class FloLexer(Lexer):

	# Noms des lexèmes (sauf les litéraux). En majuscule. Ordre non important
	tokens = { ID, ENTIER, ECRIRE, INFERIEUR_OU_EGAL, EGALITE, DIFFERENT,CONDITION,OPERATEUR,
           INFERIEUR, SUPERIEUR, SUPERIEUR_OU_EGAL, ET, OU, NON, BOOLEAN, TYPE, DECLARATION_AFFECTATION
		, INSTRUCTION,INSTRUCTIONS,OPERATEUR_LOGIQUE,SI,SINON,TANTQUE,VARIABLE}

	#Les caractères litéraux sont des caractères uniques qui sont retournés tel quel quand rencontré par l'analyse lexicale.
	#Les litéraux sont vérifiés en dernier, après toutes les autres règles définies par des expressions régulières.
	#Donc, si une règle commence par un de ces littérals (comme INFERIEUR_OU_EGAL), cette règle aura la priorité.
	literals = { '+','*','(',')',";", "-","/","%" ,",","{","}","="}
	
	# chaines contenant les caractère à ignorer. Ici espace et tabulation
	ignore = ' \t'

	# Expressions régulières correspondant au différents Lexèmes par ordre de priorité
	ID = r'[a-zA-Z][a-zA-Z0-9_]*'
	VARIABLE = r'[a-zA-Z][a-zA-Z0-9_]*'
	ID['si'] = SI
	ID['tantque'] = TANTQUE
	INFERIEUR_OU_EGAL= r'<='
	SUPERIEUR_OU_EGAL= r'>='
	EGALITE= r'=='
	DIFFERENT = r'!='
	INFERIEUR = r'<'
	SUPERIEUR = r'>'
	TYPE = r'(entier|boolean)'
	TYPE['entier'] = ENTIER
	TYPE['boolean'] = BOOLEAN
	OPERATEUR = r'(?:<|>|==|!=|<=|>=)'
	
 

	#Opérateurs logiques
	ET = 'ET'
	OU = 'OU'
	NON = 'NOT'
 
	OPERATEUR_LOGIQUE = r'(?:ET|OU|NOT)'

	# Expressions régulières pour les types et les identifiants



	# Token pour la déclaration de variable
	@_(TYPE + r'\s+' + ID + r';')
	def DECLARATION(self, t):
		t.value = (t.value.split()[0], t.value.split()[1])
		return t

    # Token pour l'affectation de variable
	@_(ID + r'\s+' + ENTIER + r';')
	def AFFECTATION(self, t):
		t.value = (t.value.split()[0], " ".join(t.value.split()[2:-1]))
		return t

	@_(r'0|[1-9][0-9]*')
	def ENTIER(self, t):
		t.value = int(t.value)
		return t

	@_("{ENTIER} {OPERATEUR} {ENTIER}")
	def CONDITION(self, t):
		op = t[1]
		if op == "<":
			t.value = t[0] < t[2]
		elif op == ">":
			t.value = t[0] > t[2]
		elif op == "<=":
			t.value = t[0] <= t[2]
		elif op == ">=":
			t.value = t[0] >= t[2]
		elif op == "==":
			t.value = t[0] == t[2]
		elif op == "!=":
			t.value = t[0] != t[2]
		return t


	@_(r'Vrai|Faux')
	def BOOLEAN(self,t):
		if t.value=='Vrai':
			t.value = TRUE
		else:
			t.value = FALSE
		return t
	
	INSTRUCTIONS = r'instruction(\s*;\s*instruction)*\s*;?'
	# The above regular expression matches one or more instructions separated by semicolons, with optional whitespace before and after

	# Define a function to handle the INSTRUCTIONS token
	@_(r'instruction(\s*;\s*instruction)*\s*;?')
	def INSTRUCTIONS(self, t):
		instruction_list = t.value.split(';')
		instruction_list = [instr.strip() for instr in instruction_list]
		t.value = instruction_list
		return t

	@_(r'entier\s+' + str(VARIABLE) + r'\s*=\s*' + str(ENTIER))
	def DECLARATION_AFFECTATION(self, t):
		name, value = t.value.split('=')
		self.variables[name.strip()] = int(value.strip())

	@_(r'boolean\s+' + str(VARIABLE) + r'\s*=\s*' + str(BOOLEAN))
	def DECLARATION_AFFECTATION(self, t):
		name, value = t.value.split('=')
		self.variables[name.strip()] = (value.strip() == TRUE)



	#@_(r'(' IDENTIFIANT '|' ENTIER ')' LT r'(' IDENTIFIANT '|' ENTIER ')')
	#def lt(self, t):
	#	return t

    # Ajoutez des règles pour les autres opérations de comparaison, les opérations arithmétiques, les opérations logiques, etc.

	@_(r'si\s*\(' + str(CONDITION) + r'\)\s*{' + str(INSTRUCTIONS) + r'}\s*' + r'(sinon\s*{' + str(INSTRUCTIONS) + r'})?\s*')
	def if_statement(self, t):
		condition = t.CONDITIONS
		if self.evaluate(condition):
			return t.INSTRUCTIONS1
		elif hasattr(t, 'INSTRUCTIONS2'):
			return t.INSTRUCTIONS2

	def evaluate(self, expression):
		# implémentez cette méthode pour évaluer les expressions booléennes
		pass

	# cas spéciaux:
	ID['ecrire'] = ECRIRE
	
	#Syntaxe des commentaires à ignorer
	ignore_comment = r'\#.*'

	# Permet de conserver les numéros de ligne. Utile pour les messages d'erreurs
	@_(r'\n+')
	def ignore_newline(self, t):
		self.lineno += t.value.count('\n')


		
     

	# En cas d'erreur, indique où elle se trouve
	def error(self, t):
		print(f'Ligne{self.lineno}: caractère inattendu "{t.value[0]}"')
		self.index += 1
  
	

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("usage: python3 analyse_lexicale.py NOM_FICHIER_SOURCE.flo")
	else:
		with open(sys.argv[1],"r") as f:
			data = f.read()
			lexer = FloLexer()
			for tok in lexer.tokenize(data):
				print(tok)
