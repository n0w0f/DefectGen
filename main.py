#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import argparse

from pymatgen.io.cif import CifWriter 
from pymatgen.ext.matproj import MPRester
from pymatgen.core import Structure, Lattice, Molecule
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.analysis.defects.generators import DefectGenerator,VoronoiInterstitialGenerator, InterstitialGenerator, VacancyGenerator

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

def gen_interstitial(structure,element):
    '''
    function to generate a list of structures with vacancies
    input --> pristine structure (pymaatgen structure), element to be removed (str)
    output --> list of unique defect objects (list)
    '''
    defects = [defect for defect in InterstitialGenerator(structure,element)]

    return defects

def gen_voronoi_interstitial(structure,element):
    '''
    function to generate a list of structures with vacancies
    input --> pristine structure (pymaatgen structure), element to be removed (str)
    output --> list of unique defect objects (list)
    '''
    defects = [defect for defect in VoronoiInterstitialGenerator(structure, element)]

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

    parser = argparse.ArgumentParser(
        "Defect creator", description="Generate Defect structures for given material and point defect "
    )
    parser.add_argument("material_composition", help="Enter the chemical formula.", type=str)
    parser.add_argument("defect_type", help="Currently support vacancy and interstitial.", type=str)
    parser.add_argument("point_defect", help="Enter element type", type=str)
    args = parser.parse_args()

    #material_composition = "Li7La3Hf2O12"
    #defect_element = "Li"

    structs = m.get_data(args.material_composition, prop="structure")
    material=structs[0]['structure']

    if(args.defect_type=="vacancy"):
        defects = gen_vacancy(material,args.point_defect)
    elif(args.defect_type=="interstitial"):
        defects = gen_voronoi_interstitial(material,args.point_defect)

    defective_structure(defects,True)



    
if __name__ == "__main__":
    main()
