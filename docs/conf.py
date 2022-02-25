"""Sphinx configuration."""
project = "Advancedlabcourse Utils"
author = "Marc Broghammer"
copyright = "2022, Marc Broghammer"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
