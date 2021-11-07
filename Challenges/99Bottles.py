# Write a program that will print the song "99 bottles of beer on the wall"


count = 99

while count > 0:
    newcount = count-1
    print(f"{count} bottles of beer on the wall, {count} bottles of beer.\nTake one down and pass it around, {newcount} bottles of beer on the wall.")
    count -= 1
    if count == 0:
        print(f"No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")
