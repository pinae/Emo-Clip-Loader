import pytube
from uuid import uuid4


class Clipstractor:
    def __int__(self, url):
        self.metadata = {
            'id': uuid4(),
            'url': url,
        }

    def load_clip(self):
        # create yt-object
        # load video stream in desired resolution
        # load audio stream
        # load subtitles
        # save data to disk and append metadata
        pass

    def trim_clip(self):
        # load video file
        # load audio file
        # combine video and audio
        # delete 0 to start pos
        # delete rest after desired length
        # save clip in desired format (note filename)
        # add filename to metadata
        # clean up metadata
        pass
