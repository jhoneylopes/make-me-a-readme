import os

# --- Configuration Constants ---
# File extensions to be considered for code analysis
RELEVANT_CODE_EXTENSIONS = ['.py', '.js', '.java', '.c', '.cpp', '.h', '.cs', '.go', '.rb', '.php', '.swift', '.kt', '.ts', '.html', '.css', '.md']
# Files and folders to be ignored during scanning
IGNORED_ITEMS = ['.git', '.idea', '__pycache__', 'node_modules', 'venv', '.vscode', 'target', 'build', 'dist', 'bin', 'obj', 'logs']
# Name of the README file to be generated or ignored if it already exists and we don't want to overwrite it
README_FILENAME = "README.md"

# --- File System Interaction Functions ---

def get_project_path() -> str:
    """
    Prompts the user for the path to the project folder.

    Returns:
        str: The absolute path to the project folder.
    """
    while True:
        path_str = input("Please enter the path to your project folder: ")
        if os.path.isdir(path_str):
            return os.path.abspath(path_str)
        else:
            print(f"Error: The path '{path_str}' is not a valid directory. Please try again.")

def read_project_files(project_path: str) -> dict[str, str]:
    """
    Reads the content of relevant files in a project, ignoring specified directories and file types.

    Args:
        project_path (str): The path to the root folder of the project.

    Returns:
        dict[str, str]: A dictionary where keys are the relative file paths
                        and values are the content of those files.
    """
    file_contents = {}
    print(f"\n🔎 Analyzing files in: {project_path}")

    for root, dirs, files in os.walk(project_path, topdown=True):
        # Remove ignored directories from the 'dirs' list to avoid traversing them
        # Using a list comprehension to modify dirs in place
        dirs[:] = [d for d in dirs if d not in IGNORED_ITEMS and not d.startswith('.')]

        for filename in files:
            # Skip the README file itself if it matches README_FILENAME (case-insensitive)
            # Also skip other specifically ignored items if they appear as files
            if filename.lower() == README_FILENAME.lower() or filename in IGNORED_ITEMS:
                continue

            # Check the file extension
            file_extension = os.path.splitext(filename)[1].lower()
            if file_extension in RELEVANT_CODE_EXTENSIONS:
                full_path = os.path.join(root, filename)
                relative_path = os.path.relpath(full_path, project_path)
                try:
                    with open(full_path, 'r', encoding='utf-8', errors='ignore') as file_obj:
                        content = file_obj.read()
                        file_contents[relative_path] = content
                        # Using f-string for formatted output
                        print(f"  📄 Read: {relative_path} ({len(content)} bytes)")
                except Exception as e:
                    # Using f-string for formatted error message
                    print(f"  ⚠️  Error reading file {relative_path}: {e}")
    
    if not file_contents:
        print("  ⚠️ No relevant files found for analysis.")
    return file_contents

if __name__ == '__main__':
    # Example usage:
    # This block will only run if the script is executed directly.
    # It's useful for testing this module independently.
    print("--- Testing File System Utilities ---")
    
    # For testing, instead of prompting, you can hardcode a path or use a known test directory.
    # For this example, we'll still prompt.
    # test_project_path = "/path/to/your/test/project" # Replace with an actual path for automated testing
    test_project_path = get_project_path()

    if test_project_path:
        print(f"\nSelected project path: {test_project_path}")
        retrieved_files = read_project_files(test_project_path)
        
        if retrieved_files:
            print(f"\n--- Retrieved {len(retrieved_files)} files ---")
            for rel_path, _ in retrieved_files.items():
                print(f"- {rel_path}")
            # To see content (can be very verbose):
            # for rel_path, content_data in retrieved_files.items():
            #     print(f"\n--- Content of {rel_path} ---")
            #     print(content_data[:200] + "..." if len(content_data) > 200 else content_data) # Print first 200 chars
        else:
            print("\nNo files were retrieved from the specified path.")
    else:
        print("No project path was provided.")
    
    print("\n--- End of File System Utilities Test ---")
