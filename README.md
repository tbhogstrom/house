# House Frame CAD Design

Professional FreeCAD models for residential house design and structural framing.

## 🏗️ BIM Workflow Available!

**NEW**: This project now includes a complete BIM (Building Information Modeling) workflow using FreeCAD's Arch workbench. The BIM approach creates industry-standard models with proper semantic objects, IFC export capability, and hierarchical organization.

**See [BIM_WORKFLOW_GUIDE.md](BIM_WORKFLOW_GUIDE.md) for the complete guide!**

### Why BIM?

Traditional 3D modeling creates basic geometric shapes. BIM modeling creates intelligent objects that:
- Know what they are (column, beam, footing)
- Can export to IFC (Industry Foundation Classes) format
- Work with professional BIM software (Revit, ArchiCAD, etc.)
- Enable structural, energy, and cost analysis
- Follow industry standards

## Files

### 🆕 House_Frame_BIM.FCStd (Coming Soon)
**BIM Model** - Professional BIM model created with Arch workbench workflow:

**BIM Features:**
- Uses `Arch::Structure` objects with proper IFC types
- Organized in `Site → Building → Floor` hierarchy
- IFC-compliant and ready for export
- Proper semantic meaning for all components
- Industry-standard BIM model

**To Create:**
Run `create_bim_model.py` in FreeCAD (see BIM Workflow Guide)

**Components:**
- Foundation: 3 concrete footings (IFC: Footing)
- Columns: 3 center columns + 8 posts (IFC: Column)
- Beams: 3 horizontal beams including ridge (IFC: Beam)
- Roof: 23 rafters at 30° pitch (IFC: Beam)
- Total: 39 structural elements in proper BIM hierarchy

### Professional_House_Frame.FCStd
**NEW** - Professional timber frame house structure with enhanced features:

**Features:**
- Complete structural framing system
- Foundation footings (3 units)
- Vertical columns and posts (11 units: 3 center columns, 8 perimeter posts)
- Horizontal beams (3 units: ridge beam and side beams)
- Roof rafter assembly (22 units: 12 left, 10 right)

**Professional Improvements:**
- **Metadata**: Added author, company, and detailed project description
- **Project Info**: Includes building type, category, building code (IBC 2021), and design load
- **Enhanced Labels**: Clear, descriptive names for all components (e.g., "Left Post 1", "Ridge Beam (Peak)")
- **Documentation**: Comprehensive comments describing the structure

### house.FCStd
Professional example house model created by Yorik van Havre (FreeCAD Arch workbench developer). This file demonstrates best practices for architectural modeling including:
- Complete architectural BIM model
- Walls, windows, and structural elements
- Proper use of Arch workbench objects
- Professional metadata and organization

### Step5_Final_BothSidesCorrect2.FCStd
Original frame structure file (retained for reference).

## Improvements Made

The `Professional_House_Frame.FCStd` file was created by enhancing the original frame with:

1. **Professional Metadata**
   - Author: Professional House Designer
   - Company: Professional Architecture Firm
   - Detailed project description

2. **Project Metadata**
   - Project: Residential House Frame
   - Type: Structural Frame
   - Category: Timber Construction
   - Building Code: IBC 2021
   - Design Load: Residential

3. **Enhanced Object Labels**
   - Renamed all components with clear, professional names
   - Foundation: "Footing 1", "Footing 2", "Footing 3"
   - Columns: "Center Column 1-3", "Left Post 1-4", "Right Post 1-4"
   - Beams: "Ridge Beam (Peak)", "Horizontal Beam (Left/Right)"
   - Rafters: "Left Rafter 1-11", "Right Rafter 0-10"

## Tools and Scripts

### 🆕 create_bim_model.py
**BIM Model Creation Script** - Generates a complete BIM model using Arch workbench workflow.

**Features:**
- Creates proper `Arch::Structure` objects with IFC types
- Organizes into `Site → Building → Floor` hierarchy
- Sets realistic timber dimensions
- Assigns proper IFC roles (Footing, Column, Beam)
- Adds professional BIM metadata
- Ready for IFC export

**Usage:**
```python
# In FreeCAD Python console:
exec(open('/home/user/house/create_bim_model.py').read())

# Or from command line (if FreeCAD CLI available):
freecadcmd create_bim_model.py
```

**Output:** `House_Frame_BIM.FCStd`

**See:** `BIM_WORKFLOW_GUIDE.md` for complete documentation

---

### improve_frame_xml.py
Python script to enhance existing FreeCAD files with professional metadata by directly modifying XML. Works without FreeCAD installation.

**Features:**
- Adds professional metadata
- Enhances object labels
- Adds project metadata
- Preserves all geometry and structure

**Usage:**
```bash
python3 improve_frame_xml.py
```

**Output:** `Professional_House_Frame.FCStd`

## Requirements

### For Viewing/Editing
- FreeCAD 0.19 or later

### For BIM Workflow
- FreeCAD 0.19+ with Arch workbench (included)
- IfcOpenShell (for IFC export): `pip install ifcopenshell`

### For Scripts
- Python 3.x (for XML-based scripts)
- FreeCAD Python API (for BIM creation script)

## Unit System

All files use the "Building US" unit system (ft-in, sqft, cft) appropriate for US residential construction.

## Structure

The professional frame includes:

**Foundation Layer**
- 3 concrete footings supporting the vertical structure
- Dimensions: 2ft × 2ft × 1ft each

**Vertical Structure**
- 3 center columns providing main support (6" × 6" × 10ft)
- 8 perimeter posts defining the building envelope (4" × 4" × 8ft)

**Horizontal Structure**
- Ridge beam at the roof peak (4" × 8" × 33ft)
- 2 horizontal beams supporting the posts (4" × 8" × 33ft each)

**Roof System**
- 23 rafters forming a gabled roof structure (2" × 6" × 10ft each)
- 30° roof pitch for proper drainage
- Symmetrical design for balanced load distribution

## Model Comparison

| Feature | Step5 (Original) | Professional | BIM Model |
|---------|------------------|--------------|-----------|
| **Object Type** | Part::Feature | Part::Feature | Arch::Structure |
| **Metadata** | None | Professional | Complete BIM |
| **Organization** | Flat list | Grouped | Site→Building→Floor |
| **IFC Export** | ❌ No | ❌ No | ✅ Yes |
| **Semantic Info** | ❌ No | ❌ No | ✅ Yes |
| **Industry Standard** | ❌ No | ❌ No | ✅ Yes |
| **Use Case** | Basic 3D | Enhanced 3D | Professional BIM |

## BIM Workflow Summary

The BIM workflow transforms basic 3D geometry into intelligent building components:

1. **Traditional Approach** (Step5_Final_BothSidesCorrect2.FCStd)
   - Created with Part workbench
   - Objects are just shapes
   - No semantic meaning

2. **Enhanced Approach** (Professional_House_Frame.FCStd)
   - Added metadata and better labels
   - Still just geometry
   - Better documentation

3. **BIM Approach** (House_Frame_BIM.FCStd)
   - Uses Arch workbench
   - Objects know what they are (Column, Beam, Footing)
   - IFC-compliant structure
   - Can export to industry-standard IFC format
   - Works with professional BIM software

**For complete BIM workflow documentation, see [BIM_WORKFLOW_GUIDE.md](BIM_WORKFLOW_GUIDE.md)**

## Next Steps

1. **View the models** in FreeCAD
2. **Run BIM script** to create the BIM model:
   ```python
   # In FreeCAD:
   exec(open('create_bim_model.py').read())
   ```
3. **Export to IFC** for interoperability:
   ```
   File → Export → Industry Foundation Classes (*.ifc)
   ```
4. **Create drawings** using Section Planes and Drawing workbench
5. **Share with others** using industry-standard IFC format

## Resources

- **FreeCAD Manual - BIM Modeling**: https://wiki.freecad.org/Manual:BIM_modeling
- **Arch Workbench**: https://wiki.freecad.org/Arch_Workbench
- **IFC Format**: https://technical.buildingsmart.org/standards/ifc/
- **IfcOpenShell**: http://ifcopenshell.org/
