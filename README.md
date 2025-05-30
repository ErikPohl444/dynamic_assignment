# Dynamic_Assignment

> [!WARNING]
> This code attempts to find and delete a pycache file for a shared state module it created.
> This is the "secret sauce" which allows repeated different "import froms" the same module.
> If you don't like this behavior, turn away!  

Converts json into variables with values, with some validation!

Use case:
- Imagine you've got some json.
- For this example, the json is fairly flat: one level deep.
- It consists, as json does, of key value pairs.
- You want to turn at least some of the keys into variables in your code.
- You want the values for those keys to become the values for the variables.
- Still with me?
- You're converting at least some of the key/value pairs in the json into variables in your code.
- But wait-- there's more.
- You only want to do this if all of the keys are present!
- So first it checks to make sure all of the keys->variables keys are present.
  - No? It provides an exception with all of the missing keys, not one at a time.  
  - Yes? It allows you to import the variables into your code from a shared state file it made on the fly.
   
Currently contains one class: write_configs and a demo usage in dynamic_assignment.py.
The class accepts as contructor params:
- A file name for a Python module containing variables to be imported
- A dictionary from which to get variables and values
- A list of keys which must be in the dictionary or else the dictionary is incomplete

What the class does is:
- Confirms all of the keys are in the dictionary
- Produces an error if not
- If all the keys are in the dictionary, creates an updated Python module assigning values to variable names based on the keys

What you do:
- Call the class object with good parameters
- Add some cruft-looking code-- the magic cruft:
```
import configs
importlib.reload(configs)
from configs import t1_xf, t2_xf, t3_xf, t4_xf
```
- Import your variables with the values from the dictionary (see above)

> [!IMPORTANT]
> No more referring to shared values in dicts!  These are first-order variables you've just made using dynamic assignment.

## Future plans

List a roadmap or future plans for the repo work.

- [ ] 

## Repo checklist

Repo checklist:

* [ ] Run foundation.py with the destination project folder as a command line argument.
    * This will copy all important files to your project, renaming at least one for your repo.
    * Don't worry.  It won't overwrite existing files with the same names there.
* [ ] Add your favorite [git aliases](https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases) to .git/config.
    * Don't have favorites?  Try out the aliases from [Ned Batchelder's](https://github.com/nedbat) [dot repo](https://github.com/nedbat/dot), extracted into [this file](https://github.com/ErikPohl444/resources/blob/main/git_aliases.txt). 
* [ ] Complete a starter [.gitignore](https://git-scm.com/docs/gitignore#:~:text=A%20gitignore%20file%20specifies%20intentionally,gitignore%20file%20specifies%20a%20pattern.)
    * [ ] Keep the current starter .gitignore and add to it.
    * [ ] OR delete the starter I'm providing and either create one via template in GitHub by typing in the name .gitignore in the file name after choosing to create a file
    * [ ] OR create one [using this tool.](https://www.toptal.com/developers/gitignore/)
* [ ] Populate AUTHORS.md with the authors of the work in the repo. 
    * Foundation will populate the first commit author if it can find a git repo and at least one commit.
    * Refer to [these instructions](https://opensource.google/documentation/reference/releasing/authors) for other ways to create and maintain this reference. 
* [ ] Add a [sponsor button](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/displaying-a-sponsor-button-in-your-repository), if you intend to solicit funding for the work in your repo.
* [ ] Add a [social media image](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview), if you'd like your repo to have a specific image when referenced in social media.
* [ ] Add [topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics) to your repo to help the repo be searchable and comprehensible.
* [ ] Enter any acknowledgements into ACKNOWLEDGEMENTS.md to acknowledge inspirations, code you've used, and people who helped you in your journey to this repo.
* [ ] Accept a license to define how people can legally use, share, etc. your repo:
    * The default license provided by this process is the [MIT License](https://en.wikipedia.org/wiki/MIT_License).  **This is automated in Foundation, but it needs to see a git repo with a commit to change this.**
    * If you don't want that one, delete it from your repo and use GitHub to [select one easily](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository).
* [ ] Accept a code of conduct to indicate how members of the community around your repo should interact:
    * Delete the current CODE_OF_CONDUCT.md if you don't want the recommended code of conduct for small projects, as currently available from GitHub.
    * If you prefer another code of conduct, you can make your own or use GitHub's [easy instructions](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project).
* [ ] Accept a CODEOWNERS file to enforce who the code owners are.
    * Blank is fine to start out with.
    * Use [these instruction](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) from Github if you'd like to develop CODEOWNERS more.
* [ ] Modify CONTRIBUTING.md, if you want [instructions for contributing to your repo](https://contributing.md/how-to-build-contributing-md/).
    * More detail can be found [here](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors).
* [ ] Add a [CITATIONS.cff file](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files) if you'd like to specify how others cite your work.
* [ ] Update README.md to pull all of the above together, along with other items important to understanding your repo.
* [ ] If you need a Makefile for builds, [make one](https://makefiletutorial.com/)
* [ ] If you need a Manifest, [manifest one](https://docs.github.com/en/apps/sharing-github-apps/registering-a-github-app-from-a-manifest).
* [ ] Consider releasing a [release plan](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).
* [ ] Do you need/want a config file in json, yaml, or .ini?
* [ ] Incorporate a [CI/CD pipeline](https://github.com/resources/articles/devops/ci-cd):
    * [ ] Create GitHub Actions [for your repo](https://github.com/features/actions).
        * Other tools like [Travis](https://www.travis-ci.com/) and [Jenkins](https://www.jenkins.io/solutions/pipeline/) and [Azure DevOps Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines?view=azure-devops) are available.    
    * [ ] Create [Git hooks](https://git-scm.com/book/ms/v2/Customizing-Git-Git-Hooks), if you'd like.
        * I recommend [pre-commit](https://pre-commit.com/).
        * [Husky](https://typicode.github.io/husky/) is also available.
    * [ ] Confirm the following items are captured using Sonarqube or other static analysis tools and that you have a minimum tolerance for each metric which is tested against:
        * Code Complexity:
            * Cognitive complexity
            * Cyclomatic code complexity
        * Duplications
        * Maintainability
        * Issues metrics
        * Reliability
        * Size
        * Test Coverage
        * Passing and failing test metrics
        * Security
        * Linting  
* [ ] Containerize the code for distribtion, if you'd like.
    * Add, for example, a Dockerfile or compose.yaml, if using Docker.   
* [ ] This is a parent checkbox for all Python-specific items:
  * [ ] Populate [requirements.txt](https://pip.pypa.io/en/stable/reference/requirements-file-format/) and keep it populated through pip freeze > requirements.txt
  * [ ] Confirm tests are in /tests.
      * [ ] Leverage [pytest](https://docs.pytest.org/en/stable/) or another fully-modernized test framework for  testing.
      * [ ] Leverage [coverage.py](https://coverage.readthedocs.io/en/7.6.10/) or a similar tool for code coverage analysis.
  * [ ] Confirm source code is in /src
      * [ ] For a linting tool in your CI/CD pipeline or for integration with your IDE, consider ruff, pylint, flake8.
      * [ ] For a type-checking tool in your CI/CD pipeline, consider mypy.
      * [ ] There is a very primitive [setup_logging.py](https://github.com/ErikPohl444/resources/blob/main/src/setup_logging.py) file included here to import for [logging purposes](https://docs.python.org/3/library/logging.html).  Delete it, make your own, etc.  
  * [ ] Confirm docs are in /docs
  * [ ] If you'd like eventually to make a Python package, there's a starter [pyproject.toml](https://packaging.python.org/en/latest/tutorials/packaging-projects/#configuring-metadata) you can edit, or you can delete this file.
    * Because this resources utility is Python build tool agnostic, I am not including a setup.py for setuptools, or any other files or configurations specific to Hatchling, Poetry, setuptools, Flit, or PDM.
    * More in-depth pyproject.toml information [here](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/).
        
## Important disclaimer

If any disclaimer exists, add it here.

Here are recommended entries for your README.md based on your repository's files and configuration:

---

## Getting Started

Clone the repository to your local machine:

```bash
git clone https://github.com/ErikPohl444/dynamic_assignment.git
cd dynamic_assignment
```

## Installing

1. (Optional but recommended) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

2. Install the project dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

   Or, if you prefer, you can use the `pyproject.toml` to install as a package manager-ready project.

---

## Prerequisites

- Python >= 3.8
- pip (Python package manager)
- (Optional) Virtual environment tool such as `venv`

The main dependencies are listed in `requirements.txt` and include:
- colorama
- coverage
- GitPython
- mypy
- pytest
- ruff
- typing_extensions
- uv
...and others.

For more details about these dependencies or advanced setup (such as building from source), consult the [`requirements.txt`](https://github.com/ErikPohl444/dynamic_assignment/blob/main/requirements.txt) or [`pyproject.toml`](https://github.com/ErikPohl444/dynamic_assignment/blob/main/pyproject.toml) files.

## Running the tests

Provide instructions on running the tests here.

## Technologies used

List the technologies used here.

e.g.
* Written in Chicken 2.0

## Minimum system requirements

List the minimum system requirements for the application to run.

e.g.
* Must be run on VALIS.

## Contributing

I invite contributions.  See the [Contribution Guidelines](CONTRIBUTING.md) for any guidelines.

## Authors

See the [Authors doc.](AUTHORS.md)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Thanks to everyone who has motivated me to learn more.
* These folks were key to this particular effort: [ACKNOWLEDGEMENTS](ACKNOWLEDGEMENTS.md)
