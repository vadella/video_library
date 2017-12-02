
from video_library.cli import main
from pathlib import Path
from video_library import video_info

def test_main():
    assert main([]) == 0
def test_video_info():
    data_dir = Path('test_data')
    for file in data_dir.glob('*.mkv'):
        print(file)
        print(file, video_info.probe_file_json(str(file)))

if __name__ == '__main__':
    test_video_info()
