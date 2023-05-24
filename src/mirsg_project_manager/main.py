from __future__ import annotations

from pathlib import Path

import pandas as pd

from mirsg_project_manager.site_management import get_site_folders


def main():
    """Entry point for running application"""
    drive_id = "b!K_ySv-8pJ0G6cFXO9uWU8HxSXGz6nCFBvUosbSy6rYHHxFY5DXN7TKPDuhD7-X05"
    filepath = Path("./projects.csv")
    projects = get_site_folders(drive_id)
    pd.json_normalize(projects.values()).to_csv(filepath)


if __name__ == "__main__":
    main()
