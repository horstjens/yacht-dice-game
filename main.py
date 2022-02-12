import random
# einmal würfeln...
# ich möchte 3 x würfeln, 
# der spieler soll aussuchen welche würfel re-rollen
categories = [
  "Ones",
  "Twos",
  "Threes",
  "Fours",
  "Fives",
  "Sixes",
  "Full House",
  "Four-Of-A-Kind",
  "Little Straight",
  "Big Straight",
  "Choice",
  "Yacht",
]
command = "abcde"
for wurf in (1,2,3):
  if "a" in command:
    würfel1 = random.randint(1,6)
  if "b" in command:
    würfel2 = random.randint(1,6)
  if "c" in command:
    würfel3 = random.randint(1,6)
  if "d" in command:
    würfel4 = random.randint(1,6)
  if "e" in command:
    würfel5 = random.randint(1,6)
    #wurf = 1
    #print("dies ist wurf nummer {}".format(wurf))
  if wurf == 1:
        print("      +---+---+---+---+---+")
        print("wurf# | a | b | c | d | e |")
  print("      +---+---+---+---+---+")
  print("  {}   | {} | {} | {} | {} | {} |".format(
      wurf,
      würfel1,
      würfel2,
      würfel3,
      würfel4,
      würfel5 ))
  print("      +---+---+---+---+---+")
  if wurf < 3:
    print("bitte jene Buchstaben geben, die nochmal würfeln sollen (z.B. ace)")
    command = input(">>>")
# ------------ auswertung -----------
# --- spieler fragen welche category er spielen will
for number, cat in enumerate(categories,1):
  print(number, ":", cat)
while True:
  command = input("welche categorie? >>>")
  try:
    index = int(command)
  except:
    print("Bitte nur zahlen zwischen 1 und 12 eingeben")
    continue # zurück zum schleifenanfang
  # es war eine zahl, aber war es eine zahl zwischen 1 und 12?
  if 0 < index < 13:
    break # alles ok, verlasse die Schleife
  print("es war eine zahl, aber keine gültige zahl")
my_cat = categories[index-1]
print("Sie haben gewählt:", my_cat)

# --- punkte ? ---
punkte = 0
# --- yacht: wenn 5x gleich augenzahl, dann 50 Punkte, sonst 0 Punkt
if my_cat == "Yacht" :
  # habe ich 5 x gleiche augenzahl ?
  if würfel1 == würfel2 == würfel3 == würfel4 == würfel5:
    print("super, eine echte Yacht! Sie haben 50 punkte!")
    punkte += 50
  else:
    print("leider keine Yacht, nur 0 Punkte")

if my_cat == "Choice":
  # summe aller Augen
  augensumme = würfel1 + würfel2 + würfel3 + würfel4 + würfel5
  print("choice ergibt", augensumme, "punkte.")
  punkte += augensumme

if my_cat == "Big Straight":
  temp = [würfel1, würfel2, würfel3, würfel4, würfel5]
  temp.sort()
  if temp == [2,3,4,5,6]:
    print("super, 30 punkte")
    punkte += 30
  else:
    print("leider nix")
    
# bitte selbständig die "Little Straight" programmieren


  





