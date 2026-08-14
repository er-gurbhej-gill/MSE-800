from ucimlrepo import fetch_ucirepo
import pandas as pd

# Fetch the Iris dataset
iris = fetch_ucirepo(id=53)

# Get features and targets
X = iris.data.features
y = iris.data.targets

# Loop through all rows
for i in range(len(X)):
    print("Record:", i + 1)

    # Get feature values
    print("Features:", X.iloc[i].values)

    # Get target value
    print("Target:", y.iloc[i].values)

    print("--------------------")