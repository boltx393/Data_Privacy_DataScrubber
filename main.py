import os
import argparse
import pandas as pd
from scrubber import clean_up
from ei_handler import mask
from qi_finder import find_qi

def data_parser(input_file_path, output_file_name):
    # Reading the CSV record file
    df = pd.read_csv(input_file_path)

    print('Processing the file')

    # Masking the explicit identifiers
    df = mask(df)
    print('Masking of explicit identifiers completed.')

    # Cleaning the data
    df = clean_up(df)
    print('Cleaning of data completed.')

    # Identifying the quasi identifiers
    print('Analyzing quasi identifiers')
    error, risky_qi = find_qi(df)

    if not error:
        if len(risky_qi) > 0:
            print('The most risky quasi identifiers that need to be anonymized in the given data are: ')
            for qi in risky_qi:
                print(qi)
            # Perform K-anonymization here
            # Implement your K-anonymization logic
            # Replace the quasi-identifiers with generalized values
        else:
            print('The data does not need any anonymization.')
    else:
        print('Quasi identifiers could not be found due to an error in input')

    # Creating the output CSV record file
    path = os.path.join(os.getcwd(), 'Output_files')
    if not os.path.isdir(path):
        os.mkdir(path)
    output_filename = str(output_file_name)
    if output_filename.find('.csv') == -1:
        output_filename += '.csv'
    output_file_path = os.path.join(path, output_filename)
    df.to_csv(output_file_path)
    print('Processing completed.')
    print(f'{output_filename} has been created and saved in the Output_files directory\n')

if __name__ == "__main__":
    # For running through command line
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--input-file-path", required=True, help="Path to the input CSV record file")
    ap.add_argument("-o", "--output-file-name", required=True, help="Name of the output CSV file")
    args = vars(ap.parse_args())
    
    data_parser(args["input_file_path"], args["output_file_name"])
