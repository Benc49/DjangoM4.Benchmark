from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.TextField()
    number = models.PositiveIntegerField()
    position = models.TextField()
    is_star = models.BooleanField()

def create_player(name, number, position, is_star):
    player = Player(name = name, number = number, position = position, is_star = is_star)
    player.save()
    return player

def all_players():
    return Player.objects.all()

def find_player_by_name(name):
    try:
        return Player.objects.get(name = name)
    except:
        None

def star_player():
    return Player.objects.filter(is_star = True)

def update_player_position(name, new_position):
    player = Player.objects.get(name = name)
    player.position = new_position
    player.save()

def delete_player(name):
    player = Player.objects.get(name = name)
    player.delete()

