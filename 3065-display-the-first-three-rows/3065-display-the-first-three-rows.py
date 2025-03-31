import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    d = pd.DataFrame(employees)
    return d.head(3)