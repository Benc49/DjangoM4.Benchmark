from django.test import TestCase
from app import models
class TestPlayer(TestCase):
    def test_can_create_player(self):
        player = models.create_player(
            "Ben",
            "14",
            "Qb",
            True,
        )
        self.assertEqual(player.id, 1)
        self.assertEqual(player.name, "Ben")
        self.assertEqual(player.number, "14")
        self.assertTrue(player.is_star)
    def test_can_view_all_players_at_once(self):
        players_data = [
            {
                "name": "Jim",
                "number": 58,
                "position": "LG",
                "is_star": True,
            },
            {
                "name": "Mike Vick",
                "number": 7,
                "position": "Qb",
                "is_star": True,
            },
            {
                "name": "Joe",
                "number": 58,
                "position": "RG",
                "is_star": False,
            },
        ]
        for player_data in players_data:
            models.create_player(
                player_data["name"],
                player_data["number"],
                player_data["position"],
                player_data["is_star"],
            )
        players = models.all_players()
        self.assertEqual(len(players), len(players_data))
        players_data = sorted(players_data, key=lambda c: c["name"])
        players = sorted(players, key=lambda c: c.name)
        for data, player in zip(players_data, players):
            self.assertEqual(data["name"], player.name)
            self.assertEqual(data["number"], player.number)
            self.assertEqual(data["position"], player.position)
            self.assertEqual(data["is_star"], player.is_star)
    def test_can_search_by_name(self):
        players_data = [
            {
                "name": "Jim",
                "number": "58",
                "position": "LG",
                "is_star": True,
            },
            {
                "name": "Mike Vick",
                "number": "7",
                "position": "Qb",
                "is_star": True,
            },
            {
                "name": "Joe",
                "number": 58,
                "position": "RG",
                "is_star": False,
            },
        ]
        for player_data in players_data:
            models.create_player(
                player_data["name"],
                player_data["number"],
                player_data["position"],
                player_data["is_star"],
            )
        self.assertIsNone(models.find_player_by_name("aousnth"))
        player = models.find_player_by_name("Joe")
        self.assertIsNotNone(player)
        self.assertEqual(player.number, 58)
    def test_can_view_favorites(self):
        players_data = [
            {
                "name": "Jim",
                "number": 58,
                "position": "LG",
                "is_star": True,
            },
            {
                "name": "Mike Vick",
                "number": "7",
                "position": "Qb",
                "is_star": True,
            },
            {
                "name": "Joe",
                "number": "58",
                "position": "RG",
                "is_star": False,
            },
        ]
        for player_data in players_data:
            models.create_player(
                player_data["name"],
                player_data["number"],
                player_data["position"],
                player_data["is_star"],
            )
        self.assertEqual(len(models.star_player()), 2)
    def test_can_update_players_position(self):
        players_data = [
            {
                "name": "Jim",
                "number": 58,
                "position": "LG",
                "is_star": True,
            },
            {
                "name": "Mike Vick",
                "number": 7,
                "position": "Qb",
                "is_star": True,
            },
            {
                "name": "Joe",
                "number": 58,
                "position": "RG",
                "is_star": False,
            },
        ]
        for player_data in players_data:
            models.create_player(
                player_data["name"],
                player_data["number"],
                player_data["position"],
                player_data["is_star"],
            )
        models.update_player_position("Joe", "LG")
        self.assertEqual(
            models.find_player_by_name("Joe").position, "LG"
        )
    def test_can_delete_player(self):
        players_data = [
            {
                "name": "Jim",
                "number": "58",
                "position": "LG",
                "is_star": True,
            },
            {
                "name": "Mike Vick",
                "number": "7",
                "position": "Qb",
                "is_star": True,
            },
            {
                "name": "Joe",
                "number": "58",
                "position": "RG",
                "is_star": False,
            },
        ]
        for player_data in players_data:
            models.create_player(
                player_data["name"],
                player_data["number"],
                player_data["position"],
                player_data["is_star"],
            )
        models.delete_player("Jim")
        self.assertEqual(len(models.all_players()), 2)
