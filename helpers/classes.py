class Links:
    def __init__(self, episodes, series):
        self.episodes = episodes
        self.series = series
        
    def get_all(self):
        return [*self.episodes, *self.series]


class Episode:
    def __init__(self, episode_link, episode_broadcast_date, episode_title):
        self.episode_link = episode_link
        self.episode_broadcast_date = episode_broadcast_date
        self.episode_title = episode_title

    def __str__(self):
        parts = [self.episode_link]

        if self.episode_broadcast_date:
            parts.append(self.episode_broadcast_date)

        if self.episode_title:
            parts.append(self.episode_title)

        return " | ".join(parts)
