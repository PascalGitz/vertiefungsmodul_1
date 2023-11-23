import pandas as pd
import os
import sys
import numpy as np




def deformation_fachwerk(Laststufe=0):
    from RFEM.enums import NodalSupportType, NodalLoadDirection, CaseObjectType
    from RFEM.initModel import CalculateSelectedCases, Model, Calculate_all
    from RFEM.BasicObjects.material import Material
    from RFEM.BasicObjects.section import Section
    from RFEM.BasicObjects.node import Node
    from RFEM.BasicObjects.member import Member
    from RFEM.TypesForNodes.nodalSupport import NodalSupport
    from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
    from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
    from RFEM.Loads.nodalLoad import NodalLoad
    from RFEM.Calculate.meshSettings import GetModelInfo
    from RFEM.Results.resultTables import ResultTables
    # Setzt den pfad aktuell
    baseName = os.path.basename(__file__)
    dirName = os.path.dirname(__file__)
    print(baseName)
    print(dirName)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path_coords = '../../../base/koordinaten/punkte_flach.re2'




    #Knoten Import aus Allplan Koordinaten
    df = pd.read_csv(path_coords, skiprows=2, skipfooter=0, delimiter=',', engine='python', names=['PKT-NR', 'X', 'Y', 'Z', 'CODE'])
    df = df.drop(columns=['CODE'])
    df['PKT-NR'] = df['PKT-NR'].astype(int)
    nodenames = list(df['PKT-NR'])

    #Modelinitiierung
    Model(False, "Fachwerk_flach", delete=True) 
    Model.clientModel.service.begin_modification()


    for i in range(len(df)):
        name = df.iloc[i,0]
        x_koord = df.iloc[i,1]
        y_koord = df.iloc[i,3]
        z_koord = df.iloc[i,2]
    #Nodes
        Node(no=int(name), 
            coordinate_X=x_koord, 
            coordinate_Y=y_koord, 
            coordinate_Z=z_koord)

    #Lagerungen
    NodalSupport(1, '44', NodalSupportType.ROLLER_IN_X)
    NodalSupport(2, '39', NodalSupportType.HINGED)

    #Einwirkung
    NodalLoad(1, 3, f'{nodenames[0]}', NodalLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W,  magnitude=Laststufe)
    Model.clientModel.service.finish_modification()

    Calculate_all()

    deformationTab = ResultTables.NodesDeformations(loading_type=CaseObjectType.E_OBJECT_TYPE_LOAD_CASE, loading_no=3, object_no=47)
    deformation_z = deformationTab[0]['displacement_z']
    
    return deformation_z


if __name__=='__main__':
        
    Laststufen = np.linspace(1000,320*10**3,1)

    w_1_fachwerk = []
    for last in Laststufen:
        w_1_fachwerk.append(deformation_fachwerk(last))



    # Specify the file path
    file_path_tot = "deformation_results_FEM_tot.txt"
    file_path_schubbewehrung = "deformation_results_FEM_schubbewehrung.txt"
    file_path_druckstrebe = "deformation_results_FEM_druckstrebe.txt"
    file_path_druckgurt = "deformation_results_FEM_druckgurt.txt"
    file_path_zuggurt = "deformation_results_FEM_zuggurt.txt"


    # Open the file in write mode
    with open(file_path_druckstrebe, "w") as file:
        # Write each element of the list to a new line
        for item in w_1_fachwerk:
            file.write(str(item) + "\n")
                
