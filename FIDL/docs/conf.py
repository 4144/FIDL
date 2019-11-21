# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import mock
sys.path.insert(0, os.path.abspath('..'))

# ---------------------------------------------------------------
# Mocking Hex-Rays
#
# This is necessary since we can't import `ida_hexrays`
# in `decompiler_utils.py`.
# All that we need are the numerical values for the variables
# below. We produce this code with the script `mock_hexrays.py`
# ---------------------------------------------------------------
m = mock.Mock()
m.cit_asm = 82
m.cit_block = 71
m.cit_break = 78
m.cit_continue = 79
m.cit_do = 76
m.cit_empty = 70
m.cit_end = 83
m.cit_expr = 72
m.cit_for = 74
m.cit_goto = 81
m.cit_if = 73
m.cit_return = 80
m.cit_switch = 77
m.cit_while = 75
m.cot_add = 35
m.cot_asg = 2
m.cot_asgadd = 6
m.cot_asgband = 5
m.cot_asgbor = 3
m.cot_asgmul = 8
m.cot_asgsdiv = 12
m.cot_asgshl = 11
m.cot_asgsmod = 14
m.cot_asgsshr = 9
m.cot_asgsub = 7
m.cot_asgudiv = 13
m.cot_asgumod = 15
m.cot_asgushr = 10
m.cot_asgxor = 4
m.cot_band = 21
m.cot_bnot = 50
m.cot_bor = 19
m.cot_call = 57
m.cot_cast = 48
m.cot_comma = 1
m.cot_empty = 0
m.cot_eq = 22
m.cot_fadd = 42
m.cot_fdiv = 45
m.cot_fmul = 44
m.cot_fneg = 46
m.cot_fnum = 62
m.cot_fsub = 43
m.cot_helper = 68
m.cot_idx = 58
m.cot_insn = 66
m.cot_land = 18
m.cot_last = 69
m.cot_lnot = 49
m.cot_lor = 17
m.cot_memptr = 60
m.cot_memref = 59
m.cot_mul = 37
m.cot_ne = 23
m.cot_neg = 47
m.cot_num = 61
m.cot_obj = 64
m.cot_postdec = 54
m.cot_postinc = 53
m.cot_predec = 56
m.cot_preinc = 55
m.cot_ptr = 51
m.cot_ref = 52
m.cot_sdiv = 38
m.cot_sge = 24
m.cot_sgt = 28
m.cot_shl = 34
m.cot_sizeof = 67
m.cot_sle = 26
m.cot_slt = 30
m.cot_smod = 40
m.cot_sshr = 32
m.cot_str = 63
m.cot_sub = 36
m.cot_tern = 16
m.cot_type = 69
m.cot_udiv = 39
m.cot_uge = 25
m.cot_ugt = 29
m.cot_ule = 27
m.cot_ult = 31
m.cot_umod = 41
m.cot_ushr = 33
m.cot_var = 65
m.cot_xor = 20

sys.modules['ida_hexrays'] = m


# -- Project information -----------------------------------------------------

project = u'FIDL'
copyright = u'2019, FLARE\'s OTF'
author = u'FLARE\'s OTF'

# The short X.Y version
version = u'1.0'
# The full version, including alpha/beta/rc tags
release = u'1.0'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx_rtd_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# Other possible themes: 'haiku', 'agogo', 'sphinxdoc', 'sphinx_rtd_theme'
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'FIDLdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'FIDL.tex', u'FIDL Documentation',
     u'FLARE\'s OTF', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'fidl', u'FIDL Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'FIDL', u'FIDL Documentation',
     author, 'FIDL', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------
autodoc_mock_imports = ["idc", "idaapi", "idautils", "ida_hexrays"]
