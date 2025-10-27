"""
Testing C++ wrapper for Wannier90
Hung Q. Pham
email: pqh3.14@gmail.com
Example: a H2 in a box
Construct one sigma-like Wannier function from 2 Bloch states
"""

import pywannier90
import numpy as np
from pyscf.pbc import gto, dft

cell = gto.Cell()
cell.atom = """
H 1.5 1.5 1
H 1.5 1.5 2
"""
cell.basis = "6-31g"
cell.a = np.eye(3) * 3
cell.verbose = 5
cell.unit = "Angstrom"
cell.build()

nk = [1, 1, 1]
abs_kpts = cell.make_kpts(nk)
kmf = dft.KRKS(cell, abs_kpts)
kmf.xc = "pbe"
ekpt = kmf.run()

num_wann = 2
keywords = """
begin projections
H:s
end projections
"""

w90 = pywannier90.W90(kmf, cell, nk, num_wann, other_keywords=keywords)
w90.kernel()
w90.plot_wf(grid=[40, 40, 40], supercell=nk)
