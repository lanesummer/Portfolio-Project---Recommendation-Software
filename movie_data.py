# data pulled from TMDB -- www.themoviedb.org
# dates 2023-05-14 thru 2023-07-01
# pulled first 2 pages of movies, deleted short films that weren't full length movies
# added tomatometer and audience_score from Rotten Tomatoes -- www.rottentomatoes.com

genres = [
    "Action",
    "Adventure",
    "Animation",
    "Comedy",
    "Crime",
    "Documentary",
    "Drama",
    "Family",
    "Fantasy",
    "History",
    "Horror",
    "Music",
    "Mystery",
    "Romance",
    "Science Fiction",
    "TV Movie",
    "Thriller",
    "War",
    "Western"
  ]

movie_data_headings = ['genre', 'title', 'overview', 'release_date', 'rating', 'tomatometer', 'audience_score']

movies =[
  [
    ['Action', 'Crime', 'Thriller'],
    "Fast X",
    "Over many missions and against impossible odds, Dom Toretto and his family have outsmarted, out-nerved and outdriven every foe in their path. Now, they confront the most lethal opponent they've ever faced: A terrifying threat emerging from the shadows of the past who's fueled by blood revenge, and who is determined to shatter this family and destroy everything—and everyone—that Dom loves, forever.",
    "2023-05-19",
    'PG-13',
    56,
    85
  ],
  [
    ['Action', 'Adventure', 'Animation', 'Science Fiction'],
    "Spider-Man: Across the Spider-Verse",
    "After reuniting with Gwen Stacy, Brooklyn’s full-time, friendly neighborhood Spider-Man is catapulted across the Multiverse, where he encounters the Spider Society, a team of Spider-People charged with protecting the Multiverse’s very existence. But when the heroes clash on how to handle a new threat, Miles finds himself pitted against the other Spiders and must set out on his own to save those he loves most.",
    "2023-06-02",
    'PG',
    96,
    94
  ],
  [
    ['Action', 'Thriller'],
    "Extraction 2",
    "Tasked with extracting a family who is at the mercy of a Georgian gangster, Tyler Rake infiltrates one of the world's deadliest prisons in order to save them. But when the extraction gets hot, and the gangster dies in the heat of battle, his equally ruthless brother tracks down Rake and his team to Vienna, in order to get revenge.",
    "2023-06-09",
    'R',
    79,
    86
  ],
  [
    ['Action', 'Adventure', 'Science Fiction'],
    "Transformers: Rise of the Beasts",
    "When a new threat capable of destroying the entire planet emerges, Optimus Prime and the Autobots must team up with a powerful faction known as the Maximals. With the fate of humanity hanging in the balance, humans Noah and Elena will do whatever it takes to help the Transformers as they engage in the ultimate battle to save Earth.",
    "2023-06-09",
    'PG-13',
    54,
    91
  ],
  [
    ['Animation', 'Comedy', 'Family', 'Fantasy', 'Romance'],
    "Elemental",
    "In a city where fire, water, land and air residents live together, a fiery young woman and a go-with-the-flow guy will discover something elemental: how much they have in common.",
    "2023-06-16",
    'PG',
    76,
    92
  ],
  [
    ['Action', 'Horror', 'Thriller'],
    "The Wrath of Becky",
    "Two years after she escaped a violent attack on her family, 16-year-old Becky attempts to rebuild her life in the care of an older woman -- a kindred spirit named Elena. However, when a violent group known as the Noble Men break into their home, attack them and take their beloved dog, Becky must return to her old ways to protect herself and her loved ones.",
    "2023-05-26",
    'R',
    86,
    76
  ],
  [
    ['Science Fiction', 'Action', 'Adventure'],
    "The Flash",
    "When his attempt to save his family inadvertently alters the future, Barry Allen becomes trapped in a reality in which General Zod has returned and there are no Super Heroes to turn to. In order to save the world that he is in and return to the future that he knows, Barry's only hope is to race for his life. But will making the ultimate sacrifice be enough to reset the universe?",
    "2023-06-16",
    'PG-13',
    64,
    84
  ],
  [
    ['Adventure', 'Family', 'Fantasy', 'Romance'],
    "The Little Mermaid",
    "The youngest of King Triton’s daughters, and the most defiant, Ariel longs to find out more about the world beyond the sea, and while visiting the surface, falls for the dashing Prince Eric. With mermaids forbidden to interact with humans, Ariel makes a deal with the evil sea witch, Ursula, which gives her a chance to experience life on land, but ultimately places her life – and her father’s crown – in jeopardy.",
    "2023-05-26",
    'PG',
    67,
    94
  ],
  [
    ['Adventure', 'Action', 'Fantasy'],
    "Indiana Jones and the Dial of Destiny",
    "Finding himself in a new era, approaching retirement, Indy wrestles with fitting into a world that seems to have outgrown him. But as the tentacles of an all-too-familiar evil return in the form of an old rival, Indy must don his hat and pick up his whip once more to make sure an ancient and powerful artifact doesn't fall into the wrong hands.",
    "2023-06-30",
    'PG-13',
    68,
    88
  ],
  [
    ['Comedy', 'Action', 'Crime'],
    "The Machine",
    "Bert Kreischer faces a familial crisis and the arrival of his estranged father when the ghost of his booze-soaked past arrives: a murderous mobster hellbent on kidnapping Bert back to the motherland to atone for his crimes. Together, he and his father must retrace the steps of his younger self in the midst of a war between a sociopathic crime family while they attempt to find common ground.",
    "2023-05-26",
    'R',
    27,
    87
  ],
  [
    ['Drama', 'Thriller'],
    "Sanctuary",
    "Confined to a claustrophobic hotel room, the heir to a hotel empire and the dominatrix who has primed him for success become locked in a battle of wits and wills as he tries to end his relationship with her.",
    "2023-05-19",
    'R',
    90,
    85
  ],
  [
    ['Animation', 'Family', 'Fantasy', 'Comedy'],
    "Ruby Gillman, Teenage Kraken",
    "A shy teenager discovers that she's part of a legendary royal lineage of mythical sea krakens and that her destiny, in the depths of the oceans, is bigger than she ever dreamed.",
    "2023-06-30",
    'PG',
    66,
    83
  ],
  [
    ['Comedy'],
    "No Hard Feelings",
    "On the brink of losing her childhood home, Maddie discovers an intriguing job listing: wealthy helicopter parents looking for someone to “date” their introverted 19-year-old son, Percy, before he leaves for college. To her surprise, Maddie soon discovers the awkward Percy is no sure thing.",
    "2023-06-23",
    'R',
    68,
    87
  ],
  [
    ['Comedy', 'Drama', 'Romance'],
    "You Hurt My Feelings",
    "A novelist's longstanding marriage is suddenly upended when she overhears her husband giving his honest reaction to her latest book.",
    "2023-05-26",
    'R',
    95,
    64
  ],
  [
    ['Family', 'Fantasy', 'Adventure'],
    "The Secret Kingdom",
    "Verity and Peter’s trip to the old family mansion takes a turn when the floor of their room suddenly gives way and they fall into an underground chamber where they are met by a civilization of creatures. The leader tells them that Peter's arrival was foretold as he’s the one who can use Great Clock of the Citadel to restart time and destroy the Shroud, a malevolent creature who feeds on fear itself...",
    "2023-06-09",
    'PG',
    67,
    58
  ],
  [
    ['Action', 'Thriller'],
    "Kandahar",
    "After his mission is exposed, an undercover CIA operative stuck deep in hostile territory in Afghanistan must fight his way out, alongside his Afghan translator, to an extraction point in Kandahar, all whilst avoiding elite enemy forces and foreign spies tasked with hunting them down.",
    "2023-05-26",
    'R',
    47,
    82
  ],
  [
    ['Horror'],
    "The Angry Black Girl and Her Monster",
    "Vicaria is a brilliant teenager who believes death is a disease that can be cured. After the brutal and sudden murder of her brother, she embarks on a dangerous journey to bring him back to life.",
    "2023-06-09",
    'Not Rated',
    87,
    86
  ],
  [
    ['Comedy'],
    "About My Father",
    "Encouraged by his fiancee, a man and his father spend the weekend with her wealthy and exceedingly eccentric family. The gathering soon develops into a culture clash, allowing father and son to discover the true meaning of family.",
    "2023-05-26",
    'PG-13',
    35,
    81
  ],
  [
    ['Mystery', 'Thriller', 'Action'],
    "Confidential Informant",
    "During a crack epidemic two narcotics agents hunting for a cop killer. Hoping for leads, Moran and Thorton pay off a junkie informant. To provide for his wife and son, Moran involves the stool pigeon in a deadly scheme. This causes the partners to come under the scrutiny of a suspicious internal affairs agent.",
    "2023-06-30",
    'R',
    '-- not enough reviews',
    '-- not enough reviews'
  ],
  [
    ['Comedy', 'Romance', 'Science Fiction'],
    "Asteroid City",
    "In an American desert town circa 1955, the itinerary of a Junior Stargazer/Space Cadet convention is spectacularly disrupted by world-changing events.",
    "2023-06-16",
    'PG-13',
    74,
    63
  ],
  [
    ['Horror', 'Mystery', 'Fantasy'],
    "The Boogeyman",
    "Still reeling from the tragic death of their mother, a teenage girl and her younger sister find themselves plagued by a sadistic presence in their house and struggle to get their grieving father to pay attention before it’s too late.",
    "2023-06-02",
    'PG-13',
    63,
    66
  ],
  [
    ['Animation', 'Science Fiction', 'Action', 'Adventure', 'Fantasy'],
    "Nimona",
    "A knight framed for a tragic crime teams with a scrappy, shape-shifting teen to prove his innocence. But what if she's the monster he's sworn to destroy?",
    "2023-06-23",
    'PG',
    92,
    94
  ],
  [
    ['Romance', 'Science Fiction', 'Fantasy', 'Comedy'],
    "Robots",
    "A womanizer and a gold digger trick people into relationships with illegal robot doubles. When they unwittingly use this scam on each other, their robot doubles fall in love and elope, forcing the duo to team up to hunt them down before the authorities discover their secret.",
    "2023-05-19",
    'R',
    12,
    29
  ],
  [
    ['Action', 'Comedy', 'Crime'],
    "Sheroes",
    "When four thick-as-thieves friends arrive in Thailand they quickly find themselves in over their heads. Fighting to stay alive they employ their unique set of skills and unleash their fierce loyalty in a heart-pumping battle for survival.",
    "2023-06-23",
    'R',
    40,
    64
  ],
  [
    ['Science Fiction', 'Thriller'],
    "Simulant",
    "Faye attempts to replace her newly deceased husband, Evan, with an android simulant (SIM). Although SIM Evan appears like human Evan in every way, Faye does not feel the same love for SIM Evan as it does for her. SIM Evan tries to win Faye back while at the same time being on-the-run from a government agent chasing down SIMs who have become “conscious” and could potentially be a threat to humankind.",
    "2023-06-02",
    'Not Rated',
    44,
    50
  ],
  [
    ['Thriller', 'Drama'],
    "Master Gardener",
    "Narvel Roth is a meticulous horticulturist who is devoted to tending the grounds of a beautiful estate and pandering to his employer, the wealthy dowager Mrs. Haverhill. When she demands that he take on her wayward and troubled niece, it unlocks dark secrets from a buried violent past.",
    "2023-05-19",
    'R',
    70,
    55
  ],
  [
    ['Drama', 'Romance'],
    "Past Lives",
    "Two childhood friends are separated after one’s family emigrates from South Korea. Two decades later, they are reunited in New York for one week as they confront notions of destiny, love, and the choices that make a life.",
    "2023-06-02",
    'PG-13',
    97,
    93
  ],
  [
    ['Thriller', 'Action'],
    "97 Minutes",
    "A hijacked 767 will crash in just 97 minutes when its fuel runs out. Against the strong will of NSA Deputy Toyin, NSA Director Hawkins prepares to have the plane shot down before it does any catastrophic damage on the ground, leaving the fate of the innocent passengers in the hands of Tyler, one of the alleged hijackers on board who is an undercover Interpol agent - or is he?",
    "2023-06-09",
    'Not Rated',
    '-- not enough reviews',
    74
  ],
  [
    ['Comedy'],
    "Maximum Truth",
    "A documentary crew follows political grifter Rick Klingman as he teams up with his sketchy buddy Simon to take down a rival congressional candidate.",
    "2023-06-23",
    'R',
    55,
    76
  ],
  [
    ['Horror', 'Comedy'],
    "The Blackening",
    "A group of black friends reunite for a Juneteenth weekend getaway only to find themselves trapped in a remote cabin with a twisted killer.",
    "2023-06-16",
    'R',
    86,
    85
  ],
  [
    ['Drama'],
    "Prisoner's Daughter",
    "Released from prison with terminal cancer, Max tries to reconnect with his estranged daughter and the grandson he’s never known. When his daughter’s abusive, drug-addicted ex-husband reappears, Max’s violent past comes back to haunt them all.",
    "2023-06-30",
    'R',
    47,
    88
  ],
  [
    ['Action', 'Drama', 'War'],
    "Warhorse One",
    "A gunned down Navy SEAL Master Chief must guide a child to safety through a gauntlet of hostile Taliban insurgents and survive the brutal Afghanistan wilderness.",
    "2023-06-30",
    'R',
    '-- not enough reviews',
    '-- not enough reviews'
  ],
  [
    ['Documentary'],
    "Every Body",
    "Focuses on three intersex individuals who overcame shame, secrecy, and unauthorized surgery throughout their childhoods to enjoy successful adulthoods. Choosing to ignore medical advice to conceal their bodies and coming out as who they truly were.",
    "2023-06-30",
    'R',
    100,
    '-- not enough reviews'
  ],
  [
    ['Comedy', 'Thriller', 'Mystery'],
    "Susie Searches",
    "Susie is an awkward college student who seizes the opportunity to bolster her popularity and her under-the-radar true-crime podcast by solving the disappearance of a classmate, but her investigation reveals that the truth and Susie aren’t at all what they seem to be.",
    "2023-06-30",
    'Not Rated',
    67,
  '-- not enough reviews'
  ]
]
