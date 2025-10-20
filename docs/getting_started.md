# Getting Started with Cambridge Corridor Analysis

## Quick Start Guide

### 1. Environment Setup
```bash
cd cambridge_corridor_analysis
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Data Collection Checklist

#### Primary Data Sources:
- [ ] **Cambridge Property Assessments**
  - Visit: https://www.cambridgema.gov/Departments/assessing
  - Download: Latest property assessment database
  - Save as: `data/raw/cambridge_assessments_2025.csv`

- [ ] **Cambridge GIS Data**  
  - Visit: https://www.cambridgema.gov/GIS/gisdatadictionary
  - Download: Property parcels shapefile
  - Save as: `data/raw/cambridge_parcels/` (with all .shp, .shx, .dbf, .prj files)

- [ ] **Zoning Data**
  - Download: Zoning districts shapefile  
  - Save as: `data/raw/cambridge_zoning/`

#### Optional Data Sources:
- [ ] MassGIS regional data
- [ ] Census demographic data
- [ ] MBTA transportation data

### 3. Analysis Workflow

1. **Start with Notebook 01**: `notebooks/01_data_acquisition.ipynb`
2. **Follow the sequence**: Each notebook builds on the previous
3. **Review outputs**: Check `output/` folder for generated reports and maps

### 4. Project Structure Navigation

```
cambridge_corridor_analysis/
├── notebooks/           # Jupyter analysis notebooks
│   ├── 01_data_acquisition.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_analysis.ipynb
│   └── ... (more notebooks)
├── data/
│   ├── raw/               # Original downloaded data
│   └── processed/         # Cleaned analysis-ready data
├── output/             # Generated reports, maps, figures
├── scripts/            # Reusable Python modules
└── docs/               # Documentation
```

### 5. Key Features

- **Interactive Maps**: Folium-based property visualizations
- **Statistical Analysis**: Property value modeling and trends
- **Investment Scoring**: Automated opportunity identification
- **Professional Reports**: Export-ready analysis summaries

## Need Help?

### Data Sources Not Working?
- Check if URLs have changed on Cambridge's website
- Look for alternative download methods or API endpoints
- Use the sample data generation feature for development/testing

### Technical Issues?
- Ensure all requirements are installed: `pip install -r requirements.txt`
- Check Python version compatibility (3.8+)
- Verify file paths in notebooks match your system

### Analysis Questions?
- Review the data dictionary: `docs/data_dictionary.md`
- Check individual notebook documentation
- Examine sample outputs in the `output/` folder

---

**Ready to start?** Open `notebooks/01_data_acquisition.ipynb` in VS Code and begin your analysis!