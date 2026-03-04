class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = Counter(tasks)
        pq = [(-cnt, task) for task, cnt in counter.items()]
        heapq.heapify(pq)

        # (available_time, -cnt, task)
        cooldown = deque()

        time = 0

        while pq or cooldown:
            time += 1

            if cooldown and cooldown[0][0] == time:
                _, cnt, task = cooldown.popleft()
                heapq.heappush(pq, (cnt, task))

            if pq:
                cnt, task = heapq.heappop(pq)
                cnt += 1

                if cnt < 0:
                    cooldown.append((time + n + 1, cnt, task))

        return time
