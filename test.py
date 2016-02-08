from Bio.PDB import *
import numpy as np
#np.set_printoptions(threshold='nan')

atoms = []
waters = []
w_id_array = []
id_array = []
header = [" "]
head = ''

# for x in range(len(atoms)] #distances should be a 2D array or a NumPy matrix

def cart_dist(atom1, atom2):
	"This will print the Cartesian distance between two atoms."
	diff =   atom1 - atom2
	return diff
	#return np.sqrt(np.sum(diff * diff))

def atom_array():
	"This will inital an array of all the atoms in the structure"

	structure = parser.get_structure(filename[0:-4], filename)
	for model in structure:
   	 	for chain in model:
       		 for residue in chain:
        		for atom in residue:
		                full_id = atom.get_full_id()
		                id_array.append(atom) #array of atoms
		                if  "W" in full_id[3][0]:
		                	w_id_array.append(atom) #array of waters
		                	header.append(str(atom.get_full_id()[3][1]))
		                	#print atom.get_full_id()
		                 #an array of full ids, which as stored as tuples                    		
	              	                	

def create_2D_array():
	"This will create a 2D array of distances between waters"
	#potentially use NumPy matrices for the matrix
	"""when printed, do null + waters for 0th row
	and null + atoms for 0th column
	data in between should be distances, with a diagonal of 0s"""

	atoms = np.array(id_array, dtype=object) #numpy array of all atoms
	waters = np.array(w_id_array, dtype=object) #numpy array of all waters
	atoms3 = len(waters) + 1 #initial col numbering
	atom1 = atoms #row
	atom2 = waters #col
	answer = np.zeros((len(atoms), atoms3) , np.object) #row, columns
	for row, atom1 in enumerate(atoms):
		#answer[row, 0] = str(atom1.get_full_id()[3][1]) #atom1.get_full_id()
		answer[row, 0] = str(atom1.get_bfactor())
		for col, atom2 in enumerate(waters):
			if (cart_dist(atom1, atom2) <= 3.4) and (cart_dist(atom1, atom2) >= 2.0):
				answer[row, (col + 1)] = cart_dist(atom1, atom2)

	return answer

def renumber(): 
	"This will inital an array of all the atoms in the structure"
	structure = parser.get_structure(filename[0:-4], filename)
	#atom_li = Selection.unfold_entities(structure, 'A')
	for model in structure:
   	 	for chain in model:
   	 		res_list = list(chain.get_residues())
       		for residue in chain:
       			if len(residue.get_list()) > 1:
       				alpha_atom = residue.get_list()[1]
       				#print alpha_atom
       				#if residue['CA'].fullname == [ 'CA' ]:
       					#alpha_atom = residue['CA']
       			for atom in residue:
       						atom.set_bfactor(alpha_atom.get_bfactor())
       						#print atom.get_bfactor()	

def generate_file_name(filename):
	return filename[0:-4] + '-distances.csv'

def save_file(file, filename):
	"This will convert the matrix to a .csv"
	saved_file = generate_file_name(filename)
	with open(saved_file, 'wb') as f:
		head = ','.join(header)
		#f.write(','.join(header))
		np.savetxt(saved_file, file, delimiter=",", header= head, fmt="%s")
	return saved_file

	
print """This program will create a file containing the distance between every atom in this structure."""

parser = PDBParser(PERMISSIVE=1)
filename = raw_input('What is the file name? The format should be xxx.pdb\n')
if ".pdb" in filename:
	renumber()
	atom_array()
	create_2D_array()
	save_file(create_2D_array(), filename)
	print "Check your folder for a file titled " + generate_file_name(filename) + "."
else: 
	print "Make sure this is a .pdb file."
