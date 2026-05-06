from __future__ import annotations # https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-deferred-annotations
from enum import Enum, auto

class State(Enum):
	NO_TOKEN = auto()
	ONE_TOKEN = auto()
	BOULE_SURPRISE_SELL = auto()
	NO_BALLS_SURPRISE = auto()

class GiftBall:
	def __init__(self, surprise_ball_count: int = 0) -> None:
		if surprise_ball_count < 0:
			raise ValueError("surprise_ball_count must be >= 0")

		self.surprise_ball_count = surprise_ball_count
		self.current_state = (
			State.NO_TOKEN if surprise_ball_count > 0 else State.NO_BALLS_SURPRISE
		)

	def insert_token(self) -> None:
		if self.current_state == State.NO_TOKEN and self.surprise_ball_count > 0:
			self.current_state = State.ONE_TOKEN

	def eject_token(self) -> None:
		if self.current_state == State.ONE_TOKEN:
			self.current_state = State.NO_TOKEN

	def turn_crank(self) -> None:
		if self.current_state == State.ONE_TOKEN:
			self.current_state = State.BOULE_SURPRISE_SELL

	def dispense_ball(self) -> None:
		if self.current_state != State.BOULE_SURPRISE_SELL:
			return

		if self.surprise_ball_count > 0:
			self.surprise_ball_count -= 1

		self.current_state = (
			State.NO_TOKEN
			if self.surprise_ball_count > 0
			else State.NO_BALLS_SURPRISE
		)