#This set of functions is in charge of annotating the protein sequence with the peptides that match to it
#To produce graphical output, it uses the Bio.Graphics module, which depends on the reportlab libraries
import os
from Bio.SeqFeature import SeqFeature, FeatureLocation
import matplotlib.pyplot as plt

def map_peptides(protein):
	#For a given protein object, sets the location of the peptide features in the sequence. This is done through FeatureLocation objects.
	pepts=protein.features
	for pept in pepts:
		start=protein.seq._data.find(pept.seq._data)
		loc=FeatureLocation(start, start+len(pept.seq))
		pept.location=loc
 

def draw_diagram(protein):
	#Using matplotlib, draw a diagram indicating where the peptides are in the protein sequence
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax.set_title(protein.description)
	ax.set_xlabel("Protein Length (aminoacid #)")
	ax.set_ylabel("Computed Peptide Intensity (Arbitrary Units)")
	ax.set_xlim(0, len(protein.seq))
	for pept in protein.features:
		x=pept.location.start
		y=int(pept.intensity)
		p=ax.bar(x, y, width=len(pept.seq), alpha=0.4)
		ax.text(p[0].get_x()+p[0].get_width()/2., y, "#%s"%pept.id,
                ha='left', va='bottom', rotation=45)

	if not os.path.exists("./proteinDiagrams"):
		os.mkdir("proteinDiagrams")
	plt.savefig("./ProteinDiagrams/"+protein.description+".pdf")
	plt.close(fig)