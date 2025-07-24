import pandas as pd
import os

def save_to_excel(data, keyword, output_dir):
    df = pd.DataFrame(data)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{keyword}.xlsx")
    df.to_excel(output_path, index=False)
    print(f"[✓] Saved data to: {output_path}")