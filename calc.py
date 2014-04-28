from collections import OrderedDict

class Worker():
    hourly_wage = 0

    def __init__(self, wage):
        self.hourly_wage = wage


class Task():
    
    def __str__(self):
        line = "{name}:{space}hours:{hours}\tcapex:{capex}\top:{opex}\tsub:{sub}"
        
        variables = {
                "name": self.name, 
                "space": space(25, len(self.name)),
                "hours": self.hours,
                "capex": self.capex,
                "opex": self.non_capex,
                "sub": self.subtotal
        }
        
        return line.format(**variables)
                    
    def __init__(self, name, who, hours, non_capex=0):

        self.name = name
        self.hours = hours
        self.capex = who.hourly_wage * hours
        self.non_capex = non_capex
        self.subtotal = self.capex + non_capex



def space(max, length):
    return " " * (max - length)


ATTENDEES = 50

# food budget for each event
FOOD = 13 * ATTENDEES

PRINTING = 50

MISC = 100

# event cost
EVENT = FOOD + PRINTING + MISC

sec_aware = Worker(40)

isac = Worker(40)

ciso = Worker(85)


tasks = [
    Task("Assign SecAware Team", ciso, 1),
    Task("Review Purchase Materials", sec_aware, 40),
    Task("Develop Tests", sec_aware, 22),
    Task("Migrate Materials", sec_aware, 4),
    Task("Web Platform", sec_aware, 80),
    Task("Appoint ISAC", ciso, 1),
    Task("Pre tests", isac, 0.5),
    Task("Curriculum 1", sec_aware, 60),
    Task("Event 1", sec_aware, 8, EVENT),
    Task("Curriculum 2", sec_aware, 60),
    Task("Event 2", sec_aware, 8, EVENT),
    Task("Curriculum 3", sec_aware, 60),
    Task("Event 3", sec_aware, 8, EVENT),
    Task("Curriculum 4", sec_aware, 60),
    Task("Event 4", sec_aware, 8, EVENT),
    Task("Post Test", isac, 1),
    Task("Feedback", sec_aware, 1),
    Task("Evaluate", sec_aware, 16),
    Task("Report", sec_aware, 8),
    Task("Revise", sec_aware, 40)
]

if __name__ == "__main__":
    
    print("Per Event:%s$%d" % (space(25, len("Per Event")), EVENT))
    
    total = 0

    for task in tasks:

        total += task.subtotal

        print(task)

    print("Total:%s$%d" % (space(25, len("Total")), total))
