import numpy as np
from pyscf.pbc import gto as pgto
from pyscf.pbc import scf as pscf
import pywannier90

# build cell object
cell = pgto.Cell()
cell.a = [[0.0, 2.7155, 2.7155], [2.7155, 0.0, 2.7155], [2.7155, 2.7155, 0.0]]
cell.atom = [["Si", [0.0, 0.0, 0.0]], ["Si", [1.35775, 1.35775, 1.35775]]]
cell.basis = "gth-dzv"
cell.pseudo = "gth-pade"
cell.exp_to_discard = 0.1
cell.build()

# build and run scf object
kmesh = [1, 1, 1]
kpts = cell.make_kpts(kmesh)
kmf = pscf.KKS(cell, kpts)
kmf.xc = "pbe"
kmf.run()

# build and run w90 object
num_wann = cell.nao
keywords = """
begin projections
random
end projections
"""
w90 = pywannier90.W90(kmf, cell, kmesh, num_wann, other_keywords=keywords)
w90.kernel()
ham = w90.get_hamiltonian_kpts()
e, v = np.linalg.eigh(ham)
print(e[0])
