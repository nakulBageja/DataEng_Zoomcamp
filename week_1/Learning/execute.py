# Code to execute ipython/jupyter notebooks from within python
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

filename = 'upload_data.ipynb'

with open(filename) as ff:
    nb_in = nbformat.read(ff, nbformat.NO_CONVERT)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

nb_out = ep.preprocess(nb_in)
