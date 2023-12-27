import pandas as pd
import os
import sys
import numpy as np


def deformation_fachwerk(modelname, nodenumber_load, resultnumber, Laststufe=0):
    from RFEM.enums import NodalLoadDirection, CaseObjectType
    from RFEM.initModel import Model, Calculate_all
    from RFEM.Loads.nodalLoad import NodalLoad
    from RFEM.Results.resultTables import ResultTables

    # Setzt den pfad aktuell
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Modelinitiierung
    Model(False, modelname, delete=True)
    Model.clientModel.service.begin_modification()

    # Einwirkung
    for i,nodenumber in enumerate(nodenumber_load):
        NodalLoad(
            i+1,
            3,
            nodenumber,
            NodalLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W,
            magnitude=Laststufe,
        )

    Model.clientModel.service.finish_modification()

    try:
        Calculate_all()
        deformationTab = ResultTables.NodesDeformations(
            loading_type=CaseObjectType.E_OBJECT_TYPE_LOAD_CASE,
            loading_no=3,
            object_no=1,
        )
        deformation_z = deformationTab[resultnumber]["displacement_z"]

        print(
            f"Berechnung für Laststufe {Laststufe} beendet, Deformation entspricht {deformation_z}"
        )
        return deformation_z

    except Exception as e:
        print(f"Fehler bei der Berechnung: {e}. Versuche es erneut.")
        return deformation_fachwerk("Fachwerk_sv14_min", ["7", "3"], -2, Laststufe)


if __name__ == "__main__":
    Laststufen = np.linspace(1000, 105 * 10**3, 50)

    w_1_fachwerk = []
    for last in Laststufen:
        w_1_fachwerk.append(
            deformation_fachwerk("Fachwerk_sv14_min", ["7", "3"], -2, last)
        )

    # Specify the file path
    versuch = "SV14_"
    file_path_tot = "deformation_results_FEM_tot"
    file_path_tot_var_z = "deformation_results_FEM_tot_var_z"

    file_path_schubbewehrung = "deformation_results_FEM_schubbewehrung"
    file_path_druckstrebe = "deformation_results_FEM_druckstrebe"
    file_path_druckgurt = "deformation_results_FEM_druckgurt"
    file_path_zuggurt = "deformation_results_FEM_zuggurt"

    # Open the file in write mode
    with open(versuch+file_path_zuggurt +  ".txt", "w") as file:
        # Write each element of the list to a new line
        for item in w_1_fachwerk:
            file.write(str(item) + "\n")

    print(f"Gespeichert in {file_path_zuggurt+versuch}")
