import webbrowser

from thomas_skills.abstract_thomas_skill import AbstractThomasSkill


class MusicSkill(AbstractThomasSkill):
    def run_skill(self, command=None):
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        webbrowser.open(url, new=0, autoraise=True)
