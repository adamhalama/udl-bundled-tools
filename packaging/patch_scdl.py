from pathlib import Path

import scdl


def main() -> None:
    path = Path(scdl.__file__).parent / "patches" / "trim_filenames.py"
    text = path.read_text(encoding="utf-8")
    text = text.replace("import yt_dlp.__init__\n", "import yt_dlp\n")
    text = text.replace(
        "from yt_dlp.__init__ import validate_options as old_validate_options\n",
        "from yt_dlp import validate_options as old_validate_options\n",
    )
    text = text.replace(
        "yt_dlp.__init__.validate_options = new_validate_options\n",
        "yt_dlp.validate_options = new_validate_options\n",
    )
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
