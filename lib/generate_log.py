from datetime import datetime
 
 
def generate_log(entries):
    """
    Generates a timestamped log file from a list of entries.
 
    Args:
        entries (list): A list of strings to write to the log file.
 
    Returns:
        str: The filename of the created log file.
 
    Raises:
        ValueError: If entries is not a list.
    """
    if not isinstance(entries, list):
        raise ValueError("entries must be a list.")
 
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"
 
    with open(filename, "w") as file:
        for entry in entries:
            file.write(entry + "\n")
 
    print(f"Log file created: {filename}")
    return filename
    