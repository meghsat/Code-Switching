def compare_word_counts(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f_in, \
         open(output_file, "r", encoding="utf-8") as f_out:
        
        input_lines = f_in.readlines()
        output_lines = f_out.readlines()
        
        for i, (in_line, out_line) in enumerate(zip(input_lines, output_lines), start=1):
            in_tokens = in_line.strip().split()
            out_tokens = out_line.strip().split()
            
            if len(in_tokens) != len(out_tokens):
                print(f"Line {i} mismatch:")
                print(f"  Input ({len(in_tokens)}): {in_tokens}")
                print(f"  Output({len(out_tokens)}): {out_tokens}")
            # else:
            #     print(f"Line {i}: OK")

# Example usage
compare_word_counts("data/massive/input.txt", "data/massive/bio.txt")
