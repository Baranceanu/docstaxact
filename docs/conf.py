import os
import sys

sys.path.insert(0, os.path.abspath('.'))

# Project info
project = 'Docs Taxact'
author = 'Irma Aguayo'
release = '1.0'

# General config
extensions = []

templates_path = ['_templates']
exclude_patterns = []

# HTML settings
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# ✅ Bing Verification (WORKING METHOD)
html_context = {
    "metatags": '<meta name="msvalidate.01" content="53640568D2E38666845B87AB3560651C" />'
}
