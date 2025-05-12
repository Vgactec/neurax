import json
import csv
import os
from datetime import datetime

def save_simulation_data(space_time, metrics, base_path="."):
    """Save simulation data and metrics to files"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save space-time data as JSON
    json_path = os.path.join(base_path, f"simulation_data_{timestamp}.json")
    with open(json_path, 'w') as f:
        json.dump({
            'space_time': space_time.tolist(),
            'metrics': metrics
        }, f)
        
    # Save metrics as CSV
    csv_path = os.path.join(base_path, f"metrics_{timestamp}.csv")
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=metrics.keys())
        writer.writeheader()
        writer.writerow(metrics)
        
    return json_path, csv_path
