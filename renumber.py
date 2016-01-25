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
	for model in structure:
   	 	for chain in model:
       		 for residue in chain:
       		 	#atom 1 in residue.get_bfactor()
     			print residue.get_segid()
        		for atom in residue:
		                b_fact = atom.get_bfactor()
		               # atom.set_bfactor(atom1.get_bfactor())
		               # print b_fact 
	
print """This program will renumber all additional generic numbers"""

parser = PDBParser(PERMISSIVE=1)
filename = raw_input('What is the file name? The format should be xxx.pdb\n')
if ".pdb" in filename:
	renumber()
	#save_file(renumber(), filename)
	print "Check your folder for a file titled " + generate_file_name(filename) + "."
else: 
	print "Make sure this is a .pdb file."
