import pandas as pd
import glob

# ---- CHANGE THESE ----
LABEL_FILES_PATTERN = "data/Massive/Base/Main_Dataset/grouped/labels_*.csv"   # pattern for label-count files
SLOT_FILES_PATTERN = "data/Massive/Base/Main_Dataset/grouped/slots_*.csv"     # pattern for slot-count files

# ---------------------- FUNCTION ----------------------

def combine_and_group(pattern, output_file):
    files = glob.glob(pattern)
    print(f"Found files: {files}")

    # Read & combine all files
    df_list = [pd.read_csv(f) for f in files]
    combined = pd.concat(df_list)

    # Group by first column (label or slot)
    col = combined.columns[0]
    grouped = combined.groupby(col)['count'].sum().reset_index()

    # Save
    grouped.to_csv(output_file, index=False)
    print(f"Saved: {output_file}")


# ---- RUN FOR LABELS ----
combine_and_group(LABEL_FILES_PATTERN, "labels_combined.csv")

# ---- RUN FOR SLOTS ----
combine_and_group(SLOT_FILES_PATTERN, "slots_combined.csv")
