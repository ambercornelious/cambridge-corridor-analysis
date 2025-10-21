"""
Cambridge Corridor Analysis - Data Acquisition Module

This module contains utility functions for acquiring and processing
Cambridge property assessment and GIS data for corridor analysis.

Author: Amber Cornelious
Created: September 2025
"""

import pandas as pd
import requests
import os
from pathlib import Path


def download_cambridge_assessments(year=2025, output_dir="data/raw"):
    """
    Download Cambridge property assessment data
    
    Args:
        year (int): Assessment year to download
        output_dir (str): Directory to save downloaded files
    
    Returns:
        str: Path to downloaded file
    """
    # This is a template function - actual implementation would depend on
    # Cambridge's current data portal APIs and download methods
    
    print(f"Downloading Cambridge Assessment Data for {year}")
    
    # Example URL structure (would need to be updated with actual endpoints)
    base_url = "https://www.cambridgema.gov/api/assessments"
    
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # In practice, this might involve:
    # 1. Making API requests to Cambridge's data portal
    # 2. Downloading Excel/CSV files from their website
    # 3. Processing multiple files and combining them
    
    print(f"Manual download required from:")
    print(f"   Cambridge Assessing: https://www.cambridgema.gov/Departments/assessing")
    print(f"   Save as: {output_path}/cambridge_assessments_{year}.csv")
    
    return output_path / f"cambridge_assessments_{year}.csv"


def download_cambridge_gis_data(output_dir="data/raw"):
    """
    Download Cambridge GIS data (parcels, zoning, etc.)
    
    Args:
        output_dir (str): Directory to save downloaded files
        
    Returns:
        dict: Paths to downloaded GIS files
    """
    print("Downloading Cambridge GIS Data")
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    gis_files = {
        'parcels': output_path / 'cambridge_parcels.shp',
        'zoning': output_path / 'cambridge_zoning.shp',
        'buildings': output_path / 'cambridge_buildings.shp'
    }
    
    print(f"Manual download required from:")
    print(f"   Cambridge GIS Portal: https://www.cambridgema.gov/GIS/gisdatadictionary")
    
    for data_type, filepath in gis_files.items():
        print(f"   {data_type.title()}: {filepath}")
    
    return gis_files


def validate_data_files(data_dir="data/raw"):
    """
    Validate that required data files are present
    
    Args:
        data_dir (str): Directory containing data files
        
    Returns:
        dict: Validation results
    """
    data_path = Path(data_dir)
    
    required_files = [
        'cambridge_assessments_2025.csv',
        'cambridge_parcels.shp',
        'cambridge_zoning.shp'
    ]
    
    validation_results = {}
    
    print("Validating Data Files")
    print("-" * 30)
    
    for filename in required_files:
        filepath = data_path / filename
        exists = filepath.exists()
        validation_results[filename] = exists
        
        status = "Yes" if exists else "No"
        print(f"{status} {filename}")
    
    all_present = all(validation_results.values())
    print(f"\nValidation Summary: {sum(validation_results.values())}/{len(required_files)} files present")
    
    return {
        'all_files_present': all_present,
        'file_status': validation_results,
        'missing_files': [f for f, exists in validation_results.items() if not exists]
    }


def create_corridor_bounds():
    """
    Define the geographical bounds for the Mass Ave corridor analysis
    
    Returns:
        dict: Corridor boundary coordinates and landmarks
    """
    return {
        'study_area': {
            'north': 42.3800,
            'south': 42.3600,
            'east': -71.0950,
            'west': -71.1250
        },
        'landmarks': {
            'Central Square': (42.3647, -71.1032),
            'Inman Square': (42.3731, -71.0995),
            'Porter Square': (42.3884, -71.1190),
            'Harvard Square': (42.3736, -71.1190)
        },
        'mass_ave_coords': {
            'start': (42.3647, -71.1032),  # Central Square
            'end': (42.3736, -71.1190)     # Harvard Square
        }
    }


if __name__ == "__main__":
    # Run data acquisition workflow
    print("Cambridge Corridor Analysis - Data Acquisition")
    print("=" * 60)
    
    # Download data files
    assessment_file = download_cambridge_assessments()
    gis_files = download_cambridge_gis_data()
    
    # Validate files
    validation = validate_data_files()
    
    if not validation['all_files_present']:
        print(f"\nMissing files: {validation['missing_files']}")
        print("Please download the required files before proceeding with analysis.")
    else:
        print("\nAll required files are present - ready for analysis!")
