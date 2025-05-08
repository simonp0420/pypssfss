"""
This is the pypssfss module.

It provides Python wrappers for Julia's PSSFSS package, including functions for analyzing strata,
extracting results, and converting data formats. 

Available functions:
- analyze
- atoutputs
- doc
- extract_result
- Layer
- res2tep
- res2fresnel
- atoutputs
"""
import juliapkg as jp
jp.require_julia('1.10')
jp.add('PSSFSS', '6b20a5d4-3c6c-44cd-883b-1480592d72be')
jp.resolve()


import os
# Invoke julia with the "-t auto" option:
os.environ["PYTHON_JULIACALL_THREADS"] = "auto"
os.environ["PYTHON_JULIACALL_HANDLE_SIGNALS"] = "no"

import numpy as np

import juliacall
from juliacall import Main as jl

# Set up the Julia Main module:
jl.seval('using PSSFSS')
jl.seval('using REPL: REPL')


from juliacall import convert, VectorValue, ArrayValue

# Definitions of Layers
def Layer(**kwargs):
    return jl.Layer(**kwargs)

# Definitions of Sheets:
from .sheets import (diagstrip, jerusalemcross, loadedcross, manji,
                     meander, pecsheet, pixels, plot_sheet, pmcsheet, polyring,
                     rectstrip, sinuous, splitring, sympixels, mm, cm, inch, mil, RWGSheet)

# Steering definitions:
from .steering import ThetaPhi, PhiTheta, Psi1Psi2, Psi2Psi1 

# Implementation of the analyze function in Python:
def analyze(strata: list,
            flist,
            steering: ThetaPhi | PhiTheta | Psi1Psi2 | Psi2Psi1,
            **kwargs):
    """
    Python wrapper for the analyze function of the PSSFSS package.

    Differences from the Julia version:
    - Named tuples containing the steering parameters must be created using the ThetaPhi, PhiTheta,
      Psi1Psi2, or Psi2Psi1 functions.

    For detailed documentation from the Julia version, type doc(analyze) or see 
    https://simonp0420.github.io/PSSFSS.jl/stable/reference/#PSSFSS.analyze
    """

    # Avoid mutating strata:
    strata = strata.copy()

    # Need to convert any RWGSheet elements sheet to sheet.jRWGSheet
    for index, v in enumerate(strata):
        if isinstance(v, RWGSheet):
            strata[index] = v.jRWGSheet

    # Convert strata Python vector to a Julia vector:
    jlstrata = convert(jl.Vector, strata)

    # Convert steering from a Python named tuple to a Julia named tuple:
    f1, f2 = steering._fields
    if isinstance(steering[0], int | float):
        v1 = steering[0]
    else:
        v1 = convert(jl.Vector, np.array(steering[0]))

    if isinstance(steering[1], int | float):
        v2 = steering[1]
    else:
        v2 = convert(jl.Vector, np.array(steering[1]))

    jlsteering = jl.seval(f'({f1}={v1}, {f2}={v2})')
    return jl.analyze(jlstrata, flist, jlsteering, **kwargs)


# Simulate the Julia @outputs macro with a Python function:
def atoutputs(string: str) -> tuple:
    """
    Wrapper function for the @outputs macro of the Julia PSSFSS package.  See the Outputs
    section of the PSSFSS user manual at 
    https://simonp0420.github.io/PSSFSS.jl/stable/manual/#Outputs for details of usage.
    The atoutputs function accepts arguments to be passed to @outputs in the form of a 
    single string.  E.g. 
        outrequests = atoutputs('FGHz theta s21dB(L,v) s21dB(R,V)')
    """
    return jl.seval('@outputs ' + string)


def extract_result(results: VectorValue | ArrayValue, outreq: tuple) -> np.array:
    """
    Wrapper function for the Julia PSSFSS extract_result function.  Returns a numpy array.
    For detailed documentation, type doc(extract_result) or see the Julia PSSFSS version 
    documentation at 
    https://simonp0420.github.io/PSSFSS.jl/stable/reference/#PSSFSS.Outputs.extract_result
    """
    outputs = np.array(jl.extract_result(results, outreq))
    return outputs

# Python wrapper for res2tep:
def res2tep(results: VectorValue | str, tepfile: str, name="tep", clas="res2tep") -> None:
    """
    Wrapper function for the Julia PSSFSS res2tep function.  Creates a Ticra-compatible
    TEP file from a PSSFSS result file, or from the vector of results returned by the 
    analyze function. For detailed documentation, type doc(res2tep) or see the Julia PSSFSS
    version documentation at 
    https://simonp0420.github.io/PSSFSS.jl/stable/reference/#PSSFSS.Outputs.res2tep
    Note that where the Julia documentation references the keyword argument "class", it must 
    be replaced here by "clas" (to avoid infringing on Python's builtin keyword).
    """
    kwdict = {"name": name, "class": clas}
    jl.res2tep(results, tepfile, **kwdict)

# Python wrapper res2fresnel:
def res2fresnel(results: VectorValue | str, tepfile: str) -> None:
    """
    Wrapper function for the Julia PSSFSS res2fresnel function.  Creates an HFSS SBR+-compatible
    Fresnel table from a PSSFSS result file, or from the vector of results returned by the 
    analyze function. For detailed documentation, type doc(res2fresnel) or see the Julia PSSFSS
    version documentation at 
    https://simonp0420.github.io/PSSFSS.jl/stable/reference/#PSSFSS.Outputs.res2fresnel
    """
    jl.res2fresnel(results, tepfile)


from rich.console import Console
from rich.markdown import Markdown
console = Console()

import types

# Documentation function to print markdown formatted Julia docstrings
def doc(arg):
    """
    Pretty-print the Julia markdown documentation for a wrapped function to the user's console. For example,
    typing 
    
    >>> import pypssfss as pf
    >>> pf.doc(pf.analyze)
     
    will generate a richly formatted printout of the Julia PSSFSS analyze function to the user's console.
    """
    name = ""
    pssfss_fnames = ('analyze', 'diagstrip', 'extract_result', 'jerusalemcross', 'Layer', 'loadedcross', 
                     'manji', 'meander', 'pecsheet', 'pixels', 'pmcsheet', 'polyring', 'rectstrip', 
                     'res2fresnel', 'res2tep', 'sinuous', 'splitring', 'sympixels')
    if isinstance(arg, types.FunctionType) and arg.__name__ in pssfss_fnames:
         name = arg.__name__
    elif isinstance(arg, RWGSheet):
         name = arg.style
    
    if len(name) > 0:
         console.print(Markdown(jl.seval(f'repr(REPL.doc({name}))')))
    else:
            help(arg)

