
import argparse

import os
import collections

# get referece .fa files in the directory
directory = "references"

def build_metadata(result_file: str):
    reference_files = [f for f in os.listdir(directory) if f.endswith(".fa")]
    reference_files.sort()

    # get fasta headers from the reference files
    reference_headers: list[str] = []
    for file in reference_files:
        with open(os.path.join(directory, file), "r") as f:
            header = [line.strip() for line in f.readlines() if line.startswith(">")][0]
            reference_headers.append(header)

    set_reference_headers = set(reference_headers)
    if len(set_reference_headers) != len(reference_headers):
        print("Reference headers are not unique. Difference is as follows:")
        print(len(reference_headers) - len(set_reference_headers))
        print("the same headers are:")
        print([item for item, count in collections.Counter(reference_headers).items() if count > 1])
        exit(1)

    # get the name of the reference files
    reference_names = [f.split(".")[0] for f in reference_files]

    # cleanup names using spaces instead of underscores
    reference_new_names = [f.replace("_", " ") for f in reference_names]

    # capitalize first letter
    reference_new_names = [f.capitalize() for f in reference_new_names]

    # create metadata csv table with reference names and new names
    metadata = zip(reference_names, reference_new_names)

    # write metadata to csv
    with open(result_file, "w", newline='') as f:
        f.write("reference_name,virus\n")
        for row in metadata:
            f.write(",".join(row) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build metadata from reference files.")
    parser.add_argument("result_file", help="Resulting metadata file.")
    args = parser.parse_args()
    build_metadata(args.result_file)

