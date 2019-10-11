def newFile():
    print('Create new file')

def openFile():
    print('Open file')

def saveFile():
    print('Save file')

def quitApp():
    print('Quit App')
    quit()

def main():
    actions = {
          'n':newFile
        , 'o':openFile
        , 's':saveFile
        , 'q':quitApp
    }

    ch = input('Command (n-new,o-open,s-save,q-quit):')

    if ch in actions:
        actions[ch]()
    else:
        print(f'Unknown command:{ch}')

main()