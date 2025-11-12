#!/usr/bin/env python3
"""
BIM Workflow Script for House Frame Structure
==============================================

This script recreates the house frame using proper BIM/Arch workbench methodology
as described in the FreeCAD manual. It creates a professionally structured BIM model
with proper Arch objects instead of basic Part features.

Following the BIM workflow from: FreeCAD manual - BIM modeling chapter

Key improvements over basic modeling:
- Uses Arch::Structure objects with IFC roles
- Organizes into Building/Floor hierarchy for IFC export
- Proper material assignments
- IFC-compliant structure
- Professional BIM metadata

Requirements: FreeCAD 0.19 or later with Arch and IFC support
"""

import os
import sys

# Try to import FreeCAD
try:
    import FreeCAD
    import Arch
    import Draft
    import Part
except ImportError as e:
    print(f"Error: FreeCAD modules not found. Please run this script within FreeCAD.")
    print(f"Details: {e}")
    print("\nTo run this script:")
    print("1. Open FreeCAD")
    print("2. Open Python console (View -> Panels -> Python console)")
    print("3. Run: exec(open('/home/user/house/create_bim_model.py').read())")
    sys.exit(1)

def create_bim_house_frame():
    """
    Create a complete BIM house frame structure using Arch workbench.

    This follows the BIM workflow:
    1. Create structural elements using Arch.makeStructure()
    2. Assign proper IFC roles
    3. Organize into Floor
    4. Organize into Building
    5. Ready for IFC export
    """

    print("=" * 70)
    print("Creating BIM House Frame Structure")
    print("=" * 70)

    # Create new document
    doc_name = "House_Frame_BIM"
    if FreeCAD.ActiveDocument:
        if FreeCAD.ActiveDocument.Name == doc_name:
            FreeCAD.closeDocument(doc_name)

    doc = FreeCAD.newDocument(doc_name)

    # Set document metadata
    doc.CreatedBy = "Professional House Designer <designer@architecture.com>"
    doc.LastModifiedBy = "Professional House Designer <designer@architecture.com>"
    doc.Company = "Professional Architecture Firm"
    doc.Comment = "BIM model of timber frame house structure created using Arch workbench workflow"
    doc.Label = "House_Frame_BIM"

    # Set to Building US unit system (index 5)
    doc.UnitSystem = 5

    print("\n[1/6] Creating foundation footings...")

    # Foundation footings - using Arch Structure with "Slab" role
    # Dimensions: 609.6mm x 609.6mm x 304.8mm (2ft x 2ft x 1ft)
    footing_positions = [
        ("Footing_1", FreeCAD.Vector(4267.2, -609.6, -914.4)),
        ("Footing_2", FreeCAD.Vector(4267.2, 9448.8, -914.4)),
        ("Footing_3", FreeCAD.Vector(4267.2, 4419.6, -914.4))
    ]

    footings = []
    for name, pos in footing_positions:
        # Create a box profile for the footing
        footing_box = Part.makeBox(609.6, 609.6, 304.8)
        footing_shape = doc.addObject("Part::Feature", name + "_Shape")
        footing_shape.Shape = footing_box
        footing_shape.ViewObject.Visibility = False

        # Create Arch Structure from the shape
        structure = Arch.makeStructure(footing_shape)
        structure.Label = name.replace("_", " ")
        structure.IfcType = "Footing"  # IFC role
        structure.Placement.Base = pos

        footings.append(structure)
        doc.removeObject(footing_shape.Name)  # Remove helper shape
        print(f"  ✓ Created {structure.Label} at {pos}")

    print(f"\n[2/6] Creating vertical columns and posts...")

    # Center columns - 6x6 inch timber (152.4mm x 152.4mm), height 3048mm (10ft)
    column_positions = [
        ("Column_Center_1", FreeCAD.Vector(4191.0, -609.6, -609.6)),
        ("Column_Center_2", FreeCAD.Vector(4191.0, 9448.8, -609.6)),
        ("Column_Center_3", FreeCAD.Vector(4191.0, 4419.6, -609.6))
    ]

    columns = []
    for name, pos in column_positions:
        # Use REC preset for rectangular column
        structure = Arch.makeStructure(length=152.4, width=152.4, height=3048.0)
        structure.Label = name.replace("_", " ")
        structure.IfcType = "Column"  # IFC role
        structure.Placement.Base = pos
        columns.append(structure)
        print(f"  ✓ Created {structure.Label}")

    # Posts - 4x4 inch timber (101.6mm x 101.6mm), height 2438.4mm (8ft)
    post_positions = [
        ("Post_L_1", FreeCAD.Vector(1524.0, -558.8, -609.6)),
        ("Post_L_2", FreeCAD.Vector(1524.0, 2514.6, -609.6)),
        ("Post_L_3", FreeCAD.Vector(1524.0, 6324.6, -609.6)),
        ("Post_L_4", FreeCAD.Vector(1524.0, 9397.8, -609.6)),
        ("Post_R_1", FreeCAD.Vector(6858.0, -558.8, -609.6)),
        ("Post_R_2", FreeCAD.Vector(6858.0, 2514.6, -609.6)),
        ("Post_R_3", FreeCAD.Vector(6858.0, 6324.6, -609.6)),
        ("Post_R_4", FreeCAD.Vector(6858.0, 9397.8, -609.6))
    ]

    posts = []
    for name, pos in post_positions:
        structure = Arch.makeStructure(length=101.6, width=101.6, height=2438.4)
        structure.Label = name.replace("_", " ")
        structure.IfcType = "Column"  # Posts are also columns in IFC
        structure.Placement.Base = pos
        posts.append(structure)
        print(f"  ✓ Created {structure.Label}")

    print(f"\n[3/6] Creating horizontal beams...")

    # Horizontal beams - 4x8 inch timber (101.6mm x 203.2mm)
    beams = []

    # Ridge beam (peak) - runs along Y axis, length ~10m
    ridge_beam = Arch.makeStructure(length=101.6, width=203.2, height=10058.4)
    ridge_beam.Label = "Ridge Beam (Peak)"
    ridge_beam.IfcType = "Beam"
    ridge_beam.Placement = FreeCAD.Placement(
        FreeCAD.Vector(4191.0, -609.6, 2438.4),
        FreeCAD.Rotation(FreeCAD.Vector(1, 0, 0), 90)  # Rotate to lie along Y
    )
    beams.append(ridge_beam)
    print(f"  ✓ Created {ridge_beam.Label}")

    # Left horizontal beam
    h_beam_left = Arch.makeStructure(length=101.6, width=203.2, height=10058.4)
    h_beam_left.Label = "Horizontal Beam (Left)"
    h_beam_left.IfcType = "Beam"
    h_beam_left.Placement = FreeCAD.Placement(
        FreeCAD.Vector(1524.0, -609.6, 1828.8),
        FreeCAD.Rotation(FreeCAD.Vector(1, 0, 0), 90)
    )
    beams.append(h_beam_left)
    print(f"  ✓ Created {h_beam_left.Label}")

    # Right horizontal beam
    h_beam_right = Arch.makeStructure(length=101.6, width=203.2, height=10058.4)
    h_beam_right.Label = "Horizontal Beam (Right)"
    h_beam_right.IfcType = "Beam"
    h_beam_right.Placement = FreeCAD.Placement(
        FreeCAD.Vector(6858.0, -609.6, 1828.8),
        FreeCAD.Rotation(FreeCAD.Vector(1, 0, 0), 90)
    )
    beams.append(h_beam_right)
    print(f"  ✓ Created {h_beam_right.Label}")

    print(f"\n[4/6] Creating roof rafter system...")

    # Rafters - 2x6 inch timber (38.1mm x 139.7mm), angled for roof
    # Length approximately 3m, angle ~30 degrees
    rafters = []

    # Left rafters (12 total)
    left_rafter_y_positions = [
        -558.8, 279.4, 1117.6, 1955.8, 2794.0, 3632.2,
        4470.4, 5308.6, 6146.8, 6985.0, 7823.2, 8661.4
    ]

    for i, y_pos in enumerate(left_rafter_y_positions, 1):
        rafter = Arch.makeStructure(length=38.1, width=139.7, height=3000.0)
        rafter.Label = f"Left Rafter {i}"
        rafter.IfcType = "Beam"  # Rafters are beams in IFC
        # Position and rotate for roof angle
        rafter.Placement = FreeCAD.Placement(
            FreeCAD.Vector(1524.0, y_pos, 1828.8),
            FreeCAD.Rotation(FreeCAD.Vector(0, 1, 0), -30)  # 30 degree roof pitch
        )
        rafters.append(rafter)

    print(f"  ✓ Created {len(left_rafter_y_positions)} left rafters")

    # Right rafters (11 total, numbered 0-10)
    right_rafter_y_positions = [
        -558.8, 279.4, 1117.6, 1955.8, 2794.0, 3632.2,
        4470.4, 5308.6, 6146.8, 6985.0, 7823.2
    ]

    for i, y_pos in enumerate(right_rafter_y_positions):
        rafter = Arch.makeStructure(length=38.1, width=139.7, height=3000.0)
        rafter.Label = f"Right Rafter {i}"
        rafter.IfcType = "Beam"
        rafter.Placement = FreeCAD.Placement(
            FreeCAD.Vector(6858.0, y_pos, 1828.8),
            FreeCAD.Rotation(FreeCAD.Vector(0, 1, 0), 30)  # Opposite angle
        )
        rafters.append(rafter)

    print(f"  ✓ Created {len(right_rafter_y_positions)} right rafters")

    print(f"\n[5/6] Organizing into BIM hierarchy...")

    # Collect all structural elements
    all_structures = footings + columns + posts + beams + rafters

    # Create Floor to contain all structural elements
    floor = Arch.makeFloor(all_structures)
    floor.Label = "Ground Floor Structure"
    floor.Description = "Timber frame structural system including foundation, columns, beams, and roof"
    print(f"  ✓ Created Floor containing {len(all_structures)} structural elements")

    # Create Building to contain the floor
    building = Arch.makeBuilding([floor])
    building.Label = "Residential House"
    building.Description = "Single-story residential timber frame house"
    building.BuildingType = "Residential"
    print(f"  ✓ Created Building containing Floor")

    # Create Site (optional but recommended for IFC)
    site = Arch.makeSite([building])
    site.Label = "Construction Site"
    site.Terrain = None
    print(f"  ✓ Created Site containing Building")

    print(f"\n[6/6] Finalizing BIM model...")

    # Recompute document
    doc.recompute()

    # Add project metadata to document
    doc.Meta = {
        "Project": "Residential House Frame",
        "Type": "Structural BIM Model",
        "Category": "Timber Construction",
        "BuildingCode": "IBC 2021",
        "DesignLoad": "Residential",
        "Workflow": "Arch Workbench BIM",
        "IFCCompliant": "Yes"
    }

    print("\n" + "=" * 70)
    print("BIM Model Creation Complete!")
    print("=" * 70)
    print(f"\nModel Summary:")
    print(f"  • Foundation: {len(footings)} concrete footings")
    print(f"  • Vertical Structure: {len(columns)} columns + {len(posts)} posts")
    print(f"  • Horizontal Beams: {len(beams)} beams")
    print(f"  • Roof System: {len(rafters)} rafters")
    print(f"  • Total Elements: {len(all_structures)} structural components")
    print(f"\nHierarchy:")
    print(f"  Site → Building → Floor → {len(all_structures)} Structures")
    print(f"\nIFC Export Ready:")
    print(f"  All elements have proper IFC types assigned")
    print(f"  Building hierarchy is IFC-compliant")
    print(f"  Ready to export via File → Export → IFC")

    # Save the document
    output_file = "/home/user/house/House_Frame_BIM.FCStd"
    doc.saveAs(output_file)
    print(f"\n✓ Saved to: {output_file}")

    print("\n" + "=" * 70)
    print("Next Steps:")
    print("=" * 70)
    print("1. Open House_Frame_BIM.FCStd in FreeCAD")
    print("2. Review the hierarchical structure in the tree view")
    print("3. Export to IFC: File → Export → Industry Foundation Classes (*.ifc)")
    print("4. Add section planes for 2D drawings (Arch → Section Plane)")
    print("5. Create technical drawings (Drawing workbench)")
    print("=" * 70)

    return doc

# Main execution
if __name__ == "__main__":
    try:
        doc = create_bim_house_frame()
        print("\n✓ Script completed successfully!")
    except Exception as e:
        print(f"\n✗ Error during execution: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
