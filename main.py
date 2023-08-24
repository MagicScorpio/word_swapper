# Assign input and output file paths
input_file_path = 'INPUT_FILE_PATH'  # İşlenecek girdi dosyası
output_file_path = 'OUTPUT_FILE_PATH'  # Çıktı dosyası

# Create an array that holds output lines
output_lines = []

# Read the data by opening the input file
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()  # Reading the files lines

    # Loop to process each line
    for line in lines:
        parts = line.strip().split(',')  # Split the line by comma
        if len(parts) == 2:  # If there is 2 words (split by comma)
            # Change the order of the words and create the new output line
            output_lines.append(f"{parts[1]},{parts[0]}")

# Create the output file and write the translated data
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(output_lines))  # Write lines to the output file

# An informational message is printed after the process is complete
print(f"Data is printed to file {output_file_path}.")