# House Frame CAD Design

Professional FreeCAD models for residential house design and structural framing.

## Files

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

## Tools

### improve_frame_xml.py
Python script to enhance FreeCAD files with professional features by directly modifying the XML structure. Works without FreeCAD installation.

**Features:**
- Adds professional metadata
- Enhances object labels
- Adds project metadata
- Preserves all geometry and structure

**Usage:**
```bash
python3 improve_frame_xml.py
```

## Requirements

- FreeCAD 0.19 or later (for viewing/editing)
- Python 3.x (for running improvement scripts)

## Unit System

All files use the "Building US" unit system (ft-in, sqft, cft) appropriate for US residential construction.

## Structure

The professional frame includes:

**Foundation Layer**
- 3 concrete footings supporting the vertical structure

**Vertical Structure**
- 3 center columns providing main support
- 8 perimeter posts (4 left, 4 right) defining the building envelope

**Horizontal Structure**
- Ridge beam at the roof peak
- 2 horizontal beams supporting the posts

**Roof System**
- 22 rafters forming a gabled roof structure
- Symmetrical design for balanced load distribution
