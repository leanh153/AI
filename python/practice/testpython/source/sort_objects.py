from operator import attrgetter

nums = [32, 1, 23, 4, 2, 3]

print(sorted(nums))
print("------------------")


class Language:

    def __init__(self, name, lang_id):
        self.name = name
        self.lang_id = lang_id

    def __repr__(self):
        return "{:2d} : {:s}".format(self.lang_id, self.name)


lang_list = [
    Language("python", 4),
    Language("C#", 4),
    Language("css", 3),
    Language("html", 5),
    Language("php", 0)
]

for lang in lang_list:
    print(lang)

print("------------------")

sorted_list = sorted(lang_list, key=attrgetter("lang_id"))

for lang in sorted_list:
    print(lang)
