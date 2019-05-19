class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.object[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc


class Goblin(GameObject):
    def __init__(self, name):
        super().__init__(name)
        self.class_name = "Goblin"
        self.health = 3
        self.desc = "a foul creature"

    @property
    def desc(self):
        health_line = ""
        if self.health >= 3:
            return self.desc
        elif self.health == 2:
            health_line = "it has a wound on its knee"
        elif self.health == 1:
            health_line = "its left arm has been cut off"
        elif self.health <= 0:
            health_line = "it dead"
        return self.desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self.desc = value


def hit(noun):
    msg = ""
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin:
            thing.heath = thing.heath - 1
            if thing.heath <= 0:
                msg = "you kill the goblin"
            else:
                msg = "you hit the {}".format(thing.class_name)
    else:
        msg = "there is no {} here".format(noun)
    return msg


def get_input():
    command = input("input verb: ").split()
    verb_word = command[0]
    if verb_word in ver_dic:
        verb = ver_dic[verb_word]
    else:
        print("Unknown verb {}".format(verb_word))
        return
    if len(command) > 1:
        noun_word = command[1]
        print(hit(noun_word))
    else:
        print(hit("nothing"))





ver_dic = {
    "say": "say",
    "hit": "hit"
}

while True:
    get_input()
