import pandas as pd
import os

def save_to_excel(data, keyword, output_dir):
    output_path = os.path.join(output_dir, f"{keyword}.xlsx")
    os.makedirs(output_dir, exist_ok=True)

    # Load old data if file exists
    if os.path.exists(output_path):
        old_df = pd.read_excel(output_path)
        new_df = pd.DataFrame(data)
        combined_df = pd.concat([old_df, new_df], ignore_index=True)
    else:
        combined_df = pd.DataFrame(data)

    # Drop duplicates based on ID or all columns (optional safety)
    combined_df.drop_duplicates(inplace=True)

    # Save combined data
    combined_df.to_excel(output_path, index=False)
    print(f"[✓] Data saved to: {output_path}")