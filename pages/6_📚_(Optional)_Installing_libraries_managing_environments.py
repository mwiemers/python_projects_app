import streamlit as st
from load_css import local_css


st.set_page_config(
    page_title='Installing libraries and managing environments',
    page_icon="📚"
)

local_css("css/style.css")

st.markdown(
    """
## Installing libraries

This page is recommended only after you have worked through the workshop series on the fundamentals of programming in Python and is entirely optional. 
Having completed the workshop series on the fundamentals of programming in Python, you should have a good understanding of the basics of programming in Python, 
and have developed some intuition about what libraries are. This will help you to get the most out of this page.

With Anaconda, many of the most important libraries for data science are already installed. However, you might have to install 
additional libraries for specific projects. To install libraries we use the conda package manager, which comes pre-installed with Anaconda. All the commands
that we will cover in this section are run in the command prompt (Windows) or terminal (Mac) and start with conda. As you will see in this section, 
we can use conda commands to:
* install libraries
* install specific versions of libraries
* check whether specific libraries are installed
* create environments
* install libraries in specific environments
* delete environments


### What is a library?
A library is a collection of tools (functions and classes) to perform specific tasks like data manipulation, visualization, and analysis. 
In the Python Fundamentals workshop, you have come across the random and math library so far. The math library, for instance, has a collection of 
functions for common mathematical functions that are not directly available in Python. The math and random library are built-in into Python and do not 
have to be installed by the user. We can get an overview of the libraries that are installed in our environment by running the following command 
in the command prompt (Windows) or terminal (Mac).

```
pip list
```

If you want to check whether a specific library is installed, you can run the following command, which will return an entry for the **pandas** library if it is installed.
If command returns an empty list, pandas has not been installed. By the way, this command will display all libraries that have the word pandas in their name!

```
pip list pandas
```

#### Installing a library

To install a library, we use the following command, which will install the latest version of the pandas library.

```
pip install pandas
```

#### Installing a specific version of a library

To install a specific version of a library, we use the following command, which will install version 1.4 of the pandas library.

```
pip install pandas==1.4
```

&nbsp;
&nbsp;

### Task: Install the yellowbrick library

The yellowbrick library is a visualization library for machine learning, which lets you create many useful charts to assess your machine learning models
with much less code.

Install the yellowbrick library from the *districtdatalabs* channel.

1. Open the command prompt (Windows) or terminal (Mac).
2. Check whether the yellowbrick library has already been installed.
3. Install the yellowbrick library.
4. Check whether the yellowbrick library has been installed.
"""
)


st.markdown("""
&nbsp;
            
## Creating Environments

### Why do we need environments in programming

You might have noticed that in the terminal or command prompt it says (base) at the beginning of the line. This indicates that you are currently
in the base Anaconda environment. This section is going to explain what an environment is and why we need them.
        
In programming it is important that you can create separate workspaces called environments to work with a 
specific collection of libraries. A library is a complex collection of tools (functions and classes) to perform specific tasks like data manipulation, visualization, analysis, 
machine learning and deep learning. Libraries depend on other libraries. This can potentially create conflicts where two libraries that you need for different projects 
require a different version of a third library. To solve such a dependency conflict, we need to create two separate workspaces or environments. In environment 1, library A 
can work with version 1 of library C. In environment 2, library B can work with version 2 of library C.

Below is an example of this problem. Let's assume you have a data science project and a web application project. For the data science project you need a 
specific data wrangling library. This data wrangling library itself needs a specific Python version and a specific numpy version. For your web 
application project you need a specific web development library. This web development library itself needs a Python version and numpy version that 
is different from the version your data wrangling library needs. The problem is that in a single environment we can only have one version of a specific 
library. You will have to chose whether to use the Python and Numpy version that is required for the data wrangling or the web development library.
""")

st.image("img/manage_environments.png")

st.markdown(
    """
### Managing libraries and environments with conda

To solve this problem, we need to create multiple environments where we can install and use different versions of the same library. To work on our 
data science project, we create a data-science-environment, where we can work with the data wrangling library
which uses Python version 3.10 and NumPy version 1.2.4. To work on our web app project, we create a web-dev-environment, where we can work with 
the web development library which uses Python version 2.7 and NumPy version 1.1.0. 

This might sound complicated, but it basically just means that we create two separate folders on our laptop with different Python and NumPy versions. 
When we want to work on a project, we have to tell conda which environment/folder we want to use to program in Python.

This process of creating separate Python versions for different projects to avoid library dependency problems is easier with Anaconda than it is with 
just Python. We can use the conda package manager not only to install/remove libraries, but also to create, manage and remove environments! Without conda, 
we would have to use separate tools to install/manage libraries and recreate/manage environments. In addition, setting this up is not a straightforward 
process.

**The simplicity of the installation with Anaconda and the fact that we can use conda to manage both libraries and environments with different Python versions is the reason
why we recommend it for beginners.**
""")

st.markdown(
    """
#### Creating a new environment

To create a new environment with conda, we use the following command, which will create a new environment called data-science with the default 
Python version. The default Python version is the version that comes with the Anaconda distribution.

```
conda create --name data-science
```

#### Creating a new environment with a specific Python version

To create a new environment with a specific Python version, we use the following command, which will create a new environment called data-science 
with Python version 3.7.

```
conda create --name data-science python=3.7
```

#### Activating an environment

Unless you switch to an environment, the base environment will be active. Use this command to switch to the an environment named data-science.

```
conda activate data-science
```

#### Deactivating an environment

Deactivating will move you back to the base environment.

```
conda deactivate
```
&nbsp;
""")

st.markdown(
    """
    
### Task: Create a new environment for machine learning projects

1. Open the command prompt (Windows) or terminal (Mac).
2. Create a new environment called mlpy39 with Python version 3.9.
3. Activate the mlpy39 environment.
4. Check whether the correct Python version is active.
5. Install the pandas library in the mlpy39 environment.
6. Check whether the pandas library has been installed in the mlpy39 environment.
7. Deactivate the mlpy39 environment.

&nbsp;
"""
)

st.markdown(
    """
### Task: Install Jupyter Lab and Jupyter Notebooks in the mlpy39 environment

In order to be able to write jupyter notebooks in the mlpy39 environment, we need to install jupyter lab and jupyter notebooks in the mlpy39 environment.

1. Activate the mlpy39 environment.
2. Install jupyter lab and jupyter notebooks in the mlpy39 environment. This has not been covered in the tutorial, so you will have to 
look up the command yourself on the internet. When thinking about how to do this, remember that jupyter lab and jupyter notebooks are libraries and 
that you are installing them with conda.
3. Check whether jupyter lab and jupyter notebooks have been installed in the mlpy39 environment. You should get output similar to the one below. 
The path, version numbers and build names might be different, but the names of the libraries should be the same.
```
# packages in environment at /Users/michaelwiemers/miniconda3:
#
# Name                    Version                   Build  Channel
jupyter                   1.0.0           py310hecd8cb5_7    anaconda
jupyter_client            7.2.2           py310hecd8cb5_0    anaconda
jupyter_console           6.4.3              pyhd3eb1b0_0    anaconda
jupyter_core              4.10.0          py310hecd8cb5_0    anaconda
jupyter_server            1.17.1          py310hecd8cb5_0    anaconda
jupyterlab                3.3.2              pyhd3eb1b0_0    anaconda
jupyterlab_pygments       0.1.2                      py_0    anaconda
jupyterlab_server         2.12.0          py310hecd8cb5_0    anaconda
jupyterlab_widgets        1.0.0              pyhd3eb1b0_1    anaconda
```

4. Deactivate the mlpy39 environment.
5. You changed your mind and decided that mlpy39 is not a good name for the environment. Remove the mlpy39 environment.
6. Check that the mlpy39 environment has been removed and does no longer show up in the list of environments.
"""
)




st.markdown(
    """
<br>

 <div class="highlight blue">
    Come to the pre-sessional workshops if you struggle with any of the steps from this tutorial. You can find more information about the workshops in the 
    <a href="Pre-sessional_Workshops", target="_self">Python Pre-sessional workshops section</a>.
    </div>
    """, unsafe_allow_html=True
)
