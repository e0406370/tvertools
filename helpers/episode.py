class Episode:
    def __init__(self, episode_link, episode_broadcast_date, episode_title):

        self.episode_link = episode_link
        self.episode_broadcast_date = episode_broadcast_date
        self.episode_title = episode_title

    def __str__(self):

        return f"{self.episode_link} | {self.episode_broadcast_date} | {self.episode_title}"
