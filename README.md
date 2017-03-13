# Indicators

### About

The plan is that this will be a collection if Jupyter Notebooks attempting to look for interesting indicators within Moodle LMS (and other) data. 

The primary aim is to help progress [the Indicators project](https://indicatorsproject.wordpress.com/) in ways that work toward ideas of reproducible research.

A longer term aim might become to explore how this type of "platform" might be useful within an institution.

[This blog post](http://djon.es/blog/2017/03/08/thinking-about-more-reproducible-research-and-learning-analytics/) describes the origins of the idea.

### Installation and use

1. Install [Jupyter notebooks](http://jupyter.org/install.html)
1. Grab a copy of this repository
1. Create a file caled *config.json* outside of the Indicators directory
> This file specifies the connection to your Moodle database and looks something like (see [sqlalchemy page](http://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls) for more detail
> {
>   "drivername": "postgresql",
>   "database": "",
>   "username": "",
>   "host": "localhost",
>   "port": "5432",
>   "password": ""
> }
1. Modify the *CONFIG* variable in Indicators.py to point to the *config.json* file

