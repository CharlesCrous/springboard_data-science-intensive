## Data Science Intensive
# By Springboard: https://www.springboard.com/workshops/data-science-intensive
# 12 week Data Science course
# 58 Resources
# 101+ Hours
# started course on 2015/12/26

COURSE OUTLINE
1.  INTRODUCTION (1+ hours)

2.  PROGRAMMING BOOTUP (4.5+ hours)
2.1 iPython Notebook
2.2 Matplotlib
2.3 Git and Github
2.4 Additional Programming Resources

3.  DATA WRANGLING (16.5+ hours)
3.1 Pandas Deep Dive
3.2 Data cleaning with Pandas
3.3 Working with data in files
3.4 Working with data in databases
3.5 Additional Resources

4.  DATA STORY (5+ hours)
4.1 Core Resources for Data Story
4.2 Additional Reading

5.  INFERENTIAL STATISTICS (25.5+ hours)
5.1 Parameter estimation, hypothesis testing and statistical significance
5.2 Regression and Correlation
5.3 A/B Testing
5.4 Additional Resources

6.  CAPSTONE MILESTONE REPORT (5+ hours)

7.  MACHINE LEARNING (22.5+ hours)
7.1 Supervised Learning
7.2 Unsupervised Learning
7.3 Dimensionality reduction and feature selection
7.4 Validation and Evaluation
7.5 Additional Scikit-learn resources

8.  CAPSTONE PROJECT (20+ hours)

9.  ELECTIVE 1: ADVANCED DATA VISUALIZATION
9.1 Communicating with Data
9.2 Interactive Data Visualisation for the Web
9.3 Stay up-to-date with this weekly newsletter

10. ELECTIVE 2: DATA SCIENCE AT SCALE
10.1 Get started with this Tutorial
10.2 Introductory course on Spark
10.3 Machine learning with Spark

11. CAREER RESOURCES



1. INTRODUCTION 1+ hours

A warm welcome to the Springboard Data Science Intensive Workshop.
Our team of industry experts has picked the best learning resources on Data Science and structured them into a logical curriculum below for you. Note that the individual resources need not be authored in-house, but are curated from the best in the field. We do provide the glue that stitches everything together and fills gaps, if any. We believe this is our unique strength because we stand on the shoulders of giants, instead of being restricted to in-house content. Think of us as a college professor who creates a curriculum with the most formidable book chapters, research papers, projects instead of teaching from only her own textbook.

As you work through the material, click "Mark Complete" and submit project files whenever you are done with a sub-unit. Any units you've marked as "complete" earlier through your Springboard account will be shown as "complete" here, too. If there are topics you are already familiar with, or feel are not relevant to your learning goals - you may discuss with your mentor and skip ahead.

We have a recommended schedule (~10-15 hours/week) so that the class can follow a rhythm and maximize benefit from discussions. However, this is a self-paced course, so feel free to go faster or slower as you please.

Week 1 & 2: Programming Bootup, Data Wrangling
Weeks 3 - 5: Data Story & Inferential Statistics
Weeks 6: Capstone Milestone Report
Weeks 7-9: Machine Learning
Weeks 10-12: Capstone Project

In addition to the core material, there are a bunch of additional resources and electives in case some topics catch your fancy and you would like to dive deeper there. Feel free to pace it and work with your mentor to tailor the course to your meet your goals and interests!
Without further ado, let's dive in!

5 Minutes
Student Onboarding Guide
This quick video will give you a tour of all the tools and resources you will be using in this workshop. 
https://www.youtube.com/watch?v=K5ADbqvQ8As

 1 Hour
Submit 3 potential Capstone project ideas and discuss with your mentor
Project Link: https%3A//drive.google.com/file/d/0B8INWTe40wCXT19nazBiWXBOQ2M/view%3Fusp%3Dsharing

Your Capstone project is one of the most important parts of this course - it will give you practice in the typical Data Science workflow, and also be a substantial project you can show off in your resume. Read the full project guidelines and evaluation criteria here.

For this section, think about what kind of data sets excite you. What would you like to get deeper insights on? Do you care about sentiment analysis on unstructured text, like news items, social media posts or support tickets? Or about sports analytics a la Moneyball? Healthcare, environment, or just analysing and predicting engagement and retention rates for different customer segments? You can explore datasets from Quandl, US Government Open Data, UCI Machine Learning Repository, Kaggle competitions or anywhere else you like. 

Submit a writeup on 3 Capstone project ideas by clicking the "Submit project" button on the right. Review them with your mentor. Your writeup should contain a short blurb for each of your ideas. The blurb should, at high level, describe the problem and the data you’ll be using to solve it. At this point, there’s no need to talk about specific methods and techniques. Post your idea (title and blurb) on the community and solicit feedback from both the mentors and other students.

Thinking of a few project ideas upfront can be a great motivator. It can also help you assimilate the curriculum material in that context, and relate to it much better.

A word of caution with Kaggle competitions: It’s perfectly fine to use a data set from Kaggle in your project. However, many Kaggle competitions are about taking a data set that’s already clean and optimized for the specific problem, and tuning a machine learning algorithm for the highest accuracy (or similar metric). While that’s an important skill for a data scientist, it’s not all. In real-world scenarios, you’ll be the person who has to collect, wrangle and clean that data. If a Kaggle competition you’re considering falls into that category, here are a couple of ways you could still use the data set:
1. Could you use that data set to solve a different problem than the one asked in the competition?
2. Could you combine it with other data sets to solve the same problem asked in the competition or a different one?

Basically, we’d like your Capstone project to demonstrate your competence with the entire data science process, not just one aspect of it.

That being said, your mentor has the final word on whether a Kaggle competition is appropriate for a Capstone Project or not. Typically, we’ve found that recruiting competitions sponsored by top companies (e.g. Airbnb) meet the criteria for a Capstone Project.

More Project Ideas
http://blog.thedataincubator.com/2014/10/data-sources-for-cool-data-science-projects-part-1/
http://blog.thedataincubator.com/2014/10/data-sources-for-cool-data-science-projects-part-2/

2. PROGRAMMING BOOTUP 4.5+ hours

In this module, you will start using an ecosystem of useful and powerful tools for doing data science with Python - primarily iPython Notebook, Pandas, and matplotlib (scikit-learn is another, but needs familiarity with machine learning, and will be introduced later in the course). The best approach is to start using them together to gain basic familiarity, and then continue learning by using them in the rest of the course. The goal is basic familiarity, hence the short time period suggestions. You will get more practice with each of them in the modules to follow. You can refer back to these resources as you need them, and spend more time as you make progress through the course.


  2.1 IPYTHON NOTEBOOK 0.5+ hours

iPython notebook is an interactive programming environment, that allows for coding, data exploration, and debugging in the web browser. It comes bundled with the Anaconda distribution, so you can start right away!
Note: iPython is now part of a larger project, Jupyter. The main difference is that while iPython is tied to Python, Jupyter can support multiple languages. For Python programmers, it makes little difference in practice, so you can simply treat Jupyter as the latest version of iPython.

 20 Minutes
Get started with iPython notebook
http://nbviewer.ipython.org/github/ipython/ipython/blob/3.x/examples/Notebook/Notebook%20Basics.ipynb

 10 Minutes
How to run code in iPython notebook
http://nbviewer.ipython.org/github/ipython/ipython/blob/3.x/examples/Notebook/Running%20Code.ipynb

 20 Minutes
A video walkthrough on how to use the iPython notebook
https://www.youtube.com/watch?v=qb7FT68tcA8

Additional resources
Read some more about iPython, and look out for a listing of keyboard shortcuts here.
http://ipython.readthedocs.org/en/stable/

 30 Minutes
Pandas - Quick Intro
Pandas extends Python with data structures and operations for data manipulation and analysis.
http://pandas.pydata.org/pandas-docs/stable/10min.html


  2.2 MATPLOTLIB 1.5+ hours

Matplotlib is a plotting library for Python

 1 - 2 Hours
Basic plotting, default settings, and formatting
http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb

 30 Minutes
Practice commonly used plot types
You will have a chance to play with some more amazing visualization tools later in the course.
http://jakevdp.github.io/mpl_tutorial/tutorial_pages/tut3.html
http://matplotlib.org/api/pyplot_summary.html
http://matplotlib.org/gallery.html


  2.3 GIT AND GITHUB 1+ hours

If you don’t have a Facebook account, some reasonable people may doubt your existence in the Multiverse. Ditto for a Github account in the Tech Universe.

 1 - 2 Hours
Start your Github profile
Stake your cyber-estate claim for free with the first four sections (upto ‘Start a new repository’) of this tutorial.
http://kbroman.org/github_tutorial/
http://git-scm.com/book/en/v2

 5 Minutes
Submit a link to your Github profile
It should contain a new repository created for code from this course.


  2.4 ADDITIONAL PROGRAMMING RESOURCES

If you would like to spend extra time on programming in Python, Learn Python and Code Academy are great. 
http://www.learnpython.org/
http://www.codecademy.com/en/tracks/python

Here's a video walkthrough of Git and Github introduction.
https://www.youtube.com/playlist?list=PL5-da3qGB5IBLMp7LtN8Nc3Efd4hJq0kD



3. DATA WRANGLING 16.5 hours

Data wrangling is the process of taking data in its ‘raw’ form and manipulating it in various ways into a ‘useful’ form. The ‘raw’ data might come to you from an original source or another intermediary source - data sources can vary from unstructured/semi-structured text files (.txt) and delimited/structured/nested format files (excel, csv, json, xml) to relational databases (SQL) and non-relational databases (‘NoSQL’). The ‘useful’ form of the data will be dictated by your current and/or anticipated needs, such as statistical inference or inputs to machine learning algorithms.

Data from original sources is often
* ‘messy’ or ‘dirty’ in the sense that it might contain values that are invalid, missing, corrupted, inconsistent or non-uniform
* ‘coarse’, in the sense that it needs to be refined, transformed or combined with other data.

For the above reasons, in order to derive meaningful conclusions from the data, it needs be ‘cleaned’, ‘scrubbed’, ‘munged’, ‘wrangled’.


  3.1 PANDAS DEEP DIVE  4+ HOURS

Pandas is often a tool of choice for data wrangling operations. You’ve already had a taster, and now it is time to dive deeper and wider with this hands-on tutorial.

 15 Minutes
Download source files
https://github.com/brandon-rhodes/pycon-pandas-tutorial
Detailed instructions for the tutorial can be found here.
https://github.com/brandon-rhodes/pycon-pandas-tutorial#detailed-instructions

 4 - 5 Hours
Watch the video and code along
https://www.youtube.com/watch?v=5JnMutdy6Fw


  3.2 DATA CLEANING WITH PANDAS 1 HOUR

 30 Minutes
Watch this talk on the different ways in which data can be messy and note the techniques employed
https://www.youtube.com/watch?v=_eQ_8U5kruQ

 30 Minutes
Working with missing data
Reinforce your bag of tricks for missing data by going through official Pandas documentation.
http://pandas.pydata.org/pandas-docs/stable/missing_data.html

 
  3.3 WORKING WITH DATA IN FILES 4 HOURS

Data sources can vary from unstructured/semi-structured text files (.txt) and delimited/structured/nested format files (excel, csv, json, xml). While working with data stored in files, the basic operation is to read files into a Pandas data frame. Most of the formats have standard row and column tables, and are relatively easy to work with. JSON and XML are nested formats and need some more work.

 30 Minutes
Practice working with different file formats
For JSON, pay particular attention to normalization.
http://pandas.pydata.org/pandas-docs/stable/io.html

 1.5 Hours
Work on JSON based data exercises and submit on your Github
Instructions for the exercise are in the iPython notebook.
https://www.springboard.com/static/project_files/data_wrangling_json.zip
http://pandas.pydata.org/pandas-docs/stable/io.html#io-json-reader
http://jsonstudio.com/resources/ --JSON datasets

 30 Minutes
Working with XML files in Python
XML does not have a direct reader in Pandas as yet, here is how to deal with it.
http://luisartola.com/software/2010/easy-xml-in-python/

 1.5 Hours
Work on XML based data exercises and submit on your Github
https://www.springboard.com/static/project_files/data_wrangling_xml.zip
https://docs.python.org/2.7/library/xml.etree.elementtree.html
http://www.dbis.informatik.uni-goettingen.de/Mondial


  3.4 WORKING WITH DATA IN DATABASES 6.5+ HOURS

There are two kinds of databases - relational (most commonly based on SQL), and more general (‘NoSQL’ or ‘Not Only SQL’).

 4 - 6 Hours
Mode Analytics: Learn SQL
The wonderful folks at Mode Analytics have created a great SQL learning tool (you'll need a free account with them). The tutorial is worth going through completely, but in order to fulfill the requirements of this class, please work through at least the "Basics" and "Intermediate" sections.
https://sqlschool.modeanalytics.com/toc/

 2 - 4 Hours
Mode Analytics: Analytics Training
Now that you have some SQL under your belt, it's time to apply it to some real data! Mode Analytics has a great set of exercises in the form of case studies using data from Yammer, a popular corporate social network tool. Read the overview and complete at least one of the three case studies to fulfill the requirements of this course
https://sqlschool.modeanalytics.com/analytics-training/yammer/yammer/

 30 Minutes
Overview of NoSQL databases
The last few years have seen a steep growth in applications for which relational databases are too limited and restrictive, and a more general family of ‘NoSQL’ databases have emerged and gained prominence. It is good to know about them, and this article gives a nice overview. We do not require hands-on work on NoSQL databases in this course, but have provided additional resources below in case you would like to explore further.
http://www.thoughtworks.com/insights/blog/nosql-databases-overview

ADDITIONAL RESOURCES
3 hour Pandas tutorial.
https://www.youtube.com/watch?v=w26x-z-BdWQ
Udacity "Data Wrangling with MongoDB" course.
https://www.udacity.com/course/data-wrangling-with-mongodb--ud032

 1 Hour
Submit your Capstone project proposal
Finalize one Capstone idea based on the feedback you got from mentor(s) and peers on your Section 1 submission, and also based on your newly acquired understanding of the tools and data wrangling. Submit a project proposal - a short (1-2 page) document that answers the following questions:

   3.5.1 What is the problem you want to solve

   3.5.2 Who is your client and why do they care about this problem? In other words, what will your client DO or DECIDE based  on your analysis that they wouldn’t have otherwise?

   3.5.3 What data are you going to use for this? How will you acquire this data?

   3.5.4 In brief, outline your approach to solving this problem (knowing that this might change later).

   3.5.5 What are your deliverables? Typically, this would include code, along with a paper and/or a slide deck.

The proposal will be part of a github repository for your project. All code and further documentation you write will be added to this repository.

Once your mentor has approved your proposal, please share the github repository URL on the community and ask for feedback.



  4. DATA STORY 5+ HOURS

Someone important and famous (to be revealed soon!) repeatedly says “Data science is about telling stories and data scientists are the storytellers.” A data story is a powerful way to present insights, by combining visualizations and text into a narrative. In this module, you will use the awesome programming and data wrangling skills you’ve gained to analyze an interesting dataset and come up with a data story.

  4.1 CORE RESOURCES FOR DATA STORY 25+ MINUTES
Ok, end of suspense about important and famous person - You want to know what DJ Patil, the current and first U.S. Chief Data Scientist, says about data scientists and storytelling, right?

 5 Minutes
Data Scientists Should Think Like Journalists
http://blogs.wsj.com/tech-europe/2012/12/13/data-scientists-should-think-like-journalists/

 17 Minutes
Watch DJ’s talk about data storytelling and products, among other things
Great talk on how all the Data around you should give us super-powers to make lives better. Hans Rosling's video on global health is a great example of storytelling with data!
https://www.youtube.com/watch?v=J_CYKk8q1Ao
https://www.youtube.com/watch?v=jbkSRLYSojo

 3 Minutes
A follow-up chat reiterating the importance of storytelling
A quick video reiterating how Data Science is all about curiosity and presenting very complex datasets as incredibly simple insights.
https://www.youtube.com/watch?v=0LtzMhr0ZCM

 5 - 10 Hours
Create your Data Story
So, if DJ says it’s important, we know that it’s important, but how does one go about creating a data story? DJ’s given us some pointers, but they’re probably a bit on the abstract side when you’re just getting started. Also, storytelling is an art, so you have to get your imagination going. Here are some pointers to get those creative juices flowing. In the following sections we will work step-by-step to create your first Data Story

   4.1.1 Pick a dataset - ideally the dataset for your Capstone. If for some reason you want to do this on a different data set, you can find one on Mode Analytics or Google's public data sets directory, or pick another one you like from elsewhere.

   4.1.2 Get going by asking the following questions and looking for the answers with some code and plots:
    4.1.2.1 Can you count something interesting?
    4.1.2.2 Can you find some trends (high, low, increase, decrease, anomalies)?
    4.1.2.3 Can you make a bar plot or a histogram?
    4.1.2.4 Can you compare two related quantities?
    4.1.2.5 Can you make a scatterplot?
    4.1.2.6 Can you make a time-series plot?

   4.1.3 Having made these plots, what are some insights you get from them? Do you see any correlations? Is there a hypothesis you would like to investigate further? What other questions do they lead you to ask?

   4.1.4 By now you’ve asked a bunch of questions, and found some neat insights. Is there an interesting narrative, a way of presenting the insights using text and plots from the above, that tells a compelling story? As you work out this story, what are some other trends/relationships you think will make it more complete?

	You could commit your iPython Notebooks Submit links to a Github (recommended)/Google Drive/Dropbox folder containing data sets, a write-up on the questions you asked and the trends you investigated, and resulting visualizations and conclusions.

ADDITIONAL READING
[Lead with story](http://www.storytellingwithdata.com/2014/07/lead-with-story.html) 
[Making beautiful visualizations with Matplotlib](http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/)
[A brief intro to visualization libraries beyond matplotlb - Seaborn, ggplot, Bokeh, pygal, Plotly](http://pbpython.com/visualization-tools-1.html)
[Why? Why? Why?! A lesson for Data Science teams](http://radar.oreilly.com/2013/04/why-why-why.html)



5. INFERENTIAL STATISTICS 25.5+ HOURS

Descriptive statistics are useful for discovering and communicating insights from data. Inferential statistics are useful for drawing conclusions and predicting outcomes. In this course, the focus is on inferential statistics. For students unfamiliar or rusty with probability and descriptive statistics, [Khan Academy’s probability track](https://www.khanacademy.org/math/probability) is a good refresher. 

We begin with selected portions from a Coursera statistics course that works through the concepts in more detail with examples and applications. Some reading material on A/B testing follows, which is a form of inference, and its use in the context of website features.
 
 
  5.1 PARAMETER ESTIMATION, HYPOTHESIS TESTING AND STATISTICAL SIGNIFICANCE 20.5+ HOURS
You have a data sample, and would like to be able to say something about the population or process that generated this sample. You have a hunch, or a hypothesis, say something like, doing X results in greater benefit or harm compared to doing Y. How can you establish this with confidence, and convince all comers? How much confidence do you have?

 16 Hours
Complete Units 3, 4 and 5 of the Coursera Data Analysis and Statistical Inference course
The videos for this course are archived on the Youtube playlist we have linked to. Start at Unit 3 and complete units 3, 4 and 5 of the course.
https://www.youtube.com/watch?v=HqVC8ut-wCg&index=29&list=PL8rlw5Vq0uG2bsSJkQZVZSNKffm6lgQXo
http://bitly.com/clt_mean

 1.5 Hours
Project 1: What is the true normal human body temperature?
In this exercise, you will analyze a dataset of human body temperatures and employ the concepts of hypothesis testing, confidence intervals, and statistical significance. Data and instructions are in the ipython notebook above.
https://www.springboard.com/static/project_files/statistics_project1.zip
http://www.amstat.org/publications/jse/jse_data_archive.htm
http://www.amstat.org/publications/jse/v4n2/datasets.shoemaker.html

 1 Hour
Project 2: Examining racial discrimination in the US job market
In this exercise, You will perform a statistical analysis to establish whether race has a significant impact on the rate of callbacks for resumes.Instructions and data are provided in the attached ipython notebook.
https://www.springboard.com/static/project_files/statistics_project2.zip

 2 Hours
Project 3: Hospital readmissions data analysis and recommendations for reduction
In this exercise, you will:
* critique a preliminary analysis of readmissions data and recommendations (provided below) for reducing the readmissions rate
* construct a statistically sound analysis and make recommendations of your own
Instructions and data are provided in the attached ipython notebook.
https://www.springboard.com/static/project_files/statistics_project3.zip


  5.2 REGRESSION AND CORRELATION 5 HOURS
You see that the amount of A depends on the quantity of B. How can you statistically quantify this dependence? How can you model a relationship between a dependent variable and independent variables?

 5 Hours
Learn about Regression and Correlation through these videos
https://www.youtube.com/watch?v=o0s2CMAsk64&index=65&list=PL8rlw5Vq0uG2bsSJkQZVZSNKffm6lgQXo


 5.3 A/B TESTING 15+ MINUTES
A/B Testing is a form of hypothesis testing, a randomized experiment with two variants, that has gained prominence for web and mobile design in recent years.

 5 Minutes
Introduction to A/B testing
http://20bits.com/article/an-introduction-to-ab-testing

 10 Minutes
A/B Testing with websites
http://blog.hubspot.com/marketing/a-b-testing-experiments-examples

5.4 ADDITIONAL RESOURCES
* Broader applications: [Randomized Control Trials for measuring social impact](http://www.ted.com/talks/*esther_duflo_social_experiments_to_fight_poverty)
* [Udacity A/B Testing course](https://www.udacity.com/course/ab-testing--ud257)
* [Testing for significance] (https://help.optimizely.com/hc/en-us/articles/200133789-How-long-to-run-a-test#calculating_significance)
* [More on A/B Testing](http://www.evanmiller.org/index.html)
* [Latex Guide](https://www.rochester.edu/College/psc/thestarlab/help/latextut2.pdf) and a [video](https://www.youtube.com/watch?v=-F4WS8o-G2A)



6. CAPSTONE MILESTONE REPORT 5+ HOURS

You have proposed a project, collected a data set, cleaned up the data and explored it with descriptive and inferential statistics techniques. Now’s the time to take stock of what you’ve learned. The project milestone is an opportunity for you to practice your data story skills. Your milestone will be reached when you produce an early draft of your final Capstone report. This is a slightly longer (3-5 page) draft that should have the following:

* An introduction to the problem: What is the problem? Who is the Client? (Feel free to reuse points 1-2 from your proposal document)

* A deeper dive into the data set:
  * What important fields and information does the data set have?
  * What are its limitations i.e. what are some questions that you cannot answer with this data set?
  * What kind of cleaning and wrangling did you need to do?
  * Are there other datasets you can find, use and combine with, to answer the questions that matter?

* Any preliminary exploration you’ve performed and your initial findings. Test the hypotheses one at a time. Often, the data story emerges as a result of a sequence of testing hypothesis e.g. You first tested if X was true, and because it wasn't, you tried Y, which turned out to be true.

* Based on these findings, what approach are you going to take? How has your approach changed from what you initially proposed, if applicable?

Add your code and milestone report to the github repository. As before, once your mentor has approved your milestone document, please share the github repository URL on the community and ask the community for feedback.

While we require only one milestone report, we encourage you and your mentor to plan multiple milestones, especially for more complex projects.

 5 - 10 Hours
Submit your Capstone Milestone Report




# Office Hours
* Data Science Intensive. Here's the video for today's Office Hour Capstone Project Presentation by Sayan de Sarkar: Predicting term deposit subscription by banking customers. A great example of a clear problem definition, and great application of machine learning. 
https://www.youtube.com/watch?v=qETo6sYBJzU&feature=youtu.be



​* Data Science Foundations. Capstone Project Presentation by Tommy Ly: Predicting BikeShare Demand
https://www.youtube.com/watch?v=RybtyRq7LtE&feature=youtu.be