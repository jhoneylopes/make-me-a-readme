import unittest
import os
import shutil # For creating and removing mock directories safely
from pathlib import Path

import app.project_crawler as file_system_utils

class TestProjectCrawler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Set up mock directory structure and files for testing.
        This runs once before all tests in the class.
        """
        cls.base_mock_path = Path("tests") / "mock_data"
        cls.project_alpha_path = cls.base_mock_path / "project_alpha"
        cls.project_beta_path = cls.base_mock_path / "project_beta"
        cls.empty_project_path = cls.base_mock_path / "empty_project"
        cls.project_only_ignored_path = cls.base_mock_path / "project_with_only_ignored_files"

        # Create mock directories and files
        # Project Alpha
        cls.project_alpha_path.mkdir(parents=True, exist_ok=True)
        (cls.project_alpha_path / "main.py").write_text("# Main Python file\nprint('hello')")
        (cls.project_alpha_path / "README.md").write_text("# Project Alpha README")
        (cls.project_alpha_path / "notes.txt").write_text("Some notes here.")
        helpers_dir = cls.project_alpha_path / "helpers"
        helpers_dir.mkdir(exist_ok=True)
        (helpers_dir / "utils.js").write_text("// Utility JS file\nfunction test() {}")

        # Project Beta
        cls.project_beta_path.mkdir(parents=True, exist_ok=True)
        (cls.project_beta_path / "script.py").write_text("# Beta script")
        git_dir = cls.project_beta_path / ".git" # Ignored directory
        git_dir.mkdir(exist_ok=True)
        (git_dir / "config").write_text("git config data")
        data_dir = cls.project_beta_path / "data"
        data_dir.mkdir(exist_ok=True)
        (data_dir / "data_file.css").write_text("body { color: blue; }")


        # Empty Project
        cls.empty_project_path.mkdir(parents=True, exist_ok=True)

        # Project with only ignored files
        cls.project_only_ignored_path.mkdir(parents=True, exist_ok=True)
        (cls.project_only_ignored_path / ".env").write_text("SECRET_KEY=123") # Typically ignored
        pycache_dir = cls.project_only_ignored_path / "__pycache__"
        pycache_dir.mkdir(exist_ok=True)
        (pycache_dir / "some.cpython-39.pyc").write_text("binary_data")


    @classmethod
    def tearDownClass(cls):
        """
        Clean up mock directory structure after all tests.
        This runs once after all tests in the class.
        """
        # Be careful with shutil.rmtree!
        if cls.base_mock_path.exists() and cls.base_mock_path.is_dir() and cls.base_mock_path.name == "mock_data":
             # Basic safety check for the path name
            try:
                shutil.rmtree(cls.base_mock_path)
                print(f"\nCleaned up mock data directory: {cls.base_mock_path}")
            except OSError as e:
                print(f"Error removing mock data directory {cls.base_mock_path}: {e}")
        else:
            print(f"\nSkipped cleanup: Mock data directory not found or path seems incorrect: {cls.base_mock_path}")


    def test_read_project_alpha_files(self):
        """
        Test reading files from a mock project with mixed relevant and irrelevant files.
        """
        # Modify RELEVANT_CODE_EXTENSIONS for this specific test if needed, or use the defaults
        # For this test, we'll assume default file_system_utils.RELEVANT_CODE_EXTENSIONS
        # which includes .py and .js but not .txt
        
        expected_files = {
            os.path.join("main.py"): "# Main Python file\nprint('hello')",
            os.path.join("helpers", "utils.js"): "// Utility JS file\nfunction test() {}"
        }
        # Normalizing paths for cross-platform compatibility in keys
        expected_files_normalized = {Path(k): v for k, v in expected_files.items()}

        retrieved_files = file_system_utils.read_project_files(str(self.project_alpha_path))
        retrieved_files_normalized = {Path(k): v for k, v in retrieved_files.items()}
        
        self.assertEqual(len(retrieved_files_normalized), len(expected_files_normalized))
        self.assertDictEqual(retrieved_files_normalized, expected_files_normalized)

    def test_read_project_beta_files_ignores_git(self):
        """
        Test that .git directory and its contents are ignored.
        """
        expected_files = {
            os.path.join("script.py"): "# Beta script",
            os.path.join("data", "data_file.css"): "body { color: blue; }"
        }
        expected_files_normalized = {Path(k): v for k, v in expected_files.items()}

        retrieved_files = file_system_utils.read_project_files(str(self.project_beta_path))
        retrieved_files_normalized = {Path(k): v for k, v in retrieved_files.items()}

        self.assertEqual(len(retrieved_files_normalized), len(expected_files_normalized))
        self.assertDictEqual(retrieved_files_normalized, expected_files_normalized)
        
        # Ensure no .git files were picked up
        for file_path in retrieved_files_normalized.keys():
            self.assertNotIn(".git", str(file_path))


    def test_read_empty_project(self):
        """
        Test reading from an empty project directory.
        """
        retrieved_files = file_system_utils.read_project_files(str(self.empty_project_path))
        self.assertEqual(len(retrieved_files), 0)
        self.assertDictEqual(retrieved_files, {})

    def test_read_project_with_only_ignored_files(self):
        """
        Test reading from a project that only contains normally ignored files/folders.
        """
        # Assuming default IGNORED_ITEMS in file_system_utils
        # and .env, .pyc are not in RELEVANT_CODE_EXTENSIONS
        retrieved_files = file_system_utils.read_project_files(str(self.project_only_ignored_path))
        self.assertEqual(len(retrieved_files), 0)
        self.assertDictEqual(retrieved_files, {})

    def test_non_existent_path(self):
        """
        Test reading from a non-existent path (os.walk handles this gracefully by not yielding).
        Our function should return an empty dict.
        """
        non_existent_path = self.base_mock_path / "this_project_does_not_exist"
        retrieved_files = file_system_utils.read_project_files(str(non_existent_path))
        self.assertEqual(len(retrieved_files), 0)
        self.assertDictEqual(retrieved_files, {})
    
    # Note: Testing get_project_path() directly is tricky because it involves `input()`.
    # This typically requires mocking `builtins.input`.
    # For now, we are focusing on `read_project_files`.

if __name__ == '__main__':
    unittest.main()
