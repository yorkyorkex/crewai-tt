import os


def write_to_file(filename: str, content: str) -> str:
    """
    Write content to a file.
    
    Args:
        filename: The filename to write to (including path)
        content: The content to write to the file
        
    Returns:
        Success or error message
    """
    try:
        # Create directory if it doesn't exist
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        
        # Write the file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return f"Successfully wrote content to {filename}"
    
    except Exception as e:
        return f"Error writing to file {filename}: {str(e)}"


class CustomFileWriterTool:
    """Simple file writer tool for CrewAI agents."""
    
    def __init__(self):
        self.name = "File Writer"
        self.description = "Write content to a file. Creates directories if they don't exist."
    
    def __call__(self, filename: str, content: str) -> str:
        return write_to_file(filename, content)