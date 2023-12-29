import numpy as np
import pandas as pd
from pathlib import Path

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

components_data = []
def calculate_ram_metrics_from_input():
    """
    Calculate RAM metrics based on user input.
    """         
    components_df = pd.DataFrame(components_data, columns=['Component', 'Failure Rate', 'Repair Time', 'Time Period'])                
    return calculate_ram_metrics(components_df)

num_components = 0
def setData(*args, **kargs):        
    global num_components, components_data
    components_data = []  
    document.querySelector("#csv").innerHTML = ""
    num_components = int(Element("numcomp").value)             
    addbtn = Element("btn2")
    addbtn.write(f"Add {num_components} Components")

def addData(*args, **kargs):   
    if len(list(components_data))+1 <= num_components:        
        component_name = Element("compname").value
        failure_rate = float(Element("failrate").value)
        repair_time = float(Element("repairtime").value)
        time_period = float(Element('period').value)
        components_data.append([component_name, failure_rate, repair_time, time_period])                  
        addbtn = Element("btn2")        
        addbtn.write(f"Add {(num_components - len(list(components_data)))} Components")        
        resetField()

def resetData(*args, **kargs):
    global num_components, components_data
    num_components = 0
    components_data = []  
    document.querySelector("#numcomp").value = ""
    document.querySelector("#csv").innerHTML = ""
    resetField()    

def resetField():    
    document.querySelector("#compname").value = ""
    document.querySelector("#failrate").value = ""
    document.querySelector("#repairtime").value = ""
    document.querySelector("#period").value = ""        

def calculate_ram_metrics(components_df):
    """
    Calculate RAM metrics for a given DataFrame.
    """    
    components_df['Reliability'] = np.exp(-components_df['Failure Rate'] * components_df['Time Period'])
    components_df['MTBF'] = 1 / components_df['Failure Rate']
    components_df['MTTR'] = components_df['Repair Time'] # Mean Time To Repair
    components_df['Availability'] = components_df['MTBF'] / (components_df['MTBF'] + components_df['MTTR'])
    return components_df

# Main program
def calcData(*args, **krgas):
    choice = Element("csvfile").value    
    if choice.lower() == 'csv':        
        file_path = Element("csvpath").value 
        result = calculate_ram_metrics_from_csv(file_path)
    else:
        result = calculate_ram_metrics_from_input()
    if result is not None:
        csv = Element('csv')
        csv.write(result)   
        global num_components, components_data
        num_components = 0
        components_data = []       
        document.querySelector("#numcomp").value = ""
