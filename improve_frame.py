#!/usr/bin/env python3
"""
FreeCAD script to improve house frame design with professional features.
This script adds proper metadata, organizes objects into groups, and enhances the model structure.
"""

import os
import sys

# Add FreeCAD lib path if needed
try:
    import FreeCAD
    import Arch
except ImportError:
    # Try common FreeCAD installation paths
    freecad_paths = [
        '/usr/lib/freecad/lib',
        '/usr/lib/freecad-python3/lib',
        '/usr/share/freecad/Mod',
    ]
    for path in freecad_paths:
        if os.path.exists(path):
            sys.path.append(path)
    import FreeCAD
    import Arch

def improve_frame_cad(input_file, output_file):
    """
    Improve the frame CAD file with professional features.

    Args:
        input_file: Path to the input FreeCAD file
        output_file: Path to save the improved file
    """
    print(f"Loading: {input_file}")

    # Open the document
    doc = FreeCAD.open(input_file)

    # Update document metadata with professional information
    print("Adding professional metadata...")
    doc.CreatedBy = "Professional House Designer"
    doc.LastModifiedBy = "Professional House Designer"
    doc.Company = "Professional Architecture Firm"
    doc.Comment = "Professional timber frame house structure with gabled roof system"
    doc.Label = "Professional_House_Frame"

    # Add metadata
    doc.Meta = {
        "Project": "Residential House Frame",
        "Type": "Structural Frame",
        "Category": "Timber Construction",
        "BuildingCode": "IBC 2021",
        "DesignLoad": "Residential",
    }

    print("Organizing objects into professional groups...")

    # Create organizational groups
    foundation_group = doc.addObject("App::DocumentObjectGroup", "Foundation")
    foundation_group.Label = "01_Foundation"

    columns_group = doc.addObject("App::DocumentObjectGroup", "Columns")
    columns_group.Label = "02_Columns_and_Posts"

    beams_group = doc.addObject("App::DocumentObjectGroup", "Beams")
    beams_group.Label = "03_Horizontal_Beams"

    roof_group = doc.addObject("App::DocumentObjectGroup", "Roof")
    roof_group.Label = "04_Roof_Rafters"

    # Master structure group
    structure_group = doc.addObject("App::DocumentObjectGroup", "Structure")
    structure_group.Label = "House_Frame_Structure"

    # Categorize and organize existing objects
    foundation_objects = []
    column_objects = []
    beam_objects = []
    rafter_objects = []

    for obj in doc.Objects:
        # Skip the groups themselves
        if obj.Name in ["Foundation", "Columns", "Beams", "Roof", "Structure"]:
            continue

        # Categorize by name
        if "Footing" in obj.Name:
            foundation_objects.append(obj)
            obj.Label = obj.Label.replace("Footing_", "Footing ")
        elif "Column" in obj.Name or "Post" in obj.Name:
            column_objects.append(obj)
            if "Column_Center" in obj.Name:
                obj.Label = obj.Label.replace("Column_Center_", "Center Column ")
            elif "Post_L_" in obj.Name:
                obj.Label = obj.Label.replace("Post_L_", "Left Post ")
            elif "Post_R_" in obj.Name:
                obj.Label = obj.Label.replace("Post_R_", "Right Post ")
        elif "Beam" in obj.Name:
            beam_objects.append(obj)
            if "RidgeBeam" in obj.Name:
                obj.Label = "Ridge Beam (Peak)"
            elif "HBeam_Left" in obj.Name:
                obj.Label = "Horizontal Beam (Left)"
            elif "HBeam_Right" in obj.Name:
                obj.Label = "Horizontal Beam (Right)"
        elif "Rafter" in obj.Name:
            rafter_objects.append(obj)
            if "Rafter_L_" in obj.Name:
                obj.Label = obj.Label.replace("Rafter_L_", "Left Rafter ")
            elif "Rafter_R_" in obj.Name:
                obj.Label = obj.Label.replace("Rafter_R_", "Right Rafter ")

    # Add objects to their respective groups
    if foundation_objects:
        foundation_group.addObjects(foundation_objects)
        print(f"  Added {len(foundation_objects)} foundation objects")

    if column_objects:
        columns_group.addObjects(column_objects)
        print(f"  Added {len(column_objects)} column/post objects")

    if beam_objects:
        beams_group.addObjects(beam_objects)
        print(f"  Added {len(beam_objects)} beam objects")

    if rafter_objects:
        roof_group.addObjects(rafter_objects)
        print(f"  Added {len(rafter_objects)} rafter objects")

    # Add subgroups to master structure group
    structure_group.addObject(foundation_group)
    structure_group.addObject(columns_group)
    structure_group.addObject(beams_group)
    structure_group.addObject(roof_group)

    print("Enhancing object properties...")

    # Add professional descriptions to groups
    foundation_group.Comment = "Foundation footings supporting the structural frame"
    columns_group.Comment = "Vertical structural columns and posts"
    beams_group.Comment = "Horizontal structural beams including ridge beam"
    roof_group.Comment = "Roof rafter system for gabled roof structure"
    structure_group.Comment = "Complete timber frame house structure"

    # Recompute the document
    print("Recomputing document...")
    doc.recompute()

    # Save the improved file
    print(f"Saving improved file: {output_file}")
    doc.saveAs(output_file)

    print("✓ Successfully improved the CAD file!")
    print(f"\nImprovements applied:")
    print("  • Added professional metadata (author, company, project info)")
    print("  • Organized into hierarchical groups:")
    print("    - 01_Foundation (footings)")
    print("    - 02_Columns_and_Posts (vertical supports)")
    print("    - 03_Horizontal_Beams (structural beams)")
    print("    - 04_Roof_Rafters (roof framing)")
    print("  • Enhanced object labels for clarity")
    print("  • Added descriptive comments to all groups")
    print("  • Renamed document to 'Professional_House_Frame'")

    return doc

if __name__ == "__main__":
    # Define file paths
    input_file = "/home/user/house/Step5_Final_BothSidesCorrect2.FCStd"
    output_file = "/home/user/house/Professional_House_Frame.FCStd"

    if not os.path.exists(input_file):
        print(f"Error: Input file not found: {input_file}")
        sys.exit(1)

    try:
        improve_frame_cad(input_file, output_file)
        print(f"\n✓ Output saved to: {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
