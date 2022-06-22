<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
html,div,body{
    background-color:#1a1a1a;
    font-family: 'IBM Plex Sans', sans-serif;
    font-size:20px;
}
.content h2,h3,h4
{
    font-family: 'IBM Plex Sans', sans-serif;
    background-color:#1a1a1a;
}
.content h2,p{
    color:#fff;
    font-family: 'IBM Plex Sans', sans-serif;
}
.content p{
  font-family: 'IBM Plex Sans', sans-serif;  
  font-size:20px;
  color: #fff;
}
pre{
    background-color:#d9dbde;
    color:#000;
    font-family: 'IBM Plex Sans', sans-serif;
    font:15px;
}
.content h4{
    font-family: 'IBM Plex Sans', sans-serif;
    background-color:#1a1a1a;
    color:#fff;
    font-size:28px;
}
.content h6{
    font-family: 'IBM Plex Sans', sans-serif;
    background-color:#1a1a1a;
    color:#fff;
}
.content h3{
    font-family: 'IBM Plex Sans', sans-serif;
    color: #fff;
    background-color:#1a1a1a;
}
ul, ol,b{ 
    font-family: 'IBM Plex Sans', sans-serif;
    color: #fff;
}
#ul1{
  font-family: 'IBM Plex Sans', sans-serif;
    color: #fff;
    font-size:20px;
}
.button.is-dark.is-medium {
  font-family: 'IBM Plex Sans', sans-serif;
  background-color: #1a1a1a;
  border-color: white;
  color: #fff;
}
.button.is-dark.is-medium:hover {
  font-family: 'IBM Plex Sans', sans-serif;
  background-color: #2a67f5;
  border-color: white;
  color: #fff;
}
.title.is-3{
  font-family: 'IBM Plex Sans', sans-serif;
  color:#fff;
}
.subtitle.is-4{
    font-family: 'IBM Plex Sans', sans-serif;
    color:#fff;
}
ol,ul,li{
  font-size:20px;
  color: #fff;
}
.tag.is-light.is-normal{
    background-color: #79a4f2;
    font-family: 'IBM Plex Mono', sans-serif;
    radius: 3px;
}
.user_exp{
  font-family: 'IBM Plex Sans', sans-serif;
  font-size:20px;
  font-weight:bold;
  color:#0f62fe;
}
</style>
</head>

<body style="font-family: 'IBM Plex Sans', sans-serif;background-color:#1a1a1a;">
<div style="font-family: 'IBM Plex Sans', sans-serif;background-color:#1a1a1a;">
<h2 class="title is-3 ">Business Cases for Partner Marketplace</h2>

<br/><br/>

<h3>Business Value </h3>

<p>The proposed solution plans to address two problems faced with partner marketplaces</p>
<ul id="ul1">
<li>Often offerings have complex configuration rules related to add-ons and a maintenance overhead for partners to code and introduce in catalog.</li>
<li>Resellers may not know the details required to provision the service and would like to delegate the customer contact. This is currently not feasible.</li>
</ul>

<p>Business value to IBM's partners<br/>
<ul>
<li>Decouple  from implementing  product configuration  rules</li>
<li>Workflow to capture product  provisioning  details,  by end  customer or reseller</li>
<li>Expedited  product  introduction  and launch</li>
</ul>
</p><br/>

<h3>IPM Marketplace Application</h3>

<p>Try out the application</p>
<ol>
<li>Before you configure and launch the application, it is necessary to retrieve the API credentials from API Hub by following the steps:<br>
<ol type='a'>
<li>Login to <a title= "IBM API Hub" href="https://developer.sl.bluecloud.ibm.com/sso/displayname?lang=en_US&d=https%3A%2F%2Fdeveloper.sl.bluecloud.ibm.com%2Fprofile%2Fmyapis%2F">IBM API Hub</a> using your IBM ID.</li><br>

<li>In  <u><i><b> API Subscriptions</b></i></u>  section, launch  <u><i><b> IBM Marketplace APIs </b></i></u>.  If you are not able to see <u><i><b> IBM Marketplace APIs </b></i></u>,<br>then click on <u><i><b> Visit IBM API Hub </b></i></u> and search for IBM Marketplace APIs and subscribe.</li><br>
<li>After launching <u><i><b> IBM Marketplace APIs </b></i></u> , you will see <u><i><b> Key management </b></i></u> section, where your existing API Keys will be listed.</li><br>

<li>If no keys listed, then click on <u><i><b> Generate API Key </b></i></u> button and create a new key.</li><br>

<li>Copy the <u><i><b> Client ID </b></i></u> and <u><i><b> Client secret </b></i></u> by expanding the key from the list.</li>
</ol><br>

<li> After obtaining API credentials, get the application code by clicking the "Clone the Repository" button. </li><br>

<a class="button is-dark is-medium" title="Clone the repository" href='didact://?commandId=extension.sendToTerminal&text=IPM-Marketplace-App%7Cclone-repo%7CIPM-Marketplace-App|git%20clone%20-b%20playground%20https%3A%2F%2Fgithub.com%2FIBM%2Fipm-marketplace-app.git%20%26%26%20cd%20${CHE_PROJECTS_ROOT}/ipm-marketplace-app%20%26%26%20touch%20.env%20%26%26%20printf%20%22%23%20IBM%20Marketplace%20API%20CLIENT_ID%5CnCLIENT_ID%3D%5Cn%5Cn%23%20IBM%20Marketplace%20CLIENT_SECRET%5CnCLIENT_SECRET%3D%22%20%3E%20.env' >Clone the Repository</a>
<br><br>

<li>Next click the "Configure Application" button in order to enter the API Credentials i.e. Client_ID and Client_Secret in the <b>.env</b> file.</li>
<br>

<a class="button is-dark is-medium" title="Configure Application" href="didact://?commandId=extension.openFile&text=IPM-Marketplace-App%7Cconfigure-app%7C/${CHE_PROJECTS_ROOT}/ipm-marketplace-app/.env">Configure Application</a>
<br><br>

<li>Now click on the "Build Application" button.</li><br/>

<a class="button is-dark is-medium" title="Build Appilication" href="didact://?commandId=extension.sendToTerminal&text=IPM-Marketplace-App%7Cbuild-application%7CIPM-Marketplace-App|cd%20${CHE_PROJECTS_ROOT}/ipm-marketplace-app%20%26%26%20touch%20.env%20%26%26%20printf%20%22%5Cn%5Cn%23%20CCP%20API%20url%5CnCCP_API%3Dhttps%3A%2F%2Fwwwstage.ibm.com%2Fmarketplace%2Fpurchase%2Fconfiguration%5Cn%5Cn%23%20Staging%20IBM%20Marketplace%20API%20url%5CnSA_URL%3Dhttps%3A%2F%2Fdev.api.ibm.com%2Fmarketplace%2Ftest%2Fv2%22%20%3E%3E%20.env%20%26%26%20npm%20install">Build Application</a><br><br>


<li>You must verify the required configurations before launching the application by clicking the "Validate all Requirements" button.</li><br><br>

| Requirement (Click to Verify)  | Status |
| :--- | :--- |
| [Check if Node exists on CLI](didact://?commandId=vscode.didact.cliCommandSuccessful&text=node-status$$npm%20--version%20%26%26%20node%20--version "Ensure that Node is available at the command line"){.didact} | *Status: unknown*{#node-status} | 
| [Check if .env exists on CLI](didact://?commandId=vscode.didact.cliCommandSuccessful&text=file-status$$%5B%20-f%20%2Fprojects%2Fipm-marketplace-app%2F.env%20%5D%20%26%26%20echo%20%24%3F "Ensure that .env file is available in the folder"){.didact}| *Status: unknown*{#file-status} |
| [Check if the credentials are valid and exists on CLI](didact://?commandId=vscode.didact.cliCommandSuccessful&text=cred-status$$grep%20-c%20%27CLIENT_ID%3D%5Ba-zA-z0-9%5D%27%20%2Fprojects%2Fipm-marketplace-app%2F.env%20%26%26%20grep%20-c%20%27CLIENT_SECRET%3D%5Ba-zA-z0-9%5D%27%20%2Fprojects%2Fipm-marketplace-app%2F.env%20%26%26%20echo%20%24%3F "Ensure that the credentials do exist."){.didact}| *Status: unknown*{#cred-status} |


<br>

<a class="button is-dark is-medium" href='didact://?commandId=vscode.didact.validateAllRequirements' title='Validate all requirements'>Validate all Requirements</a>
<br><br>

<li> Once you have configured the Application with the API credentials in the <b>.env</b> file, then launch the application by clicking the "Launch Application" button.</li><br/>
<a class="button is-dark is-medium" title="Launch Application" href="didact://?commandId=extension.sendToTerminal&text=IPM-Marketplace-App%7Claunch-application%7CIPM-Marketplace-App|cd%20${CHE_PROJECTS_ROOT}/ipm-marketplace-app%20%26%26%20npm%20run%20start">Launch Application</a><br><br>

<p>You will see a dialogue box with a message <b>"A process is now listening on port 3000. External URL is https://container-url.com"</b>. <br><br> Click the "Open Link" button. You will see your application in the Preview Tab.</p>
<br>
</ol>


<ol>
<h4>Customize Your Application</h4>

<p>You have successfully launched the application. Now, you can now customize your application by making changes in the given application code and rebuild the application. In order to view your customized application, it is required to follow the given steps below.</p>

<ol>

<li>Make the code changes in the desired file(s) of the given application code which is present in the Explorer.</li>
<br>

<li>Next stop the Application by clicking the "Stop Application" button.</li><br>
<a class="button is-dark is-medium" title="Stop Application" href="didact://?commandId=vscode.didact.sendNamedTerminalCtrlC&text=IPM-Marketplace-App$$cd%20${CHE_PROJECTS_ROOT}/ipm-marketplace-app%20%26%26%20npm%20run%20start-dev" >Stop Application</a><br>
<br>

<li>Now click the "Rebuild & Launch Application" button.</li><br>
<a class="button is-dark is-medium" title="Rebuild & Launch Application" href="didact://?commandId=extension.sendToTerminal&text=IPM-Marketplace-App%7Crelaunch-application%7CIPM-Marketplace-App|cd%20${CHE_PROJECTS_ROOT}/ipm-marketplace-app%20%26%26%20npm%20run%20build-clean%20%26%26%20npm%20run%20build-client%20%26%26%20npm%20run%20start" >Rebuild & Launch Application</a>
<br><br>

<p>You will see a dialogue box with a message <b>"A process is now listening on port 3000. External URL is https://container-url.com"</b>. <br><br> Click the "Open Link" button. This time you will need to refresh the url in the Preview tab to see your application with the code changes.</p>
<br>
</ol>
</ol>


<p>To understand more details about the interactions of APIs within the appliction, click <a class="user_exp" title="IBM Configuration for Partner Marketplace Integration" href="didact://?commandId=vscode.didact.startDidact&projectFilePath=/ipm-marketplace-app/Readme2.didact.md">IBM Configuration for Partner Marketplace Integration</a>.</p>
<br>
<br>

<p>If you have some interesting ideas and you would like to contribute, please check out the project on <a class="user_exp" href="https://github.com/IBM/ipm-marketplace-app">IPM Marketplace App Github</a>, where new ideas are welcomed and feel free to <a class="user_exp" href="https://github.com/IBM/ipm-marketplace-app/issues">submit feature requests, submit pull requests for codes, log bugs and so on</a>.</p>


<br><br>

<a class="button is-dark is-medium" title="View product details" href="didact://?commandId=extension.openURL&text=IPM-Marketplace-App%7Cview-product-details%7Chttps://www.ibm.com/products" target="_blank">View product details</a>
&nbsp;&nbsp;
<a class="button is-dark is-medium" title="Get trial subscription" href="didact://?commandId=extension.openURL&text=IPM-Marketplace-App%7Cget-trial-subscription%7Chttps://www.ibm.com/account/reg/us-en/signup?formid=urx-30474" target="_blank">Get trial subscription</a>
<br><br>
</div>
</body>
</html>


