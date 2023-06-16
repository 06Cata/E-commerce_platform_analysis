import os
import pandas as pd

# Get the current file location
current_dir = os.path.dirname(os.path.abspath(__file__))

# Input file path
input_file = os.path.join(current_dir, 'yt_Main_data.csv')

# Check if the input file exists and is not empty
if os.path.isfile(input_file) and os.path.getsize(input_file) > 0:
    # Read the CSV file
    data = pd.read_csv(input_file)

    # Check if the data DataFrame has at least one row
    if len(data) > 0:
        # Specify the number of lines per file
        lines_per_file = 100

        # Output folder
        output_folder = os.path.join(current_dir, 'jjTasks')

        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Print message
        print("Breaking up files")

        # Calculate the number of files needed
        total_rows = len(data)
        num_files = total_rows // lines_per_file + 1

        # Split the data and write to smaller files
        for i in range(num_files):
            start_index = i * lines_per_file
            end_index = start_index + lines_per_file

            # Extract the chunk of data
            chunk = data.iloc[start_index:end_index]

            # Write the chunk to a new file in the output folder
            file_path = os.path.join(output_folder, f'raw_output_{i}.csv')
            chunk.to_csv(file_path, index=False)

        # Delete the input file
        os.remove(input_file)

        print("Input file deleted.")
    else:
        print("No Data")
else:
    print("No Data")
