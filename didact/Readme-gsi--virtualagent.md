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
    margin: 5500px 0px 0px 20px;
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
    background-image: url('https://www.qsstechnosoft.com/wp-content/uploads/2020/11/WHY-CHATBOTS-ARE-NECESSARY-FOR-BUSINESS-scaled.jpg');
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
      Bot app for IBM® Developer Playground
    </div>
    <div class="header">
      <div class="right-content">
        <div>
          This sample application can help you quickly getting started with IBM Watson services like Watson Assistant, Watson Discovery, Speech To Text and also CloudantDB.
        </div>
        <div>
          Front-end (Angular based), which is simply static assets.
          Other component is the nodejs (Loopback framework) based server side logic.
        </div>
        <div>
          Don't worry, you don't have to code to figure it out. It's just a few clicks away
        </div>
      </div>
    </div>
    <div class="timeline">
      <div class="container right" style="margin-top:0px;padding-top:0px;">
        <div class="content">
          <p>To begin, we'll need to clone the GitHub repository</p>
          <a class="button is-dark is-medium" title="Clone the Repo" href="didact://?commandId=extension.sendToTerminal&text=WATSONVirtualAgent%7Cget-code%7CWATSONVirtualAgent|git%20clone%20-b%20virtualagent%20--sparse%20https://github.com/IBM/Developer-Playground.git%20${CHE_PROJECTS_ROOT}/virtualagent/%20%26%26%20cd%20${CHE_PROJECTS_ROOT}/virtualagent/%20%26%26%20git%20sparse-checkout%20init%20--cone%20%26%26%20git%20sparse-checkout%20add%20app%20client%20deployments%20docs%20pics">Get Code</a>
        </div>
      </div>
      <div class="container right">
        <div class="content">
          <p>Create and Configure IBM Services</p>
          <p>You need to be logged in to your IBM Cloud account in the Developer Playground to create and configure services.</p>
          <a class="button is-dark is-medium" title="Login to IBM Cloud" href="didact://?commandId=extension.sendToTerminal&text=WATSONVirtualAgent%7Clogin-ibmcloud%7CWATSONVirtualAgent|ibmcloud%20login%20--sso%20%26%26%20ibmcloud%20target%20--cf%20%26%26%20ibmcloud%20target%20-g%20Default">Login to IBM Cloud</a>
          <p style="margin-top:10px;">Do not have an IBM Cloud Account?<a href="https://cloud.ibm.com/registration">click here</a> to create one for free.</p>
        </div>
      </div>
      <div class="container right">
        <div class="content">
          <p>This sample application uses the following IBM Services:</p>
          <p><a href="https://cloud.ibm.com/catalog/services/cloudant">Cloudant DB</a>: IBM Cloud provides you the option of creating a fully-managed Cloudant Instance on IBM Cloud.</p>
          <p><a href="https://cloud.ibm.com/catalog/services/watson-assistant">Watson Assistant</a>: Watson Assistant lets you build conversational interfaces into any application, device, or channel.</p>
        </div>
      </div>
      <div class="container right">
        <div class="content">
          <p>Create these services and configure the credentials in the code pattern with just a click of button.</p>
          <a class="button is-dark is-medium" title="Create IBM Watson Services" href="didact://?commandId=extension.sendToTerminal&text=WATSONVirtualAgent%7Ccreate-ibm-services%7CWATSONVirtualAgent|chmod%20%2Bx%20.%2Fcreate-ibm-cloud-services.sh%20%26%26%20.%2Fcreate-ibm-cloud-services.sh">Create IBM Watson Services</a>
        </div>
      </div>
      <div class="container right">
        <div class="content">
          <p>Watson Assistant: Copy the URL from the terminal to launch Watson Assistant in your Browser.</p>
          <p>Step 1 : Click <b>Create Assistant</b></p>
          <img src = "https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/VirtualAgent_1.png" width = "750" height= "750">
          <p>Step 2 : Name the assistant & click <b>Create assistant</b></p>
          <img src = "https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/VirtualAgent_2.png" width = "750" height= "750">
          <p>Step 3 : Click <b>Add an action or dialog skill</b></p>
          <img src = "https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/VirtualAgent_3.png" width = "750" height= "750">
          <p>Step 4 : Switch to <b>Use Sample Skill</b> & select a skill</p>
          <img src = "https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/VirtualAgent_4.png" width = "750" height= "750">
          <p>Step 5 : Goto <b>Assistant settings</b> to fetch assistant name and id </p>
          <img src = "https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/VirtualAgent_5.png" width = "750" height= "750">
        </div>
      </div>
      <div class="container right">
        <div class="content">
          <p>Add the Assistant ID and Name to mapping.js</p>
           <a class="button is-dark is-medium" title="Open File" href="didact://?commandId=extension.openFile&text=WATSONVirtualAgent%7Cconfigure-application%7C${CHE_PROJECTS_ROOT}/virtualagent/mapping.js">Open File</a>
        </div>
      </div>
      <div class="container right">
        <div class="content">
          <p>Start service from server side</p>
          <a class="button is-dark is-medium" title="Start Server" href="didact://?commandId=extension.sendToTerminal&text=WATSONVirtualAgent%7Cstart-server%7CWATSONVirtualAgent|cd%20app;npm%20install;npm%20start">Start Server</a>
        </div>
      </div>
      <div class="container right">
        <div class="content">
          <p>Copy the URL generated</p>
          <p>Add the URL to previewurl.json </p>
           <a class="button is-dark is-medium" title="Open File" href="didact://?commandId=extension.openFile&text=WATSONVirtualAgent%7Cconfigure-application%7C${CHE_PROJECTS_ROOT}/virtualagent/previewurl.json">Open File</a>
        </div>
      </div>
      <div class="container right">
        <div class="content">
          <p>Send the Watson service credentials to your cloudantDB</p>
          <a class="button is-dark is-medium" title="Send Mapping" href="didact://?commandId=extension.sendToTerminal&text=WATSONVirtualAgent%7Csend-mapping%7CWATSONVirtualAgent1|cd%20virtualagent;npm%20install%20axios;node%20mapping.js;cd client;alias%20ng=/projects/virtualagent/client/node_modules/@angular/cli/bin/ng;">Send Mapping</a>
        </div>
      </div>
      <div class="container right">
        <div class="content">
          <p>Build and Run the Application</p>
          <p>You can build and run the Application within the Developer Playground, click on
            <bold> Build and Run</bold> to start the application.
          </p>
          <a class="button is-dark is-medium" title="Build and Run" href="didact://?commandId=extension.sendToTerminal&text=WATSONVirtualAgent%7Cstart-app%7CWATSONVirtualAgent1|npm%20install;ng%20build%20--configuration=production;ng%20serve%20--host%200.0.0.0%20--disableHostCheck">Build and Run</a>
        </div>
      </div>
      <div class="container right">
        <div class="content">
          <p>Lastly refresh the preview window and login as one of the users given in the below file.</p>
           <a class="button is-dark is-medium" title="Open File" href="didact://?commandId=extension.openFile&text=WATSONVirtualAgent%7Cconfigure-application%7C${CHE_PROJECTS_ROOT}/virtualagent/app/server/boot/02-load-users.js">Open File</a>
        </div>
      </div>
    </div>
    <div class="footer">
      <div class="content" style="padding:30px;padding-left:60px;padding-bottom: 0px;">
        <p>If you'd like to make changes and explore the application, make sure to stop it first!</p>
        <a class="button is-dark is-medium" title="Stop Running Server" href="didact://?commandId=vscode.didact.sendNamedTerminalCtrlC&text=WATSONVirtualAgent">Stop Running Server</a>
        <a class="button is-dark is-medium" title="Stop Running Application" href="didact://?commandId=vscode.didact.sendNamedTerminalCtrlC&text=WATSONVirtualAgent1">Stop Running Application</a>
        <p style="margin-top:10px;"> Completed the code pattern? Click on
          <bold>Clean up</bold> to delete the IBM Cloud services that were created.
        </p>
        <a class="button is-dark is-medium" title="Delete services from IBM Cloud" href="didact://?commandId=extension.sendToTerminal&text=WATSONVirtualAgent%7Cget-code%7CWATSONVirtualAgent|cd%20..;chmod%20%2Bx%20.%2Fdeleteservice.sh%20%26%26%20.%2Fdeleteservice.sh">Clean up</a>
        <p style="margin-top:10px;">You can also manage the services in
          <a href="https://cloud.ibm.com/resources">IBM Cloud Dashboard</a>.
        </p>
      </div>
      <div class="image-div">
        <p class="image-content">Want to explore this project more?
          <span style="font-size:15px;margin-top:0px;display:block;">Head over to the
            <a href="https://github.com/IBM/Developer-Playground/tree/virtualagent">Github Repository</a>
          </span>
        </p>
        <a class="image-link" href="https://github.com/IBM/Developer-Playground/tree/virtualagent" target="_blank">
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
