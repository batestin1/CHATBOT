import random

data = {
    "questions": {
        "1": "I'm the dark forest where Legolas and Gimli meet the Army of the Dead. Aragorn seeks help from me. What am I?",
        "2": "I'm a powerful tree, one of the two remaining in Middle-earth. My bark can heal wounds. What am I?",
        "3": "I'm a river that borders the land of Gondor. I'm known for my rapid waters and treacherous course. What am I?",
        "4": "I'm the fearsome dragon who once ruled over Erebor. My love for gold brought me to ruin. What am I?",
        "5": "I'm the elven city hidden in the woods, protected by a magical barrier. Arwen lived here for a time. What am I?",
        "6": "I'm the ring that binds the Nine, created for mortal men. My power comes at a great cost. What am I?",
        "7": "Alive without breath, As cold as death; Never thirsty, ever drinking, All in mail never clinking. What am I?",
        "8": "Voiceless it cries, Wingless flutters, Toothless bites, Mouthless mutters. Who am I?",
        "9": "This thing all things devours; Birds, beasts, trees, flowers; Gnaws iron, bites steel; Grinds hard stones to meal; Slays king, ruins town, And beats high mountain down. Who am I?",
        "10": "The more you take, the more you leave behind. Who am I? ",
        "11": "It cannot be seen, cannot be felt, Cannot be heard, cannot be smelt. It lies behind stars and under hills, And empty holes it fills. It comes first and follows after, Ends life, kills laughter. Who am I? ",
        "12": "A box without hinges, key, or lid, Yet golden treasure inside is hid. Who am I?",
        "13": "It's light as a feather, yet the strongest man can't hold it for much longer than a minute. Who am I? ",
        "14": "An eye in a blue face Saw an eye in a green face. 'That eye is like to this eye' Said the first eye, 'But in low place, Not in high place.'",
        "15": "Voiceless it cries, Wingless flutters, Toothless bites, Mouthless mutters. Who am I? ",
        "16": "Alive as you but without breath, As cold in my life as in my death; Never a thirst though I always drink, Dressed in mail but never a clink. Who am I?",
        "17": "A box without hinges, key, or lid, Yet golden treasure inside is hid. Who am I?",
        "18": "I'm the ancient realm of the High Elves, located across the sea from Middle-earth. What am I?",
    "19": "I'm a hobbit who played a crucial role in destroying the One Ring. I'm known for my love of potatoes. Who am I?",
    "20": "I'm the fortress city at the edge of Mordor, where Frodo and Sam observed the armies of Sauron. What am I?",
    "21": "I'm the powerful being also known as Gandalf the Grey. I help guide and advise the Fellowship of the Ring. What am I now?",
    "22": "I'm the capital of Rohan, known for its impressive horsemen and strong defenses. What city am I?",
    "23": "I'm the son of Thranduil, the Elvenking, and a skilled warrior. I form a close friendship with Legolas. Who am I?",
    "24": "I'm the deadly spider in the heart of Mirkwood, known for capturing Bilbo and the dwarves. What am I?",
    "25": "I'm a powerful artifact created by Sauron to control the other Rings of Power. What am I?",
    "26": "I'm the giant eagles that come to the aid of Frodo and Sam multiple times during their journey. What are we called?",
    "27": "I'm the evil sorcerer who serves Sauron and is responsible for capturing Gandalf. Who am I?",
    "28": "I'm the river that flows through the heart of Lothlórien. What am I?",
    "29": "I'm the king of Gondor who led the defense of Minas Tirith during the War of the Ring. Who am I?",
    "30": "I'm the fortress of Sauron, located in the heart of Mordor. What am I?",
    "31": "I'm the son of Denethor II, the Steward of Gondor, and the brother of Boromir. Who am I?",
    "32": "I'm the ancient, corrupted forest at the borders of the Shire, where Old Man Willow resides. What am I?",
    "33": "I'm the sword reforged from the shards of Narsil. Aragorn wields me in his quest to reclaim the throne of Gondor. What am I called?",
    "34": "I'm the Black Rider who relentlessly pursues Frodo and the One Ring. What am I?",
    "35": "I'm the magical, invisibility-granting object that Bilbo finds in Gollum's cave. What am I?",
    "36": "I'm the dwarf who is a skilled craftsman and one of the members of Thorin's company. I have a love for gold and jewels. Who am I?",
    "37": "I'm the beautiful elf maiden who falls in love with Aragorn. Who am I?",
    "38": "I'm the captain of the Ringwraiths and Sauron's most feared servant. What's my name?",
    "39": "I'm the ancient, hidden city of the dwarves that Bilbo and the company discover beneath the Lonely Mountain. What am I?",
    "40": "I'm the river that forms the eastern border of Gondor. What's my name?",
    "41": "I'm the name of Samwise Gamgee's daughter. What's my name?",
    "42": "I'm the hobbit who becomes the heir of Bilbo's estate and accompanies Frodo on his journey to Rivendell. Who am I?",
    "43": "I'm the villainous creature who is completely consumed by the One Ring. I was once known as Sméagol. What's my name?",
    "44": "I'm the tall stone statues that guard the northern borders of Gondor. What are we called?",
    "45": "I'm the land of the Ents, where the ancient tree-like beings reside. What is my name?",
    "46": "I'm the daughter of Elrond and one of the members of the Fellowship of the Ring. Who am I?",
    "47": "I'm the weapon created by Sauron to help him conquer Middle-earth. I was shattered by Isildur. What am I called?",
    "48": "I'm the Shire's main settlement, where Bilbo and Frodo come from. What am I called?",
    "49": "I'm the eerie, underground realm of the dwarves, filled with dark tunnels and dangerous creatures. What am I?",
    "50": "I'm the treacherous mountain pass that the Fellowship attempts to cross in the first book of 'The Lord of the Rings'. What am I?"

    },
    "answers": {
        "1": "Paths of the Dead",
        "2": "White Tree of Gondor",
        "3": "Great River Anduin",
        "4": "Smaug",
        "5": "Lothlórien",
        "6": "Nine Rings for Mortal Men",
        "7": "Fish",
        "8": "Wind",
        "9": "Time",
        "10": "Footsteps",
        "11": "Dark",
        "12": "Egg",
        "13": "Breath",
        "14": "Sun looking at a daisy",
        "15": "Wind",
        "16": "Fish",
        "17": "Egg",
        "18": "Valinor",
    "19": "Samwise Gamgee",
    "20": "Minas Morgul",
    "21": "Gandalf the White",
    "22": "Edoras",
    "23": "Legolas",
    "24": "Shelob",
    "25": "One Ring",
    "26": "Great Eagles",
    "27": "Saruman",
    "28": "Celeborn",
    "29": "Aragorn",
    "30": "Barad-dûr",
    "31": "Faramir",
    "32": "Old Forest",
    "33": "Andúril",
    "34": "Nazgûl",
    "35": "One Ring",
    "36": "Gimli",
    "37": "Arwen",
    "38": "Witch-king of Angmar",
    "39": "Erebor",
    "40": "Anduin",
    "41": "Elanor",
    "42": "Frodo Baggins",
    "43": "Gollum",
    "44": "Argonath",
    "45": "Fangorn Forest",
    "46": "Arwen",
    "47": "Sauron's Mace",
    "48": "Hobbiton",
    "49": "Moria",
    "50": "Redhorn Pass"
    }
}

def main(dict):
    start_message = dict["message"]
    random_question_number = random.choice(list(data["questions"].keys()))
    random_question = data["questions"][random_question_number]
    correct_answer = data["answers"][random_question_number]
    
    incorrect_answers = [ans for ans in data["answers"].values() if ans != correct_answer]
    random_incorrect_answer = random.choice(incorrect_answers)
    wrong_2 = random.choice(incorrect_answers)
    wrong_3 = random.choice(incorrect_answers)
    
    return {
        "message": start_message,
        "question": random_question,
        "correct": correct_answer,
        "wrong": random_incorrect_answer,
        "wrong_2": wrong_2,
        "wrong_3": wrong_3
    }
