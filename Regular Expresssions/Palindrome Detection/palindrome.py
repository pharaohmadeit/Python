import re
candidates = [
    # Valid
    "racecar", 
    "Kayak",
    "never odd or even",
    "rats live on no evil star",
    "A Toyota! Race fast... safe car: a Toyota",
    "Some men interpret nine memos",
    # Invalid
    "wombat",
    "No lemons, one melon", # lemons, one->lemon, no
    "Too bad – I hid a book", # book->boot
    "No trace; not one cartoon", # cartoon->carton
    "Ma'am, I'm Adam", # Ma'am->Madam
    "Del was a sled", # was->saw
    "Flee to Em, remote elf", # Em->me
    "Ma? Ha! A sham!" # Ha! A sham->Has a ham
]

findpalindrome = {"true": [candidate for candidate in candidates if (cleancandidate := re.sub(r'[ !?,:.\']', '', candidate).lower()) == cleancandidate[::-1]], "false": [candidate for candidate in candidates if not (cleancandidate := re.sub(r'[ !?,:.\']', '', candidate).lower()) == cleancandidate[::-1]]}

[findpalindrome[i] for i in findpalindrome]