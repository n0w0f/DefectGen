# Import statements
import os

from pymatgen.io.cif import CifWriter 
from pymatgen.ext.matproj import MPRester
from pymatgen.core import Structure, Lattice, Molecule
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.analysis.defects.generators import DefectGenerator, InterstitialGenerator, VacancyGenerator

#from matplotlib import pyplot as plt
#%matplotlib inline



def write_strcutre(structure,name,path):
    '''
    write structure in cif format 
    #TODO write in desired format
    #TODO write in desired path
    #TODO write list of objects
    input --> pymatgen structure object
    return None
    '''
    os.chdir(path)

    cif_object=CifWriter(structure , symprec=None, write_magmoms=False, significant_figures=8, angle_tolerance=5.0, refine_struct=True)
    cif_object.write_file(filename=name)

    
    

def gen_vacancy(structure,element):
    '''
    function to generate a list of structures with vacancies
    input --> pristine structure (pymaatgen structure), element to be removed (str)
    output --> list of unique defect objects (list)
    '''
    defects = [defect for defect in VacancyGenerator(structure,element)]

    return defects




def defective_structure(defect_objects,Write=bool):
    '''
    function to produce structure from defect objects

    input -> list of defect objects, boolean variable to write the structures or not
    output -> list of defective structures, write the structure 
    '''
    defect_structures = [defect.generate_defect_structure(supercell=(1, 1, 1)) for defect in defect_objects]

    
    if(Write==True):1
    # Directory
    directory = f"{defect_structures[-1].composition.reduced_formula}"
    # Parent Directory path
    parent_dir = os.getcwd()
    # Path
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

    for idx,defect in enumerate(defect_structures): 
        
        name=f"{defect.composition.reduced_formula}__{idx}.cif"
        write_strcutre(defect,name,path)
        
        
    return defect_structures


def main():
    m = MPRester("WqTnpNOkd157DcJt")
    material_composition = "Li7La3Hf2O12"
    defect_element = "Li"
    structs = m.get_data(material_composition, prop="structure")
    material=structs[0]['structure']
    defects = gen_vacancy(material,'defect_element')
    defective_structure(defects,True)

    
if __name__ == "__main__":
    main()
