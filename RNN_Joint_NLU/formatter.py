input_path = "data/Massive/train/input.txt"
output_path = "data/Massive/train/output.txt"
label_path = "data/Massive/train/label.txt"
combined_path = "data/Massive/train/Massive.test.w-intent.iob"

with open(input_path, "r", encoding="utf-8") as f_in, \
     open(output_path, "r", encoding="utf-8") as f_out, \
     open(label_path, "r", encoding="utf-8") as f_label, \
     open(combined_path, "w", encoding="utf-8") as f_combined:

    input_lines = f_in.readlines()
    output_lines = f_out.readlines()
    label_lines = f_label.readlines()

    assert len(input_lines) == len(output_lines) == len(label_lines), "Mismatch in number of lines!"

    for inp, outp, label in zip(input_lines, output_lines, label_lines):
        inp = inp.strip()
        outp = outp.strip()
        label = label.strip()

        formatted_line = f"BOS {inp} EOS\t{outp} {label}\n"
        f_combined.write(formatted_line)

print("✅ File created successfully")
