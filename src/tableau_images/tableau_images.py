from pathlib import Path
import cairosvg


def tableau_images(in_directory: Path, out_directory: Path):
    for file in in_directory.glob("*.svg"):
        print(f"{file.stem}")
        out_file = f"{file.stem}.png"
        out_path = out_directory / out_file
        cairosvg.svg2png(
            file_obj=open(file, "rb"),
            write_to=str(out_path),
            # output_height=300,
            # output_width=184,
        )


if __name__ == "__main__":
    tableau_images()
