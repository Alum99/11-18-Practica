from reverse_num import reverse_number

def main():
    print("-- Тест переворота чисел --")
    nums = [123, 450, 9001, 70007]
    for n in nums:
        print(f"{n} → {reverse_number(n)}")

if __name__ == "__main__":
    main()
