from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        # This is a catchall for the case that the programmer writes a new
        # Scene subclass and forgets to add an enter() function.
        # Implicit inheritence will allow for this error message to show the
        # developer their mistake with a useful error message.
        print("This scene has not been configured with an enter method.")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n----------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):

    quips = ['He\'s dead, Jim.',
            'Your arm\'s off!',
            '\t\tYour face is impregnated by an alien creature. You receive no\n\
            child support from the alien\'s father until it is drafted by the\n\
            NFL. After all the sacrifices you\'ve made the alien wants to\n\
            repair the broken family, but you see through it. The argument\n\
            becomes heated, and  at the high of the fight, your alien\n\
            daughter walks in, startling her alien father queen. Your\n\
            daughter and her bright future is now bleeding out acid onto the\n\
            floor of your two bedroom apartment. You hold her as the light\n\
            fades from her eyes and the alien queen that killed her slips out\n\
            of the window in then kitchen. You don\'t die,\n\
            but you wish it had been you instead.',
            'You died.']

    def enter(self):
        print(self.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print("You're on a space ship. Get off of it. Blow it up. Do it")
        print("in whatever order you want.")
        print("There's an alien or whatever that looks like it's gonna kill")
        print("you though because it has a gun pointed at you.")
        print("Also, it's standing in front of a door that says \"Armory\".")
        print("I feel that might be important.")

        response = input("(Enter a number)\n 1. Shoot\n 2. Seduce\n 3. Tell a joke\n > ")

        if response == '1':
            print("You reach for your gun, but you forgot")
            print("this alien was already pointing a gun at you.")
            # The line below works, but is not how the author does it
            #a_map.next_scene('death').enter()

            # The author decides to have the engine handle the calling of any
            # Map methods. This way, each scene should only have to return
            # a string from the result of the player's responses.
            return 'death'
        elif response == '2':
            print("You fumble around the alien's body in an attempt to seduce.")
            return 'death'
        elif response == '3':
            print("I can't be bother to think of what you said.")
            print("He laughs and you shoot him.")
            return 'laser_weapon_armory'
        else:
            print("I dunno what that means.\nTry again.")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print("You walk into the Weapon Armory.")
        print("It's empty, except for the big box labeled \"BOMB\" in the center of the room")
        print("There's a keypad lock and you need the code to get the bomb out.")
        print("If you get the code wrong 10 times then the lock closes forever.")
        print("The code is 3 digits.")
        code = "%d%d%d" % (randint(1,9),randint(1,9),randint(1,9))
        guess = input("[keypad]>")
        guesses = 0

        while guess != code and guesses < 10:

            if guess == 'hint?':
                print("You look around the box to find a sticky note with the numbers %s" % code)
            print("Try again")
            guesses += 1
            guess = input("[keypad]>")


        if guess == code:
            print("You did it. You got the bomb.")
            return 'the_bridge'
        else:
            print("You didn't do it. Aliens came because you took too long.")
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print("Look. If you got that code, then at this point, I don't think either of us care if you take the bomb to the bridge or not.")
        print("Describe in elaborate detail what you do with the bomb.")
        print("Just remember to have it ending with you searching for an escape pod.")
        who_cares = input(">")

        if len(who_cares) >= 10:
            return 'escape_pod'
        else:
            print("I said DETAILED. I can't believe you messed that up.")
            return 'death'

class EscapePod(Scene):

    def enter(self):
        print("You rush to the escape pod. Apparently the aliens don't care and want to die.")
        print("Looks like you have a few options for escape pods. Some options suck.")
        print("But you don't care to check or anything. You sorta want to die too.")
        print("Which one do you want? There are 3 pods.")

        good_pod = randint(1,3)
        guess  = input("[pod #]>")

        if int(guess) != good_pod:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod escapes out into the void of space,")
            print("you get a feeling that you should have picked pod %s"
                    % good_pod)
            return 'death'
        else:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod escapes out into the void of space, then")
            print("flies down to your home planet below. You did it. You won.")
            exit(0)


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
