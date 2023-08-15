import random

day1 = {
    "Dissolute": "Lacking moral restraint, indulging in immoral behavior.",
    "Taciturn": "Reserved or uncommunicative in speech; saying little.",
    "Dumbfounded": "Greatly astonished or shocked into silence.",
    "Addlepated": "Confused, muddled, or lacking clear thinking.",
    "Enervated": "Lacking energy, feeling drained or weakened.",
    "Turbid": "Cloudy, opaque, or difficult to see through, often used to describe liquids.",
    "Turgid": "Excessively inflated or pompous in style; overly elaborate.",
    "Tepid": "Lukewarm or lacking enthusiasm; showing little excitement.",
    "Coda": "A concluding passage or segment in a musical composition.",
    "Homily": "A sermon or speech, often with moral or spiritual lessons.",
    "Berated": "Strongly criticized or scolded in a harsh and angry manner.",
    "Inundated": "Flooded or overwhelmed by a large amount of something.",
    "Copiously": "In large quantities or abundantly; plentifully.",
    "Brusquely": "In an abrupt, blunt, and curt manner.",
    "Inscrutable": "Difficult to understand or interpret; mysterious.",
    "Enigmatic": "Mysterious, puzzling, or difficult to understand.",
    "Quixotic": "Exceedingly idealistic and unrealistic, often to the point of being foolish.",
    "Grandiloquent": "Using extravagant, impressive language to sound important or impressive.",
    "Posit": "To propose or put forward an idea or theory without concrete proof",
    "Cajole": "To persuade or coax someone using charm, flattery, or persuasion.",
    "Vicissitude": "Natural changes or variations that occur in life or circumstances.",
    "Akimbo": "With hands on hips and elbows pointing outward; standing confidently.",
    "Obtuse": "Lacking quickness of perception or intelligence; insensitive or dull.",
    "Subservient": "Excessively submissive or obedient to someone else's authority.",
    "Askance": "Looking at something with suspicion, doubt, or disapproval.",
    "Apologist": "Someone who defends or justifies a belief or idea, often controversial.",
    "Mercenary": "Someone motivated by money or financial gain.",
    "Lackey": "Someone who behaves subserviently to gain favor or approval.",
    "Warily": "Cautionly or attentively, often due to awareness of risks.",
    "Mendaciously": "Dishonestly or untruthfully.",
    "Panned": "Strongly criticized or reviewed negatively."
}

day2 = {
    "Ominously": "In a way that suggests something bad or threatening will happen.",
    "Anachronistically": "In a manner that is not in its proper historical context.",
    "Presciently": "In a way that anticipates or predicts future events accurately.",
    "Providential": "Relating to an event that is considered fortunate or timely, as if by divine intervention.",
    "Simpatico": "Having a mutual understanding and rapport; in harmony with someone.",
    "Inured": "Accustomed to or hardened by enduring difficult experiences.",
    "Effusive": "Expressing emotions or gratitude in an unrestrained and overflowing manner.",
    "Maudlin": "Overly sentimental or tearfully emotional in a self-pitying way.",
    "Agglomerated": "Clustered or formed by accumulation of various elements.",
    "Amortized": "Gradually paid off a debt or loan through regular installments.",
    "Platitudes": "Trite, overused statements lacking originality or depth.",
    "Neologisms": "Newly coined words or expressions.",
    "Quagmire": "A difficult, complex situation; a predicament that's hard to escape.",
    "depredate": "plunder, seizing and damaging resources.",
    "Autodidacts": "Individuals who are self-taught, learning independently.",
    "Recidivists": "Individuals who repeatedly commit offenses despite previous convictions.",
    "Libertines": "People who lead an unrestrained, often hedonistic lifestyle.",
    "Myrmidons": "Loyal and unquestioning followers, often with negative connotations.",
    "Defer": "Yield to the opinion or wishes of another person, often out of respect.",
    "Presage": "Predict or indicate an event or outcome in advance.",
    "Deftly": "Skillfully and adeptly, with finesse and precision.",
    "Abhorrent": "Extremely repugnant or offensive.",
    "Unbeknownst": "Without the knowledge or awareness of someone.",
    "Consanguineous": "Related by shared blood or ancestry.",
    "Tremulous": "Marked by trembling or quivering due to fear or nervousness.",
    "Coltish": "Playful, energetic, and somewhat awkward in behavior.",
    "Beguiled": "Charmingly captivated or deceived by someone's actions.",
    "Chary": "Cautious, hesitant, or wary in taking risks or making decisions.",
    "Sentries": "Individuals assigned to guard or watch over a place or area.",
    "Fecund": "Fertile, productive, capable of abundant growth or creativity.",
    "Sycophants": "Individuals who excessively flatter or seek favor from others, often with ulterior motives.",
    "Efficacious": "Effective, capable of producing desired results.",
    "Imperious": "Displaying an attitude of arrogance or dominance.",
    "Forebears": "Ancestors or earlier generations preceding someone in a lineage.",
    "Harbinger": "An indicator or omen that foreshadows the arrival of something else."
}

day3 = {
    "Equivocal": "Open to more than one interpretation; ambiguous or unclear.",
    "Ephemeral": "Lasting for a very short time; transitory or fleeting.",
    "Omnipotent": "Having unlimited or infinite power; all-powerful.",
    "Misanthropy": "Dislike or distrust of humanity or people in general.",
    "Desuetude": "The state of being no longer in use or practice; disuse.",
    "Debauchment": "Engaging in immoral or excessive behavior, often involving pleasure-seeking.",
    "Puissant": "Having great power, influence, or strength; potent or powerful.",
    "Restive": "Impatient, uneasy, or resistant to being controlled; restless.",
    "Complaisant": "Willing to please others, accommodating, or agreeable.",
    "Sanguine": "Optimistic, hopeful, and cheerful about future outcomes.",
    "High-handed": "Arrogant, overbearing, or domineering in behavior or attitude.",
    "Salubrious": "Health-promoting, beneficial to well-being, or conducive to good health.",
    "Incendiaries": "Substances, devices, or actions involved in starting fires or causing unrest.",
    "Peccadilloes": "Minor or trivial faults, mistakes, or offenses.",
    "Odious": "Extremely unpleasant, offensive, or repulsive.",
    "Potable": "Safe and suitable for drinking; fit for consumption.",
    "Risible": "Likely to provoke laughter, amusing, or funny.",
    "Cursory": "Done quickly and without attention to detail; superficial.",
    "Arch": "Playfully ironic, mischievous, or teasing in tone.",
    "Ginger": "A spice with a spicy flavor or a reddish-brown color.",
    "Verdant": "Lush, green, and covered in vegetation.",
    "Castigated": "Severely criticized, scolded, or reprimanded.",
    "Facile": "Easy, simplistic, or achieved with minimal effort.",
    "Dulcet": "Pleasant, soothing, or melodious, often related to sounds or flavors.",
    "Doctrinaire": "Rigidly sticking to a particular doctrine or set of principles.",
    "Convivial": "Friendly, cheerful, and lively in social gatherings.",
    "Sanguinary": "Involving or characterized by bloodshed or violence.",
    "Jejune": "Lacking interest, substance, or maturity; dull or simplistic.",
    "Modish": "Fashionable, stylish, or in line with current trends.",
    "Motley": "Diverse or varied, often with a lack of uniformity or coherence.",
    "Variegated": "Having a variety of colors, patterns, or forms.",
    "Facetious": "Playful, humorous,treating serious issues with deliberately inappropriate humour; flippant",
    "Disingenuous": "Not candid or sincere; pretending to be genuine or honest."
}

day4 = {
    "Mirth": "Gladness, laughter, or happiness, often accompanied by amusement.",
    "Deification": "Treating someone or something as a god; the act of exalting to divine status.",
    "Excoriation": "Strong criticism, censure, or condemnation.",
    "Calumnies": "False and malicious statements intended to damage someone's reputation; slander.",
    "Obloquies": "Strong public criticism or verbal abuse; disgraceful or harsh language.",
    "Artifices": "Clever strategies or tactics used to achieve a particular goal; tricks or deception.",
    "Pedantry": "Excessive concern with minor details or rules; ostentatious display of knowledge.",
    "Parsimony": "Extreme unwillingness to spend money or use resources; frugality or thrift.",
    "Pulchritude": "Beauty or physical attractiveness, often used in a poetic or elevated context.",
    "Minutiae": "Small, trivial, or minor details of something.",
    "Bereaved": "Grieving over the death of a loved one; experiencing loss.",
    "Altar": "A raised structure used for religious or ceremonial purposes, often as a focal point of worship.",
    "Bifurcated": "Divided or split into two branches or parts.",
    "Alacrity": "Cheerful willingness or eagerness to do something; promptness.",
    "Lulled": "Calmed or soothed, often to a state of relaxation or complacency.",
    "Quiescent": "Inactive, dormant, or temporarily at rest; in a state of quietness or tranquility.",
    "Lacunae": "Gaps, missing parts, or blank spaces in a document, record, or knowledge.",
    "Probity": "Honesty, integrity, and uprightness in character; moral soundness.",
    "Profligate": "Recklessly wasteful or extravagant, often referring to behavior or spending.",
    "Antediluvian": "Extremely old or ancient, often referring to a time before a great flood (literally 'before the flood').",
    "Ascetic": "Characterized by self-discipline, abstinence, and avoidance of indulgence; often used in a religious context.",
    "Stasis": "A state of balance, stability, or stagnation, often in a process or situation.",
    "Hedonism": "The pursuit of pleasure and sensual self-indulgence as the highest good.",
    "Seraphs": "Angelic beings often depicted as having multiple wings and a fiery appearance.",
    "Aphorisms": "Short and concise statements that express a general truth or principle; wise sayings or maxims.",
    "Gulf": "A wide gap or distance, often used metaphorically to describe a significant difference or division.",
    "Pervades": "Spread throughout and influencing every part of something; to be present in all aspects.",
    "Espouses": "Adopts, supports, or becomes an advocate for a particular idea, belief, or cause."
}

day5 = {
    "Candor": "Openness, honesty, and frankness in expressing thoughts or opinions.",
    "Effacement": "The act of erasing, wiping out, or making something less noticeable.",
    "Overture": "An introductory proposal, offer, or gesture, often made to initiate further action.",
    "Patrimony": "An inheritance or legacy, often referring to property or cultural heritage passed down from ancestors.",
    "Trenchant": "Expressing opinions or observations in a sharp, incisive, and effective manner.",
    "Insipid": "Lacking flavor, interest, or excitement; dull, bland, or unstimulating.",
    "Pacific": "Peaceful, calm, and nonaggressive in nature or demeanor.",
    "Metastasize": "Spread or extend to other parts, often used in the context of cancer or disease.",
    "Prudent": "Exercising good judgment, caution, and careful planning in decision-making.",
    "Parlous": "full of danger or uncertainty; precarious.;very",
    "Semiotic": "Relating to the study of signs and symbols and their meanings.",
    "Careened": "Moved swiftly and uncontrollably in a specific direction, often implying instability.",
    "Tarried": "Delayed, lingered, or stayed in a place longer than necessary.",
    "Intrepidity": "Fearlessness, courage, and boldness in the face of danger or challenges.",
    "Sangfroid": "Coolness and composure, especially in difficult or stressful situations.",
    "Mercurial": "Characterized by rapid and unpredictable changes in mood or temperament.",
    "Vainglorious": "Excessively proud of oneself or one's achievements, often to the point of arrogance.",
    "Paramount": "Of the greatest importance, significance, or concern; supreme or dominant.",
    "Apposed": "Placed side by side or in close proximity; juxtaposed.",
    "Irascible": "Easily provoked to anger; having a quick and irritable temper.",
    "Eremitic": "Relating to a hermit or the lifestyle of a recluse, often in a religious context.",
    "Besmirched": "Stained, tarnished, or damaged one's reputation or honor.",
    "Bleated": "Made the sound of a sheep or goat, often used metaphorically to describe a complaining voice.",
    "Oligarchy": "A form of government or power structure where a small group holds control.",
    "Rectitude": "Moral integrity, honesty, and adherence to principles; righteousness.",
    "Scruples": "Feelings of doubt, hesitation, or ethical considerations that affect decision-making.",
    "Turpitude": "Immorality, depravity, or wickedness; a morally corrupt or shameful act.",
    "Bemoan": "Express grief, regret, or distress over something; lament or complain about.",
    "Stopgap": "A temporary solution or measure used to address an immediate problem.",
    "Modicum": "A small or moderate amount of something; a token or a minimal quantity.",
    "Paragon": "A model of excellence, perfection, or a person or thing considered as the best example.",
    "Nadir": "The lowest point or the least favorable moment, often referring to a situation.",
    "Consecration": "The act of dedicating something as sacred or holy, often involving a formal ritual."
}

day6 = {
    "Duplicity": "Deceitfulness or double-dealing; the act of saying one thing while doing another.",
    "Mores": "Customs, norms, or accepted cultural practices within a society.",
    "Plaudits": "Praise, applause, or enthusiastic approval, often publicly expressed.",
    "Vitiation": "The act of making something impure, corrupted, or weakened.",
    "Derogated from": "Diminished the value or importance of something; detracted from.",
    "Bedizened": "Dressed or adorned in a showy, gaudy, or excessive manner.",
    "Aggrandized": "Enhanced or exaggerated in size, power, or status.",
    "Admonishing": "Rebuking, warning, or scolding someone with firmness or authority.",
    "Jocular": "Characterized by joking, humorous, or playful behavior.",
    "Irate": "Extremely angry, furious, or incensed.",
    "Didactic": "Intended to teach, educate, or convey moral or ethical principles.",
    "Dionysian": "Relating to the sensual, impulsive, and hedonistic aspects of human nature.",
    "Protean": "Readily able to change shape, form, or nature; versatile and adaptable.",
    "Martial": "Relating to war, the military, or armed forces.",
    "Parochial": "Limited in scope or perspective; having a narrow view, often related to local matters.",
    "Arcadian": "Relating to a simple, rural, and idyllic way of life; often associated with the countryside.",
    "Squalid": "Dirty, filthy, and extremely unpleasant or sordid in appearance.",
    "Penumbra": "A partially shaded area between light and darkness; an area of uncertainty or ambiguity.",
    "Hinterland": "The remote or less developed areas that are far from urban centers.",
    "Tony": "Stylish, fashionable, or characterized by an air of sophistication.",
    "Spartan": "Characterized by simplicity, frugality, and self-discipline, often in living conditions.",
    "Apollonian": "Characterized by rationality, reason, and restraint, often in contrast to Dionysian.",
    "Faux-naif": "Pretending to be naive or innocent while actually being aware of the situation.",
    "No-holds-barred": "Unrestricted, unrestrained, and with no limitations or rules.",
    "Dyed in the wool": "Deeply ingrained or firmly established in one's beliefs or behavior.",
    "Callow": "Inexperienced, immature, or lacking sophistication due to youth.",
    "Stonewalled": "Refused to answer or cooperate, often by avoiding giving direct answers.",
    "Storied": "Having a history or reputation filled with stories, often legendary or significant.",
    "Prudish": "Excessively concerned with modesty, decency, or propriety, often in a prudish manner.",
    "Effete": "Depleted of vitality, energy, or effectiveness; overly refined or pretentious.",
    "Whet": "To sharpen, stimulate, or increase interest or desire, often figuratively.",
    "Accrue": "To accumulate or gather over time, often referring to benefits or interest.",
    "Tout": "To promote, advertise, or praise enthusiastically, often to attract attention or support.",
    "At loggerheads": "In strong disagreement or conflict; unable to agree or find common ground.",
    "In cahoots": "Involved in a secret or conspiratorial partnership or alliance.",
    "Colluding": "Secretly cooperating or conspiring with others to deceive or achieve a specific purpose.",
    "Stymying": "Blocking, hindering, or frustrating progress or efforts.",
    "Abetting": "Assisting, encouraging, or supporting someone, often in a wrongdoing or illegal activity.",
    "Pellucid": "Transparent, clear, and easy to understand or perceive.",
    "Solipsistic": "Characterized by the belief that only one's own mind is certain to exist; self-centered."
}
day7 = {
    "Apportioned": "Distributed or allocated in specific portions or shares.",
    "Ruminate": "To think deeply, contemplate, or ponder over something.",
    "Revered": "Respected, admired, or held in high esteem.",
    "Contortion": "A twisted or distorted shape, often resulting from physical or unnatural twisting.",
    "Deluge": "A heavy downpour of rain; a flood or overwhelming abundance of something.",
    "Disabuse": "To correct someone's mistaken beliefs, misconceptions, or misunderstandings.",
    "Unconscionable": "Unreasonably excessive, extreme, or morally unacceptable.",
    "Scrupulous": "Conscientious, thorough, and attentive to detail, often with strong moral principles.",
    "Sidereal": "Relating to the stars or astronomy; measured or observed with respect to the stars.",
    "Presumptuous": "Overly bold, confident, or forward, often without proper justification.",
    "Pithy": "Concise and meaningful, often expressing a lot in few words.",
    "Insidious": "Subtly harmful or dangerous, often spreading gradually and unnoticed.",
    "Addled": "Confused, muddled, or mentally disoriented.",
    "Acerbic": "Sharp, bitter, or harsh in tone, often used to describe remarks or criticism.",
    "Caustic": "Sarcastic, biting, or corrosive in language or attitude.",
}


total={**day1,**day2,**day3,**day4,**day5,**day6,**day7}
days=[day1,day2,day3,day4,day5,day6,day7,total]
total_words=216

def display_meaning(word,dic):
    print(f"Meaning of '{word}': \n")
    input("Press Enter to get the word meaning:")
    print(f"{dic.get(word, 'Meaning not found')}")

def game(n,score,total):
    words_to_ask = list((days[n-1]).keys())
    while True:

        print("\n++++++++++++++++++++++++")        
        word = random.choice(words_to_ask)
        display_meaning(word,(days[n-1]))
        z=input("\nEnter 0 if you got it wrong....")
        total+=1
        if z!="0":
            score+=1
            
        exit_choice = input("\n click 1 to go to main menu:").lower()
        if exit_choice == "1":
            break
    return score,total


print(f"We have so far completed {len(days)-1} days, and {total_words} words!\n")
score=0
total=0
while True:
    n=int(input("Which day would you like to practise,enter 0 for all:"))
    score,total=game(n,score,total)
    m=input("Do you want to stop?")
    if m=="yes":
        break
print(f"Your final score was {score}/{total}")