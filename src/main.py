import shutil
from pathlib import Path


def main():
    folder = input("Enter folder path: ").strip()

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
        ".doc",
        ".docx",
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

    folders = [
        images_folder,
        videos_folder,
        documents_folder,
        audio_folder,
        archives_folder,
        others_folder,
    ]

    for folder in folders:
        folder.mkdir(exist_ok=True)

    operations = []

    print("\n========== Preview ==========\n")

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

        operations.append((item, destination))

        print("-" * 40)
        print(f"File : {item.name}")
        print(f"From : {item}")
        print(f"To   : {destination}")

    if not operations:
        print("No files found.")
        return

    answer = input(
        "\nDo you want to move these files? (Y/N): "
    ).strip().lower()

    if answer != "y":
        print("Operation cancelled.")
        return

    print("\nMoving files...\n")

    moved_count = 0
    failed_count = 0

    for source, destination in operations:

        try:

            shutil.move(str(source), str(destination))

            moved_count += 1

            print(f"✅ {source.name}")

        except Exception as error:

            failed_count += 1

            print(f"❌ {source.name}")
            print(f"Reason: {error}")

    print("\n========== Summary ==========")
    print(f"Moved Files : {moved_count}")
    print(f"Failed Files: {failed_count}")
    print("=============================")
