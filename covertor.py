import os

def main(x, y):
    #Folder Path Name
    path = x

    #For Loop to identify all files
    for file in os.walk(path):
        for files in file:
            for singlefile in files:
                name = f'{path}\\"{singlefile}"'
                print(name)
                print(singlefile)
                #Rename File name to y format
                os.system(f'rename {name} "{singlefile}.{y}"')


if __name__ == "__main__":
    #Will execute the main function if The main app is run
    main("C:\\Users\\lit91\\Music\\trial", "png")