#write file with python propka_run.py xxx.pdb xxx.xtc

import MDAnalysis as mda
import sys
from MDAnalysisTests.datafiles import PDB, XTC
u = mda.Universe(sys.argv[1],sys.argv[2]) #import file here
import propkatraj #import module
protein = u.select_atoms('protein') #defining your protein
pkatraj = propkatraj.PropkaTraj(protein)
pkatraj.run(verbose=True)
pkatraj.pkas
pkatraj.pkas.describe()
data = pkatraj.pkas

data.to_csv("pka-trajctory-full.csv") #save file

data2 = pkatraj.pkas.describe()

data2.to_csv("pka-trajctory-summary.csv")

