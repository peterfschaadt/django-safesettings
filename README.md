# django-safesettings

I created [django-safesettings](https://github.com/peterfschaadt/django-safesettings) to solve Django's problem with separating unique settings from development and production environments. 

## Settings variables

{{ AUTHOR_NAME }} = Your name  
{{ AUTHOR_EMAIL }} = Your email address  
{{ PROJECT_NAME }} = The name of your Django project (the folder containing settings.py)

## Files

### common_settings.py

This file holds the settings that are consistent between your development and production environments. Think of it as containing shared settings.

### dev_settings.py

This file holds the unique settings for your development environment.

### prod_settings.py

This file holds the unique settings for your production environment.

### local_settings.py

This file holds the sensitive settings for each environment, like database credentials, API keys, and your Django secret key. You will have one ```local_settings.py``` file for each environment, stored outside of your repository. See below for "Copying local_settings.py." This file does NOT get checked into version control!

## Getting started

1\. Git clone and navigate inside the repository

```
git clone https://github.com/peterfschaadt/django-safesettings
cd django-safesettings
```

2\. Copy the ```settings``` directory and its contents from this repository to the location of your app's ```settings.py```

```
cp settings /home/django/web/{{ PROJECT_NAME }}/{{ PROJECT_NAME }}
```

3\. Remove the ```settings.py``` file that you will no longer be using. You can also rename it (Example: ```old_settings.py```) and remove later if you need to copy individual settings out of it.

4\. Create a file called ```local_settings.py``` using ```example_local_settings.py``` as a template. Be sure to [generate a new Django key](http://www.miniwebtool.com/django-secret-key-generator) or copy the one over from your previous ```settings.py``` file (only if it was never checked into version control).

## Copying local_settings.py

Here are two different methods of placing your environment-specific ```local_settings.py``` file inside your settings folder. It is important that each environmeny's ```local_settings.py``` is not tracked by your version control system (django-safesettings has it included in .gitignore).

1. I recommend an SFTP tool like [FileZilla](https://filezilla-project.org) or [CyberDuck](http://cyberduck.ch) to securely place ```local_settings.py``` on the server. However, this is harder to automate with a script than the Fabfile command below.

2. Use a [Fabric](http://docs.fabfile.org/en/1.6/) command to place the correct ```local_settings.py``` file on your server. Here's a simple command to put in your ```fabfile.py``` to copy your local_settings.

```python
def copy_local_settings():
    """
    put('from/this/folder', 'to/this/folder')
    """
    put('/home/{{ AUTHOR_NAME }}/django/local_settings.py', 
        /home/django/{{ PROJECT_NAME }}/{{ PROJECT_NAME }}/settings/)
```

3. Use [Secure Copy](http://www.hypexr.org/linux_scp_help.php) (SCP) to transfer the file over SSH.

```
scp local_settings.py <USER>@<HOST>:/home/django/{{ PROJECT_NAME }}/{{ PROJECT_NAME }}/settings/
```

## Background

I created django-safesettings to use on my [ChromeFiddle](http://chromefiddle.com) project. I wanted to host the site's source code publicly on GitHub but I needed to protect Django's secret key, database credentials, and my email password. With this module I was able to make the source code available on GitHub, but I could still protect the security of my site.
