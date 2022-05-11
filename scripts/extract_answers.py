#!/usr/bin/env python
import nbformat
import os
import sys


# read notebook
notebooknode = nbformat.read(os.path.abspath(sys.argv[1]),4)
filename, fileext = os.path.splitext(os.path.basename(sys.argv[1]))

if (fileext != ".ipynb"):
	raise Exception('The first argument has to be a path to' \
						' a jupyter notebook')

f = open(filename + ".jktest", "w")

results = []
for cell in notebooknode["cells"]:
	if cell["cell_type"] == "code":
		if("outputs" in cell.keys() and cell["outputs"]):
			results.append(cell["outputs"][0]["text"].strip())
		else:
			raise Exception('One code cell is mising outputs. ' \
								'Please execute all cells and save the ' \
								'notebook before running this script')

f.write("\n*****\n".join(results))