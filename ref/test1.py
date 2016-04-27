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
		                full_id = residue.get_full_id()
		                if  "W" in full_id[3][0]:
		                	print full_id
		              
            		except:
               			pass
	
print """This program will return the full ids of every water in this structure.
		Read as follows: structure, model, chain, residue id.
		The residue id reads (water, position of residue, insertion code)."""


parser = PDBParser(PERMISSIVE=1)
filename = raw_input('What is the file name? The format should be xxx.pdb\n')
if ".pdb" in filename:
	atom_choosing()
else: 
	print "Make sure this is a .pdb file."
