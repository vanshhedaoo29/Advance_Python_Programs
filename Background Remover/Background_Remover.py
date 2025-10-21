import sys
import cv2
from rembg import remove
from PIL import Image
import numpy as np
import os

def remove_background(input_path, output_path):
    """
    Removes background from the given image and saves a transparent PNG.
    """
    try:
        if not os.path.exists(input_path):
            print(f"❌ Error: File '{input_path}' not found.")
            return

        print("🔍 Reading image...")
        input_image = Image.open(input_path)

        print("🧠 Removing background (this may take a few seconds)...")
        output_image = remove(input_image)

        output_np = np.array(output_image)
        output_cv = cv2.cvtColor(output_np, cv2.COLOR_RGBA2BGRA)

        print(f"💾 Saving result to: {output_path}")
        cv2.imwrite(output_path, output_cv)
        print("✅ Background removed successfully!")

    except Exception as e:
        print(f"⚠️ Error: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python background_remover.py <input_image> <output_image>")
        print("Example: python background_remover.py photo.jpg photo_no_bg.png")
        return

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    remove_background(input_path, output_path)

if __name__ == "__main__":
    main()
