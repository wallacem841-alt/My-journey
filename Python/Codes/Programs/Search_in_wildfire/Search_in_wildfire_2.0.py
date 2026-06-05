with open("C:\\Users\\Usuario\\Desktop\\Wallace\\Study\\Programing\\Python\\Programs\\Wildfire_lyrics.txt", "r") as WFLF:
    WFL = WFLF.read().lower()

Search = input("Search in Wildfire: ").lower()

if Search in WFL:
    print(Search, "is in Wildfire")

if Search not in WFL:
    print(Search, "is not in Wildfire")

input('Press enter to exit...')