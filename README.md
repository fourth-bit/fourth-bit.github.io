# Marin Donates Website
Hello! This is a website where you will be able to find non-profits for all of your items in Marin County, California. The website is generated through data in a json file located at json/charities.json. If you feel that you and your non-profit are missing from this website, open an issue on this repository.
## Generating the website
Generating the website is very simple. After cloning the repository, ```cd``` into the directory and run ```make all```. This will create the necessary directories, and it will generate all of the pages using python scripts. If make give you any errors regarding dependencies, plese consult the next section.
## Dependencies
This website depends on Bootstrap 4.6.0. This will need to be located at a folder called ```bootstrap-4.6.0``` at the root of the project. To get this package, please use:
```
git clone https://github.com/twbs/bootstrap.git --branch 4.6.0 --single-branch -C ./bootstrap-4.6.0
```
or download it <a href="https://getbootstrap.com/docs/4.6/getting-started/download/">here</a>. There are two other dependencies handled by ```npm```. If you run ```npm install``` in the root of this project, they should be handled. You will also need to download Font-Awesome 4 Free from <a href="https://fontawesome.com/v4.7.0/get-started/">here</a>. Unzip the archive and place it in a folder called ```font-awesome```. You will also need the Lato and Merriweather fonts from <a href="https://fonts.google.com/share?selection.family=Lato%7CMerriweather">here</a>. Leave them both in a folder called ```fonts``` unzipped.