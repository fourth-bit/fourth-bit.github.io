import os

def check_dependencies():
    bootstrap = os.popen('ls bootstrap-4.6.0 2> /dev/null').read()
    fonts = os.popen('ls fonts 2> /dev/null').read()
    npm = os.popen('npm ls').read()

    if bootstrap.find('dist') == -1 or bootstrap.find('scss') == -1:
        inp = input("Bootstrap / Parts of bootstrap are misssing. Continue with website generation? [y/n]: ")
        if inp.lower() != 'y':
            raise SystemExit(128)
    if fonts.find('Merriweather') == -1 or fonts.find('Lato') == -1:
        inp = input('Fonts are missing. Continue with website generation? [y/n]: ')
        if inp.lower() != 'y':
            raise SystemExit(128)
    if npm.find('autoprefixer') == -1 or npm.find('postcss-cli') == -1 or npm.find('uglify-js') == -1:
        inp = input('NPM packages are missing. Run npm install to get them. Continue with website generation? [y/n]: ')
        if inp.lower() != 'y':
            raise SystemExit(128)

if __name__ == "__main__":
    check_dependencies()