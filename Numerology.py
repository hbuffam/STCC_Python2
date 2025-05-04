#Holly Buffam

class Numerology:
    def __init__(self, sName, sDOB):
        self.name = sName
        self.birthdate = sDOB

        digits = [int(ch) for ch in sDOB if ch.isdigit()]
        self.lifePath = self._reduceNumber(sum(digits))

        day = int(sDOB[3:5])
        self.birthDay = self._reduceNumber(sum(int(d) for d in str(day)))

        month_day_digits = [int(ch) for ch in sDOB[:5] if ch.isdigit()]
        self.attitude = self._reduceNumber(sum(month_day_digits))

        self._char_map = {
            **dict.fromkeys(list("AJS"), 1),
            **dict.fromkeys(list("BKT"), 2),
            **dict.fromkeys(list("CLU"), 3),
            **dict.fromkeys(list("DMV"), 4),
            **dict.fromkeys(list("ENW"), 5),
            **dict.fromkeys(list("FOX"), 6),
            **dict.fromkeys(list("GPY"), 7),
            **dict.fromkeys(list("HQZ"), 8),
            **dict.fromkeys(list("IR"), 9),
        }

        soul_sum = 0
        personality_sum = 0
        for ch in sName.upper():
            val = self._char_map.get(ch, 0)
            if ch in "AEIOU":
                soul_sum += val
            elif ch.isalpha():
                personality_sum += val

        self.soul = self._reduceNumber(soul_sum)
        self.personality = self._reduceNumber(personality_sum)

        self.powerName = self._reduceNumber(self.soul + self.personality)

    def _reduceNumber(self, num: int) -> int:
        #Reduce any multi‑digit number down to a single digit 1–9
        while num > 9:
            num = sum(int(d) for d in str(num))
        return num

    def getName(self) -> str:
        return self.name

    def getBirthdate(self) -> str:
        return self.birthdate

    def getLifePath(self) -> int:
        return self.lifePath

    def getBirthDay(self) -> int:
        return self.birthDay

    def getAttitude(self) -> int:
        return self.attitude

    def getSoul(self) -> int:
        return self.soul

    def getPersonality(self) -> int:
        return self.personality

    def getPowerName(self) -> int:
        return self.powerName
