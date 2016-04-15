"""
Create a Test Suite by glob pattern maching.
"""

import os
import glob
import unittest
import pkg_resources

NAMESPACE = "error_spike"
TESTS_DIRNAME = "tests"
FNAME_PATTERN = "test_*.py"

def suite():
    ret_val = unittest.TestSuite()
    dirname = pkg_resources.resource_filename(NAMESPACE, TESTS_DIRNAME)
    fqnames = glob.glob(os.path.join(dirname, FNAME_PATTERN))
    for fqname in fqnames:
        _ns = os.path.splitext(os.path.split(fqname)[1])[0]
        name = "{0}.{1}.{2}".format(NAMESPACE, TESTS_DIRNAME, _ns)
        __import__(name)
        _suite = unittest.defaultTestLoader.loadTestsFromName(name)
        ret_val.addTest(_suite)
    return ret_val 
