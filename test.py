from Bio.PDB import *

def cartesian_distance(atom1, atom2):
	"This will print the Cartesian distance between two atoms."
	print atom1 - atom2
	return

def atom_choosing():
	"This will select an atom from the stucture"
	structure = parser.get_structure(filename[0:-4], filename)
	atoms = structure.get_atoms()
	#m = raw_input('Which model?  ')
	model = structure[0]
	#chain = raw_input('Which chain?  ')
	chain = model['A']
	residue = chain[10]
	atom = residue['CA']
	atom1 = structure[0]['A'][10]['CA']
	#print "\n\n\n", atom.get_full_id()
	atom2 = structure[0]['A'][20]['CA']
	cartesian_distance(atom1, atom2)
	return

parser = PDBParser(PERMISSIVE=1)
filename = raw_input('What is the file name? The format should be xxx.pdb\n')
if ".pdb" in filename:
	atom_choosing()
else: 
	print "Make sure this is a .pdb file."



#model, chain, residue, atom

#atom1 = raw_input("First atom, please!\n")
#atom2 = raw_input("Second one, too.\n")
#cartesian_distance(atom1, atom2)

