from qgis.core import QgsProject
from PyQt5.QtWidgets import QInputDialog
import os
import processing

# Function to select a layer
def select_layer():
    # Get a list of all loaded layer names
    layer_names = [layer.name() for layer in QgsProject.instance().mapLayers().values()]
    
    # Open a dialog box to select a layer
    layer_name, ok = QInputDialog.getItem(None, "Select Layer", "Choose the input vector layer:", layer_names, 0, False)
    
    if ok:
        return layer_name
    else:
        return None

# Function to automate vector-to-raster batch processing
def automate_vector_to_raster():
    # Get the user-selected layer
    input_layer_name = select_layer()
    
    if not input_layer_name:
        print("No layer selected!")
        return

    # Get the selected input layer
    input_layer = QgsProject.instance().mapLayersByName(input_layer_name)[0]
    input_layer_path = input_layer.dataProvider().dataSourceUri().split('|')[0]  # Extract the file path of the input layer
    output_folder = os.path.dirname(input_layer_path)  # Get the folder where the input file is located
    
    # Define fields for rasterization
    fields = ["Hazard_ARR", "SPEED2D", "DEPTH2D"]
    
    # Common parameters
    resolution = 0.5

    # Create batch parameters
    batch_params = []
    for field in fields:
        output_file = os.path.join(output_folder, f"{field}_raster.tif")  # Save in the same folder as the input
        params = {
            'INPUT': input_layer_path,
            'FIELD': field,
            'BURN': 0,  # Default burn value
            'UNITS': 1,  # 1 = Georeferenced units
            'WIDTH': resolution,
            'HEIGHT': resolution,
            'EXTENT': None,  # Default (not set, uses input layer extent)
            'NODATA': 0,
            'OUTPUT': output_file  # Output file path
        }
        batch_params.append(params)

    # Run the batch process
    for param in batch_params:
        processing.runAndLoadResults("gdal:rasterize", param)

    print("Batch rasterization completed!")

# Run the function
automate_vector_to_raster()
