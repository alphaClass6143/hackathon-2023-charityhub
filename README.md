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

### Python Packages?


## Deployment
The project was deployed to  [Heroku](https://www.heroku.com/). The deployment process is as follows:

1.  Log in to Heroku or create an account if required.

2.  Click the button labeled New from the dashboard in the top right corner, just below the header and then select "Create new app".

3.  Enter a unique application name and then select your region. Once you are ready, click "Create app".

4.  This will bring you to the project "Deploy" tab. From here, click the "Settings" tab and scroll down to the "Config Vars" section and click on "Reveal Config Vars". In the KEY input field, enter "PORT" and in the VALUE input field, enter "8000". After that, click the "Add" button to the right.

5.  Scroll down to the buildpacks section of the settings page and click the button "Add buildpack". 

6.  Add both "Python" and "node.js" and make sure that Python is above node.js. If it isn't you can just drag it above.

7.  Scroll back to the top of the settings page, and navigate to the "Deploy" tab. Select Github as the deployment method.

8.  Search for the repository name and click the connect button next to the intended repository.

9.  From the bottom of the deploy page select your preferred deployment type. I personally enabled automatic deployments. After that, click "Deploy Branch".