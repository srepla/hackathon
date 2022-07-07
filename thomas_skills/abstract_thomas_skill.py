from abc import ABC, abstractmethod


class AbstractThomasSkill(ABC):

    @abstractmethod
    def run_skill(self):
        pass