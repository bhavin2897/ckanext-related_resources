[![Tests](https://github.com/bhavin/ckanext-related_resources/workflows/Tests/badge.svg?branch=main)](https://github.com/bhavin/ckanext-related_resources/actions)

# ckanext-related_resources
While harvesting Metdata from different Chemistry Repositories, Each dataset has a relation between their corresponding datasets.(ontology mapping)  
This is used by DataCite Schema to provide hierarical relation between the samples. 
For Example:
In [Chemtion Repository](https://www.chemotion-repository.net) they relationship between sample -> Reaction is provided in metadata field "hasPart". 

To provide these corrresponding smaple links to the HOME repository, we use this plugin in CKAN, to display hyperlink of the dataset. 


## Requirements

Database Migration is done, to establibsh new tables within the CKAN PostgreSQL database. 
For more information please check offical documenation: https://docs.ckan.org/en/2.9/extensions/best-practices.html


Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.8 & eariler             | not tested    |
| 2.9             | yes   |



NOTE: If you are creating your own migration tables then,
Please follow official documentation preciesly. (https://docs.ckan.org/en/2.9/extensions/best-practices.html)

You can copy migration python file and version control files, after creating migration is done. 
if you are using different table names & column names, please name them using "lower_cases" instead of CamelCase. 

## Installation

To install ckanext-related_resources:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

    git clone https://github.com/bhavin2897/ckanext-related_resources.git
    cd ckanext-related_resources
    pip install -e .
	pip install -r requirements.txt

3. Add `related_resources` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload

5. To upgrade ckan database, for the tables you have created:
	ckan -c /etc/ckan/default/ckan.ini db upgrade -p related_resources
	
You will get a message  `Upgrading DB: SUCCESS`. 

Later, check the database list of tables for the ckan user to see the table for the migrated/generated table.  
## Config settings

None at present


## Developer installation

To install ckanext-related_resources for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/bhavin2897/ckanext-related_resources.git
    cd ckanext-related_resources
    python setup.py develop
    pip install -r dev-requirements.txt
    
Restart Server if you are using Supervisor and Nginx

    sudo service supervisor reload
    sudo service nginx reload 


## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini


## Releasing a new version of ckanext-related_resources

If ckanext-related_resources should be available on PyPI you can follow these steps to publish a new version:

1. Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.

2. Make sure you have the latest version of necessary packages:

    pip install --upgrade setuptools wheel twine

3. Create a source and binary distributions of the new version:

       python setup.py sdist bdist_wheel && twine check dist/*

   Fix any errors you get.

4. Upload the source distribution to PyPI:

       twine upload dist/*

5. Commit any outstanding changes:

       git commit -a
       git push

6. Tag the new release of the project on GitHub with the version number from
   the `setup.py` file. For example if the version number in `setup.py` is
   0.0.1 then do:

       git tag 0.0.1
       git push --tags

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
