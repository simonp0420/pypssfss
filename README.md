# PyPSSFSS - Analysis of polarization and frequency selective surfaces in Python

[`PyPSSFSS`](https://github.com/simonp0420/pypssfss) is a Python package for analyzing planar 
[polarization selective surfaces](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=polarization+selective+surface&btnG=) (PSSs), [frequency selective surfaces](https://en.wikipedia.org/wiki/Frequency_selective_surface) (FSSs), 
[reflectarray](https://en.wikipedia.org/wiki/Reflectarray_antennahttps://en.wikipedia.org/wiki/Reflectarray_antenna) elements, 
[radomes](https://en.wikipedia.org/wiki/Radome), and similar structures.  It wraps the 
[`PSSFSS`](https://github.com/simonp0420/PSSFSS.jl) package which is written in the [Julia](https://julialang.org/)
programming language.  Note that it is not necessary to preinstall Julia or [`PSSFSS`](https://github.com/simonp0420/PSSFSS.jl)
before using [`PyPSSFSS`](https://github.com/simonp0420/pypssfss).  If Julia is not found in the user's PATH, then 
[`PyPSSFSS`](https://github.com/simonp0420/pypssfss) will install it (locally to a virtual environment, if one is active). Similarly, it will automatically install and compile [`PSSFSS`](https://github.com/simonp0420/PSSFSS.jl) on first use.


To use [`PyPSSFSS`](https://github.com/simonp0420/pypssfss), one first specifies the geometry to be analyzed as a Python
`list` containing two or more dielectric `Layer`s and zero or more `RWGSheet` objects that define the PSS/FSS surfaces.
Due to the included `plot_sheet` function, FSS/PSS surface triangulations can be conveniently visualized using the standard 
[`Matplotlib`](https://matplotlib.org/stable/index.html) library. After also specifying the frequencies to be analyzed
and scan angles (or unit cell incremental phasings), the user then invokes the `analyze` function 
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

## Documentation
The documentation for `PyPSSFSS` is [here](https://simonp0420.github.io/pypssfss/).  
The documentation for the underlying Julia package `PSSFSS` is [here](https://simonp0420.github.io/PSSFSS.jl/stable/manual/).
**Familiarity with both of these manuals is required for use of `PyPSSFSS`**.
