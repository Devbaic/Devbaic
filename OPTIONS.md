# Neofetch banner options (4 variants x 3 themes = 12 files)

| variant | look                                              |
|---------|---------------------------------------------------|
| mono    | ASCII art, theme colour glow (closest to original)|
| color   | ASCII art in the photo's real colours             |
| dots    | halftone dots portrait (default)                  |
| photo   | real photo + neon frame + scanlines (sharpest)   |

| theme  | colour        |
|--------|---------------|
| shadow | purple        |
| blood  | red / orange  |
| arise  | cyan / blue   |

Use: in README.md change  ./neofetch/dots-shadow.svg  ->  ./neofetch/<variant>-<theme>.svg
Edit info (name, stack, contact, LV/HP/MP/EXP): neofetch/generate_neofetch.py (top "EDIT ME"),
then run:  python3 neofetch/generate_neofetch.py all all
Needs: pip install opencv-python numpy
