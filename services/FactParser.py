from typing import List


class FactParser:

    @staticmethod
    def getAllFacts() -> List[str]:
        allFacts = list()
        with open("C:\\Users\\14143\\PycharmProjects\\snapple-fax-api\\snapple_fax.txt", "r", encoding="utf-8") as fp:
            for line in fp:
                # we take all text after the first comma in the line
                allFacts.append(line.split(",", 1)[1].strip())
        return allFacts
