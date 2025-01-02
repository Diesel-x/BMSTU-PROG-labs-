import re

def convert_base16_to_base8(match):
    num = match.group()
    if '.' in num:
        int_part, frac_part = num.split('.')
        int_dec = int(int_part, 16)
        frac_dec = int(frac_part, 16) / (16 ** len(frac_part))
        dec = int_dec + frac_dec
        int_octal = oct(int_dec)[2:]
        frac_octal = ''
        frac = frac_dec
        for _ in range(6):
            frac *= 8
            digit = int(frac)
            frac_octal += str(digit)
            frac -= digit
        return f"{int_octal}.{frac_octal}"
    else:
        return oct(int(num, 16))[2:]

pattern = re.compile(r'\b[0-9A-Fa-f]+\.[0-9A-Fa-f]+\b|\b[0-9A-Fa-f]+\b')

with open('in.txt', 'r', encoding='utf-8') as infile, open('out.txt', 'w', encoding='utf-8') as outfile:
    for line in infile:
        sentences = line.strip().split('.')
        for sentence in sentences:
            if sentence:
                converted = pattern.sub(convert_base16_to_base8, sentence)
                outfile.write(converted.strip() + '.\n')