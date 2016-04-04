

def main():
    parser = argparse.ArgumentParser(description='Initialize an Elm page')

    parser.add_argument('module_name')
    parser.add_argument('destination')
    args = parser.parse_args()

    bootstrap(args.module_name, args.destination)

if __name__ == '__main__':
    main()
