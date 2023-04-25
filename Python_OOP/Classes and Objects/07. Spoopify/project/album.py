from project.song import Song


class Album:
    def __init__(self, name: str, *song):
        self.name = name
        self.published = False
        self.songs = [s for s in song]

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        for song_from_db in self.songs:
            if song_from_db.name == song.name:
                return f"Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        for song_from_db in self.songs:
            if song_from_db.name == song_name:
                if self.published:
                    return "Cannot remove songs. Album is published."

                self.songs.remove(song_from_db)
                return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}"
        for song in self.songs:
            result += f"\n== {song.get_info()}"

        return result