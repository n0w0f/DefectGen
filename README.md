# DefectGen
This project is to enumerate structure with defects

Given the material composition and a point defect the program will enumerate and store the generated structure in a folder

1. switch to working directory.	

cd DefectGen

2. run the script below within the directory to create the virtual environment:

python3 -m venv defectgen

start the virtual environment :

source defectgen/bin/activate

3. Install the dependencies

pip install -r requirement.txt 

4. Usage: python3 main.py material_composition defect_type point_defect_element

Generate Defect structures for given material and point defect

positional arguments:
  material_composition  Enter the chemical formula.
  defect_type           Currently support vacancy and interstitial.
  point_defect          Enter element type

optional arguments:
  -h, --help            show this help message and exit

