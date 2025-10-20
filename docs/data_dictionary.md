# Cambridge Corridor Analysis - Data Dictionary

## Overview
This document describes the data sources, variables, and data structures used in the Cambridge Retail & Mixed-Use Corridor Analysis project.

## Primary Datasets

### 1. Property Assessment Data
**Source**: City of Cambridge Assessing Department  
**URL**: https://www.cambridgema.gov/Departments/assessing  
**Format**: CSV/Excel  
**Update Frequency**: Annual (typically released in January)

#### Key Variables:
- `PARCEL_ID`: Unique identifier for each property parcel
- `PROPERTY_ADDRESS`: Street address of the property
- `PROPERTY_TYPE`: Classification code (Commercial, Residential, Mixed-Use, etc.)
- `LAND_VALUE`: Assessed value of land only
- `BUILDING_VALUE`: Assessed value of improvements/buildings
- `TOTAL_VALUE`: Combined assessed value (land + building)
- `SQUARE_FOOTAGE`: Gross building square footage
- `LOT_SIZE`: Property lot size in square feet
- `YEAR_BUILT`: Year of original construction
- `YEAR_RENOVATED`: Most recent major renovation year
- `ZONING_DISTRICT`: Current zoning classification
- `OWNER_NAME`: Property owner name
- `OWNER_ADDRESS`: Owner's mailing address

### 2. GIS Parcel Data
**Source**: Cambridge GIS Open Data Portal  
**URL**: https://www.cambridgema.gov/GIS/gisdatadictionary  
**Format**: Shapefile (.shp)  
**Coordinate System**: Massachusetts State Plane (NAD83)

#### Geometric Data:
- `PARCEL_GEOM`: Polygon geometry for property boundaries
- `CENTROID_X`: X-coordinate of parcel centroid
- `CENTROID_Y`: Y-coordinate of parcel centroid
- `AREA_SQFT`: Calculated parcel area in square feet

### 3. Zoning District Data
**Source**: Cambridge Community Development Department  
**Format**: Shapefile (.shp) with attribute table

#### Zoning Classifications:
- `ZONE_ID`: Zoning district identifier
- `ZONE_NAME`: Full zoning district name
- `ZONE_TYPE`: General category (Residential, Commercial, Mixed-Use, etc.)
- `FAR_MAX`: Maximum Floor Area Ratio allowed
- `HEIGHT_MAX`: Maximum building height (feet)
- `DENSITY_MAX`: Maximum residential density (units/acre)

### 4. Commercial Listings (Optional)
**Source**: Web scraping from LoopNet, Crexi  
**Format**: CSV (scraped data)  
**Update Frequency**: Weekly scraping runs

#### Listing Variables:
- `LISTING_ID`: Platform-specific listing identifier
- `PROPERTY_ADDRESS`: Address matching assessment data
- `LISTING_TYPE`: For Sale vs For Lease
- `ASKING_PRICE`: Listed sale price or annual rent
- `PRICE_PER_SF`: Price per square foot (calculated)
- `VACANCY_STATUS`: Current occupancy status
- `LISTING_DATE`: Date property was listed
- `DAYS_ON_MARKET`: Time since initial listing

## Derived Variables

### Market Analysis Metrics
- `VALUE_PER_SF`: Total assessed value divided by square footage
- `LAND_TO_TOTAL_RATIO`: Land value as percentage of total value
- `BUILDING_AGE`: Current year minus year built
- `RENOVATION_AGE`: Years since last renovation
- `DISTANCE_TO_T`: Distance to nearest MBTA station (meters)
- `CORRIDOR_SEGMENT`: Classification of location along Mass Ave

### Investment Indicators
- `INVESTMENT_SCORE`: Composite score based on multiple factors
- `VALUE_GROWTH_POTENTIAL`: Predicted appreciation potential
- `ADAPTIVE_REUSE_CANDIDATE`: Boolean flag for renovation opportunity
- `MARKET_COMPARABLES`: Properties with similar characteristics

## Data Quality Notes

### Known Issues:
1. **Missing Years Built**: ~5% of properties lack construction year
2. **Inconsistent Property Types**: Some mixed-use properties misclassified
3. **Address Standardization**: Minor variations in street address formats
4. **Vacancy Data**: Limited historical vacancy information

### Data Cleaning Steps:
1. Address standardization for joining datasets
2. Property type reclassification based on zoning and use
3. Outlier detection and handling for assessed values
4. Missing value imputation for building characteristics

## Geographic Scope

### Study Area Boundaries:
- **Primary Corridor**: Massachusetts Avenue from Central Square to Harvard Square
- **Buffer Zone**: Properties within 0.25 miles of Mass Ave
- **Comparison Areas**: Similar corridors in Cambridge for benchmarking

### Coordinate Systems:
- **Source Data**: Massachusetts State Plane (EPSG:2249)
- **Analysis CRS**: UTM Zone 19N (EPSG:26919) for distance calculations
- **Visualization**: WGS84 (EPSG:4326) for web mapping

## File Naming Conventions

### Raw Data:
- `cambridge_assessments_2025.csv`
- `cambridge_parcels.shp` (with associated .shx, .dbf, .prj files)
- `cambridge_zoning.shp`
- `commercial_listings_YYYYMMDD.csv`

### Processed Data:
- `corridor_properties_clean.csv`
- `spatial_analysis_results.geojson`
- `market_metrics_by_segment.csv`
- `investment_opportunities_ranked.csv`

## Update Schedule

| Dataset | Update Frequency | Last Updated | Next Update |
|---------|------------------|--------------|-------------|
| Property Assessments | Annual | Jan 2025 | Jan 2026 |
| GIS Parcels | Quarterly | Q3 2025 | Q4 2025 |
| Zoning Data | As Amended | Sep 2025 | TBD |
| Commercial Listings | Weekly | Current | Ongoing |

---

**Maintained By**: Amber Cornelious  
**Last Updated**: September 26, 2025  
**Version**: 1.0