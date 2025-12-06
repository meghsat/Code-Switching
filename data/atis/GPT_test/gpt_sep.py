def filter_by_labels(
    label_file="label",
    seq_in_file="seq.in",
    seq_out_file="seq.out",
    allowed_labels=None,
    out_label="label.filtered",
    out_seq_in="seq.in.filtered",
    out_seq_out="seq.out.filtered"
):
    if allowed_labels is None:
        raise ValueError("allowed_labels list cannot be None")

    # Convert allowed labels to a set for faster lookup
    allowed_labels = set(allowed_labels)

    # Read the 3 input files
    with open(label_file, "r", encoding="utf-8") as f:
        labels = [line.strip() for line in f]

    with open(seq_in_file, "r", encoding="utf-8") as f:
        seq_in = [line.strip() for line in f]

    with open(seq_out_file, "r", encoding="utf-8") as f:
        seq_out = [line.strip() for line in f]

    # Ensure all files have same number of lines
    assert len(labels) == len(seq_in) == len(seq_out), "Input files are not aligned!"

    # Filter and write to new files
    with open(out_label, "w", encoding="utf-8") as lf, \
         open(out_seq_in, "w", encoding="utf-8") as si, \
         open(out_seq_out, "w", encoding="utf-8") as so:

        for lab, inp, out in zip(labels, seq_in, seq_out):
            if lab in allowed_labels:
                lf.write(lab + "\n")
                si.write(inp + "\n")
                so.write(out + "\n")

    print("Filtering complete!")
    print(f"Saved: {out_label}, {out_seq_in}, {out_seq_out}")


allowed = [
    # "atis_airport",
    # "atis_city",
    # "atis_ground_fare",
    # "atis_flight_no",
    # "atis_meal",
    # "atis_fligh",
    # "atis_restriction",
    # "atis_day_name",
    # "atis_cheapest",
    # "atis_flig"
    # "atis_ground_service",
    # "atis_airline"
    # "atis_flight",
    # "atis_airfare"
    "atis_quantity"
]

filter_by_labels(allowed_labels=allowed)
