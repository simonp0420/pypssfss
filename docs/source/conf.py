# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pypssfss'
copyright = '2025, Peter S. Simon'
author = 'Peter S. Simon'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    #"myst_parser", # Cannot specify this along with myst_nb.  Only the latter is required since it uses this.
    "myst_nb",
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

autoapi_dirs = ["../../src/pypssfss"]  # location to parse for API reference
templates_path = ['_templates']
exclude_patterns = []
autoapi_options = [#'members', 
                   #'undoc-members',
                   #'private-members',
                   #'show-inheritance',
                   #'show-module-summary',
                   'special-members',
                   'imported-members',
                   ]

def skip_modules(app, what, name, obj, skip, options):
    if what == "module":
       skip = True
    return skip

def setup(sphinx):
   sphinx.connect("autoapi-skip-member", skip_modules)

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
