from collections import OrderedDict

def space(length):
    return " " * (35 - length)


# CISO gets paid $85 / hour
CISO = 85

# SecAware team average wage / hour
SEC_AWARE = 40

ATTENDEES = 50

# food budget for each event
FOOD = 13 * ATTENDEES

PRINTING = 50

MISC = 100

# event cost
EVENT = FOOD + PRINTING + MISC

# ISAC wage / hour
ISAC = 40

costs = OrderedDict([
    ("Assign SecAware Team", CISO * 1),
    ("Review Purchase Materials", 1600),
    ("Develop Tests", SEC_AWARE * 22),
    ("Migrate Materials", SEC_AWARE * 4),
    ("Web Platform", SEC_AWARE * 80),
    ("Appoint ISAC", CISO * 1),
    ("Pre tests", ISAC * 0.5),
    ("Curriculum 1", SEC_AWARE * 40),
    ("Event 1", SEC_AWARE * 4 + EVENT),
    ("Curriculum 2", SEC_AWARE * 40),
    ("Event 2", SEC_AWARE * 4 + EVENT),
    ("Curriculum 3", SEC_AWARE * 40),
    ("Event 3", SEC_AWARE * 4 + EVENT),
    ("Curriculum 4", SEC_AWARE * 40),
    ("Event 4", SEC_AWARE * 4 + EVENT),
    ("Post Test", ISAC * 1),
    ("Feedback", SEC_AWARE * 1),
    ("Evaluate", SEC_AWARE * 16),
    ("Report", SEC_AWARE * 8),
    ("Revise", SEC_AWARE * 40)
])

if __name__ == "__main__":
    
    print("Per Event:%s$%d" % (space(len("Per Event")), EVENT))
    
    total = 0

    for key in costs.keys():

        subtotal = costs[key]

        total += subtotal

        print("%s:%s$%d" % (key, space(len(key)), subtotal))

    print("Total:%s$%d" % (space(len("Total")), total))
