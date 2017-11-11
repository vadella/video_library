import json
import subprocess

import collections

import datetime
import pathlib


class MkvFile:
    def __init__(self, filename: pathlib.Path, parsers=None):
        self.filename = filename

        info = probe_file_json(str(filename))
        if info['succes']:
            file_info_json = json.loads(info['output'])
        else:
            print(info['error'])
            return

        format_info = file_info_json['format']
        format_labels = ['duration', 'size', 'nb_streams', 'format_name']
        duration, size, self.nb_streams, self.format_name = (format_info.get(info, None) for info in
                                                             format_labels)
        self.duration = get_duration(duration)
        self.size = round(int(size.split()[0]) / 1e9, 1)

        def _parse_stream_info(stream_info, parsers=parsers):
            def parse_streams(streams: dict):
                # print(streams)
                default_parsers = {'subtitle': SubtitleStreamInfo, 'video': VideoStreamInfo, 'audio': AudioStreamInfo}
                default_parsers.update(parsers)

                for stream in streams:
                    typ = stream['codec_type']
                    # print(stream)
                    yield typ, parsers[typ](stream)

            result = collections.OrderedDict([(typ, []) for typ in ('video', 'audio', 'subtitle')])
            for typ, stream_info_parsed in parse_streams(stream_info):
                result[typ].append(stream_info_parsed)
            return result

        stream_info = _parse_stream_info(file_info_json['streams'])
        self.video = stream_info.get("video", ())
        self.audio = stream_info.get("audio", ())
        self.subtitle = stream_info.get("subtitle", ())

        self._format_info = file_info_json['format']
        self._stream_info = file_info_json['streams']

    def __repr__(self):
        video_info = f'{self.duration}, {self.size} GB, {[repr(info) for info in self.video]}'
        audio_info = f'{[repr(info) for info in self.audio]}'
        subtitle_info = f'{[repr(info) for info in self.subtitle]}'

        return f'''{str(self.filename)}
            video: {video_info}
            audio: {audio_info}
            sub: {subtitle_info}'''


class StreamInfo:
    def __init__(self, stream_info):
        self.index = stream_info.get('index', None)
        self.codec_name = stream_info.get('codec_name', None)
        self.lang = stream_info.get('tags', {}).get('language', 'unknown_lang')
        self.disposition = self.get_disposition(stream_info)

    @staticmethod
    def get_disposition(stream_info):
        return [k for k, v in stream_info.get('disposition', {}).items() if v]


class VideoStreamInfo(StreamInfo):
    def __init__(self, stream_info):
        super(VideoStreamInfo, self).__init__(stream_info)
        self.width = stream_info.get('width', None)
        self.height = stream_info.get('height', None)

    def __repr__(self):
        return f'<VideoStreamInfo({self.codec_name}, ({self.width} x {self.height}))>'


class AudioStreamInfo(StreamInfo):
    def __init__(self, stream_info):
        super(AudioStreamInfo, self).__init__(stream_info)
        self.channels = stream_info.get('channels', None)
        self.channel_layout = stream_info.get('channel_layout', None)
        bit_rate = stream_info.get('bit_rate', None)
        self.bit_rate = round(int(bit_rate.split()[0]) / 1000) if bit_rate else -1

    def __repr__(self):
        return f'<AudioStreamInfo({self.lang}, {self.codec_name}, {self.channels}ch, {self.channel_layout}, {self.bit_rate}kb/s)>'


class SubtitleStreamInfo(StreamInfo):
    def __init__(self, stream_info):
        super(SubtitleStreamInfo, self).__init__(stream_info)
        duration = stream_info.get('duration', None)
        self.duration = get_duration(duration) if duration else datetime.time(0)

    def __repr__(self):
        return f'<SubtitleStreamInfo({self.lang}, {self.duration})>'


def get_duration(duration):
    dt = datetime.datetime.strptime(duration, '%X.%f')
    return datetime.time(hour=dt.hour, minute=dt.minute, second=dt.second)


def probe_file_json(filename):
    '''Runs ``ffprobe`` executable over ``filename``, returns parsed XML

    Parameters:

        executable (str): Full path leading to ``ffprobe``
        filename (str): Full path leading to the file to be probed

    Returns:

        xml.etree.ElementTree: containing all parsed elements

    '''

    # https://codereview.stackexchange.com/questions/23277/trying-to-get-output-of-ffprobe-into-variable
    #
    # https://stackoverflow.com/questions/9896644/getting-ffprobe-information-with-python

    cmd = [
        'ffprobe',
        '-v', 'quiet',
        '-print_format', 'json',  # here is the trick
        '-show_format',
        '-show_streams',
        '-sexagesimal',
        # '-count_frames',
        # '-unit',
        filename,
    ]
    result = subprocess.run(cmd)
    return{'succes': not bool(result.returncode), 'output': result.stdout, 'error': result.stdout}
