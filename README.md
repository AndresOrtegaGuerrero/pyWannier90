[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
![GitHub last commit](https://img.shields.io/github/last-commit/hungpham2017/pyWannier90.svg?color=green)
![GitHub issues](https://img.shields.io/github/issues-raw/hungpham2017/pyWannier90.svg?color=crimson)

# pyWannier90: A Python interface for wannier90
[wannier90](http://www.wannier.org/) is a well-established package to construct maximally-localied Wannier functions (MLWFs) as well as to perform MLWF-based analysis.
pyWannier90 uses the library-mode of wannier90 to perform the wannierization on the wave function obtained by PySCF.

<img src="https://github.com/hungpham2017/pyWannier90/blob/master/doc/Si_sp3.png" width="500" align="middle">

## News:
- pyWannier90 is now available for wannier90 community, check it out [here](http://www.wannier.org/download/).
- pyWannier90 only supports the latest version from the wannier90 using the python wrap using F90Wrap .

## pyWannier90 can use the wave function obtained by:
- PySCF 1.5 and

## Why pyWannier90?
- If you would like to construct MLWFs for the wave function obtained by [PySCF](https://github.com/pyscf/pyscf)

## How to install pyWannier90
Install wannier90 and follow the instruction to build the wrap

- Compile wannier90-xxx:
	```
	make & make lib
	```
- Clone the repository and do
	```
	pip install .
	```

## How to cite?
Please cite this paper when you use pyWannier90 code in your research:
- pyWannier90 for PySCF: Q. Sun et al.,Recent developments in the PySCF program package, [**J. Chem. Phys**](https://doi.org/10.1063/5.0006074), **2020**, Just Accepted
