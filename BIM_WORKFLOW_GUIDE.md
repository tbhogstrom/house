# BIM Workflow Guide for House Frame Structure

This guide explains how to create a professional BIM (Building Information Modeling) model using FreeCAD's Arch workbench, following industry best practices.

## Table of Contents

1. [What is BIM?](#what-is-bim)
2. [Differences: Basic vs. BIM Modeling](#differences-basic-vs-bim-modeling)
3. [Using the BIM Workflow Script](#using-the-bim-workflow-script)
4. [Manual BIM Workflow Steps](#manual-bim-workflow-steps)
5. [IFC Export](#ifc-export)
6. [Creating Technical Drawings](#creating-technical-drawings)

---

## What is BIM?

BIM (Building Information Modeling) is how modern buildings and structures are designed and documented. Unlike basic 3D modeling, BIM models include:

- **Semantic Information**: Objects know what they are (wall, column, beam, etc.)
- **Material Properties**: Structural materials, fire ratings, etc.
- **Relationships**: How objects connect and depend on each other
- **IFC Compliance**: Industry standard format for exchanging building data
- **Hierarchical Organization**: Site → Building → Floor → Components

### Benefits of BIM

- **Interoperability**: Export to IFC for use in any BIM software
- **Analysis**: Structural, energy, cost calculations
- **Coordination**: Clash detection, construction sequencing
- **Documentation**: Automatic generation of plans, sections, schedules
- **Lifecycle Management**: Construction through maintenance

---

## Differences: Basic vs. BIM Modeling

### Basic Modeling (What We Had Before)

```
Step5_Final_BothSidesCorrect2.FCStd
├── Part::Feature - Footing_1
├── Part::Feature - Footing_2
├── Part::Feature - Column_Center_1
└── ...39 basic geometric shapes
```

**Characteristics:**
- Objects are just geometry (boxes, cylinders)
- No semantic meaning (computer doesn't know what they are)
- No IFC export capability
- No proper organization
- Not industry-standard

### BIM Modeling (What We're Creating Now)

```
House_Frame_BIM.FCStd
├── Arch::Site
    └── Arch::Building "Residential House"
        └── Arch::Floor "Ground Floor Structure"
            ├── Arch::Structure (IFC: Footing) - Footing 1
            ├── Arch::Structure (IFC: Footing) - Footing 2
            ├── Arch::Structure (IFC: Column) - Center Column 1
            ├── Arch::Structure (IFC: Beam) - Ridge Beam (Peak)
            └── ...39 properly typed structural elements
```

**Characteristics:**
- Objects have semantic meaning (Column, Beam, Footing)
- IFC roles assigned for interoperability
- Hierarchical organization (Site → Building → Floor)
- IFC export ready
- Industry-standard BIM model
- Professional metadata and documentation

---

## Using the BIM Workflow Script

### Prerequisites

1. **FreeCAD 0.19 or later** installed
2. **Arch workbench** (included with FreeCAD)
3. **IfcOpenShell** (for IFC export)
   - Check: Help → About FreeCAD → Copy to clipboard → Look for IfcOpenShell

### Running the Script

**Method 1: From FreeCAD Python Console**

1. Open FreeCAD
2. Open Python console: `View → Panels → Python console`
3. Run the script:
   ```python
   exec(open('/home/user/house/create_bim_model.py').read())
   ```

**Method 2: From FreeCAD Macro**

1. Open FreeCAD
2. `Macro → Macros...`
3. Browse to `create_bim_model.py`
4. Click `Execute`

**Method 3: From Command Line (Linux/Mac)**

```bash
freecad -c create_bim_model.py
# or
freecadcmd create_bim_model.py
```

### What the Script Creates

The script automatically creates:

1. **Foundation** (3 footings)
   - Concrete footings: 2ft × 2ft × 1ft
   - IFC Type: Footing

2. **Vertical Structure** (11 elements)
   - 3 center columns: 6" × 6" × 10ft
   - 8 perimeter posts: 4" × 4" × 8ft
   - IFC Type: Column

3. **Horizontal Beams** (3 elements)
   - Ridge beam (peak): 4" × 8" × 33ft
   - 2 horizontal beams: 4" × 8" × 33ft
   - IFC Type: Beam

4. **Roof System** (23 rafters)
   - 12 left rafters: 2" × 6" × 10ft (30° pitch)
   - 11 right rafters: 2" × 6" × 10ft (30° pitch)
   - IFC Type: Beam

5. **BIM Hierarchy**
   - Site → Building → Floor → Components
   - All properly organized for IFC export

---

## Manual BIM Workflow Steps

If you want to create the model manually (educational purposes), follow these steps:

### Step 1: Setup

1. Create new document: `File → New`
2. Switch to Arch workbench: Workbench dropdown → Arch
3. Set unit system: `Edit → Preferences → General → Units → Building US (ft-in)`
4. Set grid: `Edit → Preferences → Draft → Grid → Grid spacing: 1000mm`

### Step 2: Create Foundation

For each footing:

1. Create a box: `Part → Cube`
2. Set dimensions: 609.6mm × 609.6mm × 304.8mm
3. Select the box
4. `Arch → Structure`
5. In Properties panel:
   - `IFC Type: Footing`
   - Set position in Placement property

### Step 3: Create Columns

For each column/post:

1. `Arch → Structure`
2. In Structure tool:
   - Set `Length: 152.4` (for 6" columns) or `101.6` (for 4" posts)
   - Set `Width: 152.4` or `101.6`
   - Set `Height: 3048` (for columns) or `2438.4` (for posts)
3. Set `IFC Type: Column`
4. Position using Placement property

### Step 4: Create Beams

For each beam:

1. `Arch → Structure`
2. Set dimensions: 101.6mm × 203.2mm × length
3. Set `IFC Type: Beam`
4. Rotate and position as needed

### Step 5: Create Rafters

For each rafter:

1. `Arch → Structure`
2. Set dimensions: 38.1mm × 139.7mm × 3000mm
3. Set `IFC Type: Beam`
4. Rotate for roof pitch (~30°)
5. Position along roof line

### Step 6: Organize Hierarchy

1. Select all structural elements
2. `Arch → Floor`
3. Label: "Ground Floor Structure"
4. Select floor
5. `Arch → Building`
6. Label: "Residential House"
7. Select building
8. `Arch → Site` (optional)

### Step 7: Set Metadata

In document properties:
- `CreatedBy`: Your name
- `Company`: Your company
- `Comment`: Project description
- `Meta`: Project details

---

## IFC Export

### Prerequisites

Install IfcOpenShell:
```bash
pip install ifcopenshell
```

### Export Process

1. Select the Building object (or Site if created)
2. `File → Export...`
3. File type: `Industry Foundation Classes (*.ifc)`
4. Enter filename: `House_Frame.ifc`
5. Click `Save`

### Verify IFC File

Open the IFC file in:
- **FreeCAD**: `File → Import → IFC`
- **IfcPlusPlus Viewer**: http://ifcplusplus.com/
- **BIM Vision**: Free IFC viewer
- **Solibri**: Professional BIM software

### IFC Export Settings

`Edit → Preferences → Import-Export → IFC`

Important settings:
- ☑ Export full parametric model
- ☑ Reuse existing entities
- ☐ Skip invisible objects
- Schema: IFC4 (recommended) or IFC2X3

---

## Creating Technical Drawings

### Step 1: Create Section Planes

1. Switch to Arch workbench
2. Select Building
3. `Arch → Section Plane`
4. Position for plan view:
   - Rotation: 0° (looking down)
   - Height: Through building mid-height
5. Create another section plane for elevation:
   - Rotation: 90° (looking from side)

### Step 2: Create Drawing Page

1. Switch to Drawing workbench
2. `Drawing → Insert new drawing`
3. Select template (A3_Landscape recommended)

### Step 3: Add Views

For each section plane:

1. Select section plane
2. `Drawing → Insert Draft workbench object`
3. Properties:
   - `X, Y`: Position on sheet
   - `Scale`: 0.02 - 0.05 (depending on sheet size)
   - `Show Cut`: True
   - `Show Fill`: True

### Step 4: Add Dimensions

1. Switch to Draft workbench
2. Set working plane to match section
3. Create dimensions: `Draft → Dimension`
4. Add to Drawing:
   - Select dimensions
   - `Drawing → Insert Draft workbench object`

### Step 5: Export Drawing

1. Select Page in tree
2. `File → Export`
3. Choose format:
   - **SVG**: For editing in Inkscape
   - **DXF**: For CAD software
   - **PDF**: For printing

---

## Comparison: Files in This Project

| File | Type | Description |
|------|------|-------------|
| `Step5_Final_BothSidesCorrect2.FCStd` | Basic 3D | Original frame with Part::Feature objects |
| `Professional_House_Frame.FCStd` | Enhanced 3D | Improved metadata, still basic objects |
| `House_Frame_BIM.FCStd` | **BIM Model** | **Full BIM with Arch objects & IFC** |

### When to Use Each Approach

**Basic 3D Modeling**: Quick visualization, concept studies

**Enhanced 3D**: Better organization, clear documentation

**BIM Modeling**: Professional projects, IFC exchange, industry collaboration

---

## Key Arch Workbench Objects

### Arch::Structure
- **Purpose**: Structural elements (columns, beams, slabs, footings)
- **IFC Types**: Column, Beam, Slab, Footing, Brace
- **Properties**: Material, profile, length, IFC role

### Arch::Wall
- **Purpose**: Walls (exterior, interior, retaining)
- **Created from**: Lines, polylines
- **Features**: Openings (windows, doors), layers, alignment

### Arch::Floor
- **Purpose**: Group objects by floor level
- **Contains**: Structures, walls, windows, doors
- **Properties**: Height, elevation

### Arch::Building
- **Purpose**: Top-level container for building
- **Contains**: Floors
- **Properties**: Building type, address

### Arch::Site
- **Purpose**: Overall project container
- **Contains**: Buildings
- **Properties**: Location, terrain, civil data

### Arch::Window / Door
- **Purpose**: Openings in walls
- **Created from**: Sketches
- **Properties**: Frame, sill, panels

---

## Best Practices

### 1. Always Use Proper Object Types
❌ Don't: Create a column as `Part → Box`
✓ Do: Create a column as `Arch → Structure` with IFC Type: Column

### 2. Organize Hierarchically
```
Site
  └── Building
      └── Floor(s)
          └── Components
```

### 3. Set IFC Types
Every Arch object should have an IFC Type:
- Footings: "Footing"
- Columns/Posts: "Column"
- Beams/Rafters: "Beam"
- Slabs: "Slab"

### 4. Use Real Dimensions
Use actual lumber sizes:
- 2x4: 38.1mm × 88.9mm (actual milled size)
- 2x6: 38.1mm × 139.7mm
- 4x4: 88.9mm × 88.9mm
- 6x6: 139.7mm × 139.7mm

### 5. Document Thoroughly
- Add descriptive labels
- Set document metadata
- Add comments to complex objects

### 6. Test IFC Export Early
Export and re-import to verify:
- All objects export correctly
- Hierarchy is maintained
- IFC types are correct

---

## Troubleshooting

### IFC Export Fails

**Problem**: "IfcOpenShell not found"

**Solution**:
```bash
pip install ifcopenshell
```
Restart FreeCAD after installation.

### Objects Don't Appear in IFC

**Problem**: Objects missing after export/import

**Solution**:
- Ensure objects are inside Building
- Check IFC Type is set
- Recompute document before export

### Hierarchy Looks Wrong

**Problem**: Objects not nested properly

**Solution**:
1. Select all components
2. `Arch → Floor` to create floor
3. Select floor
4. `Arch → Building` to create building

### Script Fails with Import Error

**Problem**: "No module named 'Arch'"

**Solution**:
Run script from within FreeCAD, not from system Python:
```python
# In FreeCAD Python console:
exec(open('create_bim_model.py').read())
```

---

## Additional Resources

### FreeCAD Documentation
- Arch Workbench: https://wiki.freecad.org/Arch_Workbench
- BIM Workbench: https://wiki.freecad.org/BIM_Workbench
- IFC: https://wiki.freecad.org/Arch_IFC

### IFC Resources
- IFC Specification: https://technical.buildingsmart.org/standards/ifc/
- IfcOpenShell: http://ifcopenshell.org/
- BuildingSMART: https://www.buildingsmart.org/

### BIM Software (IFC Compatible)
- **FreeCAD**: Open source BIM
- **BlenderBIM**: Open source BIM in Blender
- **Revit**: Commercial BIM (Autodesk)
- **ArchiCAD**: Commercial BIM (Graphisoft)
- **Tekla**: Structural BIM

### Learning Resources
- FreeCAD Manual BIM Chapter: https://wiki.freecad.org/Manual:BIM_modeling
- FreeCAD YouTube Channel: Official tutorials
- OSArch Community: https://osarch.org/

---

## Conclusion

BIM modeling represents the industry standard for professional architectural and structural design. By following this workflow, you create models that:

- **Interoperate** with professional BIM software via IFC
- **Contain semantic information** beyond just geometry
- **Follow industry standards** for organization and metadata
- **Enable advanced analyses** (structural, energy, cost)
- **Generate documentation** automatically (plans, sections, schedules)

The `create_bim_model.py` script automates this professional workflow, creating a fully compliant BIM model ready for IFC export and professional use.

---

## License

This guide and associated scripts are provided for educational purposes. The BIM workflow described follows FreeCAD documentation and industry best practices.
