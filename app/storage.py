from pathlib import Path
import json

DATA_DIR=Path("Data")
DATA_FILE=DATA_DIR/"issues.json"


# load data

def load_data():
    # if file not exists
    if DATA_FILE.exists():
        with open(DATA_FILE) as f:
            our_data = f.read()
            if our_data.strip():
                return json.loads(our_data)
    
    return []


def save_data(data):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)