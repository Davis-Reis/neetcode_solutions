import sys
from typing import List

class solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        running = []
        currTimes = [0] * n
        epoc = 0
        for string in logs:
            # split = [id, action, epoc]
            split = string.split(":")
            funcId = int(split[0])
            timestamp = int(split[2])
            # adding to stack
            if split[1] == "start":
                # stack is not empty
                if len(running) != 0:
                    currTimes[running[-1]] += timestamp - epoc
                running.append(funcId)
                epoc = timestamp
            else:
                currTimes[funcId] += timestamp - epoc + 1
                running.pop()
                epoc = timestamp + 1
        return currTimes

sys.stdin = open("tests/test0")
n = int(sys.stdin.readline())
log = [line.rstrip() for line in sys.stdin]
test = solution()
print(test.exclusiveTime(n, log))
sys.stdin = open("tests/test1")
n = int(sys.stdin.readline())
log = [line.rstrip() for line in sys.stdin]
test = solution()
print(test.exclusiveTime(n, log))
sys.stdin = open("tests/test2")
n = int(sys.stdin.readline())
log = [line.rstrip() for line in sys.stdin]
test = solution()
print(test.exclusiveTime(n, log))
