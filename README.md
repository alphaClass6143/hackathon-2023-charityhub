<h1  align="center">Charity Hub</h1>

[View the live project here](#link)

Charity Hub is an app that works as a research tool for those interested in supporting charities. The target audience is people looking to donate to, volunteer at, and keep up-to-date with  specific charities of their choosing. The app functions as a one-stop-location for research into active charities on a global scale; as a searchable and filterable database of information about these charities; and resource for current news and facts about the featured charities. 

[Responsive Mockup Image]

## Table of Contents
- Contributors
- User Experience (UX)
- Features
- Technologies Used
- Testing
- Deployment
- Credits

## Contributors

[Tony Wilson](https://github.com/Tonywilson1211)
[Hernan Diaz](https://github.com/hernanpd)
[Robin Bosch](https://github.com/alphaClass6143)
[Samar Ziadat](https://github.com/SamarZiadat)
[Samuel Sadovoi ](https://github.com/SamSswi)
[Soorya](https://github.com/SooryaGeorge7)

This app was developed as part of Code Institute's Feb 2023 Hackathon for World NGO Day. The app was conceived, designed, developed and deployed by a team of 6 Code Institute students at various stages of learning, over the course of 5 days (February 16th-20th 2023). 

## User experience (UX)

### User Stories
1.  As a user, I want to learn what this website is about so that I understand its purpose.
    
2.  As a user, I want to see the featured charities, so that I can find out which I want to support.
    
3.  As a user, I want to know who is responsible for the project, so that I can learn more about them.
    
4.  As a user, I want to search for a charity that I have recently heard about, so that I can find out information about it.
    
5.  As a user, I want to search for all the charities in a certain category, so that I can support the cause that is important to me.
    
6.  As a user, I want to search for charities that have certain keywords attached to them, so that I can search for the charity that is best suited to me.

7. As a user, I want to find out where in the world the charity is based, so that I can make the choice to support either an internationally-based or local charity.
    
8.  As a user, I want to find out what I certain charity does, so that I can decide if I want to support them.
    
9.  As a user, I want to visit the website of a charity so that if I want to volunteer at or donate directly to a charity, I can get the information I need.
 
10. As a user, I want to stay up-to-date with charities worldwide, so that I might learn about new ones and receive current news about ones I know and perhaps support.

### Owner group

1.  As an owner, I want the user to subscribe to the newsletter, so I can inform them about the newest charities, current news in the world of charities, new features of the app, and redirect traffic back to the app.
    
2.  As an owner, I want to promote myself, so that users can find out more about me.
    
3.  As an owner, I want to promote the app's social media, where I share information about charities and what is happening in that sector, so that users can stay up to date.

## Design

### Colour Scheme

The app's colour scheme was devised using the colour palette generator [coolors](https://coolors.co/), and is consists of 5 colours: black, white, green, orange and grey. We decided on this colour scheme as it reinforces the friendly, fresh and optimistic branding that is important to the app's tone. It also has colours with appropriate contrast for legibility and accessibility, while also including brighter colours for guiding the user's eye to important features and actions.

### Typography

The Playfair font is the main font used throughout the website. It is crisp and easy to read, which is appropriate for legibility. It is also an interesting, rather than a standard font, encouraging intrigue in the user, encouraging them to engage in research on our app.

### Imagery

The favicon we utilised features open hands and and floating globe. We chose it because it symbolises a charitable generosity that extends worldwide. It was sourced from [SVG Repo](https://www.svgrepo.com/) and generated with [Real Favicon Generator](https://realfavicongenerator.net/).

[Image of favicon]

## Technology

### Technologies Used
-   [HTML5](https://en.wikipedia.org/wiki/HTML)  - Provides the content and structure for the website.
-   [CSS3](https://en.wikipedia.org/wiki/CSS)  - Provides the styling for the website.
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))  - Provides the functionality of the website.
- [Flask](https://flask.palletsprojects.com/en/2.2.x/) - Used as the primary framework for the app.
-   [VSCode](https://code.visualstudio.com/)  - Used to create and edit the website.
-   [GitHub](https://github.com/)  - Used to develop the website.
-   [GitBash](https://en.wikipedia.org/wiki/Bash_(Unix_shell))  - Terminal used to push changes to the GitHub repository.
- [Heroku](https://www.heroku.com/) - Used to host and deploy the website.
-   [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/)  - Used to test responsiveness and debug.
- [Google Fonts](https://fonts.google.com/) - Used to import font into the style.css file which is used throughout the project.
- [Font Awesome](https://fontawesome.com/) - Used throughout the website to add icons for aesthetic and UX purposes.
- [Coolors](https://coolors.co/) - Used to generate the colour scheme.
- [SVG Repo](https://www.svgrepo.com/) - Used to source the favicon.
- [Real Favicon Generator](https://realfavicongenerator.net/)  - Used to generate the favicon.

?? <<<<
-   [Lucidchart](https://www.lucidchart.com/)  - Used to create the logic flow chart.
-   [??]()  - Used to host the application data.
- [Tech Sini](https://techsini.com/multi-mockup/) - Used to generate the mockup of the app.
- [Fsymbols](https://fsymbols.com/generators/carty/) - Used to generate ASCII art.
- [Pexels](https://www.pexels.com/) - Used to source free stock images.
-  [Balsamiq](https://balsamiq.com/)  - Used to create the wire-frame.
>>>>

### Python Packages

- flask
- gunicorn
- python-dotenv

## Deployment

You can fork the repository by following these steps:

1. Go to the repository on GitHub  
2. Click on the "Fork" button in the upper right hand corner

You can clone the repository by following these steps:

1. Go to the repository on GitHub
2. Locate the "Code" button above the list of files and click it  
3. Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the "copy" button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone <https://github.com/YOUR-USERNAME/YOUR-REPOSITORY>)  
7. Press Enter to create your local clone.

### Local

1. Follow the clone steps and go to step 2
2. Run the following command to install all required packages

```
pipenv install
```

3. Create a .env file and add the following keys to it:
    - DEVELOPMENT --> Is optional, default without it is True

4. Enter the following commands to start up the server:

```
pipenv shell
cd app
python app.py
```

5. The package can now be accessed locally under [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### Heroku

1. Create an account at Heroku and login.
2. Click the "Create new app" button on your dashboard, add app name and region.
3. Click on the "Create app" button.
4. Click on the "Settings" tab.
5. Under "Config Vars" click "Reveal Config Vars" add the following keys:
    - DEVELOPMENT --> Is optional but should be set to False, default without it is True
6. Under "Buildpacks" click "Add buildpack" and then choose "Python" first and click "Save changes"
7. Go to the "Deploy" tab and choose GitHub as your deployment method
8. Connect your GitHub account
9. Enter your repository name, search for it and click connect when it appears below.
10. In the manual deploy section click "Deploy branch"
11. Optional: You can enable automatic deploys if you want the app to automatically update


