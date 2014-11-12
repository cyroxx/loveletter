# shamelessly ported from
# https://raw.githubusercontent.com/gingerbeardman/loveletter/master/index.php
import random
sals1 = ["Beloved", "Darling", "Dear", "Dearest", "Fanciful", "Honey"]

sals2 = ["Chickpea", "Dear", "Duck", "Jewel", "Love", "Moppet", "Sweetheart"]

adjs = ["affectionate", "amorous", "anxious", "avid", "beautiful", "breathless", "burning", "covetous", "craving", "curious", "eager", "fervent", "fondest", "loveable", "lovesick", "loving", "passionate", "precious", "seductive", "sweet", "sympathetic", "tender", "unsatisfied", "winning", "wistful"]

nouns = ["adoration", "affection", "ambition", "appetite", "ardour", "being", "burning", "charm", "craving", "desire", "devotion", "eagerness", "enchantment", "enthusiasm", "fancy", "fellow feeling", "fervour", "fondness", "heart", "hunger", "infatuation", "little liking", "longing", "love", "lust", "passion", "rapture", "sympathy", "thirst", "wish", "yearning"]

advs = ["affectionately", "ardently", "anxiously", "beautifully", "burningly", "covetously", "curiously", "eagerly", "fervently", "fondly", "impatiently", "keenly", "lovingly", "passionately", "seductively", "tenderly", "wistfully"]

verbs = ["adores", "attracts", "clings to", "holds dear", "hopes for", "hungers for", "likes", "longs for", "loves", "lusts after", "pants for", "pines for", "sighs for", "tempts", "thirsts for", "treasures", "yearns for", "woos"]



LONG = 1
SHORT = 2
last = None
ll = ""
for i in range(5):
    if random.randint(0, 9) < 5:
        # long
        #
        optadj1  = '' if random.randint(0,9) < 5 else random.choice(adjs)
        noun1 = random.choice(nouns)
        optadv  = '' if (random.randint(0,9) < 5)  else random.choice(advs)
        verb = random.choice(verbs)
        optadj2 = '' if (random.randint(0,9) < 5)  else random.choice(adjs)
        noun2 = random.choice(nouns)
        if (last is not None) or (last is LONG):
            concat = ". "
        else:
            concat = ""
        ll += "%s My %s %s %s %s your %s %s" % (concat, optadj1, noun1, optadv, verb, optadj2, noun2)
        last = LONG
    else:
        #SHORT
        adj = random.choice(adjs);
        noun = random.choice(nouns);
        if last is SHORT:
            concat = ", "
        elif last == LONG:
            concat = ". You are"
        else:
            concat = "You are "
        ll += "%s my %s %s" % (concat, adj, noun)
        last = SHORT

adv = random.choice(advs)
ll += ".\n     Yours %s,\n     M.U.C.\n\n" % (adv)

print ll

with open("loveletters.txt", "a") as myfile:
    myfile.write(ll + "\n\n")