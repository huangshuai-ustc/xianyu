# Contains the data for the comprpg game.
# This is the full version of the data used in the game.
# This file is intended to be visible to students.

all_characters = [
    {
        "name": "Binary Bot",
        "max_health": 20,
        "attack_moves": [
            {
                "name": "Binary Blast",
                "damage": 5,
                "target": 1,
                "cost": 5,
            },
            {
                "name": "Keyboard Bash",
                "damage": 2,
                "target": 1,
                "cost": 0,
            },
            {
                "name": "Assembly Attack",
                "damage": 2,
                "target": 2,
                "cost": 1,
            }
        ],
        "defend_moves": [
            {
                "name": "Firewall",
                "protect": 2,
                "cost": 0,
            }
        ]
    },
    {
        "name": "Python Pal",
        "max_health": 22,
        "attack_moves": [
            {
                "name": "Syntax Strike",
                "damage": 4,
                "target": 1,
                "cost": 3,
            },
            {
                "name": "Indentation Impact",
                "damage": 3,
                "target": 1,
                "cost": 2,
            },
            {
                "name": "Commenting Crush",
                "damage": 1,
                "target": 2,
                "cost": 0,
            }
        ],
        "defend_moves": [
            {
                "name": "Try-except Tactics",
                "protect": 5,
                "cost": 3,
            },
            {
                "name": "Duck Type Dodge",
                "protect": 1,
                "cost": 0,
            }
        ]
    },
    {
        "name": "Network Ninja",
        "max_health": 15,
        "attack_moves": [
            {
                "name": "DDoS",
                "damage": 3,
                "target": 1,
                "cost": 1,
            },
            {
                "name": "Code Injection",
                "damage": 10,
                "target": 1,
                "cost": 15,
            },
            {
                "name": "Packet Sniffer",
                "damage": 1,
                "target": 2,
                "cost": 0,
            }
        ],
        "defend_moves": [
            {
                "name": "Firewall",
                "protect": 2,
                "cost": 0,
            },
            {
                "name": "VPN Tunnel",
                "protect": 5,
                "cost": 5,
            }
        ]
    },
    {
        "name": "HTML Hero",
        "max_health": 25,
        "attack_moves": [
            {
                "name": "Entity Eruption",
                "damage": 2,
                "target": 2,
                "cost": 2,
            },
            {
                "name": "CSS Crusade",
                "damage": 3,
                "target": 1,
                "cost": 2,
            },
            {
                "name": "JavaScript Jab",
                "damage": 1,
                "target": 1,
                "cost": 0,
            }
        ],
        "defend_moves": [
            {
                "name": "Firewall",
                "protect": 2,
                "cost": 0,
            },
            {
                "name": "Websafe Wand",
                "protect": 5,
                "cost": 5,
            }
        ]
    },
    {
        "name": "C Charmer",
        "max_health": 20,
        "attack_moves": [
            {
                "name": "Pointer Pinch",
                "damage": 1,
                "target": 2,
                "cost": 0,
            },
            {
                "name": "Malloc Maul",
                "damage": 4,
                "target": 1,
                "cost": 3,
            },
            {
                "name": "Segfault Slam",
                "damage": 2,
                "target": 2,
                "cost": 2,
            }
        ],
        "defend_moves": [
            {
                "name": "Compiler Crash",
                "protect": 3,
                "cost": 0,
            },
            {
                "name": "Buffer Overflow Block",
                "protect": 7,
                "cost": 5,
            }
        ]
    },
    {
        "name": "Java Judger",
        "max_health": 15,
        "attack_moves": [
            {
                "name": "Exception Eruption",
                "damage": 4,
                "target": 2,
                "cost": 3,
            },
            {
                "name": "Object Oriented Obliteration",
                "damage": 6,
                "target": 1,
                "cost": 6,
            },
        ],
        "defend_moves": [
            {
                "name": "Encapsulator",
                "protect": 5,
                "cost": 2,
            }
        ]
    },
    {
        "name": "Haskell Heroine",
        "max_health": 18,
        "attack_moves": [
            {
                "name": "Lambda Lunge",
                "damage": 3,
                "target": 1,
                "cost": 0,
            },
            {
                "name": "Monadic Might",
                "damage": 5,
                "target": 1,
                "cost": 2,
            },
        ],
        "defend_moves": [
            {
                "name": "Functional Fortress",
                "protect": 5,
                "cost": 3,
            },
            {
                "name": "Recursion Rebuff",
                "protect": 2,
                "cost": 0,
            }
        ]
    },
    {
        "name": "Hardware Hacker",
        "max_health": 25,
        "attack_moves": [
            {
                "name": "Harddrive Hit",
                "damage": 3,
                "target": 1,
                "cost": 0,
            },
            {
                "name": "Overclocking Overload",
                "damage": 6,
                "target": 1,
                "cost": 4,
            },
            {
                "name": "Power Surge",
                "damage": 2,
                "target": 2,
                "cost": 0,
            }
        ],
        "defend_moves": [
            {
                "name": "Firewall",
                "protect": 2,
                "cost": 0,
            },
            {
                "name": "Cable Disconnection",
                "protect": 5,
                "cost": 3,
            },
        ]
    },
    {
        "name": "Linux Legend",
        "max_health": 20,
        "attack_moves": [
            {
                "name": "Kernel Kick",
                "damage": 4,
                "target": 1,
                "cost": 3,
            },
            {
                "name": "Bash Bonk",
                "damage": 2,
                "target": 1,
                "cost": 0,
            },
            {
                "name": "Root Reckoning",
                "damage": 4,
                "target": 2,
                "cost": 5,
            }
        ],
        "defend_moves": [
            {
                "name": "Firewall",
                "protect": 2,
                "cost": 0,
            },
            {
                "name": "Sudo Shield",
                "protect": 5,
                "cost": 3,
            }
        ]
    }
]

all_items = [
    {
        "name": "Reboot in Safe Mode",
        "description": "Heals 5 health",
        "health": 5,
        "price": 15,
    },
    {
        "name": "Screen Repair Kit",
        "description": "Heals 10 health",
        "health": 10,
        "price": 30,
    },
    {
        "name": "RAM Boost",
        "description": "Increases damage by 2 when attacking. Lasts 3 turns.",
        "damage": 2,
        "turns": 3,
        "price": 10,
    },
    {
        "name": "Debugging Tool",
        "description": "Automatically protects by 2. Lasts 3 turns.",
        "protect": 2,
        "turns": 3,
        "price": 10,
    },
    {
        "name": "Backup Battery",
        "description": "Recharges 10 electricity",
        "electricity": 10,
        "price": 20,
    },
    {
        "name": "USB-C Charger",
        "description": "Recharges 20 electricity",
        "electricity": 20,
        "price": 30,
    }
]
