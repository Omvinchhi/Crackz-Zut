import zipfile

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        return

def main():
    zfile = zipfile.ZipFile('protected.zip')
    passFile = open('passlist.txt', 'r', encoding='utf-8')
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extractFile(zfile, password)
        if guess:
            print('Password = ' + password)
            break

if __name__ == '__main__':
    main()