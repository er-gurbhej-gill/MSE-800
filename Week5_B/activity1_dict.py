def main():
    keys = ['a', 'b', 'c', 'd']
    values = [1, 2, 3]
    dictionary={k:v for k, v in zip(keys, values)} 
    print(dictionary)

if __name__ == "__main__":
    main()