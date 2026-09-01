import json
from pathlib import Path


class HockeyStats:

    def __init__(self, file_name: str):
        self.file_name = (
            file_name if file_name.endswith(".json") else f"{file_name}.json"
        )
        self.data = []

    def load_file(self):
        parent_folder = Path(__file__).parent
        path = parent_folder / self.file_name

        with open(path, "r", encoding="utf-8") as file:
            self.data = json.load(file)

        return self.data

    def player_stats(self, player_name: str):
        for stats in self.data:
            if stats["name"].lower() == player_name.lower():
                return stats
        return None

    def team_abbreviations(self):
        return sorted(set(stats["team"] for stats in self.data))

    def country_abbreviations(self):
        return sorted(set(stats["nationality"] for stats in self.data))

    def players_in_team(self, team: str):
        players = [s for s in self.data if s["team"] == team]
        return sorted(
            players, key=lambda x: (x["goals"] + x["assists"]), reverse=True
        )

    def players_from_country(self, country: str):
        players = [s for s in self.data if s["nationality"] == country]
        return sorted(
            players, key=lambda x: (x["goals"] + x["assists"]), reverse=True
        )

    def most_points(self, n: int):
        return sorted(
            self.data,
            key=lambda x: (x["goals"] + x["assists"], x["goals"]),
            reverse=True,
        )[:n]

    def most_goals(self, n: int):
        return sorted(
            self.data, key=lambda x: (x["goals"], -x["games"]), reverse=True
        )[:n]


class SearchListApplication:

    def __init__(self, file_name: str):
        self._hockeystats = HockeyStats(file_name=file_name)
        self._hockeystats.load_file()

    def print_help(self):
        print("\ncommands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def format_player(self, p: dict) -> str:
        points = p["goals"] + p["assists"]
        return f"{p['name']:20} {p['team']}  {p['goals']:2} + {p['assists']:2} = {points:3}"

    def execute(self):
        self.print_help()

        while True:
            command = input("\ncommand: ").strip()

            if command == "0":
                break
            elif command == "1":
                name = input("name: ")
                player = self._hockeystats.player_stats(name)
                if player:
                    print(self.format_player(player))
                else:
                    print("Player not found")
            elif command == "2":
                for team in self._hockeystats.team_abbreviations():
                    print(team)
            elif command == "3":
                for country in self._hockeystats.country_abbreviations():
                    print(country)
            elif command == "4":
                team = input("team: ")
                for p in self._hockeystats.players_in_team(team):
                    print(self.format_player(p))
            elif command == "5":
                country = input("country: ")
                for p in self._hockeystats.players_from_country(country):
                    print(self.format_player(p))
            elif command == "6":
                n = int(input("how many: "))
                for p in self._hockeystats.most_points(n):
                    print(self.format_player(p))
            elif command == "7":
                n = int(input("how many: "))
                for p in self._hockeystats.most_goals(n):
                    print(self.format_player(p))


if __name__ == "__main__":
    file_input = input("file name: ")
    app = SearchListApplication(file_input)
    app.execute()