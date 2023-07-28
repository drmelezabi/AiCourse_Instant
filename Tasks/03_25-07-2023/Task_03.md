<!DOCTYPE html>
<html>
<head>
</head>
<body>

<h1>Create Anaconda Environment</h1>

<h3>Using Anaconda Navigator</h3>

<ul>
  <li>Open "<b>ANACONDA NAVIGATOR</b>"
    <br>
    <img src="/Tasks/03_25-07-2023/Images/01_Anaconda_navigator.png" alt="ANACONDA NAVIGATOR">
  </li>
  <li>From the "<b>Side Tabs Bar</b>" select "<b>Environments</b>"
    <br>
    <img src="/Tasks/03_25-07-2023/Images/02_Tabs_bar.png" alt="Side Tabs Bar">
  </li>
  <li>It will open the Environment show the UI window
    <br>
    <img src="/Tasks/03_25-07-2023/Images/03_Enviroments_Tab.png" alt="Environment UI">
  </li>
  <li>From the "<b>Environment Side Tabs Bar</b>"
    <br>
    <img src="/Tasks/03_25-07-2023/Images/04_Enviroments_Side_Bar.png" alt="Environment Side Tabs Bar">
  </li>
  <li>Select "<b>Create</b>" from the "<b>Action buttons</b>"
    <br>
    <img src="/Tasks/03_25-07-2023/Images/05_Action_bottons.png" alt="Action buttons">
  </li>
  <li>It will open a popup "<b>creating window</b>"
    <br>
    <img src="/Tasks/03_25-07-2023/Images/06_Create_new_Enviroment_popup_window.png" alt="popup creating window">
  </li>
  <li>Enter your custom ENV "<b>name</b>"
    <br>
    <img src="/Tasks/03_25-07-2023/Images/07_Enter_Name.png" alt="popup creating window">
  </li>
  <li>Then choose Environment "<b>Python version</b>"
    <br>
    <img src="/Tasks/03_25-07-2023/Images/08_Select_Python_Version.png" alt="popup creating window">
  </li>
  <li>Finally Press "<b>Create</b>"
    <br>
    <img src="/Tasks/03_25-07-2023/Images/09_Press_create.png" alt="popup creating window">
  </li>
  <li>Now you can check that the Environment Created
    <br>
    <img src="/Tasks/03_25-07-2023/Images/10_Enviroment_created.png" alt="popup creating window">
  </li>
</ul>

<h3>Using Terminal method</h3>

<ul>
<li>
<p>Open "<b>Anaconda Powershell Prompt</b>"</p>

<pre><code>
conda create --name &lt;custom-name&gt; python=&lt;python-version&gt;
</code></pre>
</li>

<li>
<p>Example</p>

<pre><code>
conda create --name instant-3-9-17-ENV-terminal python=3.9.17
</code></pre>
</li>

<li>
<p>It will load some data then ask you to confirm => type <b>y</b> and press <b>Enter</b></p>
<pre><code>
The following NEW packages will be INSTALLED:

ca-certificates pkgs/main/win-64::ca-certificates-2023.05.30-haa95532_0
openssl pkgs/main/win-64::openssl-3.0.9-h2bbff1b_0
pip pkgs/main/win-64::pip-23.2.1-py39haa95532_0
python pkgs/main/win-64::python-3.9.17-h1aa4202_0
setuptools pkgs/main/win-64::setuptools-68.0.0-py39haa95532_0
sqlite pkgs/main/win-64::sqlite-3.41.2-h2bbff1b_0
tzdata pkgs/main/noarch::tzdata-2023c-h04d1e81_0
vc pkgs/main/win-64::vc-14.2-h21ff451_1
vs2015_runtime pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
wheel pkgs/main/win-64::wheel-0.38.4-py39haa95532_0

Proceed ([y]/n)? y
</code></pre>

</li>

<li>
<p>It will download the packages and notice that it's ready to activate with conda command</p>

<pre><code>
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
</code></pre>
</li>
<li>
<p>Now you can activate it</p>

<pre><code>
conda activate instant-3-9-17-ENV-terminal
</code></pre>
</li>
</ul>
</body>
</html>
