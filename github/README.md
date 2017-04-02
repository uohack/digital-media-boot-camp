[Github](https://github.com/) is a version control tool that allows you to backup your code, as well as collaborate with others. It also helps manage projects by providing a useful history of commits, a issue ticket system (to keep track of issues or things you need to work on) and editable wiki pages for documentation.

You can think of Github as half social media for programmers, half code repository.

There is a bit of a learning curve with Github but once you begin to understand some of the vocabulary, it's really quite simple.

# Intro

Github is build off of a tool called git. Git is a text version control software that tracks changes made to text documents. It's similar to viewing changes made to a Google doc, but it is not automatic.

In order for git to know about the changes you've made you need to add and commit them to git. This allows git to follow what you're doing and create a history of commits.

After you've committed things to git then you can push them up to Github. In other words, git will track your changes, but Github is the cloud hosting for your files and changes. It's like if you write an essay in a Word document, you want to save early and often (that's equivalent to git), but you also want cloud backups to you save that file to a Dropbox folder (that's equivalent to Github). That way, each time you save, it is backed up.

Each project lives in its own Github repository. You can have as many repositories as you'd like and each one comes with the features mentioned above like issues, wikis and commit histories.

Repositories can have different branches. Typically you have one branch for development and one branch for production. Github also offers a free special feature called Github Pages where they'll host basic HTML/CSS/JS files for you if you put them in a branch called "gh-pages". Then your files will render out at `yourusernam.github.io/repositoryname/`.

# Getting started

Github has some great documentation so I won't walk through everything here, but here's the basic workflow.

  * Create repository for new project on Github.com and clone empty repo to your computer (this should just be an empty folder)
  * Code out part of project in that folder on your machine
  * Commit and push changes to Github using Github Desktop application (or command line if you're into that sort of thing)
  * Code more stuff, commit & push new changes, repeat

And here are some helpful links.

  * [Download Github Desktop](https://desktop.github.com/)
  * [Hello World - Github Guides](https://guides.github.com/activities/hello-world/)
  * [Getting started with Github Pages - Github Guides](https://guides.github.com/features/pages/)  

# Vocab

All of the vocab below, and more, can be found at the [Github Glossary](https://help.github.com/articles/github-glossary/). Please note, I've taken these definitions and simplified them as best I can.

  * Git - Git is an open source program for tracking changes in text files. It is the core technology that GitHub is built on top of.
  * User - Users are personal GitHub accounts. Each user has a personal profile, and can own multiple repositories, public or private. They can create or be invited to join organizations.
  * Repository - A repository is the most basic element of GitHub. They're easiest to imagine as a project's folder. A repository contains all of the project files, and stores each file's commit history. Repositories can have multiple collaborators and can be either public or private.
  * Commit - A commit, or "revision", is an individual change to a project file or set of files. It's like when you save a Word document, except with Git, every time you commit a project it creates a unique ID (a.k.a. the "SHA" or "hash") that allows you to keep record of what changes were made when and by who. Commits usually contain a commit message which is a brief description of what changes were made.
  * Push - Pushing refers to sending your committed changes to a remote repository such as GitHub. For instance, if you change something locally, you'd want to then push those changes so that others may access them and for them to have a cloud backup.
  * Pull - Pull refers to when you are fetching changes to a project, not seen in your local project. For instance, if someone has edited a project you're both working on, you'll want to pull in those changes to your local project so that it's up to date.
  * Clone - A clone is a copy of a repository that lives on your computer instead of on a website's server somewhere, or the act of making that copy. With your clone you can edit the files on your local machine and use Git to keep track of your changes without having to be online. It is, however, connected to the remote version so that changes can be synced between the two. You can push your local changes to the remote to keep them synced when you're online.

