# Vector-to-Raster-Batch-process
A Python script to automate the conversion of vector layers to raster layers in QGIS, designed to simplify batch processing with consistent settings for multiple fields

# QGIS Vector-to-Raster Automation Script

This repository contains a Python script to automate the process of converting vector layers to raster layers in QGIS. Designed for hydraulic engineers and GIS professionals, the script enables efficient batch processing for fields such as hazard, speed, and depth with consistent rasterization settings.

## Features
- Selects an input vector layer through a GUI dialog.
- Automatically configure rasterization settings for multiple fields.
- Save output rasters in the same directory as the input file.
- Supports batch processing of fields like `Hazard_ARR`, `SPEED2D`, and `DEPTH2D`.
- Loads generated raster files directly into the QGIS project.
- Relevant for hydraulic and flood engineers in australia. Hazard categories under ARR, depths and Velocities required to submit flood reports in Australia. Refer to styles upload seperately.

## Prerequisites
- QGIS 3.x with Python enabled.
- GDAL plugin activated in the QGIS Processing Toolbox.

## How to Use
1. Open QGIS and load your vector layers.
2. Open the Python Console (`Ctrl+Alt+P`) in QGIS.
3. Copy and paste the script from the `vector_to_raster.py` file into the Python Console, or load it as a `.py` file.
4. Follow the prompts:
   - Select the input vector layer.
   - The script will create rasters for the specified fields and save them in the same folder as the input layer.
5. View the generated raster layers automatically loaded into the QGIS project.
6. (Optional) Add custom style layers for Depths, velocities and Hazards. See attached documents for reference

## Output
- Raster files for `Hazard_ARR`, `SPEED2D`, and `DEPTH2D` fields.
- File names are generated based on the field names (e.g., `Hazard_ARR_raster.tif`).

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
