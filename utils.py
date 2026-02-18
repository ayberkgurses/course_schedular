from typing import List

class LectureHall():
    def __init__(
        self,
        capacity: int
    ):
        self.capacity = capacity
        self.niceness = capacity
        
class Course():
    def __init__(
        self, demand: int,
        n_sections: int,
        n_hours: int
    ):
        self.demand = demand
        self.n_sections = n_sections
        self.n_hours = n_hours

class Lecturer():
    def __init__(
        self,
        courses: list[Course] | None = None,
        schedule: dict | None = None
    ):
        self.courses = courses if courses is not None else []
        self.schedule = schedule if schedule is not None else {}
