import MDAnalysis as mda
import sys
from MDAnalysisTests.datafiles import PDB, XTC
u = mda.Universe(sys.argv[1],sys.argv[2])
import propkatraj
protein = u.select_atoms('protein')
pkatraj = propkatraj.PropkaTraj(protein)
pkatraj.run(verbose=True)
pkatraj.pkas
pkatraj.pkas.describe()
data = pkatraj.pkas

data.to_csv("pka-trajctory-full.csv")

data2 = pkatraj.pkas.describe()

data2.to_csv("pka-trajctory-summary.csv")

