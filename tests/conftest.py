import os
import sys

# Rend les modules du site (build, urls, i18n, presentation_text, ...)
# importables depuis les tests, quel que soit le repertoire d'execution de
# pytest.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
