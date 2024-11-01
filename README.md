# Data Privacy Scrubber

A data privacy tool that uses **K-anonymization** to protect sensitive information by anonymizing datasets. This scrubber helps organizations maintain privacy standards, enabling secure data sharing while preserving essential data structure.

## Features

- **K-Anonymization**: Ensures anonymity by making each record indistinguishable from at least `K-1` others.
- **Sensitive Data Handling**: Detects and processes personally identifiable information (PII) and sensitive attributes.
- **Output Customization**: Allows for easy configuration of anonymized output files.

## File Structure

- **Input_files/**: Directory for uploading datasets to be anonymized.
- **Output_files/**: Directory where the processed, anonymized files are saved.
- **list/**: Contains lists or mappings used by the scrubber to identify quasi-identifiers.
- **ei_handler.py**: Handles explicit identifiers in the dataset.
- **k_anonymization.py**: Core file implementing K-anonymization.
- **main.py**: Main script to run the data scrubber.
- **qi_finder.py**: Identifies quasi-identifiers (attributes that could potentially reveal identities).
- **scrubber.py**: General utility functions for the scrubber.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/data-privacy-scrubber.git
   cd data-privacy-scrubber
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your dataset in the `Input_files` directory.
2. Run the main script to anonymize the data:
   ```bash
   python main.py
   ```
3. Find the anonymized output in the `Output_files` directory.

## Configuration

- Modify the `K` value in `k_anonymization.py` to change the anonymity level.
- Customize the quasi-identifier selection in `qi_finder.py` as needed.
