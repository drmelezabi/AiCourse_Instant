# Create Anaconda Enviroment

### Using Anaconda navigator

- Open "_ANACONDA NAVIGATOR_"
  ![ANACONDA NAVIGATOR](/Tasks/03_25-07-2023/Images/01_Anaconda_navigator.png)

- From the "_Side Tabs Bar_" select "_Environments_"
  ![Side Tabs Bar](/Tasks/03_25-07-2023/Images/02_Tabs_bar.png)

- It will open the Environment show the UI window
  ![Environment UI](/Tasks/03_25-07-2023/Images/03_Enviroments_Tab.png)

- From the "_Environment Side Tabs Bar_"
  ![Environment Side Tabs Bar](/Tasks/03_25-07-2023/Images/04_Enviroments_Side_Bar.png)

- Select "_Create_" from the "_Action buttons_"
  ![Action buttons](/Tasks/03_25-07-2023/Images/05_Action_bottons.png)

- it will open a popup "_creating window_"
  ![popup creating window](/Tasks/03_25-07-2023/Images/06_Create_new_Enviroment_popup_window.png)

- Enter your custom ENV "_name_"
  ![popup creating window](/Tasks/03_25-07-2023/Images/07_Enter_Name.png)

- then choose Environment "_Python version_"
  ![popup creating window](/Tasks/03_25-07-2023/Images/08_Select_Python_Version.png)

- Finally Press "_Create_"
  ![popup creating window](/Tasks/03_25-07-2023/Images/09_Press_create.png)

- Now you can check that the Environment Created
  ![popup creating window](/Tasks/03_25-07-2023/Images/10_Enviroment_created.png)

### Using Terminal method

- open "_Anaconda Powershell Prompt_"
  ```ps
  conda create --name <cutom-name> python=<python-version>
  ```
- Example
  ```ps
  conda create --name instant-3-9-17-ENV-terminal python=3.9.17
  ```
- It will load some data then ask you to confirm => type <b>y</b> and press <b>Enter</b>

  ```ps
  The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/win-64::ca-certificates-2023.05.30-haa95532_0
  openssl            pkgs/main/win-64::openssl-3.0.9-h2bbff1b_0
  pip                pkgs/main/win-64::pip-23.2.1-py39haa95532_0
  python             pkgs/main/win-64::python-3.9.17-h1aa4202_0
  setuptools         pkgs/main/win-64::setuptools-68.0.0-py39haa95532_0
  sqlite             pkgs/main/win-64::sqlite-3.41.2-h2bbff1b_0
  tzdata             pkgs/main/noarch::tzdata-2023c-h04d1e81_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  wheel              pkgs/main/win-64::wheel-0.38.4-py39haa95532_0


  Proceed ([y]/n)? y

  ```

- it will download the packages and notice that it's ready to activate with conda command

  ```ps
  Downloading and Extracting Packages

  Preparing transaction: done
  Verifying transaction: done
  Executing transaction: done
  #
  # To activate this environment, use
  #
  #     $ conda activate instant-3-9-17-ENV-terminal
  #
  # To deactivate an active environment, use
  #
  #     $ conda deactivate

  ```

- now you can activate it
  ```ps
  conda activate instant-3-9-17-ENV-terminal
  ```
