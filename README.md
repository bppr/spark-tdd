### Setup to Run Locally (MacOS)

 - https://brew.sh/ if you don't have homebrew 
 
 in the terminal...
 - `brew install java` - apache spark needs the jvm
 - `echo 'export JAVA_HOME=/opt/homebrew/opt/java' >> ~/.zprofile`
 - These instructions assume 
    - `echo 'alias python=python3' >> ~/.zprofile` 
    - `echo 'alias pip=pip3' >> ~/.zprofile` 
but you may use any aliases or none.
 - `cd` into the project's root & run:
 - `python -m venv .venv` which should genreate 
   - a `pyvenv.cfg` file and other env deps into a folder called `.venv`
 - `source .venv/bin/activate` needed each time you cd into the project dir :nauseated_face:
 - `pip install -r requirements-test.txt`

### Test Locally

 - `pytest` :tada: