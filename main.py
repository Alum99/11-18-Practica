from merge import merge_arrays

def main():
    print("-- Тест функции объединения массивов --")
    a = [1, 2, 3]
    b = [4, 5]
    print("Массив 1:", a)
    print("Массив 2:", b)
    result = merge_arrays(a, b)
    print("Объединённый массив:", result)

if __name__ == "__main__":
    main()



