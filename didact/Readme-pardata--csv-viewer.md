<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
html,
div,
body {
background-color: #1a1a1a;
font-family: 'IBM Plex Sans', sans-serif;
font-size: 18px;
outline: none;
}
body {
font-family: Helvetica, sans-serif;
}
/* The actual timeline (the vertical ruler) */
.timeline {
position: absolute;
max-width: 1200px;
margin: 0 auto;
margin-left: 50px;
}
.content p {
margin: 0px;
}
.content .afterbutton
{
padding-top: 16px;
}
/* The actual timeline (the vertical ruler) */
.timeline::after {
content: '';
position: absolute;
width: 1px;
background-color: white;
top: 15px;
bottom: 80px;
left: 18px;
margin-left: -2px;
}
/* Container around content */
.container {
padding: 0px 0px;
width: 70%;
align-content: left;
margin: 0px 0px 0px 0px;
margin-left: 25px;
margin-top: 32px;
}
/* The circles on the timeline */
.container::after {
content: '';
position: absolute;
width: 10px;
height: 10px;
right: -6px;
background-color: white;
border: 0px solid #FF9F55;
top: 15px;
border-radius: 50%;
z-index: 1;
margin: 0px 0px 0px 0px;
}
/* Place the container to the left */
.left {
left: 0px;
}
/* Place the container to the right */
.right {
left: 0px;
}
/* Add arrows to the left container (pointing right) */
.left::before {
content: " ";
height: 0;
top: 22px;
width: 0;
z-index: 1;
right: 30px;
border: medium solid white;
border-width: 10px 0 10px 10px;
border-color: transparent transparent transparent white;
}
/* Fix the circle for containers on the right side */
.right::after {
left: -13px;
}
/* The actual content */
.content {
padding: 5px 10px;
color: white;
background: transparent;
}
.button.is-dark.is-medium {
font-family: 'IBM Plex Sans', sans-serif;
background: transparent;
border-color: white;
color: #fff;
border: 1px solid white;
padding: 10px;
padding-left: 20px;
margin-bottom: 13px;
border-radius: 0px;
min-width: 180px;
font-size: 14px;
text-align: left;
min-height: 48px;
margin: 0px;
justify-content:left;
}
.button.is-dark.is-medium:hover {
font-family: 'IBM Plex Sans', sans-serif;
background-color: #2a67f5;
border-color: white;
color: #fff;
}
.footer {
display: flex;
background-color: #343A3E;
margin: 500px 0px 0px 20px;
padding: 0px;
max-width: 1200px;
}
.github-icon {
min-height: 100%;
min-width: 100%;
object-fit: cover;
object-position: 250% 100px;
opacity: 15%;
bottom: 15px;
}
.image-content {
padding: 5px 10px;
background: transparent;
color: black;
position: absolute;
font-size: 27px;
}
.image-div {
position: relative;
background-color: white;
min-width: 50%;
background-image: linear-gradient(rgba(255,255,255,0.9), rgba(255,255,255,0.9)), url("https://github.com/bodarajeshkumar/Developer-Playground/blob/master/didact/images/git.svg?raw=true");
background-position: -50% 60px;
background-repeat: no-repeat;
padding-top: 20px;
padding-left: 20px;
}
.image-btn {
position: absolute;
right: 0;
bottom: 0%;
background-color: #0062FF;
max-width: 300px;
min-width: 100px;
width: 300px;
padding: 0px;
padding-bottom: 20px;
}
.image-link span
{
float: right;
font-size: 32px;
padding-right: 10px;
}
.image-btn .image-link:hover
{
text-decoration: none;
color: white;
background-color: #0353E9;
}
.image-btn  a:hover
{
text-decoration: none;
color: white;
}
.image-link {
color: white;
display: block;
padding: 5px 10px 5px 10px;
line-height: 28px;
font-size: 16px;
}
.header
{
background-image: url('https://wallpaperaccess.com/full/1426870.png');
width: 100%;
height: fixed;
min-height: 300px;
display: inline-block;
margin-top: 20px;
margin-bottom: 20px;
margin-left: 30px;
margin-right: 30px;
background-size: contain;
max-width: 1200px;
background-size: cover;
}
.header .right-content
{
float: right;
width: 45%;
background-color:#2a67f5;
min-height:400px;
padding:20px;
font-size: 14px;
}
.header .right-content h4
{
background: none;
color: white;
padding-left: 25px;
padding-right: 25px;
}
.header .right-content div
{
background: none;
color: white;
padding-left: 25px;
padding-right: 25px;
font-size: 14px;
margin-bottom: 10px;
}
.header .right-content ul
{
margin: 0px;
margin-left: 25px;
margin-bottom: 10px;
line-height: 16px;
}
.container a
{
color: #78A9FF;
background-color: transparent;
text-decoration: none;
}
.container a:visited
{
color: #8C43FC;
background-color: transparent;
text-decoration: none;
}
.apptitle
{
margin-left: 25px;
margin-top: 20px;
margin-bottom: 0px;
font-size: 25px;
color: white;
}
@media only screen and (max-width: 800px) {
.footer {
    margin: 950px 0px 0px 20px;
}
}
@media only screen and (max-width: 700px) {
.footer {
    margin: 1050px 0px 0px 20px;
}
}
@media only screen and (max-width: 600px) {
.footer {
    margin: 1050px 0px 0px 20px;
}
}
@media only screen and (max-width: 500px) {
.footer {
    margin: 1100px 0px 0px 20px;
}
}
@media only screen and (max-width: 400px) {
.footer {
    margin: 1200px 0px 0px 20px;
}
}
}
</style>
</head>
<body>
    <div class="apptitle">
        CSV viewer for IBM® Developer Playground
    </div>
    <div class="header">
        <div class="right-content">
            <div>        
                The CSV Viewer provides a simple Flask application to load and view data archive files. In the backend, ParData is used to easily extract the data files that is ultimately displayed in the UI.
            </div>
            <div>
                ParData (homophone of partake) is a Python API that enables data consumers and distributors to easily use and share datasets, and establishes a standard for exchanging data assets
            </div>
            <div>
                It enables:
                <ul>
                    <li>a data scientist to have a simpler and more unified way to begin working with a wide range of datasets, and</li>
                    <li>a data distributor to have a consistent, safe, and open source way to share datasets with interested communities.</li>
                </ul>
            </div>
            <div>
                Don't worry, you don't have to code to figure it out. It's just a few clicks away
            </div>
        </div>
    </div>
    <div class="timeline">
        <div style="margin-top:0;" class="container right">
            <div class="content">
                <p>To begin, we'll need to clone the GitHub repository</p>
                <a class="button is-dark is-medium" title="Clone the Repo" href="didact://?commandId=extension.sendToTerminal&text=PardataCSVViewer%7Cget-code%7CPardataCSVViewer|git%20clone%20-b%20pardata%20--sparse%20https://github.com/IBM/Developer-Playground.git%20${CHE_PROJECTS_ROOT}/pardata/%20%26%26%20cd%20${CHE_PROJECTS_ROOT}/pardata/%20%26%26%20git%20sparse-checkout%20init%20--cone%20%26%26%20git%20sparse-checkout%20add%20docs%20pardata%20requirements%20tests%20examples">Get Code</a>        
            </div>
        </div>
        <div class="container right">
            <div class="content">
                <p>Need we need to install all the requirements</p>
                <a class="button is-dark is-medium" title="Install requirements" href="didact://?commandId=extension.sendToTerminal&text=PardataCSVViewer%7Cinstall-requirememnts%7CPardataCSVViewer|cd%20pardata/examples/csv-viewer;pip%20install%20-r%20requirements.txt">Install requirements</a>
            </div>
        </div>
        <div class="container right">
            <div class="content">
                <p>We can now start the app</p>
                <a class="button is-dark is-medium" title="Start the app" href="didact://?commandId=extension.sendToTerminal&text=PardataCSVViewer%7Cstart-app%7CPardataCSVViewer|python%20app.py">Start the app</a>
            </div>
        </div>
    </div>
    <div class="footer">
      <div class="content" style="padding:30px;padding-left:60px;padding-bottom: 0px;">
        <p>If you'd like to make changes and explore the application, make sure to stop it first!</p>
        <a class="button is-dark is-medium" title="Stop Running Application" href="didact://?commandId=vscode.didact.sendNamedTerminalCtrlC&text=PardataCSVViewer">Stop Running Application</a>
        </br></br></br>
      </div>
      <div class="image-div">
        <p class="image-content">Want to explore this project more?
          <span style="font-size:15px;margin-top:10px;display:block;">Head over to the
            <a href="https://github.com/IBM/Developer-Playground/tree/pardata">Github Repository</a>
          </span>
        </p>
        <a class="image-link" href="https://github.com/IBM/Developer-Playground/tree/pardata" target="_blank">
          <div class="image-btn">
            <p class="image-link">View Product Details</p>
            <p class="image-link"></p>
            <p class="image-link">
              <span>
                <svg style="position: absolute; right: 10px;" fill="#ffffff" focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/  svg" width="25" height="25" viewBox="0 0 32 32" aria-hidden="true">
                <path d="M18 6L16.6 7.4 24.1 15 3 15 3 17 24.1 17 16.6 24.6 18 26 28 16z"></path>
                <title>Arrow right</title>
              </svg>
              </span>
            </p>
          </div>
        </a>
      </div>
    </div>
</body>
</html>
