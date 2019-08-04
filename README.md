# Perferct Pitch

## Built By [Emmanuel Muchiri](https://github.com/emmanuelmuchiri/)

## Screenshots
![homepage](app/static/images/home.png);
![register](app/static/images/register.png);
![Add A Pitch](app/static/images/pitch.png);
![View Pitch](app/static/images/pitch_base.png);

## Description
{erfect Pitch is an application that allows you to Post a pitch based on various categories.You can view other pitches as long as you have an account and can either comment or upvote or downvote

You can view the site at: 

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* See various news sources 
* Select the ones they prefer
* See the top news articles from that news source
* See the image, description and time the news article was created
* Click on an article and read it fully from the news source

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display Welcome Message | **On page load** | Select between Add a pitch and View Pitch|
| Display Pitch Form | **Click add pitch** | Redirected to a page where He types the title and content and then selects the category from the drop-down arrow|
| Display the Pitch| **Click view pitch** | Each pitch displays  title, description and category|



## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv

### Cloning
* In your terminal:
        
        $ git clone https://github.com/EmmanuelMuchiri/pitch.git
        $ cd News-Highlights

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python 
        
* Installing Flask and other Modules

        $ python3.6 -m pip install Flask
        $ python3.6 -m pip install Flask-Bootstrap
        $ python3.6 -m pip install Flask-Font-Mail
        $ python3.6 -m pip install Flask-upload
        $ python3.6 -m pip install Flask-login
        $ python3.6 -m pip install Flask-Alchemy
        $ python3.6 -m pip install Flask-Simplemde

        
        
* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh
        
## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py tests
        
## Technologies Used
* Python3.6
* Flask

## License
MIT &copy;2019 [Emmanuel Muchiri](https://github.com/emmanuelmuchiri/)