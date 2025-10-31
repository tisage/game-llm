"""
Game Core Package - Backend logic for Snake Game
"""
from .constants import *
from .snake import Snake
from .food import Food
from .collision import CollisionDetector
from .scoring import ScoreManager
from .game_state import GameEngine

__all__ = ['Snake', 'Food', 'CollisionDetector', 'ScoreManager', 'GameEngine', 'GameState', 'UP', 'DOWN', 'LEFT', 'RIGHT']