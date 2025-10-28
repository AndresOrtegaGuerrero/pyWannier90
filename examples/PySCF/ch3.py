"""
Testing C++ wrapper for Wannier90
Hung Q. Pham
email: pqh3.14@gmail.com

Example: a CH3 radical in a box.
Construct four sp3-like Wannier functions from nine Bloch states.
"""

import pywannier90
import numpy as np
from pyscf.pbc import gto, dft


cell = gto.Cell()
cell.atom = """
C 3.175 3.175 3.175
H 3.175 3.175 4.264
H 4.1181 3.175 2.6305
H 2.2319 3.175 2.6305
"""
cell.basis = "gth-dzv"
cell.a = np.eye(3) * 6.35
cell.spin = 1
cell.verbose = 5
cell.unit = "Angstrom"
cell.build()


nk = [1, 1, 1]
abs_kpts = cell.make_kpts(nk)
kmf = dft.KUKS(cell, abs_kpts).mix_density_fit()
kmf.xc = "pbe"
ekpt = kmf.run()

num_wann = 4
keywords = """
num_iter       : 20
exclude_bands : 5-14
begin projections
C:sp3
end projections
"""

w90 = pywannier90.W90(
    kmf, cell, nk, num_wann, gamma=True, spin="up", other_keywords=keywords
)
w90.kernel()
w90.plot_wf(grid=[40, 40, 40], supercell=nk)
