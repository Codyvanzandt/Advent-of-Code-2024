def read_input(file_path):
    day_folder = f"day-{str(file_path).zfill(2)}"
    input_path = f"{day_folder}/input.txt"
    with open(input_path, 'r') as file:
        return file.read()
