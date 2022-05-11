#!/usr/bin/env python
import nbformat
import os
import sys
from nbconvert.preprocessors import ExecutePreprocessor
from pathlib import Path


# Get path of this script
my_path = os.path.abspath(os.path.dirname(__file__))
# Path to testfiles
test_dir = os.path.join(my_path, "../test")
# Path to lectures
notebook_dir = os.path.join(my_path, "../lectures")

# Run tests for all testfiles
for test in os.listdir(test_dir):
    print("Testing " + test)
    # Get test results to compare to
    test_path = os.path.join(test_dir, test)
    print(test_path)
    with open(test_path,'r') as test_file:
        test_list_ = test_file.read().strip().split("*****")
        test_list = [e.strip().split(",\n") for e in test_list_]
    
    # Get notebook path
    name, fileext = os.path.splitext(test)
    nb_path = os.path.join(notebook_dir, name + ".ipynb")

    # Open Notebook
    with open(nb_path) as nb_file:
        nb_in = nbformat.read(nb_file, nbformat.NO_CONVERT)

    # Execute Notebook
    ep = ExecutePreprocessor(kernel_name='jknowrob')
    nb_out = ep.preprocess(nb_in)[0]

    # Comparing result with tests
    test_id = 0
    for cell in nb_out["cells"]:
        if cell["cell_type"] == "code":
            # Get the list of results and sort them to make them comparable
            result = cell["outputs"][0]["text"].strip().split(",\n")
            result.sort()
            expected = test_list[test_id]
            expected.sort()
            # Test if the result equals the expected result
            print("-----------------------------")
            if expected == result:
                    print('Test successfull for: \n ' \
                        + str(cell["source"]))
            else:
                raise Exception('Test failed for: \n ' \
                        + str(cell["source"]) + \
                        '\nExpected: ' + str(expected) + \
                        '\nResult: \n' + str(result))
            test_id += 1


            