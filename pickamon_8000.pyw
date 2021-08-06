import random
import tkinter as tk
from webbrowser import open_new_tab

gen_1_mons = {1: "Bulbasaur", 2: "Ivysaur", 3: "Venusaur", 4: "Charmander", 5: "Charmeleon", 6: "Charizard", 7: "Squirtle", 8: "Wartortle", 9: "Blastoise", 10: "Caterpie", 11: "Metapod", 12: "Butterfree", 13: "Weedle", 14: "Kakuna", 15: "Beedrill", 16: "Pidgey", 17: "Pidgeotto", 18: "Pidgeot", 19: "Rattata", 20: "Raticate", 21: "Spearow", 22: "Fearow", 23: "Ekans", 24: "Arbok", 25: "Pikachu", 26: "Raichu", 27: "Sandshrew", 28: "Sandslash", 29: "Nidoran♀", 30: "Nidorina", 31: "Nidoqueen", 32: "Nidoran♂", 33: "Nidorino", 34: "Nidoking", 35: "Clefairy", 36: "Clefable", 37: "Vulpix", 38: "Ninetales", 39: "Jigglypuff", 40: "Wigglytuff", 41: "Zubat", 42: "Golbat", 43: "Oddish", 44: "Gloom", 45: "Vileplume", 46: "Paras", 47: "Parasect", 48: "Venonat", 49: "Venomoth", 50: "Diglett", 51: "Dugtrio", 52: "Meowth", 53: "Persian", 54: "Psyduck", 55: "Golduck", 56: "Mankey", 57: "Primeape", 58: "Growlithe", 59: "Arcanine", 60: "Poliwag", 61: "Poliwhirl", 62: "Poliwrath", 63: "Abra", 64: "Kadabra", 65: "Alakazam", 66: "Machop", 67: "Machoke", 68: "Machamp", 69: "Bellsprout", 70: "Weepinbell", 71: "Victreebel", 72: "Tentacool", 73: "Tentacruel", 74: "Geodude", 75: "Graveler", 76: "Golem", 77: "Ponyta", 78: "Rapidash", 79: "Slowpoke", 80: "Slowbro", 81: "Magnemite", 82: "Magneton", 83: "Farfetch\'d", 84: "Doduo", 85: "Dodrio", 86: "Seel", 87: "Dewgong", 88: "Grimer", 89: "Muk", 90: "Shellder", 91: "Cloyster", 92: "Gastly", 93: "Haunter", 94: "Gengar", 95: "Onix", 96: "Drowzee", 97: "Hypno", 98: "Krabby", 99: "Kingler", 100: "Voltorb", 101: "Electrode", 102: "Exeggcute", 103: "Exeggutor", 104: "Cubone", 105: "Marowak", 106: "Hitmonlee", 107: "Hitmonchan", 108: "Lickitung", 109: "Koffing", 110: "Weezing", 111: "Rhyhorn", 112: "Rhydon", 113: "Chansey", 114: "Tangela", 115: "Kangaskhan", 116: "Horsea", 117: "Seadra", 118: "Goldeen", 119: "Seaking", 120: "Staryu", 121: "Starmie", 122: "Mr.Mime", 123: "Scyther", 124: "Jynx", 125: "Electabuzz", 126: "Magmar", 127: "Pinsir", 128: "Tauros", 129: "Magikarp", 130: "Gyarados", 131: "Lapras", 132: "Ditto", 133: "Eevee", 134: "Vaporeon", 135: "Jolteon", 136: "Flareon", 137: "Porygon", 138: "Omanyte", 139: "Omastar", 140: "Kabuto", 141: "Kabutops", 142: "Aerodactyl", 143: "Snorlax", 144: "Articuno", 145: "Zapdos", 146: "Moltres", 147: "Dratini", 148: "Dragonair", 149: "Dragonite", 150: "Mewtwo", 151: "Mew"}
gen_2_mons = {152: "Chikorita", 153: "Bayleef", 154: "Meganium", 155: "Cyndaquil", 156: "Quilava", 157: "Typhlosion", 158: "Totodile", 159: "Croconaw", 160: "Feraligatr", 161: "Sentret", 162: "Furret", 163: "Hoothoot", 164: "Noctowl", 165: "Ledyba", 166: "Ledian", 167: "Spinarak", 168: "Ariados", 169: "Crobat", 170: "Chinchou", 171: "Lanturn", 172: "Pichu", 173: "Cleffa", 174: "Igglybuff", 175: "Togepi", 176: "Togetic", 177: "Natu", 178: "Xatu", 179: "Mareep", 180: "Flaaffy", 181: "Ampharos", 182: "Bellossom", 183: "Marill", 184: "Azumarill", 185: "Sudowoodo", 186: "Politoed", 187: "Hoppip", 188: "Skiploom", 189: "Jumpluff", 190: "Aipom", 191: "Sunkern", 192: "Sunflora", 193: "Yanma", 194: "Wooper", 195: "Quagsire", 196: "Espeon", 197: "Umbreon", 198: "Murkrow", 199: "Slowking", 200: "Misdreavus", 201: "Unown", 202: "Wobbuffet", 203: "Girafarig", 204: "Pineco", 205: "Forretress", 206: "Dunsparce", 207: "Gligar", 208: "Steelix", 209: "Snubbull", 210: "Granbull", 211: "Qwilfish", 212: "Scizor", 213: "Shuckle", 214: "Heracross", 215: "Sneasel", 216: "Teddiursa", 217: "Ursaring", 218: "Slugma", 219: "Magcargo", 220: "Swinub", 221: "Piloswine", 222: "Corsola", 223: "Remoraid", 224: "Octillery", 225: "Delibird", 226: "Mantine", 227: "Skarmory", 228: "Houndour", 229: "Houndoom", 230: "Kingdra", 231: "Phanpy", 232: "Donphan", 233: "Porygon2", 234: "Stantler", 235: "Smeargle", 236: "Tyrogue", 237: "Hitmontop", 238: "Smoochum", 239: "Elekid", 240: "Magby", 241: "Miltank", 242: "Blissey", 243: "Raikou", 244: "Entei", 245: "Suicune", 246: "Larvitar", 247: "Pupitar", 248: "Tyranitar", 249: "Lugia", 250: "Ho-Oh", 251: "Celebi"}
gen_3_mons = {252: "Treecko", 253: "Grovyle", 254: "Sceptile", 255: "Torchic", 256: "Combusken", 257: "Blaziken", 258: "Mudkip", 259: "Marshtomp", 260: "Swampert", 261: "Poochyena", 262: "Mightyena", 263: "Zigzagoon", 264: "Linoone", 265: "Wurmple", 266: "Silcoon", 267: "Beautifly", 268: "Cascoon", 269: "Dustox", 270: "Lotad", 271: "Lombre", 272: "Ludicolo", 273: "Seedot", 274: "Nuzleaf", 275: "Shiftry", 276: "Taillow", 277: "Swellow", 278: "Wingull", 279: "Pelipper", 280: "Ralts", 281: "Kirlia", 282: "Gardevoir", 283: "Surskit", 284: "Masquerain", 285: "Shroomish", 286: "Breloom", 287: "Slakoth", 288: "Vigoroth", 289: "Slaking", 290: "Nincada", 291: "Ninjask", 292: "Shedinja", 293: "Whismur", 294: "Loudred", 295: "Exploud", 296: "Makuhita", 297: "Hariyama", 298: "Azurill", 299: "Nosepass", 300: "Skitty", 301: "Delcatty", 302: "Sableye", 303: "Mawile", 304: "Aron", 305: "Lairon", 306: "Aggron", 307: "Meditite", 308: "Medicham", 309: "Electrike", 310: "Manectric", 311: "Plusle", 312: "Minun", 313: "Volbeat", 314: "Illumise", 315: "Roselia", 316: "Gulpin", 317: "Swalot", 318: "Carvanha", 319: "Sharpedo", 320: "Wailmer", 321: "Wailord", 322: "Numel", 323: "Camerupt", 324: "Torkoal", 325: "Spoink", 326: "Grumpig", 327: "Spinda", 328: "Trapinch", 329: "Vibrava", 330: "Flygon", 331: "Cacnea", 332: "Cacturne", 333: "Swablu", 334: "Altaria", 335: "Zangoose", 336: "Seviper", 337: "Lunatone", 338: "Solrock", 339: "Barboach", 340: "Whiscash", 341: "Corphish", 342: "Crawdaunt", 343: "Baltoy", 344: "Claydol", 345: "Lileep", 346: "Cradily", 347: "Anorith", 348: "Armaldo", 349: "Feebas", 350: "Milotic", 351: "Castform", 352: "Kecleon", 353: "Shuppet", 354: "Banette", 355: "Duskull", 356: "Dusclops", 357: "Tropius", 358: "Chimecho", 359: "Absol", 360: "Wynaut", 361: "Snorunt", 362: "Glalie", 363: "Spheal", 364: "Sealeo", 365: "Walrein", 366: "Clamperl", 367: "Huntail", 368: "Gorebyss", 369: "Relicanth", 370: "Luvdisc", 371: "Bagon", 372: "Shelgon", 373: "Salamence", 374: "Beldum", 375: "Metang", 376: "Metagross", 377: "Regirock", 378: "Regice", 379: "Registeel", 380: "Latias", 381: "Latios", 382: "Kyogre", 383: "Groudon", 384: "Rayquaza", 385: "Jirachi", 386: "Deoxys"}
gen_4_mons = {387: "Turtwig", 388: "Grotle", 389: "Torterra", 390: "Chimchar", 391: "Monferno", 392: "Infernape", 393: "Piplup", 394: "Prinplup", 395: "Empoleon", 396: "Starly", 397: "Staravia", 398: "Staraptor", 399: "Bidoof", 400: "Bibarel", 401: "Kricketot", 402: "Kricketune", 403: "Shinx", 404: "Luxio", 405: "Luxray", 406: "Budew", 407: "Roserade", 408: "Cranidos", 409: "Rampardos", 410: "Shieldon", 411: "Bastiodon", 412: "Burmy", 413: "Wormadam", 414: "Mothim", 415: "Combee", 416: "Vespiquen", 417: "Pachirisu", 418: "Buizel", 419: "Floatzel", 420: "Cherubi", 421: "Cherrim", 422: "Shellos", 423: "Gastrodon", 424: "Ambipom", 425: "Drifloon", 426: "Drifblim", 427: "Buneary", 428: "Lopunny", 429: "Mismagius", 430: "Honchkrow", 431: "Glameow", 432: "Purugly", 433: "Chingling", 434: "Stunky", 435: "Skuntank", 436: "Bronzor", 437: "Bronzong", 438: "Bonsly", 439: "MimeJr.", 440: "Happiny", 441: "Chatot", 442: "Spiritomb", 443: "Gible", 444: "Gabite", 445: "Garchomp", 446: "Munchlax", 447: "Riolu", 448: "Lucario", 449: "Hippopotas", 450: "Hippowdon", 451: "Skorupi", 452: "Drapion", 453: "Croagunk", 454: "Toxicroak", 455: "Carnivine", 456: "Finneon", 457: "Lumineon", 458: "Mantyke", 459: "Snover", 460: "Abomasnow", 461: "Weavile", 462: "Magnezone", 463: "Lickilicky", 464: "Rhyperior", 465: "Tangrowth", 466: "Electivire", 467: "Magmortar", 468: "Togekiss", 469: "Yanmega", 470: "Leafeon", 471: "Glaceon", 472: "Gliscor", 473: "Mamoswine", 474: "Porygon-Z", 475: "Gallade", 476: "Probopass", 477: "Dusknoir", 478: "Froslass", 479: "Rotom", 480: "Uxie", 481: "Mesprit", 482: "Azelf", 483: "Dialga", 484: "Palkia", 485: "Heatran", 486: "Regigigas", 487: "Giratina", 488: "Cresselia", 489: "Phione", 490: "Manaphy", 491: "Darkrai", 492: "Shaymin", 493: "Arceus"}
gen_5_mons = {494: "Victini", 495: "Snivy", 496: "Servine", 497: "Serperior", 498: "Tepig", 499: "Pignite", 500: "Emboar", 501: "Oshawott", 502: "Dewott", 503: "Samurott", 504: "Patrat", 505: "Watchog", 506: "Lillipup", 507: "Herdier", 508: "Stoutland", 509: "Purrloin", 510: "Liepard", 511: "Pansage", 512: "Simisage", 513: "Pansear", 514: "Simisear", 515: "Panpour", 516: "Simipour", 517: "Munna", 518: "Musharna", 519: "Pidove", 520: "Tranquill", 521: "Unfezant", 522: "Blitzle", 523: "Zebstrika", 524: "Roggenrola", 525: "Boldore", 526: "Gigalith", 527: "Woobat", 528: "Swoobat", 529: "Drilbur", 530: "Excadrill", 531: "Audino", 532: "Timburr", 533: "Gurdurr", 534: "Conkeldurr", 535: "Tympole", 536: "Palpitoad", 537: "Seismitoad", 538: "Throh", 539: "Sawk", 540: "Sewaddle", 541: "Swadloon", 542: "Leavanny", 543: "Venipede", 544: "Whirlipede", 545: "Scolipede", 546: "Cottonee", 547: "Whimsicott", 548: "Petilil", 549: "Lilligant", 550: "Basculin", 551: "Sandile", 552: "Krokorok", 553: "Krookodile", 554: "Darumaka", 555: "Darmanitan", 556: "Maractus", 557: "Dwebble", 558: "Crustle", 559: "Scraggy", 560: "Scrafty", 561: "Sigilyph", 562: "Yamask", 563: "Cofagrigus", 564: "Tirtouga", 565: "Carracosta", 566: "Archen", 567: "Archeops", 568: "Trubbish", 569: "Garbodor", 570: "Zorua", 571: "Zoroark", 572: "Minccino", 573: "Cinccino", 574: "Gothita", 575: "Gothorita", 576: "Gothitelle", 577: "Solosis", 578: "Duosion", 579: "Reuniclus", 580: "Ducklett", 581: "Swanna", 582: "Vanillite", 583: "Vanillish", 584: "Vanilluxe", 585: "Deerling", 586: "Sawsbuck", 587: "Emolga", 588: "Karrablast", 589: "Escavalier", 590: "Foongus", 591: "Amoonguss", 592: "Frillish", 593: "Jellicent", 594: "Alomomola", 595: "Joltik", 596: "Galvantula", 597: "Ferroseed", 598: "Ferrothorn", 599: "Klink", 600: "Klang", 601: "Klinklang", 602: "Tynamo", 603: "Eelektrik", 604: "Eelektross", 605: "Elgyem", 606: "Beheeyem", 607: "Litwick", 608: "Lampent", 609: "Chandelure", 610: "Axew", 611: "Fraxure", 612: "Haxorus", 613: "Cubchoo", 614: "Beartic", 615: "Cryogonal", 616: "Shelmet", 617: "Accelgor", 618: "Stunfisk", 619: "Mienfoo", 620: "Mienshao", 621: "Druddigon", 622: "Golett", 623: "Golurk", 624: "Pawniard", 625: "Bisharp", 626: "Bouffalant", 627: "Rufflet", 628: "Braviary", 629: "Vullaby", 630: "Mandibuzz", 631: "Heatmor", 632: "Durant", 633: "Deino", 634: "Zweilous", 635: "Hydreigon", 636: "Larvesta", 637: "Volcarona", 638: "Cobalion", 639: "Terrakion", 640: "Virizion", 641: "Tornadus", 642: "Thundurus", 643: "Reshiram", 644: "Zekrom", 645: "Landorus", 646: "Kyurem", 647: "Keldeo", 648: "Meloetta", 649: "Genesect"}
gen_6_mons = {650: "Chespin", 651: "Quilladin", 652: "Chesnaught", 653: "Fennekin", 654: "Braixen", 655: "Delphox", 656: "Froakie", 657: "Frogadier", 658: "Greninja", 659: "Bunnelby", 660: "Diggersby", 661: "Fletchling", 662: "Fletchinder", 663: "Talonflame", 664: "Scatterbug", 665: "Spewpa", 666: "Vivillon", 667: "Litleo", 668: "Pyroar", 669: "Flabébé", 670: "Floette", 671: "Florges", 672: "Skiddo", 673: "Gogoat", 674: "Pancham", 675: "Pangoro", 676: "Furfrou", 677: "Espurr", 678: "Meowstic", 679: "Honedge", 680: "Doublade", 681: "Aegislash", 682: "Spritzee", 683: "Aromatisse", 684: "Swirlix", 685: "Slurpuff", 686: "Inkay", 687: "Malamar", 688: "Binacle", 689: "Barbaracle", 690: "Skrelp", 691: "Dragalge", 692: "Clauncher", 693: "Clawitzer", 694: "Helioptile", 695: "Heliolisk", 696: "Tyrunt", 697: "Tyrantrum", 698: "Amaura", 699: "Aurorus", 700: "Sylveon", 701: "Hawlucha", 702: "Dedenne", 703: "Carbink", 704: "Goomy", 705: "Sliggoo", 706: "Goodra", 707: "Klefki", 708: "Phantump", 709: "Trevenant", 710: "Pumpkaboo", 711: "Gourgeist", 712: "Bergmite", 713: "Avalugg", 714: "Noibat", 715: "Noivern", 716: "Xerneas", 717: "Yveltal", 718: "Zygarde", 719: "Diancie", 720: "Hoopa", 721: "Volcanion"}
gen_7_mons = {722: "Rowlet", 723: "Dartrix", 724: "Decidueye", 725: "Litten", 726: "Torracat", 727: "Incineroar", 728: "Popplio", 729: "Brionne", 730: "Primarina", 731: "Pikipek", 732: "Trumbeak", 733: "Toucannon", 734: "Yungoos", 735: "Gumshoos", 736: "Grubbin", 737: "Charjabug", 738: "Vikavolt", 739: "Crabrawler", 740: "Crabominable", 741: "Oricorio", 742: "Cutiefly", 743: "Ribombee", 744: "Rockruff", 745: "Lycanroc", 746: "Wishiwashi", 747: "Mareanie", 748: "Toxapex", 749: "Mudbray", 750: "Mudsdale", 751: "Dewpider", 752: "Araquanid", 753: "Fomantis", 754: "Lurantis", 755: "Morelull", 756: "Shiinotic", 757: "Salandit", 758: "Salazzle", 759: "Stufful", 760: "Bewear", 761: "Bounsweet", 762: "Steenee", 763: "Tsareena", 764: "Comfey", 765: "Oranguru", 766: "Passimian", 767: "Wimpod", 768: "Golisopod", 769: "Sandygast", 770: "Palossand", 771: "Pyukumuku", 772: "Type:Null", 773: "Silvally", 774: "Minior", 775: "Komala", 776: "Turtonator", 777: "Togedemaru", 778: "Mimikyu", 779: "Bruxish", 780: "Drampa", 781: "Dhelmise", 782: "Jangmo-o", 783: "Hakamo-o", 784: "Kommo-o", 785: "TapuKoko", 786: "TapuLele", 787: "TapuBulu", 788: "TapuFini", 789: "Cosmog", 790: "Cosmoem", 791: "Solgaleo", 792: "Lunala", 793: "Nihilego", 794: "Buzzwole", 795: "Pheromosa", 796: "Xurkitree", 797: "Celesteela", 798: "Kartana", 799: "Guzzlord", 800: "Necrozma", 801: "Magearna", 802: "Marshadow", 803: "Poipole", 804: "Naganadel", 805: "Stakataka", 806: "Blacephalon", 807: "Zeraora", 808: "Meltan", 809: "Melmetal"}
gen_8_mons = {810: "Grookey", 811: "Thwackey", 812: "Rillaboom", 813: "Scorbunny", 814: "Raboot", 815: "Cinderace", 816: "Sobble", 817: "Drizzile", 818: "Inteleon", 819: "Skwovet", 820: "Greedent", 821: "Rookidee", 822: "Corvisquire", 823: "Corviknight", 824: "Blipbug", 825: "Dottler", 826: "Orbeetle", 827: "Nickit", 828: "Thievul", 829: "Gossifleur", 830: "Eldegoss", 831: "Wooloo", 832: "Dubwool", 833: "Chewtle", 834: "Drednaw", 835: "Yamper", 836: "Boltund", 837: "Rolycoly", 838: "Carkol", 839: "Coalossal", 840: "Applin", 841: "Flapple", 842: "Appletun", 843: "Silicobra", 844: "Sandaconda", 845: "Cramorant", 846: "Arrokuda", 847: "Barraskewda", 848: "Toxel", 849: "Toxtricity", 850: "Sizzlipede", 851: "Centiskorch", 852: "Clobbopus", 853: "Grapploct", 854: "Sinistea", 855: "Polteageist", 856: "Hatenna", 857: "Hattrem", 858: "Hatterene", 859: "Impidimp", 860: "Morgrem", 861: "Grimmsnarl", 862: "Obstagoon", 863: "Perrserker", 864: "Cursola", 865: "Sirfetch\'d", 866: "Mr.Rime", 867: "Runerigus", 868: "Milcery", 869: "Alcremie", 870: "Falinks", 871: "Pincurchin", 872: "Snom", 873: "Frosmoth", 874: "Stonjourner", 875: "Eiscue", 876: "Indeedee", 877: "Morpeko", 878: "Cufant", 879: "Copperajah", 880: "Dracozolt", 881: "Arctozolt", 882: "Dracovish", 883: "Arctovish", 884: "Duraludon", 885: "Dreepy", 886: "Drakloak", 887: "Dragapult", 888: "Zacian", 889: "Zamazenta", 890: "Eternatus", 891: "Kubfu", 892: "Urshifu", 893: "Zarude", 894: "Regieleki", 895: "Regidrago", 896: "Glastrier", 897: "Spectrier", 898: "Calyrex"}

all_mons = {**gen_1_mons, **gen_2_mons, **gen_3_mons, **gen_4_mons, **gen_5_mons, **gen_6_mons, **gen_7_mons, **gen_8_mons}

def pickamon(mondict=all_mons):
    num = random.randint(list(mondict.keys())[0], list(mondict.keys())[-1])
    return f"{num}: {mondict[num]}"

window = tk.Tk()
window.title("Random Pokemon Generator (All Gens)")

frm_buttons = tk.Frame(master=window)
frm_output = tk.Frame(master=window)
frm_bulbapedia = tk.Frame(master=window)

frm_buttons.pack(pady=3)
frm_output.pack(padx=3, pady=3)
frm_bulbapedia.pack(pady=3)

txt_output = tk.Text(master=frm_output, width=20, height=3)
txt_output.pack()

def gen_1():
    txt_output.delete("1.0", tk.END)
    txt_output.insert("1.0", pickamon(gen_1_mons))
def gen_2():
    txt_output.delete("1.0", tk.END)
    txt_output.insert("1.0", pickamon(gen_2_mons))
def gen_3():
    txt_output.delete("1.0", tk.END)
    txt_output.insert("1.0", pickamon(gen_3_mons))
def gen_4():
    txt_output.delete("1.0", tk.END)
    txt_output.insert("1.0", pickamon(gen_4_mons))
def gen_5():
    txt_output.delete("1.0", tk.END)
    txt_output.insert("1.0", pickamon(gen_5_mons))
def gen_6():
    txt_output.delete("1.0", tk.END)
    txt_output.insert("1.0", pickamon(gen_6_mons))
def gen_7():
    txt_output.delete("1.0", tk.END)
    txt_output.insert("1.0", pickamon(gen_7_mons))
def gen_8():
    txt_output.delete("1.0", tk.END)
    txt_output.insert("1.0", pickamon(gen_8_mons))
def all_gens():
    txt_output.delete("1.0", tk.END)
    txt_output.insert("1.0", pickamon(all_mons))

btn_gen_1 = tk.Button(master=frm_buttons, text="Gen 1", command=gen_1)
btn_gen_1.pack(side=tk.LEFT, padx=3)
btn_gen_2 = tk.Button(master=frm_buttons, text="Gen 2", command=gen_2)
btn_gen_2.pack(side=tk.LEFT, padx=3)
btn_gen_3 = tk.Button(master=frm_buttons, text="Gen 3", command=gen_3)
btn_gen_3.pack(side=tk.LEFT, padx=3)
btn_gen_4 = tk.Button(master=frm_buttons, text="Gen 4", command=gen_4)
btn_gen_4.pack(side=tk.LEFT, padx=3)
btn_gen_5 = tk.Button(master=frm_buttons, text="Gen 5", command=gen_5)
btn_gen_5.pack(side=tk.LEFT, padx=3)
btn_gen_6 = tk.Button(master=frm_buttons, text="Gen 6", command=gen_6)
btn_gen_6.pack(side=tk.LEFT, padx=3)
btn_gen_7 = tk.Button(master=frm_buttons, text="Gen 7", command=gen_7)
btn_gen_7.pack(side=tk.LEFT, padx=3)
btn_gen_8 = tk.Button(master=frm_buttons, text="Gen 8", command=gen_8)
btn_gen_8.pack(side=tk.LEFT, padx=3)
btn_all_gens = tk.Button(master=frm_buttons, text="All Gens", command=all_gens)
btn_all_gens.pack(side=tk.RIGHT, padx=6)

def bulbapedia():
    mon = txt_output.get("1.0", tk.END)
    name = list(mon.split(": "))[-1].title()
    open_new_tab(f"https://bulbapedia.bulbagarden.net/wiki/{name}_(Pok%C3%A9mon)")

btn_bulbapedia = tk.Button(master=frm_bulbapedia, text="Open Bulbapedia Page", command=bulbapedia, padx=3)
btn_bulbapedia.pack(side=tk.RIGHT)

def handle_1(event):
    gen_1()
def handle_2(event):
    gen_2()
def handle_3(event):
    gen_3()
def handle_4(event):
    gen_4()
def handle_5(event):
    gen_5()
def handle_6(event):
    gen_6()
def handle_7(event):
    gen_7()
def handle_8(event):
    gen_8()
def handle_enter(event):
    bulbapedia()
    txt_output.delete(tk.END)

window.bind("1", handle_1)
window.bind("2", handle_2)
window.bind("3", handle_3)
window.bind("4", handle_4)
window.bind("5", handle_5)
window.bind("6", handle_6)
window.bind("7", handle_7)
window.bind("8", handle_8)
window.bind("<Return>", handle_enter)

window.mainloop()
