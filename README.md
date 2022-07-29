
# Online Forum Project

This is a Django web app I am developing to learn how to use Django 
and brush up on my general web development skills. The plan is to make 
it a website where lovers of football, or Futbol, can come to post their 
thoughts on the current happenings in the football world, and other 
users can comment on these posts to say how they feel about the topic 
in the post.  
I plan on adding more features, like a fixtures and results section, in 
the future, but for now, this is what I am going for.


## Authors

- [@chigoziedavis](https://www.github.com/chidave)


## Acknowledgements

 - [Readme Generator](https://readme.so)
 - [Database Model for an Online Discussion Forum](https://vertabelo.com/blog/database-model-for-an-online-discussion-forum-part-1/)


## Run Locally

Clone the project

```bash
  git clone https://github.com/chidave/Online-Forum-Project.git
```

Go to the project directory

```bash
  cd Online-Forum-Project
```

Install dependencies and libraries

```bash
  pip install -r requirements.txt
```

Setup the database of choice, and change database settings in 
setting.py accordingly.

Run migrations

```bash
  python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```

