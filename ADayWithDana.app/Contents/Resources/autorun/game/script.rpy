image bg black = "bg black.png"
image hangoutopt = "bg hangoutopt.png"
image bg ownroom = "bg ownroom.png"
image bg ali = "bg ali.png"
image bg coco = "bg coco.png"
image bg nadine = "bg nadine.png"
image bg maria1 = "maria1.png"
image bg maria2 = "maria2.png"
image jukebox = "jukebox.png"
image msg1 = "msg1.png"
image msg2 = "msg2.png"

define d = Character(_("Dana"), color="#05b8cc")
define a = Character(_("Ali"), color="#ffb6c1")
define c = Character(_("Coco"), color="#fffdd0")
define n = Character(_("Nadine"), color="#551a8b")
define m = Character(_("Maria"), color="#ffff99")
define pushup = PushMove(10.0, "pushup")

label start:
    play music "MassDestruction.mp3"
    $ aproj = True
    $ cproj = True
    $ nproj = True
    $ mproj = False
    $ points = 0

label start1:
    scene bg black
    with fade

    "......"
    "fuuuuuuuuuckkkk"
    d "I'm so boRED"

    "You collaspe on your bed. Today is a Sunday and it's been a while since school has cooled down with its intensive training"

label choic:
    
    scene bg ownroom
    with fade
    
    menu:
        "How will you spend your day?"

        "Sleep":
            jump sleep

        "Play some chill beats":
            jump jukebox

        "Pester someone":
            jump hangout

label sleep:
    d "Maybe I should just pass the time until I have something to do..."

    scene bg black
    with dissolve

    "You passed out on your bed, and the day never passed"
    "{b}Bad Ending{/b}"

return
    
label jukebox:
    scene jukebox
    with fade
    
    menu:
        d "Let's see..."

        "Aftermath":
            stop music
            play music "Aftermath.mp3"
            jump choic
        "Black dress":
            stop music
            play music "BlackDress.mp3"
            jump choic
        "Carmen":
            stop music
            play music "Carmen.mp3"
            jump choic
        "Cigarette daydream":
            stop music
            play music "CigaretteDaydream.mp3"
            jump choic
        "Dancing Star Night": 
            stop music
            play music "DancingStarNight.mp3"
            jump choic
        "Next Page":
            jump page2
        "Nevermind":
            jump choic
            
label page2:
    menu:
        d "Let's see..."
        
        "Fear and delight":
            stop music
            play music "FearDelight.mp3"
            jump choic
        "feelings are fatal":
            stop music
            play music "feelingsrfatal.mp3"
            jump choic
        "Happy birthday":
            stop music
            play music "LMFAO.mp3"
            jump choic
        "Happy pills":
            stop music
            play music "HappyPills.mp3"
            jump choic
        "Heavy in your arms":
            stop music
            play music "Heavyinyourarms.mp3"
            jump choic
        "Next Page":
            jump page3
        "Nevermind":
            jump choic
            
label page3:
    menu:
        d "Let's see..."
        
        "Little pistol":
            stop music
            play music "LittlePistol.mp3"
            jump choic
        "Lonely hearts club":
            stop music
            play music "LonelyHeartsClub.mp3"
            jump choic
        "Mass Destruction":
            stop music
            play music "MassDestruction.mp3"
            jump choic
        "Murders":
            stop music
            play music "Murders.mp3"
            jump choic
        "RIP 2 My Youth":
            stop music
            play music "RIP2MyYouth.mp3"
            jump choic
        "Next Page":
            jump page4
        "Nevermind":
            jump choic

label page4:
    menu:
        d "Let's see..."
           
        "Sunflower":
            stop music
            play music "Sunflower.mp3"
            jump choic
        "The moss":
            stop music
            play music "TheMoss.mp3"
            jump choic
        "This is home":
            stop music
            play music "ThisisHome.mp3"
            jump choic
        "This is the best":
            stop music
            play music "Thisisthebest.mp3"
            jump choic
        "West coast smoker":
            stop music
            play music "WestCoastSmoker.mp3"
            jump choic
        "Nevermind":
            jump choic

label hangout:
    
    if points == 3:
        $ mproj = True
    
    d "Mmm..."

    scene hangoutopt
    with fade

    menu:
        "You decided to pester..."

        "Ali" if aproj == True: 
            $ aproj = False
            jump ali

        "Coco" if cproj == True: 
            $ cproj = False
            jump coco

        "Nadine" if nproj == True: 
            $ nproj = False
            jump nadine

        "Maria" if mproj == True:
            jump maria
            
        "Your music" if mproj == False:
            jump jukebox

label ali:
    $ points += 1

    "You started texting Ali"
    
    scene msg1
    with fade
    
    d "hey, u free? lets hang out im bored"
    "Two minutes passed and Ali replied."
    
    scene msg2
    
    a "Bored?"
    a "Why don’t you finish some work?"
    a "It’s the perfect opportunity."
    d "but allllliiiiiii"
    d "who does work on a sunnndayyyyyyyy"
    a "…"
    a "Alright, I’m free so let’s see what we can do!"

    scene bg ali
    with fade

    "Being in a sweet tooth mood, Both of you decided to bake a carrot cake."
    "With Alis precised baking skills, you both enjoyed a relaxing tea time!"

    jump hangout


label coco:
    $ points += 1
    $ coco = False

    "You started texting Coco"
    
    scene msg1
    with fade
    
    d "hey, u free? lets hang out im bored"
    "Five minutes passed and Coco replied."
    
    scene msg2
    
    c "huh?"
    c "it’s sunday"
    c "how are you bored?"
    d "I want to escape my responsibilities"
    d "and since you’re online"
    d "."
    d "so are you free?"
    c "well, I don’t really have anything urgent to complete atm"
    c "let’s chill"

    scene bg coco
    with fade

    "You decided to see the fun in skateboarding"
    "Coco attempted to teach you how to stable your balance"
    "Despite the many fails and bruises, you both had fun messing around!"
    jump hangout

label nadine:
    $ points += 1
    $ nadine = False

    "You started texting Nadine"
    
    scene msg1
    with fade
    
    d "hey, u free? lets hang out im bored"
    "An hour passed and Nadine replied."
    
    scene msg2 

    n "?"
    n "h"
    n "what"
    "oh my god"
    d "i have nothing to do"
    d "and i thought maybe you would have nothing to do"
    d "so i thought it would be good to have some fun tgt"
    n "tgt?"
    d "together"
    n "o"
    "A couple of minutes passed"
    n "what will we do"
    d "fun things"
    n "what"
    d "dont worry, if you dont want to hang out, its ok, ill just ask someone else"
    n "wait"
    "More minutes pass, you wonder if this is a bad idea"
    n "ok, i accept"

    scene bg nadine
    with fade

    "With Nadines closed condition, You thought it'd be a good idea to help her explore more."
    "You shared your chill beats with Nadine"
    "Nadine seemed intrigued with the chill beats and offered to share some of her music taste as well, it seems she enjoys classical"
    "Both of you learnt more about each other."
    jump hangout

label maria:
    
    "You started texting Maria"
    
    scene msg1
    with fade
    
    d "hey, u free? lets hang out im bored"
    "A minute passed and Maria replied"
    
    scene msg2 

    m "NYAHAHAHAHA"
    m "YOU DARE REQUEST MOI PRESENCE?"
    m "MOI ACCEPTS"
    d "omg"
    m ">:3c"
    m "meet u at the pit @5"
    m "thy shall witness thE SUNSET WITH MOI"
    d "alright, can't wait"
   
    scene black
    with fade
    scene bg maria1
    with fade
    
    "You spend some time with Maria watching the sunset"
    "Hearing the waves soothed you"
    
    d "..."
    d "Hey Maria."
    d "I feel like today's a special day..."
    m "That's because you witnessed the sun going to bed"
    m "You stalker!"
    "Dana chuckled"
    d "Will I ever be redeemed for doing such a scandelous act?"
    m "Hmm..."
    m "As the messenger of god, The only way you're released from this curse is if you buy me..."
    m "C"
    m "A"
    m "K-"
    d "You already had ice cream"
    m ":c"
    m "I want more"
    d "Maybe I should just be cursed forever"
    m "No fair!"
    "The conversation continues..."
    
    scene bg maria2
    with pushup
    
    "You're glad you hung out with everyone today"
    "{b}The End{/b}"


return