class solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        running = []
        currTimes = [] * n
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
                        currTimes[funcId] += timestamp - epoc
                    running.append(funcId)
                    epoc = timestamp
                else:
                    currTimes[funcId] += timestamp - epoc + 1
                    running.pop()
                    epoc = timestamp
        return currTimes
