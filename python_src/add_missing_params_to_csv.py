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

    if not os.path.exists(config.band_plan_output_dir):
        os.makedirs(config.band_plan_output_dir)

    band_plan_file_list = os.listdir(config.band_plan_source_dir)
    for band_plan_file in band_plan_file_list:
        if band_plan_file.endswith(".csv") and not is_band_plan_exception_file(band_plan_file):
            add_missing_params_to_csv(config.band_plan_source_dir, band_plan_file)

    print("-" * 40)


# -------------------------------------------------------------------------------- #

def is_band_plan_exception_file(band_plan_file):
    if "FM" in band_plan_file:
        return True

    return False


# -------------------------------------------------------------------------------- #

def add_missing_params_to_csv(band_plan_dir, band_plan_file):
    print("-" * 40)
    print("Processing file: ", band_plan_file)

    band_plan_file_path = os.path.join(band_plan_dir, band_plan_file).replace("\\", "/")
    band_plan_output_file_path = os.path.join(config.band_plan_output_dir, band_plan_file).replace("\\", "/")

    with open(band_plan_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        raw_data = list(csv_reader)

    filled_data = add_missing_params(raw_data)

    with open(band_plan_output_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerows(filled_data)

    print("Output file: ", band_plan_output_file_path)


# -------------------------------------------------------------------------------- #

def add_missing_params(raw_data):
    filled_data = []
    source_key_list = []

    for i, row in enumerate(raw_data):
        if i == 0:
            source_key_list = row
        else:
            filled_dict = fill_up_dict_with_given_data(source_key_list, row, i-1)
            filled_data.append(list(filled_dict.values()))

    header = default_params.Channels_default.keys()
    filled_data.insert(0, list(header))

    return filled_data


def fill_up_dict_with_given_data(source_key_list, row, index=0):
    pattern_dict = default_params.Channels_default.copy()

    for key, value in zip(source_key_list, row):
        pattern_dict[key] = value

    if "TxFreq" in source_key_list and "RxFreq" not in source_key_list:
        pattern_dict["RxFreq"] = pattern_dict["TxFreq"]

    if "RxFreq" in source_key_list and "TxFreq" not in source_key_list:
        pattern_dict["TxFreq"] = pattern_dict["RxFreq"]

    if "chanIndex" not in source_key_list:
        pattern_dict["chanIndex"] = index

    return pattern_dict

# -------------------------------------------------------------------------------- #

if __name__ == "__main__":
    main()
