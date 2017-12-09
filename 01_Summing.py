''' From http://adventofcode.com/2017/day/1

--- Day 1: Inverse Captcha ---

The night before Christmas, one of Santa's Elves calls you in a panic. "The printer's broken! We can't print the Naughty or Nice List!" By the time you make it to sub-basement 17, there are only a few minutes until midnight. "We have a big problem," she says; "there must be almost fifty bugs in this system, but nothing else can print The List. Stand in this square, quick! There's no time to explain; if you can convince them to pay you in stars, you'll be able to--" She pulls a lever and the world goes blurry.

When your eyes can focus again, everything seems a lot more pixelated than before. She must have sent you inside the computer! You check the system clock: 25 milliseconds until midnight. With that much time, you should be able to collect all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day millisecond in the advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You're standing in a room with "digitization quarantine" written in LEDs along one wall. The only door is locked, but it includes a small interface. "Restricted Area - Strictly No Digitized Users Allowed."

It goes on to explain that you may only leave by solving a captcha to prove you're not a human. Apparently, you only get one millisecond to solve the captcha: too fast for a normal human, but it feels like hours to you.

The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.

For example:

    1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
    1111 produces 4 because each digit (all 1) matches the next.
    1234 produces 0 because no digit matches the next.
    91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

What is the solution to your captcha?

Your puzzle answer was 1251.

--- Part Two ---

You notice a progress bar that jumps to 50% completion. Apparently, the door isn't yet satisfied, but it did emit a star as encouragement. The instructions change:

Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.

For example:

    1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
    1221 produces 0, because every comparison is between a 1 and a 2.
    123425 produces 4, because both 2s match each other, but no other digit has a match.
    123123 produces 12.
    12131415 produces 4.

What is the solution to your new captcha?

Your puzzle answer was 1244.
'''

def sum_of_repeats(in_str, offset=1):
    ''' Returns the sum of all numbers
        in the string that have a twin
        <offest> characters to the right
    '''
    sum =0
    for i in range(len(in_str)):
        if in_str[i]==in_str[(i+offset)%len(in_str)]:
            sum += int(in_str[i])
    return sum

# Input supplied by adventofcode
my_input = '5162992814911695127194252761945964242912687126971558636'\
           '5184693792592845695881362442815621846833142385842261347'\
           '1962165756423837756856519754524985759763747559711257977'\
           '3612283576782935726988397544447528988353133998157485625'\
           '1995832992791186165478421635548931999556629749983629598'\
           '5943899373615223375271231128914745273184498915241488393'\
           '7616767999143852654599839237431465554651778864919799624'\
           '6591888839666423369324398396941268256179962878956929437'\
           '4554575677368219724142536789649121758582991345537639888'\
           '8581137637385185111844398542233868687641891339645437219'\
           '4116978627478177565899132933175967994334221757853264351'\
           '9615296424396487669451453728113114748217177826874953466'\
           '4354361291652953791572263457867568999357473367851617454'\
           '8793372152723939411872151719584918667681423288741317558'\
           '7327214144876898248571248517121796766248817366614333915'\
           '1547969836121742812378461651291149884531888447451197986'\
           '4331485787152775783126529884683332786378134155938123845'\
           '8322786192379487455671563757123534253463563421716138641'\
           '6119156862473434171266553173786393141684613456134272627'\
           '8662468949848559994233681399572514516935594261667281279'\
           '2174556866436158375938988738721253664772584577384558696'\
           '4775462321893122872624394521415645223299871396922819847'\
           '8351369185753833553755344891981954533212548312887892549'\
           '2334361562192621672993868479566688564752226111784486619'\
           '7895883181717459952536458868338726654472412453299356438'\
           '8389244752428664229695535424947881511651731583217992549'\
           '4818748478164317669471654464867111924676961162162841232'\
           '4734743947397939686249743979164956672333373972419337655'\
           '1377724191635916699438492386974146817465335354114761664'\
           '5393917694581811193977311981752554551499629219873391493'\
           '4268838865362194558483544264615629952841623239617736445'\
           '8181563377976263474533956519679872484772278166694862623'\
           '1631632144371873154872575615636322965353254642186897127'\
           '4233526188794314991384188723561166248187332324456491887'\
           '9331882974878934981329521867349729113416439573966566725'\
           '5443366383299669973689528188264386373591424149784473698'\
           '4873153166766371653179726489161167552245985199345988896'\
           '27918883283534261513179931798591959489372165295'

print "Part One: " + str(sum_of_repeats(my_input))
print "Part Two: " + str(sum_of_repeats(my_input, offset=len(my_input)/2))
