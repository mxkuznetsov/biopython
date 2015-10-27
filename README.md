## biopython
Using the biopython module to find the distance between two atoms.


####10/27 eod:
the script will display the full id of any water molecule in the chain! The information is stored as a tuple, where the 'W' identifier signifies water. The next step would be to take those atoms and find the distance between them.

####9/24 eod:
use file 1FAT.pdb as detailed in <a href = "http://www.biotnet.org/sites/biotnet.org/files/documents/25/biopython_pdb.pdf" alt="the source"> this example source </a>. Will find distance between two atoms (everthing is hard coded at this point)

####to run (in powershell/python): 
- make sure you are in the ```Python27``` folder and that the required ```.pdb``` files are in the same folder.  Mine are nested as ```Python27\biopython\filename```
- run ```python test.py```
- when prompted from input, type ```1FAT.pdb```

####roadblocks:
* I'm not quite sure how to identify where waters are in the molecule
* need to sort out how the hierarchy (Structure > Model > Chain > Residue > Atom) works 
* how to search within atoms when location is unknown

#### future things to include in the code:
* checks for proper file format
* ability to pull .pdb files from the database
* ability to preview which chain one is looking for