import pathlib


def parse_text(text: str) -> str:
    """
    Parse the text and return the parsed content

    Args:
        text: The text to be parsed
        
    Returns:
        str: The parsed content
    
    Notes:
        First 3 lines are skipped they contain title of youtube video and the date of the video and the link to the video
    """
    lines = text.split("\n")
    lines = lines[3:]
    parsed_lines = []
    for line in lines:
        parsed_line = line[13:] 
        parsed_lines.append(parsed_line)
    return "\n".join(parsed_lines)

# ============================================================

def parse_file_tactiq(file_path: str | pathlib.Path) -> str:
    """
    Parse a text file and save the parsed content to a new file with '_tactiq' suffix.
    
    Args:
        file_path: Path to the file as string or Path object
        
    Returns:
        str: Message indicating where the parsed file was saved
    """
 
    path = pathlib.Path(file_path)
    

    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    
    parsed_content = parse_text(content) 
    
    parsed_filename = path.with_name(f"{path.stem}_tactiq{path.suffix}")
    
    with open(parsed_filename, "w", encoding="utf-8") as file:
        file.write(parsed_content)
    
    return f"File saved to {parsed_filename}"

# ====================================================

