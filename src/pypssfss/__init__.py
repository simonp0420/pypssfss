"""
Python wrapper for Julia's PSSFSS package

This package provides Python wrappers for Julia's PSSFSS package, enabling functionality for analyzing radomes, 
frequency selective surfaces, polarization selective surfaces, metasurfaces, reflectarray elements, and similar
structures.  It is not necessary to install Julia prior to using this package.  If Julia is not in the user's path
then it will be installed automatically.  If pypssfss is installed in a Python virtual environment, then the Julia
installation will be private to that environment. The extensive documentation of PSSFSS at https://simonp0420.github.io/PSSFSS.jl/stable/ 
is required reading to use this package effectively.  Important differences in the pypssfss wrapper:
- Since Python lacks built-in named tuples, steering is specified by calling one of the functions ThetaPhi, PhiTheta, Psi1Psi2,
  or Psi2Psi1
- Since Python doesn't have macros, the @outputs macro functionality is replaced by the atoutputs function in Python.
- Plotting of sheet triangulations from Python is done via the plot_sheet function exported by this package. 
The extensive Julia markdown-formatted help strings for wrapped Julia functions can be pretty-printed to the user's 
console using the doc function exported by this package.  E.g. doc(analyze) or doc(diagstrip)

Modules:
- pypssfss: Core functionality and wrappers
- sheets: Sheet definitions and plotting
- steering: Steering definitions
"""

# Quantities to export:
from .pypssfss import (
    analyze,
    atoutputs,
    cm,
    diagstrip,
    doc,
    extract_result,
    inch,
    jerusalemcross,
    Layer,
    loadedcross,
    manji,
    mil,
    mm,
    meander,
    pecsheet,
    PhiTheta,
    pixels,
    plot_sheet,
    pmcsheet, 
    polyring,
    Psi1Psi2,
    Psi2Psi1,
    rectstrip,
    res2fresnel,
    res2tep,
    sinuous,
    splitring,
    sympixels,
    ThetaPhi,
)

__all__ = ['analyze', 'atoutputs', 'cm', 'diagstrip', 'doc', 'extract_result', 
           'inch', 'jerusalemcross', 'Layer', 'loadedcross', 'manji',
           'meander', 'mil', 'mm', 'pecsheet', 'PhiTheta', 'pixels', 
           'plot_sheet', 'pmcsheet', 'polyring',  'Psi1Psi2', 'Psi2Psi1', 'rectstrip',
           'res2fresnel', 'res2tep', 'sinuous', 'splitring', 'sympixels', 'ThetaPhi']
