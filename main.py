def main():
    name = input('Enter your name: ')
    print(f'Hello, {name}!')

    characters = set()
    
    for char in name:
        characters.add(char)

if __name__ == '__main__':
    main()
