from Bio.PDB import *


parser = PDBParser()
structure = parser.get_structure('RR','Redepostion_Renumbered.pdb')
resolution = structure.header['resolution']
name = structure.header['name']

print resolution
print name 