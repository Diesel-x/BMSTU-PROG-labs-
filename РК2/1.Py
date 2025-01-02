import os

def main():
    filename = "РК2/in.txt"
    m = 0
    n = 0
    with open(filename, 'r', encoding="utf-8") as file_m:
        for line in file_m:
            if n == 0:
                n = len(line.split())
            m += 1
        file_m.seek(0)
        
        with open("РК2/output.txt", "w", encoding="utf-8") as file_2:
            for col in range(n):
                file_m.seek(0)
                for line in file_m:
                    elements = line.split()
                    file_2.write(elements[col] + " ")
                file_2.write("\n")

if __name__ == "__main__":
    main()