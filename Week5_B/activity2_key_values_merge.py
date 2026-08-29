def main():

    Key1 = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'e', 'a']
    Value1 = [20, 3, 1, 88, 55, 92, 6, 90, 910]
    Key2 = ['u', 'b', 'o', 'x',  'e', 'a']
    Value2 = [200, 30, 10, 88, 55, 920]
    dictionary={k:v for k, v in zip(Key1, Value1)
                if v%2 == 1}
 
    print(dictionary)

if __name__ == "__main__":
    main()