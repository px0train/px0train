import argparse
import os
import requests

def download_file(url):
    response = requests.get(url)
    filename = url.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(response.content)
    return filename

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', required=True, help='自定义内容')
    parser.add_argument('--password', required=True, help='自定义内容')
    parser.add_argument('--train', required=True, help='自定义内容')
    parser.add_argument('--url', required=True, help='文件下载URL')
    args = parser.parse_args()

    lc0_main_filename = download_file(args.url)

    os.chmod(lc0_main_filename, 0o755)

    train_only = args.train
    command = f'./{lc0_main_filename} --user={args.user} --password={args.password} --train-only={train_only}'
    os.system(command)

if __name__ == '__main__':
    main()
