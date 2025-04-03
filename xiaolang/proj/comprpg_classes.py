# A simplified version of the classes used in the Comprpg game.
# This version is intended to be visible to students.
# It is not the full version of the classes used in the game.

from comprpg_data import all_characters
from copy import deepcopy, copy
import random

N_PLAYERS = 2
N_CHARACTERS = 5
MONEY_MIN_MAX = (20, 60)
ELECTRICITY_MIN_MAX = (40, 50)

NAME = "name"
HEALTH = "health"
DEFENCE = "defence"
DEFEATED = "defeated"
EFFECTS = "effects"
MAX_HEALTH = "max_health"


class Player():
    """ This class stores the state of the player. """

    def __init__(self, player_id, characters, money, electricity,
                 active_characters=None, items=None, n_active=2):
        """ initialising the Player object """
        # the id of the player (index in the list of players in the game state)
        self.player_id = player_id
        # list of available characters for this player
        self.characters = deepcopy(characters)
        # player will choose active players at beginning of the game
        if active_characters is not None:
            self.active_characters = deepcopy(active_characters)
        else:
            self.active_characters = []
        # player will choose items at beginning of the game
        if items is not None:
            self.items = deepcopy(items)
        else:
            self.items = []
        # the amount of money the player has
        self.money = money
        # the amount of electricity the player has
        self.electricity = electricity
        # the number of active characters
        self.n_active = n_active

    def __copy__(self):
        """ This method is called when the copy() function is
        called on the object. """

        # copy the characters and items lists
        characters = [deepcopy(character) for character in self.characters]
        items = [deepcopy(item) for item in self.items]
        active_characters = copy(self.active_characters)

        # create a new Player object with the same attributes
        new_player = Player(
            player_id=self.player_id,
            characters=characters,
            money=self.money,
            electricity=self.electricity,
            active_characters=active_characters,
            items=items,
            n_active=self.n_active,
        )

        return new_player

    def __repr__(self):
        """ This method is called when the Player object is printed or shown in
        the terminal. It returns a string representation of the object. """

        player_str = "Player({}, {}, {}, {}, {}, {}, {})".format(
            self.player_id,
            self.characters,
            self.money,
            self.electricity,
            self.active_characters,
            self.items,
            self.n_active,
        )
        return player_str

    def __eq__(self, other):
        """ This method is called when comparing two Player objects using the
        == operator. It returns True if the two objects are equal, False
        otherwise. """

        if not isinstance(other, Player):
            return False

        if not self.same_elements(self.characters, other.characters):
            return False

        if not self.same_elements(self.active_characters,
                                  other.active_characters):
            return False

        if not self.same_elements(self.items, other.items):
            return False

        return (
                self.player_id == other.player_id
                and self.money == other.money
                and self.electricity == other.electricity
                and self.n_active == other.n_active
        )

    def __ne__(self, other):
        """ This method is called when comparing two Player objects using the
        != operator. It returns True if the two objects are not equal, False
        otherwise. """

        return not self.__eq__(other)

    def same_elements(self, list1, list2):
        """ Helper method for checking lists of dictionaries.
        Note: assumes at least one of the lists has no duplicates. """
        for element in list1:
            if element not in list2:
                return False

        for element in list2:
            if element not in list1:
                return False

        if len(list1) != len(list2):
            return False

        return True

    def get_character(self, character_name):
        """ returns the character dictionary with the given name or None. """

        for character in self.characters:
            if character[NAME] == character_name:
                return character
        return None


class Game():
    """ This class stores the state of the game. """

    def __init__(self, players=None, turn=0, history=None):
        """ initialising the Game object.
        If players is None, then they are initialised randomly."""

        if players is not None:
            self.players = players
        else:
            # initialise the players
            self.players = []
            for player_id in range(N_PLAYERS):
                # choose 5 random characters for each player
                characters = [deepcopy(char) for char in random.sample(all_characters, N_CHARACTERS)]
                # set the health of each character to its maximum health
                for character in characters:
                    character[HEALTH] = character[MAX_HEALTH]
                    character[DEFEATED] = False
                # set defence of each character to 0
                for character in characters:
                    character[DEFENCE] = 0
                # set temporary effects list to empty for each character
                for character in characters:
                    character[EFFECTS] = []
                # randomly assign money and electricity to each player
                money = random.randint(*MONEY_MIN_MAX)
                electricity = random.randint(*ELECTRICITY_MIN_MAX)
                # create a player object and append it to the list of players
                player = Player(player_id, characters, money, electricity)
                self.players.append(player)

        # initialise the turn (default is 0)
        self.turn = turn

        # this will store the history of the game
        if history is not None:
            self.history = history
        else:
            self.history = []

    def __copy__(self):
        """ This method is called when the copy() function is called
          on the object. """

        # create a new Game object with the same players, turn, and history
        new_game = Game(
            players=[copy(player) for player in self.players],
            turn=self.turn,
            history=deepcopy(self.history),
        )

        return new_game

    def __repr__(self):
        """ This method is called when the object is printed or displayed
          in the terminal. It returns a string representation. """

        game_str = f"Game({self.players}, {self.turn}, {self.history})"

        return game_str

    def __eq__(self, other):
        """ This method is called when comparing two Game objects using the
        == operator. It returns True if the two objects are equal, False
        otherwise. """

        if not isinstance(other, Game):
            return False

        return (
                self.players == other.players
                and self.turn == other.turn
                and self.history == other.history
        )

    def __ne__(self, other):
        """ This method is called when comparing two Game objects using the
        != operator. It returns True if the two objects are not equal, False
        otherwise. """

        return not self.__eq__(other)
