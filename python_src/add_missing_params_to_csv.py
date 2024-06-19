import os
import csv

import default_params
import config


# -------------------------------------------------------------------------------- #

def main():
    print("Running add_missing_params_to_csv.py")

    if not os.path.exists(config.band_plan_source_dir):
        print("Error: band_plan_source_dir does not exist")
        exit(1)

    band_plan_file_list = os.listdir(config.band_plan_source_dir)
    for band_plan_file in band_plan_file_list:
        if band_plan_file.endswith(".csv") and not is_band_plan_exception_file(band_plan_file):
            add_missing_params_to_csv(band_plan_file)

    print("-" * 40)


# -------------------------------------------------------------------------------- #

def is_band_plan_exception_file(band_plan_file):
    if "FM" in band_plan_file:
        return True

    return False


# -------------------------------------------------------------------------------- #

def add_missing_params_to_csv(band_plan_file):
    print("-" * 40)
    print("Processing file: " + band_plan_file)



# -------------------------------------------------------------------------------- #

if __name__ == "__main__":
    main()
