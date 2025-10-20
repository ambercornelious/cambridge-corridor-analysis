# Cambridge Retail & Mixed-Use Corridor Analysis

## Project Objective

Comprehensive analysis of the commercial real estate landscape along Massachusetts Avenue between Central Square and Harvard Square in Cambridge, MA. This project identifies patterns in property values, assesses market health through vacancy analysis, and pinpoints prime investment opportunities.

## Project Scope

- **Study Area**: Massachusetts Avenue corridor (Central Square to Harvard Square)
- **Property Types**: Retail, mixed-use, and commercial properties
- **Analysis Period**: Current market conditions with historical context
- **Key Metrics**: Property values, vacancy rates, spatial patterns, investment opportunities

## Methodology & Tech Stack

- **Language**: Python
- **Key Libraries**: pandas, geopandas, matplotlib, seaborn, scikit-learn, folium
- **Data Sources**: 
  - Cambridge Public Property Assessment Database
  - Cambridge GIS Open Data Portal
  - Commercial listing platforms (LoopNet, Crexi)
- **Tools**: VS Code, Jupyter Notebooks, Git/GitHub

## Project Structure

```
cambridge_corridor_analysis/
├── README.md                 # Project overview and documentation
├── requirements.txt          # Python dependencies
├── data/
│   ├── raw/                 # Original, unprocessed data files
│   └── processed/           # Cleaned and processed datasets
├── notebooks/
│   ├── 01_data_acquisition.ipynb      # Data collection and initial loading
│   ├── 02_data_cleaning.ipynb        # Data preprocessing and cleaning
│   ├── 03_exploratory_analysis.ipynb # EDA and visualizations
│   ├── 04_spatial_analysis.ipynb     # GIS mapping and spatial patterns
│   └── 05_predictive_modeling.ipynb  # Property value modeling
├── scripts/
│   ├── data_acquisition.py   # Automated data collection scripts
│   ├── data_cleaning.py      # Data preprocessing utilities
│   └── visualization.py      # Reusable plotting functions
├── output/
│   ├── figures/             # Generated charts and maps
│   └── reports/             # Final analysis reports
└── docs/
    └── data_dictionary.md   # Documentation of data sources and variables
```

## Analysis Workflow

### Phase 1: Data Acquisition & Cleaning
- [ ] Download Cambridge property assessment data
- [ ] Acquire GIS parcel and zoning data
- [ ] Filter properties along Mass Ave corridor
- [ ] Clean and standardize datasets

### Phase 2: Exploratory Data Analysis
- [ ] Property value distribution analysis
- [ ] Building age and composition analysis
- [ ] Market composition by property type
- [ ] Spatial value patterns mapping

### Phase 3: Advanced Analytics
- [ ] Predictive modeling for property values
- [ ] Investment opportunity scoring
- [ ] Market trend analysis
- [ ] Comparative corridor analysis

### Phase 4: Deliverables
- [ ] Interactive property value maps
- [ ] Investment opportunity dashboard
- [ ] Executive summary report
- [ ] GitHub repository with full documentation

## Key Research Questions

1. **Value Patterns**: How do property values vary along the corridor?
2. **Market Health**: What are the current vacancy rates and market dynamics?
3. **Investment Opportunities**: Which properties show the highest potential for value-add investment?
4. **Spatial Clustering**: Where are the high-value retail nodes concentrated?
5. **Building Stock**: What percentage of buildings are candidates for adaptive reuse?

## Expected Outcomes

- Comprehensive property database for the corridor
- Interactive maps showing value gradients
- Statistical model predicting property values
- Ranked list of investment opportunities
- Professional-grade analysis demonstrating CRE analytical capabilities

## Getting Started

1. **Environment Setup**:
   ```bash
   cd cambridge_corridor_analysis
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Data Collection**:
   - Start with `notebooks/01_data_acquisition.ipynb`
   - Follow the sequential notebook workflow

3. **Analysis Execution**:
   - Run notebooks in order (01 → 02 → 03 → 04 → 05)
   - Each notebook builds on the previous results

## Data Sources

### Primary Sources
- **Cambridge Open Data Portal**: Property assessments, parcels, zoning
- **MassGIS**: State-level geographic data
- **U.S. Census**: Demographic and economic indicators

### Secondary Sources (Optional)
- **LoopNet/Crexi**: Current commercial listings
- **CoStar**: Market research and comparables (if available)

## Analysis Highlights

This project demonstrates:
- **Data Engineering**: ETL processes for municipal datasets
- **Spatial Analysis**: GIS techniques for real estate analysis  
- **Statistical Modeling**: Predictive analytics for property valuation
- **Data Visualization**: Professional mapping and charting
- **Business Intelligence**: Actionable insights for CRE investment

---

**Author**: Amber Cornelious  
**Created**: September 2025  
**Last Updated**: September 26, 2025