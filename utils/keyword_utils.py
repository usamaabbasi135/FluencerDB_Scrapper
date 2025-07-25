def remove_keyword_from_file(keyword, file_path="keywords.txt"):
    with open(file_path, "r") as f:
        lines = f.readlines()

    # Keep only lines that are not the completed keyword
    with open(file_path, "w") as f:
        for line in lines:
            if line.strip().lower() != keyword.lower():
                f.write(line)
