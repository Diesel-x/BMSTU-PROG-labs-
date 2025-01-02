import numpy as np

def generate_grid(size):
    grid = np.zeros((size, size), dtype=int)
    positions = [(i, j) for i in range(size) for j in range(size)]
    np.random.shuffle(positions)
    for i in range(size * size // 4):
        x, y = positions[i]
        grid[x, y] = 1
    return grid

def rotate_grid(grid):
    return np.rot90(grid)

def encrypt(text, grid):
    size = grid.shape[0]
    text = text.ljust(size * size)
    encrypted = np.full((size, size), ' ')
    idx = 0
    for _ in range(4):
        for i in range(size):
            for j in range(size):
                if grid[i, j] == 1:
                    encrypted[i, j] = text[idx]
                    idx += 1
        grid = rotate_grid(grid)
    return ''.join(''.join(row) for row in encrypted)

def decrypt(encrypted_text, grid):
    size = grid.shape[0]
    decrypted = [''] * (size * size)
    idx = 0
    for _ in range(4):
        for i in range(size):
            for j in range(size):
                if grid[i, j] == 1:
                    decrypted[idx] = encrypted_text[i * size + j]
                    idx += 1
        grid = rotate_grid(grid)
    return ''.join(decrypted).strip()

def main():
    text = "Бу, испугался? Не бойся! Я друг! Я тебя не обижу! Иди сюда, иди ко мне, сядь рядом со мной"
    size = 8  # Размер решётки должен быть квадратным числом
    grid = generate_grid(size)
    encrypted_text = encrypt(text, grid)
    decrypted_text = decrypt(encrypted_text, grid)
    print("Original text:", text)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()