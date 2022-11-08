from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        deformalized = toml.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            deformalized["tool"]["poetry"]["name"],
            deformalized["tool"]["poetry"]["description"],
            deformalized["tool"]["poetry"]["dependencies"], # .keys()
            deformalized["tool"]["poetry"]["dev-dependencies"]
        )
