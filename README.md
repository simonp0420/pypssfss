# pypssfss

Python wrapper for the Julia [`PSSFSS`](https://github.com/simonp0420/PSSFSS.jl) package.  
It is not necessary to preinstall Julia or `PSSFSS` before using `pypssfss`.  If Julia is not found in your PATH, then
`pypssfss` will install it (locally to a virtual environment, if one is active).  Similarly, it will automatically install
`PSSFSS` on first use.

[`PSSFSS`](https://github.com/simonp0420/PSSFSS.jl) is a Julia package for analyzing planar 
[polarization selective surfaces](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=polarization+selective+surface&btnG=) (PSSs), [frequency selective surfaces](https://en.wikipedia.org/wiki/Frequency_selective_surface) (FSSs), 
[reflectarray](https://en.wikipedia.org/wiki/Reflectarray_antennahttps://en.wikipedia.org/wiki/Reflectarray_antenna) elements, 
[radomes](https://en.wikipedia.org/wiki/Radome), and similar structures.  It is intended to be useful to antenna design engineers and others who work in applied electromagnetic engineering.

The user specifies the geometry to be analyzed as a `list` containing two or more dielectric `Layer`s 
and zero or more `RWGSheet` objects that define the PSS/FSS surfaces.  Due to the included `plot_sheet` function, 
the surface triangulations can be conveniently visualized using the standard 
[`Matplotlib`](https://matplotlib.org/stable/index.html) library After also specifying the scan angles or
unit cell incremental phasings, frequencies to be analyzed, the user then invokes the `analyze` function 
to perform the analysis.  Post-processing and plotting of results can be performed in the same Python analysis script.


## Features

* Designed to be useful and accessible to working engineers and students.
* Accommodates planar FSS/PSS surfaces with no limits to number of dielectric layers or FSS/PSS sheets.
* Automatically chooses number of modes needed for cascading multiple FSS/PSS sheets using
  generalized scattering matrices (GSMs).
* Supports (approximate) cascading multiple sheets of different periodicities, as in a multilayer
  meanderline polarizer.
* Simple specification of geometry to be analyzed.
* Solution of mixed-potential integral equation using Rao-Wilton-Glisson triangle subdomain basis functions 
  and multi-threaded method of moments.
* Fast analysis for frequency sweeps using an extremely robust rational function interpolation algorithm.
* Automatic triangulation of sheet geometries to user-specified number of triangles.
* Exploits redundancies inherent in structured meshes for greater numerical efficiency.
* Easy extraction of useful engineering performance parameters, including 
    * Reflection and transmission coefficient magnitudes and/or phases for the field components of 
        * TE/TM 
        * Vertical/horizontal (Ludwig 3)
        * LHCP/RHCP (circular polarization)
    * Delta insertion phase delay (ΔIPD)
    * Delta insertion loss (ΔIL)
    * Axial ratio 
* FSS/PSS element geometry can be exported to STL files for later import into CAD programs.
* Analysis results can be exported to 
    * HFSS SBR+-compatible Fresnel tables
    * TICRA-compatible TEP (tabulated electrical properties) files.

## Limitations

* Only zero-thickness FSS/PSS sheets are currently supported.
* Frequency sweeps are fastest for normal incidence or for the case where unit cell incremental phase shifts ψ₁ and ψ₂ are
  constant with frequency (as in a waveguide).  This is due to the use of a wide-band expansion of the 
  potential Green's functions for a stratified medium with quasi-periodic excitation. Frequency sweeps for non-normal
  angle of incidence are typically slower. However, as of `PSSFSS` version 1.1, all frequency sweeps are now much faster, 
  often by more than an order of magnitude, compared to previous versions.  The speedup is due to the use of a fast interpolated sweep by default.


## Installation

### Installing Using pip
```bash
pip install pypssfss
```

### Installing from the base repository

Activate Python environment and then clone and install:
```bash
git clone https://github.com/simonp0420/pypssfss.git
cd pypssfss
pip install .
```




