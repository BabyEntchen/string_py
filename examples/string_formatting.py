from string_py import Format

print(Format.align(values={"Username:": "John", "Register Date:": "01.01.2001"}))
# Output:
#
# Username:        John
# Register Date:   01.01.2001

print(Format.surround("Hello World", char="*"))
# Output:
#
# ***************
# * Hello World *
# ***************

print(Format.table([["Product", "Value", "Sold"], ["Carrot", "3.99$", "34"], ["Milk", "5$", "103"]]))
# Output:
#
# ┌────────────────────────┐
# │ Product │ Value │ Sold │
# ├────────────────────────┤
# │ Carrot  │ 3.99$ │ 34   │
# │────────────────────────│
# │ Milk    │ 5$    │ 103  │
# └────────────────────────┘
