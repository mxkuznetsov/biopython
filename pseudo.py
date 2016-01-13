from Bio.PDB import *
import numpy as np


waters = []
atoms = np.array([])
# for x in range(len(atoms)] #distances should be a 2D array or a NumPy matrix

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
            		#try:
		                full_id = residue.get_full_id()
		                atoms.append(full_id) #an array of all the atoms
		                at1 = np.array(atoms, dtype = tuple)
		                at2 = np.array(atoms, dtype = tuple)
		                print at1[1] - at2[1]
		               # i = 0
		                #j = 0
		                #while i <= 10:
		               # 	while i <= 10:
		                		#distances[i][j] =  atoms[i] - atoms[j]
		                #		j = j +1
		               # 	i = i + 1
		               # if  "W" in full_id[3][0]:
		                #	waters.append(full_id) #an array of all the waters
 
		                	                	



def create_2D_array():
	"This will create a 2D array of distances between waters"
	#potentially use NumPy matrices for the matrix
	"""when printed, do null + waters for 0th row
	and null + atoms for 0th column
	data in between should be distances, with a diagonal of 0s"""

	""" for waters[i] and atoms[j]
	run through every atom and subtract the water in the column 
	to fill the column, 
	then increment the waters and continue until all waters 
	have been incemented"""
	dist = np.zeros(len(atoms), dtype = int)
	print dist

	return	
	
print """This program will return the full ids of every water in this structure.
		Read as follows: structure, model, chain, residue id.
		The residue id reads (water, position of residue, insertion code)."""


parser = PDBParser(PERMISSIVE=1)
filename = raw_input('What is the file name? The format should be xxx.pdb\n')
if ".pdb" in filename:
	atom_choosing()
	create_2D_array()
else: 
	print "Make sure this is a .pdb file."
