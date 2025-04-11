import pickle

def save_to_file(employees, filename="employees.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(employees, f)

def load_from_file(filename="employees.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []
