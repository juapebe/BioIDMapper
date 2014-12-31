====BioIDMAPPER version 0.9 (beta)====
=======================================

Written by Juan A Perez-Bermejo, University of California, San Francisco.

Table of contents
——————————

1. Brief description. Version notes. Usage. Input files. Output files. Requirements.
2. Description of BioID procedure. Rationale for BioIDMapper.
3. Features to be added in the future.
4. Contact info.


1. Brief description.
————————————

BioIDMapper (provisional name) is a program aimed to provide a mapping of the peptides identified from Mass Spectrometry analyses into the sequence of the protein they are supposed to come from. It is specifically aimed to expand the knowledge obtained from the BIOID technique, for which the location of the peptides may provide information on the protein-protein interaction interface regions.

BioIDMapper was originally developed as the final project for the “Introduction to Object Oriented Programming” class (PC204). Fall quarter 2014. 

NOTE: BioIDMapper can also be used for the analysis of APEX2 data. For more info on APEX2, see Rhee et al, “Proteomic Mapping of Mitochondria in Living Cells via Spatially-Restricted Enzymatic Tagging”, Science. Mar 15, 2013; 339(6125): 1328–1331. 

==Version notes==
The 0.9 beta version allows for the mapping of the peptides into the proteins they belong to, and produces a diagram on where in the primary sequence do they map to. The diagram also provides information on the relative intensity of each one of the peptides.

==Usage==
python bioidmapper.py <peptides.txt file>


==Input Files==
As of beta version, BioIDMapper is designed to use the peptides.txt file obtained from MaxQuant as input. MaxQuant is a free software that is used for the analysis of protein Mass Spectrometry data and provides identification of the peptides in the sample, along with the proteins they most likely come from. MaxQuant is a widely used piece of software for the analysis of Mass Spectrometry raw data, especially when an Orbitrap instrument is used. 
More information on MaxQuant can be obtained from the website, www.maxquant.org.

==Output files==
A folder with diagrams for every protein identified (as long as number of peptides >2) and where the peptides map in the sequence.

==Requirements==
BioIDMapper has been tested on Python 2.7.2.
Third-party module dependencies are Biopython (www.biopython.org) and ReportLab (www.reportlab.org; the open-source software is enough).



2. Description of BioID procedure.
—————————————————

BioID is a technique for the identification of proteins that interact with a given protein (bait). It was described in a paper in 2012 (Roux et al. “A promiscuous biotin ligase fusion protein identifies proximal and interacting proteins in mammalian cells.” J Cell Biol. 2012 Mar 19;196(6):801-10).
The BioID procedure can be summarized as follows:

a) A protein fusion between the bait protein and a promiscuous biotin ligase (BirA) is expressed on the cell of interest.
b) Upon activation, the  biotin ligase will biotinylate any protein around the bait protein within a given radius.
c) Cells are then lysed, and all biotinylated proteins are purified using streptavidin-coated beads.
d) Beads are incubated with trypsin to chew proteins into mass spec-suitable peptides.
e) After mass spectrometry analysis, peptides are identified using a software procedure of choice (MAXQUANT is the most widespread one).

Advantages of BioID include that it allows for the identification of transient protein interactions, and also that the strength of the biotin-streptavidin interaction allows for very stringent washes. Since its original publication it has been widely implemented by many groups.


===Rationale for BioIDMapper.===
When using BioID, potential interactions of the bait are labeled on a distance-dependent manner. This makes us wonder whether we would be able to anticipate which proteins are closer to the bait (depending on the intensity of the peptides identified) and, most interestingly, the orientation of such interaction (by looking at the position of the 
peptides in the protein sequence/structure).

BioIDMapper aims to answer this question by mapping the identified peptides into the protein sequence and providing relative intensity values.

3. Features to be added in the future.
————————————————

Top priority:
+BioIDMapper currently retrieves PDB codes for the identified proteins. It would be very intereesting to map the peptides into the structure file, and output a .PDB file that indicates where the peptides are highlighted. This could be done by editing the original template PDB by adding extra chains, one per peptide.

Others:
+Handling of other input files would be interesting.
+Currently, it only deals with peptides that map to a single protein. Maybe introduce the functionality to work with non-unique peptides in the future.
+Providing protein coverage may help prioritize the 
+Comparing intensity ratios with those obtained from other techniques that pulldown whole proteins may help identify the peptides that lie closer to bait.

4. Contact info.
——————————————

Author: Juan A Perez-Bermejo. University of California, San Francisco.
e-mail: juan.perez-bermejo@ucsf.edu

PC204 Course Contact: Tom E Ferrin. tef@cgl.ucsf.edu