# Marin Donates Website
Hello! This is a website where you will be able to find non-profits for all of your items in Marin County, California. The website is generated through data in a json file located at json/charities.json. If you feel that you and your non-profit are missing from this website, open an issue on this repository.
## Generating the website
Generating the website is very simple. After cloning the repository, ```cd``` into the directory and run ```make clean install```. This will create the necessary directories, and it will generate all of the pages using python scripts. If make give you any errors regarding dependencies, plese consult the next section.
## Dependencies
This website depends on Bootstrap 4.6.0. Alothough there is a bootstrap folder which already exists, there is only the bare minimum needed to run the website on github. In order to generate the css, the necessary scss is not present. You will need place the download of bootstrap in a folder called ```bootstrap-4.6.0``` at the root of the project. To get this package, please use:
```
git clone https://github.com/twbs/bootstrap.git bootstrap-4.6.0 --branch v4.6.0 --single-branch --depth 1
```
or download it <a href="https://getbootstrap.com/docs/4.6/getting-started/download/">here</a>. There are two other dependencies handled by ```npm```. If you run ```npm install``` in the root of this project, they should be handled. Font-Awesome is already supplied, but it is the bare minimun, so if you need all of its contents, tou can find them here. <a href="https://fontawesome.com/v4.7.0/get-started/">here</a>.