import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join('..', '..', 'djangotutorial')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

project = 'djangotutor'
copyright = '2025, Arsen Sardaryan'
author = 'Arsen Sardaryan'
release = '0.0.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',  # для автогенерации подсказок типов
    'sphinxcontrib_django',  # для поддержки Django
]

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': True,
    'show-inheritance': True,
}

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

html_theme = 'alabaster'
html_static_path = ['_static']
