#!/usr/bin/env python3
"""
Helper script to check what was created and clean up if needed.
Run this in FreeCAD Python console to diagnose the current state.
"""

import FreeCAD
import Arch

def check_bim_model_status():
    """Check what objects were created and their status."""

    print("\n" + "=" * 70)
    print("BIM Model Status Check")
    print("=" * 70)

    # Check if document exists
    try:
        doc = FreeCAD.getDocument("House_Frame_BIM")
        print(f"\n✓ Document 'House_Frame_BIM' found")
    except:
        print(f"\n✗ Document 'House_Frame_BIM' not found")
        print("\nAvailable documents:")
        for doc in FreeCAD.listDocuments():
            print(f"  - {doc}")
        return

    # Count objects by type
    print(f"\n📊 Objects in document:")
    print(f"   Total objects: {len(doc.Objects)}")

    # Categorize objects
    structures = []
    floors = []
    buildings = []
    sites = []
    others = []

    for obj in doc.Objects:
        obj_type = obj.TypeId
        if "Structure" in obj_type:
            structures.append(obj)
        elif "Floor" in obj_type or "BuildingPart" in obj_type:
            floors.append(obj)
        elif "Building" in obj_type:
            buildings.append(obj)
        elif "Site" in obj_type:
            sites.append(obj)
        else:
            others.append(obj)

    print(f"   Structures (Arch::Structure): {len(structures)}")
    print(f"   Floors (Arch::Floor): {len(floors)}")
    print(f"   Buildings (Arch::Building): {len(buildings)}")
    print(f"   Sites (Arch::Site): {len(sites)}")
    if others:
        print(f"   Other objects: {len(others)}")

    # Show structures by IFC type
    if structures:
        print(f"\n🏗️  Structures by IFC Type:")
        ifc_types = {}
        for s in structures:
            ifc_type = getattr(s, 'IfcType', 'Unknown')
            if ifc_type not in ifc_types:
                ifc_types[ifc_type] = []
            ifc_types[ifc_type].append(s.Label)

        for ifc_type, labels in ifc_types.items():
            print(f"   {ifc_type}: {len(labels)} items")
            for label in labels[:5]:  # Show first 5
                print(f"      - {label}")
            if len(labels) > 5:
                print(f"      ... and {len(labels) - 5} more")

    # Show hierarchy
    if buildings or sites or floors:
        print(f"\n🏛️  BIM Hierarchy:")
        if sites:
            for site in sites:
                print(f"   Site: {site.Label}")
                if hasattr(site, 'Group'):
                    for building in site.Group:
                        print(f"      └─ Building: {building.Label}")
                        if hasattr(building, 'Group'):
                            for floor in building.Group:
                                print(f"         └─ Floor: {floor.Label}")
                                if hasattr(floor, 'Group'):
                                    print(f"            └─ Contains {len(floor.Group)} structures")
        elif buildings:
            for building in buildings:
                print(f"   Building: {building.Label}")
                if hasattr(building, 'Group'):
                    for floor in building.Group:
                        print(f"      └─ Floor: {floor.Label}")
                        if hasattr(floor, 'Group'):
                            print(f"         └─ Contains {len(floor.Group)} structures")
        elif floors:
            for floor in floors:
                print(f"   Floor: {floor.Label}")
                if hasattr(floor, 'Group'):
                    print(f"      └─ Contains {len(floor.Group)} structures")

    print(f"\n" + "=" * 70)

    # Determine if model is complete
    expected_structures = 39  # 3 footings + 11 columns/posts + 3 beams + 23 rafters (actually 40 as per error)

    if len(structures) >= expected_structures:
        print("✓ Model appears complete!")
        print(f"  All {len(structures)} structural elements created")
        if buildings:
            print("  ✓ Building hierarchy created")
        else:
            print("  ⚠ Building hierarchy incomplete (this is fixable)")

        print("\n💡 Next steps:")
        print("  1. Check if objects are visible in 3D view")
        print("  2. If not visible, try: View → View All (or press 'V' then 'F')")
        print("  3. Save the file: File → Save As → House_Frame_BIM.FCStd")
        if not buildings:
            print("  4. Re-run the fixed script to complete the building hierarchy")
    else:
        print(f"⚠ Model is incomplete")
        print(f"  Expected ~{expected_structures} structures, found {len(structures)}")
        print("\n💡 Next steps:")
        print("  1. Close this document: File → Close")
        print("  2. Run the fixed create_bim_model.py script")

    print("=" * 70 + "\n")

    return {
        'doc': doc,
        'structures': structures,
        'floors': floors,
        'buildings': buildings,
        'sites': sites,
        'others': others
    }

def cleanup_bim_document():
    """Clean up and close the BIM document for a fresh start."""

    print("\n" + "=" * 70)
    print("Cleaning up BIM document...")
    print("=" * 70)

    try:
        doc = FreeCAD.getDocument("House_Frame_BIM")
        print(f"\n✓ Found document 'House_Frame_BIM'")
        print(f"   Contains {len(doc.Objects)} objects")

        response = input("\nAre you sure you want to close and discard this document? (yes/no): ")

        if response.lower() in ['yes', 'y']:
            FreeCAD.closeDocument("House_Frame_BIM")
            print("✓ Document closed")
            print("\n💡 You can now run the fixed create_bim_model.py script")
        else:
            print("❌ Cleanup cancelled")

    except:
        print("\n✗ Document 'House_Frame_BIM' not found")
        print("   Nothing to clean up")

    print("=" * 70 + "\n")

def fix_existing_model():
    """Try to fix the existing model by completing the Building hierarchy."""

    print("\n" + "=" * 70)
    print("Attempting to fix existing model...")
    print("=" * 70)

    try:
        doc = FreeCAD.getDocument("House_Frame_BIM")
        print(f"\n✓ Found document 'House_Frame_BIM'")
    except:
        print(f"\n✗ Document 'House_Frame_BIM' not found")
        return

    # Find the Floor object
    floors = [obj for obj in doc.Objects if "Floor" in obj.TypeId or "BuildingPart" in obj.TypeId]

    if not floors:
        print("✗ No Floor object found - model may be too incomplete to fix")
        print("   Recommendation: Clean up and start fresh")
        return

    floor = floors[0]
    print(f"✓ Found Floor: {floor.Label}")

    # Check if Building already exists
    buildings = [obj for obj in doc.Objects if "Building" in obj.TypeId]

    if buildings:
        print(f"✓ Building already exists: {buildings[0].Label}")
        building = buildings[0]
    else:
        print("Creating Building...")
        building = Arch.makeBuilding([floor])
        building.Label = "Residential House"
        building.Description = "Single-story residential timber frame house"
        print(f"✓ Created Building: {building.Label}")

    # Check if Site already exists
    sites = [obj for obj in doc.Objects if "Site" in obj.TypeId]

    if sites:
        print(f"✓ Site already exists: {sites[0].Label}")
        site = sites[0]
    else:
        print("Creating Site...")
        site = Arch.makeSite([building])
        site.Label = "Construction Site"
        print(f"✓ Created Site: {site.Label}")

    # Recompute
    doc.recompute()

    print("\n✓ Model fixed!")
    print("\n💡 Next steps:")
    print("  1. Save the file: File → Save As → House_Frame_BIM.FCStd")
    print("  2. Export to IFC: File → Export → IFC")

    print("=" * 70 + "\n")

# Main menu
def main_menu():
    """Show main menu for BIM helper tools."""

    print("\n" + "=" * 70)
    print("BIM Helper Tools")
    print("=" * 70)
    print("\nAvailable commands:")
    print("  1. check_bim_model_status()  - Check what was created")
    print("  2. fix_existing_model()       - Try to fix the existing model")
    print("  3. cleanup_bim_document()     - Close and discard the document")
    print("\nExample usage:")
    print("  >>> check_bim_model_status()")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    # If run directly, show the menu
    main_menu()
else:
    # If imported, just print available functions
    print("\n✓ BIM Helper Tools loaded")
    print("  Available functions: check_bim_model_status(), fix_existing_model(), cleanup_bim_document()")
    print("  Type main_menu() for more info\n")
