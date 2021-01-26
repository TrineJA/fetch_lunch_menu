# fetch_lunch_menu
Get the lunch menu for Novo Nordisk canteen in VTA

# Heroku (deployment)
1) install heroku `brew install heroku/brew/heroku`
2) log in using heroku cli: `heroku login`
3) `heroku create APPNAME` to create your app (here APPNAME=taltrans-sailgp). This just needs to be done once!
4) `heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git` to add buildpack for poetry. I cant get this to work, so just go with pipenv for heroku...
5) `git push heroku main` will push your changes to heroku (it does NOT push to your git repo)
This will make your app run in 1 dyno (container).

Use `heroku open` to open your app (https://APPNAME.herokuapp.com/)

Use `heroku apps` to see how many dynos you have running (by your user).

Use `make heroku-local` to run locally (http://localhost:5000)