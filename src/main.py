from pathlib import Path


def main():
    folder = input("Enter folder path: ")

    folder_path = Path(folder)

    if not folder_path.exists():
        print("The specified path does not exist.")
        return

    if not folder_path.is_dir():
        print("The specified path is not a directory.")
        return

    image_extensions = [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".webp",
    ]

    video_extensions = [
        ".mp4",
        ".mkv",
        ".avi",
        ".mov",
        ".wmv",
    ]

    document_extensions = [
        ".pdf",
        ".docx",
        ".doc",
        ".txt",
        ".xlsx",
        ".pptx",
    ]

    audio_extensions = [
        ".mp3",
        ".wav",
        ".aac",
        ".flac",
    ]

    archive_extensions = [
        ".zip",
        ".rar",
        ".7z",
        ".tar",
    ]

    images_folder = folder_path / "Images"
    videos_folder = folder_path / "Videos"
    documents_folder = folder_path / "Documents"
    audio_folder = folder_path / "Audio"
    archives_folder = folder_path / "Archives"
    others_folder = folder_path / "Others"

    images_folder.mkdir(exist_ok=True)
    videos_folder.mkdir(exist_ok=True)
    documents_folder.mkdir(exist_ok=True)
    audio_folder.mkdir(exist_ok=True)
    archives_folder.mkdir(exist_ok=True)
    others_folder.mkdir(exist_ok=True)

    print("\nFiles to organize:\n")

    for item in folder_path.iterdir():

        if not item.is_file():
            continue

        extension = item.suffix.lower()

        if extension in image_extensions:
            destination = images_folder / item.name

        elif extension in video_extensions:
            destination = videos_folder / item.name

        elif extension in document_extensions:
            destination = documents_folder / item.name

        elif extension in audio_extensions:
            destination = audio_folder / item.name

        elif extension in archive_extensions:
            destination = archives_folder / item.name

        else:
            destination = others_folder / item.name

        if destination.exists():

            counter = 1

            while destination.exists():

                destination = destination.parent / (
                    f"{item.stem}_{counter}{item.suffix}"
                )

                counter += 1

        print("-" * 40)
        print(f"Moving:      {item.name}")
        print(f"Source:      {item}")
        print(f"Destination: {destination}")

    answer = input("\nDo you want to move these files? (Y/N): ").strip().lower()

    if answer != "y":
        print("Operation cancelled.")
        return

    print("Moving files...")
    print("(Real file moving will be implemented in the next step.)")
