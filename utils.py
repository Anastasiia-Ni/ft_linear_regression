import os
import pandas as pd
import sys


def load_data(path):
    """Load and validate the dataset from a CSV file."""
    if not os.path.exists(path):
        print(f"\033[31mThe file \033[1m{path}\033[0m\033[31m does not exist.\033[0m")
        return None

    try:
        data_csv = pd.read_csv(path)
    except Exception as e:
        print(f"\033[31mError reading the file:\033[0m {e}")
        return None

    if data_csv.empty or data_csv.shape[0] == 0:
        print("\033[31mNo data\033[0m in the DataFrame.")
        return None
    if data_csv.isnull().any().any():
        print("\033[31mMissing values\033[0m detected in the data.")
        return None
    if (data_csv == 0).any().any():
        print("\033[31mZero values\033[0m detected in the data.")
        return None

    return data_csv


def save_theta_values(theta0, theta1, path):
    """Save the trained model parameters (theta0 and theta1) to a CSV file."""
    try:
        df = pd.DataFrame({'theta0': [theta0], 'theta1': [theta1]})
        df.to_csv(path, index=False)
        print(f"\033[36mTheta values successfully saved to \033[1m{path}\033[0m")
    except Exception as e:
        print(f"\033[31mError saving theta values: \033[0m{e}")


def handle_ctrl_c(sig, frame):
    """Handle the Ctrl+C signal by printing a message and exiting."""
    print("\nCtrl+C pressed. Exiting.")
    sys.exit(0)


def handle_ctrl_z(sig, frame):
    """Handle the Ctrl+Z signal by printing a message and exiting."""
    print("\nCtrl+Z pressed. Exiting.")
    sys.exit(0)
