from PIL import Image
import sys

img_path = "/Users/zaccharie/.gemini/antigravity/brain/6dc56677-69d0-491c-91f9-d184e125e639/gardening_cursor_v2_1774203942232.png"
out_path = "/Users/zaccharie/Documents/gift papa/docs/assets/cursor.png"

img = Image.open(img_path).convert("RGBA")
img = img.resize((32, 32), Image.Resampling.LANCZOS)
img.save(out_path, format="PNG")
print("Done")
