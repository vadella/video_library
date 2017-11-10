import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Time, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from video_bibliotheek.video_info import VideoStreamInfo, StreamInfo, AudioStreamInfo, SubtitleStreamInfo, MkvFile

Base = declarative_base()


class MkvFileDB(Base, MkvFile):
    __tablename__ = 'mkv_file'
    id = Column(Integer, primary_key=True)
    size = Column(Float)
    duration = Column(Time)
    video = relationship('VideoStreamInfoDB', back_populates='mkv_file')
    audio = relationship('AudioStreamInfoDB', back_populates='mkv_file')
    subtitle = relationship('SubtitleStreamInfoDB', back_populates='mkv_file')

    # association table
    # streams = Table('post_keywords', Base.metadata,
    #                 Column('mkv_file_id', ForeignKey('mkv_file.id')),
    #                 Column('stream_id', ForeignKey('stream.id'), primary_key=True))

    # keywords = relationship('Streams',
    #                         secondary=streams,)

    def __init__(self, filename):
        parsers = {'subtitle': SubtitleStreamInfoDB, 'video': VideoStreamInfoDB, 'audio': AudioStreamInfoDB}
        MkvFile.__init__(self, filename=filename, parsers=parsers)

class Stream_MKV(Base):
    __tablename__ = 'stream_mkv'
    stream_id = Column(Integer, ForeignKey('stream_info.id'), primary_key=True)
    mkv_id = Column(Integer, ForeignKey('mkv_file.id'))

class StreamInfoDB(Base, StreamInfo):
    __tablename__ = 'stream_info'

    id = Column(Integer, primary_key=True)
    index = Column(Integer)
    codec_name = Column(String)
    lang = Column(String)
    typ = Column(String)
    __mapper_args__ = {
        'polymorphic_identity': 'stream_info',
        'polymorphic_on': typ
    }
    pass


# class Disposition(Base):
#     __tablename__ = 'disposition'
#     id = Column(Integer, primary_key=True)
#     disposition = Column(String)
#     stream_id = Column(ForeignKey('stream.id'))

class VideoStreamInfoDB(StreamInfoDB, VideoStreamInfo):
    __tablename__ = 'video_stream_info'
    id = Column(Integer, ForeignKey('stream_info.id'), primary_key=True)
    width = Column(Integer)
    height = Column(Integer)
    mkv_file_id = Column(Integer, ForeignKey('mkv_file.id'))
    mkv_file = relationship('MkvFileDB', back_populates='video')
    # stream_id = Column(Integer, ForeignKey('stream_info.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'video_stream_info',
    }

    def __init__(self, stream_info):
        VideoStreamInfo.__init__(self, stream_info)


class AudioStreamInfoDB(StreamInfoDB, AudioStreamInfo):
    __tablename__ = 'audio_stream_info'
    id = Column(Integer, ForeignKey('stream_info.id'), primary_key=True)
    channels = Column(Integer)
    channel_layout = Column(String)
    bit_rate = Column(Integer)
    mkv_file_id = Column(Integer, ForeignKey('mkv_file.id'))
    mkv_file = relationship('MkvFileDB', back_populates='audio')
    # stream_id = Column(Integer, ForeignKey('stream_info.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'audio_stream_info',
    }

    def __init__(self, stream_info):
        AudioStreamInfo.__init__(self, stream_info)


class SubtitleStreamInfoDB(StreamInfoDB, SubtitleStreamInfo):
    __tablename__ = 'subtitle_stream_info'
    id = Column(Integer, ForeignKey('stream_info.id'), primary_key=True)
    duration = Column(Time)
    mkv_file_id = Column(Integer, ForeignKey('mkv_file.id'))
    mkv_file = relationship('MkvFileDB', back_populates='subtitle')
    # stream_id = Column(Integer, ForeignKey('stream_info.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'subtitle_stream_info',
    }

    def __init__(self, stream_info):
        SubtitleStreamInfo.__init__(self, stream_info)
