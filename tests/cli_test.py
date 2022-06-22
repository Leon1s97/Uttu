import argparse

def cli():
    parser = argparse.ArgumentParser()

    # parser.add_argument("--name", dest="str", help="Set project name")
    # parser.add_argument("--path", dest="str", help="Set project path")
    # parser.add_argument("--templ", dest="str", help="Using pre-built project templates")

    parser.add_argument("-n", "--name", dest="name", required=True, help="Set project name")
    parser.add_argument("-p", "--path", dest="path", help="Set project path")
    parser.add_argument("-t", "--templ", dest="templ", choices=['sfss', 'credit'], help="Using pre-built project templates")

    args = parser.parse_args(["--name", "app", "--path", "C:/", "--templ", "sfss"])
    print(args)

if __name__ == "__main__":
    cli()
