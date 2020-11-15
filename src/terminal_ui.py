from calculate import *

def welcome_screen():
    print('    .           ..         .           .       .           .           .')
    print('      .         .            .          .       .')
    print('            .         ..xxxxxxxxxx....               .       .             .')
    print('    .             MWMWMWWMWMWMWMWMWMWMWMWMW                       .')
    print('              IIIIMWMWMWMWMWMWMWMWMWMWMWMWMWMttii:        .           .')
    print(' .      IIYVVXMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWxx...         .           .')
    print('     IWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMx..')
    print('   IIWMWMWMWMWMWMWMWMWBY%ZACH%AND%OWENMWMWMWMWMWMWMWMWMWMWMWMWMx..        .')
    print('    \"\"MWMWMWMWMWM\"\"\"\"\"\"\"\".  .:..   .\"\"\"\"\"MWMWMWMWMWMWMWMWMWMWMWMWMWti.')
    print(' .     \"\"   . `  .: . :. : .  . :.  .  . . .  \"\"\"\"MWMWMWMWMWMWMWMWMWMWMWMWMti=')
    print('        . .   :` . :   .  .\'.\' \'....xxxxx...,\'. \'   \' .\"\"\"YWMWMWMWMWMWMWMWMWMW+')
    print('     ; . ` .  . : . .\' :  . ..XXXXXXXXXXXXXXXXXXXXx.    `     . \"YWMWMWMWMWMWMW')
    print('.    .  .  .    . .   .  ..XXXXXXXX   -----------  `.  .     .     \"\"\"\"\"\"\"')
    print('        \' :  : . : .  ...XXXXXWWW\"   W88N88@888888W    XX.   .   .       . .')
    print('   . \' .    . :   ...XXXXXXWWW\"    M8              8M  WMBX.          .   ..  :')
    print('         :     ..XXXXXXXXWWW\"     M88               8M   WWMX.     .    :    .')
    print('           \"XXXXXXXXXXXXWW\"       WN8888WWWWWWW8@@@8M    BMBRX.         .  : :')
    print('  .       XXXXXXXX=MMWW\":  .      W8N                       XRBRXX.  .       .')
    print('     ....  \"\"XXXXXMM::::. .        W8@                     . . :RRXx.    .')
    print('         ``...\'\'\'  MMM::.:.  .      W88                   . . ::::\"RXV    .  :')
    print(' .       ..\'\'\'\'\'      MMMm::.  .      WW888N88888WW     .  . mmMMMMMRXx')
    print('      ..\' .            \"\"MMmm .  .       WWWWWWW   . :. :,miMM\"\"\"  : \"\"`    .')
    print('   .                .       \"\"MMMMmm . .  .  .   ._,mMMMM\"\"\"  :  \' .  :')
    print('               .                  \"\"MMMMMMMMMMMMM\"\"\" .  : . \'   .        .')
    print('          .              .     .    .                      .         .')
    print('.                                         .          .         .')

    print('='*100)
    print('=\n=  Destiny 2 Light Leveling Help')
    print('=  Copyright Sēēk Inc.')
    print('=')
    print('='*100)
    print()

def get_gear_level():
    gear_names = ['Primary: ','Secondary: ','Heavy: ','Helmet: ','Arms: ','Chest: ','Legs: ','Class Item: ']
    gear = []

    for prompt in gear_names:
        while True:
            entered = input(prompt)
            if entered.isdigit() and int(entered) > 0:
                gear.append(int(entered))
                break
    
    return gear
    
def print_result(current, even):
    print('\n++++++++++++++++++++++++++++++++++')
    print('+                                +')
    print('+  Current Light: {:.2f}        +'.format(current))
    print('+  Evened Out Light: {:.2f}     +'.format(even))
    print('+                                +')
    print('+  {}       +'.format('You SHOULD NOT even out' if math.floor(even) == math.floor(current) else 'You SHOULD even out    '))
    print('++++++++++++++++++++++++++++++++++')

def main():
    welcome_screen()

    while True:
        gear_dict = create_dictionary(get_gear_level())
        current = current_light(gear_dict)
        even = even_out(gear_dict)

        print_result(current, even)

        entered = input('\nEnter again? (Y/N): ')

        if entered.lower() == 'n':
            quit()

if __name__ == '__main__':
    """Calls the main definition"""
    main()