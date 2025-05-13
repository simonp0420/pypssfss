
# Introduction

## Background Information
In order to learn how to use `PyPSSFSS` please first read the [PSSFSS User Manual](https://simonp0420.github.io/PSSFSS.jl/stable/manual/).  Only after looking over this material will you understand the steps needed to set up a desired geometry, visualize triangulations, perform an analysis, and extract the desired performance parameters from the solution.

## Differences in PyPSSFSS versus PSSFSS

### Specifying the Geometry
The stratified medium to be analyzed is specified as a Python `list` containing 2 or more `Layer` objects and zero or more
`RWGSheet` objects.

#### Length Variables
The package exports the following variables that represent lengths: `mm`, `cm`, `inch`, `mil`.  To represent
a length of, say, 0.6 mil, one would type `0.6 * mil` to perform the necessary multiplication.

#### The `Layer` Constructor
The `Layer` constructor in this package accepts only ASCII for keyword argument names.  For example:
`Layer(epsr = 2.2, tandel = 0.002, width = 1.5*mm)` to represent a 1.5 millimeter thick dielectric layer with the specified
relative permittivity and loss tangent.

#### The `RWGSheet` Constructors
`RWGSheet` objects are instantiated by use of one of the constructor methods `diagstrip`,
`jerusalemcross`, `loadedcross`, `manji`, `meander`, `pecsheet`, `pixels`, `pmcsheet`, `polyring`, `rectstrip`,
`sinuous`, `splitring`, and `sympixels`.  Examples of all of these are shown in the 
[Element Gallery](https://simonp0420.github.io/PSSFSS.jl/stable/PSS_&_FSS_Element_Gallery)
of the `PSSFSS` documentation.  Clicking on one of the images in the gallery will open a page showing the code used
to generate triangulation in the image.  Extensive documentation for these constructors, obtained from the Julia source docstring, and pretty-printed to the user's terminal, is available by use of the `doc` function exported by this package.
E.g. `doc(manji)` will provide documentation for the `manji` element.

Sheet geometry can be exported to STL files using the `export_sheet` method as follows:
```python
import pypssfss as pf
sheet = pf.rectstrip(....)
sheet.export_sheet("rectstrip.stl")
```

#### Plotting Sheet Triangulations
It is important to visualize the triangulation of an FSS/PSS element prior to analysis.  This is easily done with the
`plot_sheet` function, which uses the standard Matplotlib library.  See `help(plot_sheet)` for more information, and 
the Usage Examples section of this manual for an example of its use. 


### Steering
In the Julia version, one would use a named tuple, e.g., `steer = (θ=0, ϕ=0)` to specify a normal incidence case.  Since
Python lacks named tuples as built-in objects, `PyPSSFSS` exports four constructors `ThetaPhi`, `PhiTheta`, `Psi1Psi2`,
and `Psi2Psi1` which are used to construct the steering specifyers.  The first two are used to define the θ and ϕ steering
angles; the second two are used to specify the unit cell incremental phase shifts.  Each accepts two input arguments, which
may be numeric scalars or iterables, interpreted in degrees.  Some examples:

```python
>>> import pypssfss as pf
>>> pf.ThetaPhi(0,0)
ThetaPhi(theta=0, phi=0)
>>> pf.ThetaPhi(range(0, 21, 10), [0, 45])
ThetaPhi(theta=range(0, 21, 10), phi=[0, 45])
>>> pf.PhiTheta([0, 45], range(0, 21, 10))
PhiTheta(phi=[0, 45], theta=range(0, 21, 10))
```

The only difference in the last two examples is the order of execution. If passed to the `analyze` function,
the final example above would cause ϕ to be incremented in the outmost analysis loop, with the loop over θ nested
just inside it, and the loop over frequency nested inside the θ loop.  In the `ThetaPhi` examples, θ would be 
the outermost loop.

### Performing the Analysis
For this, use the `analyze` function, which takes the same positional and optional keyword arguments as the 
Julia version documented [here](https://simonp0420.github.io/PSSFSS.jl/stable/reference/#PSSFSS.analyze), 
except for the steering inputs as described previously.  The `analyze` function returns a list of Julia `Result` objects
which should usually be assigned to a variable for further processing using the `extract_result` function.

### Extracting Performance Parameters
Because of the large number of performance parameters that are available to be extracted, the `PSSFSS` package
has implemented a tiny Domain Specific Language (DSL) to specify the desired outputs, using the macro facility
built into Julia. This is implemented in the `@outputs` macro of the `PSSFSS` package, as documented
in [this](https://simonp0420.github.io/PSSFSS.jl/stable/manual/#Requesting-Additional-Outputs) section of the
manual (which is essential reading). Here in `PyPSSFSS`, the user must create a string containing the text
that would be passed to the `@outputs` macro. The string is passed as an argument to the `atoutputs` function
which returns an object that can be used to retrieve the desired data using the `extract_result` function.
For example:

```python
results = analyze(...)
outrequests = atoutputs('FGHz theta s21dB(L,v) s21dB(R,V)')
data = extract_result(results, outrequests)
```

The `extract_result` function will return a NumPy matrix, each column of which contains the data corresponding to one
of the items in the string passed to `atoutputs`. There are more examples using the `atoutputs` and `extract_result`
functions in the Usage Examples section of this manual.

### Exporting Results
Results can be exported to HFSS SBR+-compatible Fresnel tables using `res2fresnel` or to Ticra-compatible
TEP files using `res2tep`.