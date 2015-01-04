from classes import *
from mapping import *

#Code in this file reads processes the entries from the peptides.txt input file and loads them into peptide and protein objects.

def get_indexes(header):
	#The MS output file (from MAXQUANT software) providing varying number of fields depending on experimental design.
	#For that reason I generate a dictionary with the indexes of each field.
	h=header.split('\t')
	d=dict(zip(h, range(0, len(h))))
	return d


def readpept(line, ind):
	#Reads the peptide line and creates an object with the relevant information
	#relevant info includes sequence, Uniprot accesion,
	#protein it belongs to and whether it is unique to that protein or not.
	line=line.split('\t')
	pseq=Bio.Seq.Seq(line[ind["Sequence"]], alphabet="IUPAC.Protein")
	#creates the peptide object. it is set to remove the prefixes that MAXQUANT adds to potential contaminations of the sample.
	pept=Peptide(seq=pseq, uniprot=line[ind["Leading razor protein"]].split("_")[-1],
		unique=line[ind["Unique (Proteins)"]], intensity=line[ind["Intensity"]], id=line[ind["id"]])
	pept.id=line[ind["id"]]
	if pept.unique=="yes":
		pept.unique=True
	else:
		pept.unique=False
	return pept

def fillproteins(pepts):
	#Creates unique protein records and fills in the list with the peptides that map to that protein.
	#Uses only the peptides that uniquely match to the protein. Use of non-unique ones can be implemented in the future.
	protIDs={}
	proteins=set()

	#First,creates a list of the proteins present.
	#It is a dictionary of includes the list of peptide features for every protein.
	for pep in pepts:
		if pep.unique==False or pep.intensity=="0": #Discards the peptide if the intensity is 0 or if the peptide is not unique to protein.
			continue
		if pep.uniprot not in protIDs:
			protIDs[pep.uniprot]=[pep]
		else:
			protIDs[pep.uniprot].append(pep)

	#Then, creates protein objects. The features attribute is a list of peptide objects
	for c, protein in enumerate(protIDs):
		if len(protIDs[protein])<2: #Discards protein with less than 2 unique peptides
			continue
		p=Protein(id=protein, features=protIDs[protein])
		p.getprotinfo()
		proteins.add(p)
		#Print status.
		if c%50==0:
			r=round(len(proteins)*100./len(protIDs), 2)
			print str(r) + "% complete"
	return proteins


def processfile(f):
	fil=open(f)
	peptides=set()
	print "***Parsing input file. Creating peptide records.***"
	for c, line in enumerate(fil):
		if len(peptides)==0:
			ind=get_indexes(line)
			#Checks input file is valid
			reqfields=["Sequence", "Leading razor protein", "Intensity", "Unique (Proteins)", "id"]
			if not all(x in ind for x in reqfields):
				return False
		peptides.add(readpept(line, ind))
		# if c>25:
		# 	break

	fil.close()
	return peptides



