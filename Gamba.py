from __future__ import annotations # https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-deferred-annotations
from abc import ABC, abstractmethod # Abstract conversion
from sre_parse import State

class StateInterface(ABC):
	# Abstract interface {GiftBall states}
	@abstractmethod
	def insert_token(self, gift_ball: GiftBall) -> None:
		pass

	@abstractmethod
	def eject_token(self, gift_ball: GiftBall) -> None:
		pass

	@abstractmethod
	def turn_crank(self, gift_ball: GiftBall) -> None:
		pass

	@abstractmethod
	def dispense_ball(self, gift_ball: GiftBall) -> None:
		pass

class NoTokenState(StateInterface):
	# state when /any token -> insert
	def insert_token(self, gift_ball: GiftBall) -> None:
		if gift_ball.surprise_ball_count > 0:
			gift_ball.current_state = OneTokenState()

	def eject_token(self, gift_ball: GiftBall) -> None:
		pass

	def turn_crank(self, gift_ball: GiftBall) -> None:
		pass

	def dispense_ball(self, gift_ball: GiftBall) -> None:
		pass

class OneTokenState(StateInterface):
	# state when a token -> insert

	def insert_token(self, gift_ball: GiftBall) -> None:
		pass

	def eject_token(self, gift_ball: GiftBall) -> None:
		gift_ball.current_state = NoTokenState()

	def turn_crank(self, gift_ball: GiftBall) -> None:
		gift_ball.current_state = BouleSurpriseVendoState()

	def dispense_ball(self, gift_ball: GiftBall) -> None:
		pass

class BouleSurpriseVendoState(StateInterface):
	#  after the crank -> turned

	def insert_token(self, gift_ball: GiftBall) -> None:
		pass

	def eject_token(self, gift_ball: GiftBall) -> None:
		pass

	def turn_crank(self, gift_ball: GiftBall) -> None:
		pass

	def dispense_ball(self, gift_ball: GiftBall) -> None:
		if gift_ball.surprise_ball_count > 0:
			gift_ball.surprise_ball_count -= 1

		if gift_ball.surprise_ball_count > 0:
			gift_ball.current_state = NoTokenState()
		else:
			gift_ball.current_state = NoBallesSurpriseState()

class NoBallesSurpriseState(StateInterface):
	# No more balls 

	def insert_token(self, gift_ball: GiftBall) -> None:
		pass

	def eject_token(self, gift_ball: GiftBall) -> None:
		pass

	def turn_crank(self, gift_ball: GiftBall) -> None:
		pass

	def dispense_ball(self, gift_ball: GiftBall) -> None:
		pass

class GiftBall:
	def __init__(self, surprise_ball_count: int = 0) -> None:
		if surprise_ball_count < 0:
			raise ValueError("surprise_ball_count must be >= 0")

		self.surprise_ball_count = surprise_ball_count
		self.current_state: StateInterface = (
			NoTokenState() if surprise_ball_count > 0 else NoBallesSurpriseState()
		)

	def insert_token(self) -> None:
		self.current_state.insert_token(self)

	def eject_token(self) -> None:
		self.current_state.eject_token(self)

	def turn_crank(self) -> None:
		self.current_state.turn_crank(self)

	def dispense_ball(self) -> None:
		self.current_state.dispense_ball(self)