from Numerology import Numerology

class NumerologyLifePathDetails(Numerology):
    def __init__(self, Name: str, DateOfBirth: str):
        super().__init__(Name, DateOfBirth)


    @property
    def Name(self) -> str:
        return self.name

    @property
    def Birthdate(self) -> str:
        return self.birthdate

    @property
    def LifePath(self) -> int:
        return self.lifePath

    @property
    def BirthDay(self) -> int:
        return self.birthDay

    @property
    def Attitude(self) -> int:
        return self.attitude

    @property
    def Soul(self) -> int:
        return self.soul

    @property
    def Personality(self) -> int:
        return self.personality

    @property
    def PowerName(self) -> int:
        return self.powerName

    @property
    def LifePathDescription(self) -> str:

        descriptions = {
            1: "The Independent: Wants to work/think for themselves",
            2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art and to perform or get attention",
            4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer: Likes to travel and meet others, often a extrovert",
            6: "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality",
            8: "The Executive: Gravitates to money and power",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way"
        }
        return descriptions[self.LifePath]