from Bio.PDB import *
import numpy as np


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
                if len(residue.get_list()) > 1:
                    alpha_atom = residue.get_list()[1]
                    print alpha_atom
                for atom in residue:
                    atom.set_bfactor(alpha_atom.get_bfactor())
                    print atom.get_bfactor()



parser = PDBParser(PERMISSIVE=1)
filename = raw_input('What is the file name? The format should be xxx.pdb\n')

if ".pdb" in filename:
    renumber()
    save_file(renumber(), filename)
    print "Check your folder for a file titled " + generate_file_name(filename) + "."
else: 
    print "Make sure this is a .pdb file."
