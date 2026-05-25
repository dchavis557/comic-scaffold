import os
import json
from pathlib import Path

# Constants
ISSUE_SUBFOLDERS = ["Inks", "Flats", "Colors"]
DOCUMENTS_FOLDER = "Docs"
CONFIG_PATH = os.path.expanduser("/home/dj/project-creator/project-config.json")

def load_config():
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def create_project_structure(project_name, start_issue, end_issue, base_path):
    folder_name = project_name.strip()
    root_path = Path(base_path).expanduser() / folder_name
    root_path.mkdir(parents=True, exist_ok=True)

    # Create _Documents folder
    documents_path = root_path / DOCUMENTS_FOLDER
    documents_path.mkdir(exist_ok=True)

    print(f"\n📁 Creating project: {folder_name}")
    print(f"📍 Location: {root_path}")

    if start_issue == end_issue == 1:
        # Single-issue layout
        print(f"🗂️  Single-issue layout (no sub-issue folders)")
        for subfolder in ISSUE_SUBFOLDERS:
            subfolder_path = root_path / subfolder
            subfolder_path.mkdir(exist_ok=True)
            print(f"✅ Created: {subfolder_path}")
    else:
        # Series layout
        print(f"🗂️  Issues: {start_issue} to {end_issue}\n")
        for i in range(start_issue, end_issue + 1):
            issue_label = f"Issue {str(i).zfill(2)}"
            issue_path = root_path / issue_label
            issue_path.mkdir(exist_ok=True)

            for subfolder in ISSUE_SUBFOLDERS:
                subfolder_path = issue_path / subfolder
                subfolder_path.mkdir(exist_ok=True)

            print(f"✅ Created: {issue_path}")

    print(f"\n🎉 Project setup complete!\n")

    return str(root_path)

def create_metadata_file(project_path):
    """
    Prompts user for metadata fields and creates metadata.json
    in the project root directory.
    """

    print("\n--- Metadata Creation ---")

    writers = input("Writers: ").strip()
    line_artists = input("Line Artists: ").strip()
    publisher = input("Publisher: ").strip()

    metadata = {
        "writers": writers,
        "line_artists": line_artists,
        "publisher": publisher
    }

    metadata_path = os.path.join(project_path, "metadata.json")

    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=4)

    print(f"Created metadata file at: {metadata_path}")


def prompt_user():
    print("🎨 Comic Project Creator\n")

    # Load config and get default root path
    config = load_config()
    default_path = config.get("default_root_path", "")

    while True:
        default_prompt = f" [{default_path}]" if default_path else ""
        base_path = input(f"🗂️ Root folder where project should be created{default_prompt}: ").strip()
        base_path = os.path.expanduser(base_path or default_path)

        if not base_path:
            print("⚠️ Please provide a path.")
            continue
        if not os.path.isdir(base_path):
            print("❌ That directory does not exist. Try again.")
        else:
            break

    # Ask for project title
    project_name = input("📁 Project title: ").strip()
    while not project_name:
        project_name = input("⚠️ Please enter a project title: ").strip()

    # Ask if it's a series
    is_series_input = input("📘 Is this a series? [Y/n]: ").strip().lower()
    is_series = (is_series_input != "n")

    # Determine issue range
    if not is_series:
        start_issue = end_issue = 1
    else:
        while True:
            try:
                start_input = input("🔢 Start issue number [default 1]: ").strip()
                start_issue = int(start_input) if start_input else 1

                end_input = input(f"🔢 End issue number [must be ≥ {start_issue}]: ").strip()
                end_issue = int(end_input)

                if start_issue > 0 and end_issue >= start_issue:
                    break
            except ValueError:
                print("⚠️ Please enter valid integers.")
            except Exception as e:
                print(f"❌ Error: {e}")

    project_path = create_project_structure(project_name, start_issue, end_issue, base_path)

    # Ask if user wants metadata file
    create_meta = input("\nWould you like to create a metadata.json file? (y/n): ").strip().lower()
    if create_meta == "y":
        create_metadata_file(project_path)


if __name__ == "__main__":
    prompt_user()
