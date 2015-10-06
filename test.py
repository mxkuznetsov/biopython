from Bio.PDB import *

def cartesian_distance(atom1, atom2):
	"This will print the Cartesian distance between two atoms."
	print atom1 - atom2
	return

def atom_choosing():
	"This will select an atom from the stucture"
	structure = parser.get_structure(filename[0:-4], filename)
	for model in structure:
   	 	for chain in model:
       		 for residue in chain:
            		try:
		                atom_1 = residue['N'] 
		                atom_2 = residue['CA'] 
		              	distance = atom_1 - atom_2
		              	print distance
            		except:
               			pass
	return

parser = PDBParser(PERMISSIVE=1)
filename = raw_input('What is the file name? The format should be xxx.pdb\n')
if ".pdb" in filename:
	atom_choosing()
else: 
	print "Make sure this is a .pdb file."



