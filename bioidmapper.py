#The main program. includes the progress report messages and also a couple of checks for the input file.

import sys
from classes import *
from mapping import *
from processfile import *

if __name__=="__main__":
	if len(sys.argv)==1:
		print "Input file is missing. \n usage: python bioidmapper.py <peptides.txt file>"
		sys.exit()

	print "******BIOIDMAPPER v0.9 (beta)*******"
 	peptides=processfile(sys.argv[1])
 	if peptides==False:
 		print "The input file doesn't seem to be a valid peptides.txt file.\nPlease check it contains the required fields." 
 		sys.exit()

	print "***Creating protein records (downloading full sequence and PDB codes).***"
	proteins=fillproteins(peptides)

	print "%i peptide records parsed."%len(peptides)
	print "%i proteins found and mapped."%len(proteins)

	print "***Drawing sketches for peptide locations.***"
 	for p in proteins:
 		if p.description=="UnknownDescription":
			continue
 		map_peptides(p)
 		draw_diagram(p)
 	print "***Process completed!***\nResults can be found in the ProteinDiagrams folder in the local directory."