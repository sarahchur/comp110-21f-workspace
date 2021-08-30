"""This exercise demonstrates the use of relational operators in programming."""
__author__ = "730228276"

left_hand_side: str = input("Left-hand side: ")
right_hand_side: str = input("Right-hand side: ")

less_than_bool: bool = bool(left_hand_side < right_hand_side)
greater_than_or_equal_to_bool: bool = bool(left_hand_side >= right_hand_side)
equal_to_bool: bool = bool(left_hand_side == right_hand_side)
not_equal_to_bool: bool = bool(left_hand_side != right_hand_side)

less_than_str: str = str(less_than_bool)
greater_than_or_equal_to_str: str = str(greater_than_or_equal_to_bool)
equal_to_str: str = str(equal_to_bool)
not_equal_to_str: str = str(not_equal_to_bool)

print(left_hand_side + " < " + right_hand_side + " is " + less_than_str)
print(left_hand_side + " >= " + right_hand_side + " is " + greater_than_or_equal_to_str)
print(left_hand_side + " == " + right_hand_side + " is " + equal_to_str)
print(left_hand_side + " != " + right_hand_side + " is " + not_equal_to_str)
