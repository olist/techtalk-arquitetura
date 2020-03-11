import logging
from collections import Counter

import httpx

from .config import settings
from .exceptions import HandlerException

logger = logging.getLogger(__name__)


class TeamHandler:
    def handle(self, message, *args):
        home_team_name = message["home_team_name"]
        home_team_score = message["home_team_score"]
        guest_team_name = message["guest_team_name"]
        guest_team_score = message["guest_team_score"]

        self.process_match(home_team_name, home_team_score, guest_team_score)
        self.process_match(guest_team_name, guest_team_score, home_team_score)

        return True

    def process_match(self, name, goals, goals_conceded):
        team = self.get_team(name)
        if not team:
            team = self.create_team(name)

        if goals > goals_conceded:
            team["points"] += 3
            team["wins"] += 1
        elif goals < goals_conceded:
            team["losses"] += 1
        else:
            team["points"] += 1
            team["draws"] += 1

        team["matches"] += 1
        team["goals"] += goals
        team["goals_conceded"] += goals_conceded

        self.update_team(team)

        msg = f"team_updated, {team=!r}"
        logger.info(msg)

    def get_team(self, name):
        params = {"name": name}
        response = httpx.get(f"{settings.TEAMS_API_URL}/", params=params)
        if response.status_code != 200:
            msg = f"get_team_error, status_code={response.status_code}, content={response.text}"
            logger.error(msg)
            raise HandlerException(msg)

        return next(iter(response.json()["results"]), None)

    def create_team(self, name):
        data = {"name": name}

        response = httpx.post(f"{settings.TEAMS_API_URL}/", json=data)
        if response.status_code != 201:
            msg = f"create_team_error, status_code={response.status_code}, content={response.text}"
            logger.error(msg)
            raise HandlerException(msg)

        return response.json()

    def update_team(self, data):
        tid = data["id"]
        response = httpx.patch(f"{settings.TEAMS_API_URL}/{tid}", data=data)
        if response.status_code != 200:
            msg = f"update_team_error, status_code={response.status_code}, content={response.text}"
            logger.error(msg)
            raise HandlerException(msg)

        return response.json()


class PlayerHandler:
    def handle(self, message, *args):
        players = Counter(message["home_team_goals"] + message["guest_team_goals"])

        # criar dict com players com count
        for name, goals in players.items():
            self.process_player(name, goals)

        return True

    def process_player(self, name, goals):
        player = self.get_player(name)
        if not player:
            player = self.create_player(name)

        player["goals"] += goals

        self.update_player(player)

        msg = f"player_updated, {player=!r}"
        logger.info(msg)

    def get_player(self, name):
        params = {"name": name}
        response = httpx.get(f"{settings.PLAYERS_API_URL}/", params=params)
        if response.status_code != 200:
            msg = f"get_palyer_error, status_code={response.status_code}, content={response.text}"
            logger.error(msg)
            raise HandlerException(msg)

        return next(iter(response.json()["results"]), None)

    def create_player(self, name):
        data = {"name": name, "position": "tbd"}

        response = httpx.post(f"{settings.PLAYERS_API_URL}/", json=data)
        if response.status_code != 201:
            msg = f"create_player_error, status_code={response.status_code}, content={response.text}"
            logger.error(msg)
            raise HandlerException(msg)

        return response.json()

    def update_player(self, data):
        pid = data["id"]
        response = httpx.patch(f"{settings.PLAYERS_API_URL}/{pid}", data=data)
        if response.status_code != 200:
            msg = f"update_player_error, status_code={response.status_code}, content={response.text}"
            logger.error(msg)
            raise HandlerException(msg)

        return response.json()


def error_handler(exc_info, message):
    logger.error(f"error, {exc_info=!r}, {message=!r}")
