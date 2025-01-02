import struct
import os

def main():
    input_file = "РК2/numbers.bin"
    output_file = "РК2/transformed_numbers.bin"
    long_size = 8 
    size = os.path.getsize(input_file)
    num_c = size // long_size 
    half = num_c // 2

    with open(input_file, "rb") as fin, open(output_file, "wb") as fut:
        fin.seek(half * long_size)
        for _ in range(half):
            fut.write(fin.read(long_size))

        for i in range(half - 1, -1, -1):
            fin.seek(i * long_size)
            data = fin.read(long_size)
            fut.write(data)

        #Вывод
        with open(output_file, "rb") as fout:
            while True:
                data = fout.read(long_size)
                if not data:
                    break
                number = struct.unpack('q', data)[0]
                print(number)
if __name__ == "__main__":
    main()

# for _ in range(half):
#     data = fin.read(long_size)
#     number = struct.unpack('q', data)[0]
#     packed_data = struct.pack('q', number)
#     fout.write(packed_data)