import numpy as np
import pandas as pd

def calculate_ram_metrics_from_csv(file_path):
    """
    Calculate RAM metrics from a CSV file.
    The CSV file should have columns: Component, Failure Rate, Repair Time.
    """
    try:
        components_df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return None
    return calculate_ram_metrics(components_df)

def calculate_ram_metrics_from_input():
    """
    Calculate RAM metrics based on user input.
    """
    components_data = []    
    # num_components = int(Element("#numcomp").value)
    # print(num_components)    
    component_name = Element("compname").value
    failure_rate = float(Element("failrate").value)
    repair_time = float(Element("repairtime").value)
    components_data.append([component_name, failure_rate, repair_time])                            
    print(components_data)
    components_df = pd.DataFrame(components_data, columns=['Component', 'Failure Rate', 'Repair Time'])    
    return calculate_ram_metrics(components_df)

def calculate_ram_metrics(components_df):
    """
    Calculate RAM metrics for a given DataFrame.
    """
    time_period = float(Element('period').value)
    components_df['Reliability'] = np.exp(-components_df['Failure Rate'] * time_period)
    components_df['MTBF'] = 1 / components_df['Failure Rate']
    components_df['MTTR'] = components_df['Repair Time'] # Mean Time To Repair
    components_df['Availability'] = components_df['MTBF'] / (components_df['MTBF'] + components_df['MTTR'])
    return components_df

# Main program
def clickdata(*args, **krgas):
    choice = Element("csvfile").value    
    if choice.lower() == 'csv':        
        file_path = Element("csvpath").value 
        result = calculate_ram_metrics_from_csv(file_path)
    else:
        result = calculate_ram_metrics_from_input()
    if result is not None:
        csv = Element('csv')
        csv.write(result)
        print(result)
