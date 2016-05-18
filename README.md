## biopython
Using the biopython module to find the distance between two atoms.


##to run (in powershell/python): 
- make sure you are in the ```Python27``` folder and that the required ```.pdb``` files are in the same folder.  Mine are nested as ```Python27\biopython\filename```
- run ```python test.py```
- when prompted from input, type the name of the file in the format xxx.pdb
- this may take a while, but the file is being generated.
- once it is complete, check the window for a message that reads ```Check your folder for a file titled 'pdbfilename-distances.csv'.```
in the same folder as the program should be a .csv containing the name of your pdb file

###which files are relevant?
- program has been run on several files for testing
- use  ```test.py``` and the .pdb file of your choosing


###test.py
- this file generates a .csv file
- filters to distances of 2.0 to 3.5 A, with waters on x-axis and atoms on y-axis
- the x-axis is the atom number of the water
- the y-axis is the residue number of the atom it's being compared to
- any value greater or larger is printed as a 0


###renumber.py
- this file is not complete
- the end goal is to have the output save as a file
- the script takes the file and renumbers all atoms in a residue to have the same b factor
- the b factor is taken from the alpha carbon
- when run, the console will print the alpha carbon, followed by the b factor of every atom in it (which is all the same)
- the file used for input should be one that has had the b factors of its alpha carbons renumbered using consensus numbering
