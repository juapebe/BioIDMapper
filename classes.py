#I am keeping the classes altogether here.
import Bio
from Bio import Seq
from Bio import SeqRecord
from Bio import SeqFeature
from Bio import SeqIO
from Bio import ExPASy
from Bio import SwissProt

class Peptide(SeqFeature.SeqFeature):
	#A class derived from the regular SeqFeature. I chose SeqFeature so it will be easy to embed them in the protein objects.
	#It is actually kind of a mixture between SeqFeature and SeqRecord in that it incorporates some attributes from the latter.
	#Also include others that are relevant to this procedure, such as uniqueness, protein the peptide comes from and intensity value on mass spec
	def __init__(self, location=None, seq="NA", unique=False, uniprot="UniProtNotSet", intensity=0, id="NA"):
		Bio.SeqFeature.SeqFeature.__init__(self, location=location)
		self.id=id
		self.seq=seq
		self.unique=unique
		self.uniprot=uniprot
		self.intensity=intensity

	def __str__(self):
		if self.unique:
			return "Peptide with sequence %s, unique to protein %s"%(self.seq, self.uniprot)
		else:
			return "Peptide with sequence %s, not unique but likely belonging to protein %s"%(self.seq, self.uniprot)

class Protein(SeqRecord.SeqRecord):
	#A class that represents the proteins. the 'id' attribute is used to store the UniProt ID.
	#Most important attribute is .features, here a dictionary, which contain peptide feature objects
	def __init__(self, seq=Bio.Seq.Seq("", alphabet="IUPAC.Protein"), id="UniProtNotSet", 
		PDB=None, features=[], description="Description"):
		Bio.SeqRecord.SeqRecord.__init__(self, seq=seq)
		self.id=id
		self.features=features
		self.PDB=PDB
		self.description=description

	def __str__(self):
		l=[]
		for e in self.features:
			l.append(e.seq._data + ": " + str(e.intensity))
		return "Protein %s (%s) with %s unique peptides identified. Sequence and intensities are:\n"%(self.id, self.description, len(l)) + "\n".join(l)

	def getprotinfo(self):
		#Uses UniprotID to retrieve the sequence and the PDB entry(es) for the protein.
		try:
			handle=ExPASy.get_sprot_raw(self.id)
			record = SwissProt.read(handle)
			self.seq=Bio.Seq.Seq(record.sequence, alphabet="IUPAC.Protein")
			self.description=record.entry_name
			for r in record.cross_references:
				if r[0]=="PDB":
					if self.PDB==None:
						self.PDB=[]
					self.PDB.append(r[1])
		except:
			print "Could not retrieve sequence, PDB info for: " + self.id
			self.seq="NOTRETRIEVED"
			self.PDB=None
			self.description="UnknownDescription"


