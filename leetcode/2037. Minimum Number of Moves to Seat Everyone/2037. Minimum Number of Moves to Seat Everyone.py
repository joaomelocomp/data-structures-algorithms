class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        def organizer(seats):
            maior = seats[0]
            for i in range(len(seats)):
                for j in range(len(seats)):
                    temp = 0
                    if seats[i] < seats[j]:
                        temp = seats[i]
                        seats[i] = seats[j]
                        seats[j] = temp
            return seats
        seats = organizer(seats)
        students = organizer(students)

        y = []
        for i in range(len(seats)):
            x = abs(seats[i] - students[i])
            y.append(x)

        return sum(y)
