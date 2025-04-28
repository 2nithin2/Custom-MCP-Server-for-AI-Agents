# server.py
from mcp.server.fastmcp import FastMCP
import os

# Create an MCP server
mcp = FastMCP("Demo")

notes_file=os.path.join(os.path.dirname(__file__), "notes.txt")
# Add a note-taking tool

def ensure_file_exists(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write("")
@mcp.tool()
def add_note(note: str)-> str:
    """
    Add a note to the notes file. returns a confirmation message.
    Args:
        note (str): The note to add.
    Returns:
        str: Confirmation message.
    """
    ensure_file_exists(notes_file) #document is should to read by cluade
    with open(notes_file, 'a') as f:# Open the file in append mode
        f.write(note + "\n")
    return "Note added."
@mcp.tool()
def read_notes()-> str:
    """
    Read the notes from the notes file.
    Returns:
        str: The contents of the notes file.
    """
    ensure_file_exists(notes_file)
    with open(notes_file, 'r') as f:
        content = f.read().strip()
    return content if content else "No notes found."
@mcp.resource("notes://latest")
def get_notes():
    """
    Get the latest notes.
    Returns:
        str: The latest notes.
    """
    ensure_file_exists(notes_file)
    with open(notes_file, 'r') as f:
        lines = f.read().strip()
    return lines[-1].strip() if lines else "No notes found." 

@mcp.prompt()
def note_summary_prompt()-> str:
    """
    Prompt the user for a note.
    Returns:
        str: The note entered by the user.
    """
    ensure_file_exists()
    with open(notes_file, 'r') as f:
        content=f.read().strip()
    if not content:
        return "No notes found."
    return f"summarise the current note {content}"
