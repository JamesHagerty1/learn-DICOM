"""
pydicom is not a DICOM server (see pynetdicom instead), and is not primarily 
about viewing images. It is designed to let you manipulate data elements in 
DICOM files with Python code.
"""


import pydicom
from pydicom.data import get_testdata_file


################################################################################


def main():
    fpath = get_testdata_file("CT_small.dcm") # comes with package
    print(fpath)
    print(pydicom.__version__)

if __name__ == "__main__":
    main()
