#This set of functions is in charge of annotating the protein sequence with the peptides that match to it
#To produce graphical output, it uses the Bio.Graphics module, which depends on the reportlab libraries
import os
from Bio.SeqFeature import SeqFeature, FeatureLocation
from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram

def map_peptides(protein):
	#For a given protein object, sets the location of the peptide features in the sequence.
	pepts=protein.features
	for pept in pepts:
		start=protein.seq._data.find(pept.seq._data)
		loc=FeatureLocation(start, start+len(pept.seq))
		pept.location=loc

def color_factor(protein):
	l=[]
	for f in protein.features:
		l.append(float(f.intensity))
	return max(l)

def draw_diagram(protein):
	#Draws a sketch of the location of the peptides in the protein sequence.
	#This is the part that uses the GenomeDiagram module and ReportLabs.
	cfactor=color_factor(protein)	#first, calculate a normalized peptide intensity to use in the coloring.
	diagram=GenomeDiagram.Diagram(protein.description)
	track=diagram.new_track(1, name="Identified Peptides")
	features=track.new_set()
	for f in protein.features:
		features.add_feature(f, color=colors.Color(0,0,100, alpha=float(f.intensity)/cfactor), 
			label=True, label_size=15, name="PepID:"+f.id+"  "+str(f.location))

	#adds a start and end feature to mark the length of the protein.
	features.add_feature(SeqFeature(FeatureLocation(0,1)), color=colors.black, label=True, label_size=20, name="  0")
	features.add_feature(SeqFeature(FeatureLocation(len(protein.seq)-1,len(protein.seq))),
		color=colors.black, name="  "+ str(len(protein.seq)), label_size=20, label=True)

	#writes output	
	if not os.path.exists("./proteinDiagrams"):
		os.mkdir("proteinDiagrams")
	diagram.draw(format="linear", orientation="landscape", pagesize="A4", fragments=1, start=0, end=len(protein))
	diagram.write("./proteinDiagrams/"+protein.description+".pdf", "PDF")
