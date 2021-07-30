# random_pokemon_generator
Gives a random Pokemon (Gens 1-5 only) and its Bulbapedia page

My first public coding project! Sorry if anything is oddly formatted; I'm newly self-taught.

This script opens a tkinter window with several buttons and a text box.

For each button labelled "Gen n", pressing the button randomly selects a Pokemon from Generation n and displays its Pokedex number and name in the text box.

Pressing the button labelled "All Gens 1-5" randomly selects a Pokemon from anywhere in Generations 1 through 5 and displays its number and name.

Pressing the button labelled "Open Bulbapedia Page" opens the Bulbapedia page for the Pokemon currently displayed in the text box.

I also included a few keyboard shortcuts. With the window open, you can press 1 instead of clicking "Gen 1", 2 instead of clicking "Gen 2", and so on (there is no shortcut for "All Gens 1-5" yet). You can then press Enter instead of clicking "Open Bulbapedia Page"

A bonus effect of the way I wrote this script is that you can actually just type the name of a Pokemon into the text box and hit Enter/press the "Open Bulbapedia Page" button and be taken right to the correct page. The script takes the text in to box, splits it at ": ", and takes the last string formed by the split (ordinarily, the Pokemon's name). It then capitalizes the first letter of this string, and enters it in the {name} portion of https://bulbapedia.bulbagarden.net/wiki/{name}_(Pok%C3%A9mon). Therefore, "Open Bulbapedia Page" works whether the textbox says "1: Bulbasaur", "Bulbasaur", or "bulbasaur". Hypothetically, you could type "fndu948 tyhfr08h:fsa0{)h8: 4039jg: jfi: bulbasaur", hit Enter, and still be taken to https://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pok%C3%A9mon) successfully. (In fact, I just tested that exact string, and it works!)

Have fun with this Pick-a-'Mon 5000!
