This app is v1.0 of the HelloInsights Security Insights application. 
It is designed to compile daily security updates.
Along with training resources for cybersecurity employees and enthusiasts.
HelloInsights is actively being worked on. 
The final iteration of the source code will be maintained but no longer remain in the public domain.

The app is built using Flask, a lightweight Python web framework. 
It has two endpoints, /news and /update.
The /news endpoint retrieves news from the MongoDB database and returns it in JSON format. 
The database has a collection called news, which contains documents with the fields title, summary, link, and date.
The /update endpoint scrapes news from various sources, processes it, and inserts it into the database. 
The sources are defined in the news_sources list. 
BeautifulSoup is used to parse the HTML content of the news sources, and the find_all() method is used to extract the relevant information. 
The date field is generated using the strftime() method of the datetime module.

This app has been built for two purposes, to provide a much needed avenue to daily cybersecurity updates in a neat manner in which a user can choose to populate their feed according to their interests.
The second purpose was to present another cybersecurity service that could potentially be added to the Hello Security Research Labs lineup of tools and services. 

The app is currently designed to run on the localhost for testing purposes, and the MongoDB database is also running on the localhost. 
The app can be run by executing the app.py file, and it will start a development server on the local machine. 
The debug=True parameter in the app.run() method enables debug mode, which provides detailed error messages in case of any issues.

The HelloInsight app is Developed by abtzpro, Adam R, and Hello Security
