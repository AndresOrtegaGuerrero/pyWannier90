import numpy as np
from pyscf.pbc import gto as pgto
from pyscf.pbc import dft as pscf
import pywannier90

# build cell object
cell = pgto.Cell()
cell.a = [[0.0, 2.7155, 2.7155], [2.7155, 0.0, 2.7155], [2.7155, 2.7155, 0.0]]
cell.atom = [["Si", [0.0, 0.0, 0.0]], ["Si", [1.35775, 1.35775, 1.35775]]]
cell.basis = "gth-dzv"
cell.pseudo = "gth-pade"
cell.exp_to_discard = 0.1
cell.verbose = 5
cell.build()

# build and run scf object
kmesh = [2, 1, 1]
kpts = cell.make_kpts(kmesh)
kmf = pscf.KRKS(cell, kpts).density_fit()
kmf.xc = "pbe"
kmf.run()

# build and run w90 object
num_wann = 8
keywords = """
num_iter      : 800
wannier_plot           : true
wannier_plot_supercell : 1 1 1
wannier_plot_list      =  1-8
begin projections
Si:sp3
end projections
"""
w90 = pywannier90.W90(kmf, cell, kmesh, num_wann, other_keywords=keywords)
w90.kernel()
kmesh_w90 = [1, 1, 1]
w90.plot_wf(supercell=kmesh_w90)
ham = w90.get_hamiltonian_kpts()
e, v = np.linalg.eigh(ham)
print(e[0])
