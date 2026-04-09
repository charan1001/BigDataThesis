import os
import json
import glob

import pandas as pd


class YelpJsonToCsvConverter:
    """Converts Yelp Academic Dataset JSON files to CSV format."""

    LIST_SEPARATOR = "/_/"

    def __init__(self, source_directory: str, output_directory: str):
        """
        Args:
            source_directory: Path to the folder containing JSON files.
            output_directory: Path to the folder where CSV files will be saved.
        """
        self.source_directory = source_directory
        self.output_directory = output_directory

    def flatten_record(self, raw_json_string: str) -> dict:
        """
        Parse a single JSON string and flatten it into a plain dictionary.

        - List values are joined into a single string using LIST_SEPARATOR.
        - Nested dict values are flattened as 'parent_child' keys.

        Args:
            raw_json_string: A single line of JSON text.

        Returns:
            A flat dictionary suitable for a pandas DataFrame row.
        """
        record = json.loads(raw_json_string)
        keys_to_delete = []

        for key, value in list(record.items()):
            if isinstance(value, list):
                record[key] = self.LIST_SEPARATOR.join(value)
            elif isinstance(value, dict):
                for nested_key, nested_value in value.items():
                    flattened_key = f"{key}_{nested_key}"
                    record[flattened_key] = nested_value
                keys_to_delete.append(key)

        for key in keys_to_delete:
            del record[key]

        return record

    def convert_file(self, json_file_path: str) -> str:
        """
        Convert a single JSON file to CSV.

        Args:
            json_file_path: Full path to the source JSON file.

        Returns:
            Full path to the output CSV file.
        """
        base_name = os.path.splitext(os.path.basename(json_file_path))[0]
        csv_file_path = os.path.join(self.output_directory, f"{base_name}.csv")

        with open(json_file_path, encoding="utf-8") as json_file:
            records = [self.flatten_record(line) for line in json_file if line.strip()]

        dataframe = pd.DataFrame(records)
        dataframe.to_csv(csv_file_path, encoding="utf-8", index=False)

        return csv_file_path

    def convert_all(self):
        """
        Convert all JSON files in the source directory to CSV.

        Prints the status of each file conversion.
        """
        os.makedirs(self.output_directory, exist_ok=True)

        json_file_paths = glob.glob(os.path.join(self.source_directory, "*.json"))

        if not json_file_paths:
            print(f"No JSON files found in '{self.source_directory}'.")
            return

        for json_file_path in json_file_paths:
            print(f"Converting: {json_file_path}")
            csv_file_path = self.convert_file(json_file_path)
            print(f"  Saved to: {csv_file_path}")

        print(f"\nDone. {len(json_file_paths)} file(s) converted.")


if __name__ == "__main__":
    SOURCE_DIR = "."
    OUTPUT_DIR = "yelp_csv"

    converter = YelpJsonToCsvConverter(
        source_directory=SOURCE_DIR,
        output_directory=OUTPUT_DIR,
    )
    converter.convert_all()
