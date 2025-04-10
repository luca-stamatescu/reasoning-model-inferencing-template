import pandas as pd
import os
import json

def get_bankruptcy_data(years=None):
    """
    Retrieve bankruptcy data for specified years or all years if none specified.
    
    Args:
        years (list, optional): List of years to filter the data. If None or empty, returns all years.
        
    Returns:
        dict: Dictionary containing the bankruptcy data
    """
    try:
        # Path to the CSV file
        csv_path = os.path.join(os.path.dirname(__file__), "sample_data.csv")
        
        # Check if file exists
        if not os.path.exists(csv_path):
            return {"error": f"Data file not found at {csv_path}"}
        
        # Read the CSV file
        df = pd.read_csv(csv_path)
        
        # Convert Year column to string to ensure it works as keys in JSON
        df['Year'] = df['Year'].astype(str)
        
        # Filter by years if specified
        if years:
            years = [str(year) for year in years]  # Convert all years to strings
            df = df[df['Year'].isin(years)]
        
        # Convert to dictionary format
        # Format: {year1: status, year2: status, ...}
        result = dict(zip(df['Year'], df['Bankruptcy Status']))
        
        # Add metadata
        metadata = {
            "total_records": len(result),
            "source": "sample_data.csv",
            "years_covered": sorted(list(result.keys()))
        }
        
        return {
            "metadata": metadata,
            "data": result
        }
        
    except Exception as e:
        return {"error": f"Error retrieving bankruptcy data: {str(e)}"}

def execute_tool_function(function_name, function_args):
    """
    Execute a tool function based on its name and arguments.
    
    Args:
        function_name (str): The name of the function to execute
        function_args (dict): The arguments to pass to the function
        
    Returns:
        object: The result of the function execution
    """
    if function_name == "get_bankruptcy_data":
        print(f"Executing get_bankruptcy_data with years: {function_args.get('years')}. If no year specified, all years will be returned.")
        return get_bankruptcy_data(function_args.get("years"))
    
    return {"error": f"Unknown function: {function_name}"} 