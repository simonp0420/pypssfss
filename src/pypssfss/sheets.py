
import numpy as np

from juliacall import Main as jl
import juliacall
import matplotlib.pyplot as plt

# Definitions of PSSFSS compatible units:
class pssfss_units:
    def __init__(self, label: str) -> None:
        self.label = label        

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return jl.seval(str(other) + self.label)
        else:
            raise TypeError("Cannot multiply pssfss_units with non-numeric type")
        
    def __rmul__(self, other):
            return self * other
    
    def __repr__(self):
        return self.label

    def __str__(self):
        return self.label

mm = pssfss_units('mm')
cm = pssfss_units('cm')
inch = pssfss_units('inch')
mil = pssfss_units('mil')

# Utility function for correcting Python arguments prior to calling the Julia sheet constructor.
# Checks for 'units' key and replaces the value with the Julia equivalent.  
# Checks for list values and converts them to numpy arrays.
# Checks for 'clas' keyword and replaces with 'class'.
def fixsheetargs(kwargs) -> None:
    for (k, v) in kwargs.items():
        if k == 'units':
             if isinstance(v, pssfss_units):
                kwargs[k] = jl.seval(v.label)
        if isinstance(v, (list, np.ndarray)):
            kwargs[k] = jl.convert(jl.Vector, v)
    if 'clas' in kwargs:
        classvalue = kwargs.pop('clas')
        kwargs["class"] = classvalue

# Define the RWGSheet class:
class RWGSheet:
    def __init__(self, jlsheet: juliacall.AnyValue) -> None:
        self.jRWGSheet = jlsheet
        self.units = pssfss_units(str(jl.getfield(jlsheet, jl.Symbol('units'))))
        self.s1 = jl.getfield(jlsheet, jl.Symbol('s₁')).to_numpy()
        self.s2 = jl.getfield(jlsheet, jl.Symbol('s₂')).to_numpy()
        self.e1 = jl.getfield(jlsheet, jl.Symbol('e1')).to_numpy()
        self.e2 = jl.getfield(jlsheet, jl.Symbol('e2')).to_numpy()
        self.fv = jl.getfield(jlsheet, jl.Symbol('fv')).to_numpy()
        self.fe = jl.getfield(jlsheet, jl.Symbol('fe')).to_numpy()
        self.clas = jl.getfield(jlsheet, jl.Symbol('class'))
        self.info = jl.getfield(jlsheet, jl.Symbol('info'))
        self.style = jl.getfield(jlsheet, jl.Symbol('style'))
        self.rho = jl.getfield(jlsheet, jl.Symbol('ρ')).to_numpy()
        
    def __repr__(self) -> str:
         return self.jRWGSheet.__repr__()[7:]    

    def edgecount(self) -> int:
        return jl.edgecount(self.jRWGSheet)

    def facecount(self) -> int:
        return jl.facecount(self.jRWGSheet)

    def nodecount(self) -> int:
        return jl.nodecount(self.jRWGSheet)

    def export_sheet(self, fname: str, export_type:str = 'STL_ASCII') -> None:
        jl.export_sheet(fname, self.jRWGSheet, jl.seval(export_type))        


# Define the Python sheet constructors:
def diagstrip(**kwargs) -> RWGSheet:
    """
    Wrapper function for the Julia PSSFSS diagstrip constructor. For detailed documentation of the Julia PSSFSS
    version, type doc(diagstrip), or see
    https://simonp0420.github.io/PSSFSS.jl/stable/reference/#PSSFSS.Elements.diagstrip .
    Note that where the Julia documentation refers to the "class" keyword argument, here "clas" must be substituted
    to avoid infringing on the Python builtin keyword.
    """
    fixsheetargs(kwargs)
    return RWGSheet(jl.diagstrip(**kwargs))

def jerusalemcross(**kwargs) -> RWGSheet:
    """
    Wrapper function for the Julia PSSFSS jerusalemcross constructor. For detailed documentation of the Julia PSSFSS
    version, type doc(jerusalemcross), or see
    https://simonp0420.github.io/PSSFSS.jl/stable/reference/#PSSFSS.Elements.jerusalemcross .
    Note that where the Julia documentation refers to the "class" keyword argument, here "clas" must be substituted
    to avoid infringing on the Python builtin keyword.
    """
    "See the Julia documentation at https://simonp0420.github.io/PSSFSS.jl/stable/reference/#PSSFSS.Elements.jerusalemcross"
    fixsheetargs(kwargs)
    return RWGSheet(jl.jerusalemcross(**kwargs))

def loadedcross(**kwargs) -> RWGSheet:
    """
    Wrapper function for the Julia PSSFSS loadedcross constructor. For detailed documentation of the Julia PSSFSS
    version, type doc(loadedcross), or see
    https://simonp0420.github.io/PSSFSS.jl/stable/reference/#PSSFSS.Elements.loadedcross .
    Note that where the Julia documentation refers to the "class" keyword argument, here "clas" must be substituted
    to avoid infringing on the Python builtin keyword.
    """
    fixsheetargs(kwargs)
    return RWGSheet(jl.loadedcross(**kwargs))

def manji(**kwargs) -> RWGSheet:
    """
    Wrapper function for the Julia PSSFSS manji constructor. For detailed documentation of the Julia PSSFSS
    version, type doc(manji), or see
    https://simonp0420.github.io/PSSFSS.jl/stable/reference/#PSSFSS.Elements.manji .
    Note that where the Julia documentation refers to the "class" keyword argument, here "clas" must be substituted
    to avoid infringing on the Python builtin keyword.
    """
    fixsheetargs(kwargs)
    return RWGSheet(jl.manji(**kwargs))

def meander(**kwargs) -> RWGSheet:
    """
    Wrapper function for the Julia PSSFSS meander constructor. For detailed documentation of the Julia PSSFSS
    version, type doc(meander), or see
    https://simonp0420.github.io/PSSFSS.jl/stable/reference/#PSSFSS.Elements.meander .
    Note that where the Julia documentation refers to the "class" keyword argument, here "clas" must be substituted
    to avoid infringing on the Python builtin keyword.
    """
    fixsheetargs(kwargs)
    return RWGSheet(jl.meander(**kwargs))

def pecsheet() -> RWGSheet:
    """
    Return a variable of type RWGSheet that contains a perfect electric conducting sheet (i.e. an "E-wall").
    """
def pixels(**kwargs) -> RWGSheet:
    """
    Wrapper function for the Julia PSSFSS pixels constructor. For detailed documentation of the Julia PSSFSS
    version, type doc(pixels), or see
    https://simonp0420.github.io/PSSFSS.jl/stable/reference/#PSSFSS.Elements.pixels .
    Note that where the Julia documentation refers to the "class" keyword argument, here "clas" must be substituted
    to avoid infringing on the Python builtin keyword.
    """
    fixsheetargs(kwargs)
    return RWGSheet(jl.pixels(**kwargs))

def pmcsheet() -> RWGSheet:
    """
    Return a variable of type RWGSheet that contains a perfect magnetic conducting sheet (i.e. an "H-wall").
    """
    return RWGSheet(jl.pmcsheet())

def polyring(**kwargs) -> RWGSheet:
    """
    Wrapper function for the Julia PSSFSS polyring constructor. For detailed documentation of the Julia PSSFSS
    version, type doc(polyring), or see
    https://simonp0420.github.io/PSSFSS.jl/stable/reference/#PSSFSS.Elements.polyring .
    Note that where the Julia documentation refers to the "class" keyword argument, here "clas" must be substituted
    to avoid infringing on the Python builtin keyword.
    """
    fixsheetargs(kwargs)
    return RWGSheet(jl.polyring(**kwargs))
polyring.__doc__ = jl.seval('@doc polyring')

def rectstrip(**kwargs) -> RWGSheet:
    """
    Wrapper function for the Julia PSSFSS rectstrip constructor. For detailed documentation of the Julia PSSFSS
    version, type doc(rectstrip), or see
    https://simonp0420.github.io/PSSFSS.jl/stable/reference/#PSSFSS.Elements.rectstrip .
    Note that where the Julia documentation refers to the "class" keyword argument, here "clas" must be substituted
    to avoid infringing on the Python builtin keyword.
    """
    fixsheetargs(kwargs)
    return RWGSheet(jl.rectstrip(**kwargs))

def sinuous(**kwargs) -> RWGSheet:
    """
    Wrapper function for the Julia PSSFSS sinuous constructor. For detailed documentation of the Julia PSSFSS
    version, type doc(sinuous), or see
    https://simonp0420.github.io/PSSFSS.jl/stable/reference/#PSSFSS.Elements.sinuous .
    Note that where the Julia documentation refers to the "class" keyword argument, here "clas" must be substituted
    to avoid infringing on the Python builtin keyword.
    """
    fixsheetargs(kwargs)
    return RWGSheet(jl.sinuous(**kwargs))

def splitring(**kwargs) -> RWGSheet:
    """
    Wrapper function for the Julia PSSFSS splitring constructor. For detailed documentation of the Julia PSSFSS
    version, type doc(splitring), or see
    https://simonp0420.github.io/PSSFSS.jl/stable/reference/#PSSFSS.Elements.splitring .
    Note that where the Julia documentation refers to the "class" keyword argument, here "clas" must be substituted
    to avoid infringing on the Python builtin keyword.
    """
    fixsheetargs(kwargs)
    return RWGSheet(jl.splitring(**kwargs))

def sympixels(**kwargs) -> RWGSheet:
    """
    Wrapper function for the Julia PSSFSS sympixels constructor. For detailed documentation of the Julia PSSFSS
    version, type doc(sympixels), or see
    https://simonp0420.github.io/PSSFSS.jl/stable/reference/#PSSFSS.Elements.sympixels .
    Note that where the Julia documentation refers to the "class" keyword argument, here "clas" must be substituted
    to avoid infringing on the Python builtin keyword.
    """
    fixsheetargs(kwargs)
    return RWGSheet(jl.sympixels(**kwargs))

# Plotting
import matplotlib.pyplot as plt
import numpy as np

def plot_sheet(sheet, edges=True, faces=False, nodes=False,
               edgenumbers=False, facenumbers=False, nodenumbers=False,
               edgecolor = 'red', facecolor = 'red', nodecolor = 'black', unitcellcolor = 'blue',
               unitcell=False, rep=(1, 1), fontsize=9, linewidth=1.5):
    """
    Plot an RWGSheet object using Matplotlib.  This function must be followed by a call to matplotlib.pyplot.show()
    to make the plot visible.

    Parameters (all but `sheet` are optional keyword arguments):
        sheet: RWGSheet
            The sheet object to plot.
        edges=True, faces=False, nodes=False: bool
            Whether to plot edges, faces, or nodes.
        edgenumbers=False, facenumbers=False, nodenumbers=False: bool
            Whether to annotate edges, faces, or nodes with their indices.
        edgecolor='red', facecolor='red', nodecolor='black', unitcellcolor='blue': str,
            Colors to use for the plotted items.
        unitcell=False: bool
            Whether to plot the unit cell boundary.
        rep: tuple
            A 2-tuple of positive integers giving the number of repetitions to display in the two periodic directions.
        fontsize: int
            Font size for annotations.
    """
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlabel(f"x ({sheet.units})")
    ax.set_ylabel(f"y ({sheet.units})")

    mrange = range(1, rep[0] + 1) if isinstance(rep[0], int) else rep[0]
    nrange = range(1, rep[1] + 1) if isinstance(rep[1], int) else rep[1]

    for m in mrange:
        for n in nrange:
            x0, y0 = (m - 1) * sheet.s1 + (n - 1) * sheet.s2

            # Plot faces
            if faces:
                for i in range(sheet.fv.shape[1]):
                    points = sheet.rho[sheet.fv[:, i] - 1]
                    x = x0 + np.array([p[0] for p in points] + [points[0][0]])
                    y = y0 + np.array([p[1] for p in points] + [points[0][1]])
                    ax.fill(x, y, color=facecolor, alpha=0.8)

            # Plot edges
            if edges:
                for i in range(len(sheet.e1)):
                    points = sheet.rho[[sheet.e1[i] - 1, sheet.e2[i] - 1]]
                    x = x0 + np.array([p[0] for p in points])
                    y = y0 + np.array([p[1] for p in points])
                    ax.plot(x, y, linestyle='solid', color=edgecolor, lw=linewidth)

            # Plot unit cell
            if unitcell:
                points = [np.zeros(2), sheet.s1, sheet.s1 + sheet.s2, sheet.s2]
                x = x0 + np.array([p[0] for p in points] + [0])
                y = y0 + np.array([p[1] for p in points] + [0])
                ax.plot(x, y, color=unitcellcolor, linestyle='dotted', lw=linewidth)

            # Plot nodes
            if nodes:
                x = x0 + np.array([p[0] for p in sheet.rho])
                y = y0 + np.array([p[1] for p in sheet.rho])
                ax.scatter(x, y, color='black', s=10)

            # Annotate nodes
            if nodenumbers:
                for i, p in enumerate(sheet.rho):
                    x, y = x0 + p[0], y0 + p[1]
                    ax.text(x, y, str(i + 1), fontsize=fontsize, color='black', ha='center', va='center')

            # Annotate edges
            if edgenumbers:
                for i in range(len(sheet.e1)):
                    p1, p2 = sheet.rho[sheet.e1[i] - 1], sheet.rho[sheet.e2[i] - 1]
                    x, y = x0 + (p1[0] + p2[0]) / 2, y0 + (p1[1] + p2[1]) / 2
                    ax.text(x, y, str(i + 1), fontsize=fontsize, color=edgecolor, ha='center', va='center')

            # Annotate faces
            if facenumbers:
                for i in range(sheet.fv.shape[1]):
                    points = sheet.rho[sheet.fv[:, i]]
                    x = x0 + np.mean([p[0] for p in points])
                    y = y0 + np.mean([p[1] for p in points])
                    ax.text(x, y, str(i + 1), fontsize=fontsize, color=facecolor, ha='center', va='center')
