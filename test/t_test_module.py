#!/home/jeremy/Envs/atmos/bin/python

# TEST PATH PARSING

inputs = [
    "./test.txt",
    "../test/test.txt",
    "/home/jeremy/atmos/test/test.txt",
]

expected = [
    ["abc", "123", "zyx", "987"],
    ["abc", "123", "zyx", "987"],
    ["abc", "123", "zyx", "987"],
]

failed = False

for num, case in enumerate(inputs):
    result = load_testfile(case)
    if not result == expected[num]:
        failed = True
        print(
            f"load_testfile({case}) failed\n\tExpected: {expected[num]}\tResult: {result}"
        )
        print()

# TEST FILE LOADING


if not failed:
    print("*** All tests passed successfully!***")
