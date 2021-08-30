"""This exercise demonstrates the use of numeric operators in programming."""
__author__ = "730228276"

left_hand_side: str = input("Left-hand side: ")
right_hand_side: str = input("Right-hand side: ")
left_hand_side_integer: int = int(left_hand_side)
right_hand_side_integer: int = int(right_hand_side)

exponentiation: str = str(left_hand_side_integer ** right_hand_side_integer)
division: str = str(left_hand_side_integer / right_hand_side_integer)
integer_division: str = str(left_hand_side_integer // right_hand_side_integer)
remainder: str = str(left_hand_side_integer % right_hand_side_integer)

print(left_hand_side + " ** " + right_hand_side + " is " + exponentiation)
print(left_hand_side + " / " + right_hand_side + " is " + division)
print(left_hand_side + " // " + right_hand_side + " is " + integer_division)
print(left_hand_side + " % " + right_hand_side + " is " + remainder)