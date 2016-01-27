from Bio.PDB import *



def generate_file_name(filename):
	return filename[0:-4] + '-bfact.pdb'

def save_file(file, filename):
	"This will save the file as a .pdb"
	saved_file = generate_file_name(filename)
	with open(saved_file, 'wb') as f:
		np.savetxt(saved_file, file)
	return saved_file

def renumber(): 
	"This will inital an array of all the atoms in the structure"
	structure = parser.get_structure(filename[0:-4], filename)
	#atom_li = Selection.unfold_entities(structure, 'A')
	for model in structure:
   	 	for chain in model:
   	 		res_list = list(chain.get_residues())
       		for residue in chain:
       			#res = residue.get_id()[1]
       			if residue.get_atom() == ['CA']:
       				alpha_atom = atom
       				for atom in residue:
       					atom.set_bfactor(alpha_atom.get_bfactor())
       					print atom.get_bfactor()

	
#print """This program will renumber all additional generic numbers"""

parser = PDBParser(PERMISSIVE=1)
filename = raw_input('What is the file name? The format should be xxx.pdb\n')
if ".pdb" in filename:
	renumber()
	#save_file(renumber(), filename)
	print "Check your folder for a file titled " + generate_file_name(filename) + "."
else: 
	print "Make sure this is a .pdb file."
