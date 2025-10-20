# Investment Analysis Output

## Files in this directory:

- **investment_financial_analysis.csv** - Detailed financial metrics for all properties
- **investment_recommendations_report.txt** - Executive summary of investment opportunities
- **portfolio_analysis.png** - Visual analysis of investment portfolio
- **portfolio_summary.csv** - Summary statistics
- **risk_assessment_analysis.png** - Risk visualization
- **top_investment_opportunities_detailed.csv** - Top-ranked investment properties
- **dashboard_summary.json** - Dashboard configuration

## Large Interactive Dashboard

The `investment_opportunity_dashboard.html` file (106MB) is not included in this repository due to GitHub's file size limits.

### To regenerate the interactive dashboard:

1. Run the Jupyter notebook: `notebooks/05_investment_opportunity_analysis.ipynb`
2. The notebook will create the full interactive Folium dashboard with all properties mapped
3. The resulting HTML file will be saved to this directory

### Dashboard Features:
- Interactive map with all 29,876+ Cambridge properties
- Color-coded investment scoring
- Property details on click
- Neighborhood clustering analysis
- Red Line proximity analysis

**Note:** The dashboard contains the complete Cambridge assessment dataset and is best viewed locally due to its size.