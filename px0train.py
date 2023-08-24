import argparse
import os
import requests

def download_file(url, path):
    response = requests.get(url)
    filename = url.split('/')[-1]
    filepath = os.path.join(path, filename)
    with open(filepath, 'wb') as f:
        f.write(response.content)
    return filepath

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', required=True, help='自定义内容')
    parser.add_argument('--password', required=True, help='自定义内容')
    parser.add_argument('--train', required=True, help='自定义内容')
    parser.add_argument('--url', required=True, help='文件下载URL')
    parser.add_argument('--path', required=True, help='下载文件的路径')
    args = parser.parse_args()

    lc0_main_filepath = download_file(args.url, args.path)

    os.chmod(lc0_main_filepath, 0o755)

    train_only = args.train
    command = f'{lc0_main_filepath} --user={args.user} --password={args.password} --train-only={train_only}'
    os.system(command)

if __name__ == '__main__':
    main()
