import pywannier90
import numpy as np

from pyscf.pbc import gto, dft

cell = gto.Cell()
cell.atom = """
C       8.904500000000001      7.500000000000000      7.500000000000000
C       8.202199999999999      8.716400000000000      7.500000000000000
C       6.797700000000000      8.716400000000000      7.500000000000000
C       6.095499999999999      7.500000000000000      7.500000000000000
C       6.797700000000000      6.283600000000000      7.500000000000000
C       8.202299999999999      6.283600000000000      7.500000000000000
H      10.007899999999999      7.500000000000000      7.500000000000000
H       8.754000000000000      9.672000000000001      7.500000000000000
H       6.246000000000000      9.672000000000001      7.500000000000000
H       4.992100000000001      7.500000000000000      7.500000000000000
H       6.246000000000000      5.328100000000000      7.500000000000000
H       8.754000000000000      5.327999999999999      7.500000000000000
"""
cell.a = np.array(
    [[15.000, 0.0000, 0.0000], [0.0000, 15.0000, 0.0000], [0.0000, 0.0000, 15.0000]]
)
# cell.gs = [15] * 3
cell.verbose = 5
cell.basis = "gth-tzvp"
cell.unit = "Angstrom"
cell.pseudo = "gth-pbe"
cell.exp_to_discard = 0.1
cell.precision = 1e-10
cell.ke_cutoff = 120
cell.build()


nk = [1, 1, 1]
abs_kpts = cell.make_kpts(nk)
kmf = dft.KRKS(cell, abs_kpts).density_fit()
kmf.xc = "pbe"
ekpt = kmf.run()

num_wann = 6
keywords = """
translate_home_cell : true
guiding_centres : true
wannier_plot           : true
wannier_plot_supercell : 1
wannier_plot_list      =  1-6
dis_num_iter   : 10
num_iter       : 10
write_hr       : true
write_tb       : true
begin projections
C:pz:zona=6
end projections
"""

w90 = pywannier90.W90(kmf, cell, nk, num_wann, gamma=True, other_keywords=keywords)


w90.kernel()
w90.plot_wf(grid=[60, 60, 60], supercell=nk)
