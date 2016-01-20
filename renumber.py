from Bio.PDB import *

def generate_file_name(filename):
	return filename[0:-4] + '-bfact.pdb'

def save_file(file, filename):
	"This will save the file as a .pdb"
	saved_file = generate_file_name(filename)
	with open(saved_file, 'wb') as f:
		np.savetxt(saved_file, file)
	return saved_file

def renumber(): #needs to return a giant array??
	"This will inital an array of all the atoms in the structure"
	structure = parser.get_structure(filename[0:-4], filename)
	for model in structure:
   	 	for chain in model:
       		 for residue in chain:
        		for atom in residue:
		                b_fact = atom.get_bfactor()
		               # id_array.append(atom) #array of atoms
		                if  "W" in full_id[3][0]:
		                	w_id_array.append(atom) #array of waters
		                	header.append(str(atom.get_full_id()[3][1]))
		                	#print atom.get_full_id()
		                 #an array of full ids, which as stored as tuples  
	
print """This program will create a file containing the distance between every atom in this structure."""

parser = PDBParser(PERMISSIVE=1)
filename = raw_input('What is the file name? The format should be xxx.pdb\n')
if ".pdb" in filename:
	
	save_file(renumber(), filename)
	print "Check your folder for a file titled " + generate_file_name(filename) + "."
else: 
	print "Make sure this is a .pdb file."