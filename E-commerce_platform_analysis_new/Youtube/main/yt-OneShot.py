import os
import glob
import pandas as pd

# List of files to be executed
files = [
    "yt-scrap-MainV12.py",
    "yt-FileBreak.py",
    "yt-scrap-BERTV6.py",
    "yt-MariaV6.py"
]

# Set the output directory
current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir)

# Iterate through the files and execute them
for file_name in files:
    file_path = os.path.join(current_dir, file_name)
    print("Running:", file_name)
    if file_name == "yt-scrap-BERTV6.py":
        csv_files = glob.glob(os.path.join(current_dir, "jjTasks", "raw_output_*.csv"))
        for csv_file_path in csv_files:
            os.system(f"python {file_path} --csv {csv_file_path}")
    elif file_name == "yt-MariaV4.py":
        csv_file_path = os.path.join(current_dir, "jjTasks", "Final_BERT.csv")
        command = f"python {file_path} --input {csv_file_path}"
        output = os.popen(command).read()
        data_count = output.split(":")[-1].strip()  # Extract the number of new data imported
        print(f"New data count: {data_count}")
    else:
        os.system(f"python {file_path}")
