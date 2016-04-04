import argparse


def main():
    parser = argparse.ArgumentParser(description='Initialize an Elm page')

    parser.add_argument('module_name', help='the component name e.g Some.Module.Name')
    parser.add_argument('destination', help='the destination folder. Defaults to current', default="./")
    args = parser.parse_args()

    bootstrap(args.module_name, args.destination)

if __name__ == '__main__':
    main()
