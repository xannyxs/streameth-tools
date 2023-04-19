class Session:
    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        stage_id: str,
        day: str,
        start: str,
        end: str,
        speaker_ids: list[str],
        video: str,
        is_tweeted: str,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.stage_id = stage_id
        self.day = day
        self.start = start
        self.end = end
        self.speaker_ids = speaker_ids
        self.video = video
        self.is_tweeted = is_tweeted

    def __str__(self):
        return f"Session({self.id}, {self.name}, {self.description}, {self.stage_id}, {self.day}, {self.start}, {self.end}, {self.speaker_ids}, {self.video}, {self.is_tweeted})"