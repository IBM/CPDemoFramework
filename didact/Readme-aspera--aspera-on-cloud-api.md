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
    margin: 1350px 0px 0px 20px;
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
    background-image: linear-gradient(rgba(255,255,255,0.9), rgba(255,255,255,0.9)), url("https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/github.svg");
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
    width: 300px;
    padding: 0px;
    padding-bottom: 20px;
  }
  .image-link span 
  {
    float: right;
    font-size: 32px;
    padding-right: 20px;
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
    margin-left: 20px;
    margin-top: 20px;
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
  .headercontent
  {
    margin-bottom: 25px;
  }
  @media only screen and (max-width: 1200px) {
    .footer {
      margin: 1500px 0px 0px 20px;
    }
  }
  @media only screen and (max-width: 900px) {
    .footer {
      margin: 1650px 0px 0px 20px;
    }
  }
  @media only screen and (max-width: 700px) {
    .footer {
      margin: 1800px 0px 0px 20px;
      height: 650px;
    }
  }
  @media only screen and (max-width: 600px) {
    .footer {
      margin: 1950px 0px 0px 20px;
      height: 650px;
    }
  }
  @media only screen and (max-width: 500px) {
    .footer {
      margin: 2250px 0px 0px 20px;
      height: 650px;
    }
  }
  @media only screen and (max-width: 400px) {
    .footer {
      margin: 2500px 0px 0px 20px;
      height: 750px;
    }
  }
}
</style>
</head>
<body>
   <div class="header">
      <h4 class="title is-3 ">Aspera on Cloud API  Sample Application</h4>
      <div class="headercontent">Aspera on Cloud or (AoC) is Aspera’s on-demand SaaS offering for global content sharing. AoC enables fast, easy, and secure exchange of files and folders of any size between end users, even across separate organizations, in both local and remote locations. Using AoC, organizations can store and readily access files and folders in multiple cloud-based and on-premises storage systems.</div>
   </div>
   <div class="timeline">
      <div class="container right" style="margin-top:0px;padding-top:0px;">
         <div class="content">
            <p>To begin, you will need the application's source code. Click `Get the code` to clone the code to your playground session.</p>
            <a class="button is-dark is-medium" title="Get the Code" href="didact://?commandId=extension.sendToTerminal&text=AsperaonCloud%7Cget-code%7CAsperaonCloud|git%20clone%20-b%20aspera%20https://github.com/IBM/Developer-Playground.git%20${CHE_PROJECTS_ROOT}/aspera-on-cloud/">Get the Code</a> 
         </div>
      </div>
      <div class="container right">
         <div class="content">
            <p>You've successfully cloned the code, so click `Build the application` to start the build process.</p>
            <a class="button is-dark is-medium" title="Build the Application" href="didact://?commandId=extension.sendToTerminal&text=AsperaonCloud%7Cbuild-application%7CAsperaonCloud|cd%20${CHE_PROJECTS_ROOT}/aspera-on-cloud/AoCSampleApp%20%26%26%20npm%20install%20--production">Build the Application</a>
            <p class="afterbutton"> To obtain credentials and configure the application, complete the following steps</p>
         </div>
      </div>
      <div class="container right">
         <div class="content">
            <p>Subscribe to the <a title="AoC Subscribe" href="https://developer.ibm.com/apis/catalog/aspera--aspera-on-cloud-api/Introduction">Aspera on Cloud API</a> </p>
         </div>
      </div>
      <div class="container right">
         <div class="content">
            <p>In a few mins, you should be able to "Launch" the IBM Aspera on Cloud Platform, and login with your IBM ID </p>
         </div>
      </div>
      <div class="container right">
         <div class="content">
            <p>Once you're in, Click the "Admin" App </p>
         </div>
      </div>
      <div class="container right">
         <div class="content">
            <p>Great! Let's get the credentials. To do that, Go to "Integrations" and then to "API clients" </p>
         </div>
      </div>
      <div class="container right">
         <div class="content">
            <p>Click "Create new" and type in "my-custom-integration", and check the box right below it </p>
         </div>
      </div>
      <div class="container right">
         <div class="content">
            <p>Under "Redirect URIs" give a name and select it. Click "Save". Voila! Your Client ID and Client Secret's here! </p>
         </div>
      </div>
      <div class="container right">
         <div class="content">
            <p>We're almost done! Within the same tab, next to 'Profile', go to 'JSON Web Token Auth'. Beside 'Settings', check both the boxes </p>
         </div>
      </div>
      <div class="container right">
         <div class="content">
            <p>Next to 'Keys', under "Allowed keys", choose "User-specific keys and global key", and paste the "Public Key (PEM Format)". Click to copy this from <a href="didact://?commandId=vscode.didact.copyToClipboardCommand&text=-----BEGIN%20PUBLIC%20KEY-----%0AMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAyklcsZFn99KW77qMIs8K%0AX5EmATzIsLfwbpOG5B%2BlUMQGsp1kFwqMzSZaf0b4fuyKKBqSCpj8bqhUmUxFkjPM%0AvpIz0zduqLyBDt%2BJMZbD4E6Rxg797WnCHuVVgOK74dYf4KdfiJ0OUua6frqavFL%2B%0AmhvNp6uTCfmLBfWVqnCKjht80zib7n%2BM00Y7zht6ZDTrxcGMH2qtqoYSI77YZGxg%0Andw7SLcehicHVzST7KzepkQvAYMexM%2FeiLeaDj6ymfwflvJHH8J3i9LfBJZ0%2FmUa%0AXbgOSn7VCv5rZB6gpihsic4Gs2nn9I7cxOQS%2FXLmaVfgsGiIpUfNA7cby%2FQ7bf%2Fw%0AuBy6beoI0a5nxr4z8MdrK2e1HXhOnG8TXSFQAulGMOPP6exZaeiWk%2B%2F3xTRFjrsP%0AB8%2FA5iDtvF0BvL6OY868HwnT%2Bvitvtq4JdH1gAY8An0Unh%2BvnZqPhl9jWOjycXQJ%0AHWo8g3P1uqgJL0dkHfBDHObfYTZuiEFjbJgAO3MLesbX7mTSkva5ZA7%2Fo5awKbY7%0AVEgA0p1sSgFxEdYlZKAyra3bAL4iQ9j8B%2F3kPyQDMfYB4lZwV7Qdp%2BiAho7UjYaB%0AbQds3PxeeEmDyI0a2qa6wrxfJllDDGW9b2eGnlZvXZunt57JLHLcJ32YAEYjEm7W%0AowXAMbm9fMi6X5aEyVbqI4cCAwEAAQ%3D%3D%0A-----END%20PUBLIC%20KEY-----%0A">here</a> </p>
         </div>
      </div>
      <div class="container right">
         <div class="content">
            <p>Click "Save". We've now completed the Authentication setup! </p>
         </div>
      </div>
      <div class="container right">
         <div class="content">
            <p>Let's get the credentials by configuring the application</p>
            </p> <a class="button is-dark is-medium" title="Configure the Application" href="didact://?commandId=extension.openFile&text=AsperaonCloud%7Cconfigure-application%7C${CHE_PROJECTS_ROOT}/aspera-on-cloud/AoCSampleApp/.env">Configure the Application</a> 
         </div>
      </div>
      <div class="container right">
         <div class="content">
            <p>You're all set to get started! </p>
            <a class="button is-dark is-medium" title="Launch the Application" href="didact://?commandId=extension.sendToTerminal&text=AsperaonCloud%7Claunch-application%7CAsperaonCloud|cd%20${CHE_PROJECTS_ROOT}/aspera-on-cloud/AoCSampleApp%20%26%26%20node%20token.js%20%26%26%20node%20server.js">Launch the Application</a> 
         </div>
      </div>
   </div>
   <div class="footer">
      <div class="content" style="padding:30px;padding-left:60px;padding-bottom: 0px;">
         <p>If you'd like to make changes and explore the application, make sure to stop it first!</p>
         <a class="button is-dark is-medium" title="Stop Application" href="didact://?commandId=vscode.didact.sendNamedTerminalCtrlC&text=AsperaonCloud">Stop Application</a>
         <p class="afterbutton">The stage is yours!</p>
         <a class="button is-dark is-medium" title="Explore the Code" href="didact://?commandId=extension.openFile&text=AsperaonCloud%7Cexplore-code%7C${CHE_PROJECTS_ROOT}/aspera-on-cloud/AoCSampleApp/src/App.js">Explore the Code</a>
         <p class="afterbutton ">To view the changes you've made, re-launch the application</p>
         <a class="button is-dark is-medium" title="Re-Launch the Application" href="didact://?commandId=extension.sendToTerminal&text=AsperaonCloud%7Crelaunch-application%7CAsperaonCloud|cd%20${CHE_PROJECTS_ROOT}/aspera-on-cloud/AoCSampleApp%20%26%26%20npm%20install%20--only=dev%20%26%26%20export%20REACT_APP_mode=dev%20%26%26%20npm%20start">Re-Launch the Application</a> 
      </div>
      <div class="image-div">
         <p class="image-content">Want to explore this project more? <span style="font-size:15px;margin-top:0px;display:block;">Head over to the <a href="https://github.com/IBM/Developer-Playground/tree/aspera">Github Repository</a></span> </p>
         <div class="image-btn">
            <a class="image-link" href="didact://?commandId=extension.openURL&text=AsperaonCloud%7Cview-product-details%7Chttps://www.ibm.com/cloud/aspera" target="_blank">
               View Product Details 
               <span>
                  <svg style="position: absolute; right: 10px;" fill="#ffffff" focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/  svg" width="25" height="25" viewBox="0 0 32 32" aria-hidden="true">
                     <path d="M18 6L16.6 7.4 24.1 15 3 15 3 17 24.1 17 16.6 24.6 18 26 28 16z"></path>
                     <title>Arrow right</title>
                  </svg>
               </span>
            </a>
            <a class="image-link" href="didact://?commandId=extension.openURL&text=AsperaonCloud%7Cbuy-this-product%7Chttps://www.ibm.com/cloud/aspera/pricing" target="_blank">
               Buy this API 
               <span>
                  <svg style="position: absolute; right: 10px;" fill="#ffffff" focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/  svg" width="25" height="25" viewBox="0 0 32 32" aria-hidden="true">
                     <path d="M18 6L16.6 7.4 24.1 15 3 15 3 17 24.1 17 16.6 24.6 18 26 28 16z"></path>
                     <title>Arrow right</title>
                  </svg>
               </span>
            </a>
            <a class="image-link" href="didact://?commandId=extension.openURL&text=AsperaonCloud%7Cget-trial-subscription%7Chttps://www.ibm.com/account/reg/us-en/signup?formid=urx-30538" target="_blank">
               Get Trial Subcription 
               <span>
                  <svg style="position: absolute; right: 10px;" fill="#ffffff" focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/  svg" width="25" height="25" viewBox="0 0 32 32" aria-hidden="true">
                     <path d="M18 6L16.6 7.4 24.1 15 3 15 3 17 24.1 17 16.6 24.6 18 26 28 16z"></path>
                     <title>Arrow right</title>
                  </svg>
               </span>
            </a>
         </div>
      </div>
   </div>
   <br>
   <br> 
</body>
</html>
