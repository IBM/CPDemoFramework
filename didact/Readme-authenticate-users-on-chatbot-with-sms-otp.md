<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  html,
  div,
  body {
    background-color: #1a1a1a;
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 14px;
    outline: none;
  }
  body {
    font-family: Helvetica, sans-serif;
  }
  a{
    color:#78A9FF;
  }
  a:visited{
    color: #8C43FC;
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
    top: 47px;
    bottom: 134px;
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
    margin: 1150px 0px 0px 20px;
    padding: 0px;
    max-width: 1200px;
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
    background-position: -30% 50px;
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
    margin-right:5px;
    margin-bottom:10px;
  }
  .image-btn .image-link:hover
  {   
    text-decoration: none;
    color: white;
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
    margin-bottom: 6px;
  }
  .flow{
    background-color: white;
    display: flex;
    flex-direction: column;
    max-width: 1200px;
    margin-top: 20px;
    margin-bottom: 20px;
    margin-left: 20px;
  }
  .flow .content ol{
    justify-content: space-between;
    align-items: center;
    min-width: 40%;
    margin-top:90px;
  }
  .flow .content li{ 
    background-color: white;
    flex-direction:column;
    float: left;
    color: black;
    font-size: 14px;
    margin: 10px 200px 10px 0;
  }
  .flow .content h3{
    background-color: white;
    float: left;
    color: black;
    margin: 30px 0 20px 20px;
  }
  .flow-image-div{
    background-color: white;
    display:flex;
    justify-content: center;
    align-items: center;
  }
  .flow-image{
    background-color: transparent;
    height: auto;
    width: auto;
    max-width: 900px;
    margin-top: 30px;
    margin-bottom:30px;
    margin-left: -10px;
    margin-right: -10px;
  }
  .container a
  {
    color: #0072C3;
    background-color: transparent;
    text-decoration: none;
  }
  .container a:visited
  {
    color: #8C43FC;
    background-color: transparent;
    text-decoration: none;
  }
  @media screen and (max-width: 1200px) {
    .footer {
      margin: 1150px 0px 0px 20px;
    }
    .flow{
      flex-direction:column;
    }
    .flow .content ol{
        align-items: left;
        margin-top:80px;
    }
    .flow .content li{ 
        margin-right:200px
    }
    .flow-image-div{
      overflow:auto;
    }
  }
  @media screen and (max-width: 1000px) {
    .flow{
      flex-direction:column;
    }
    .flow .content ol{
    justify-content: space-between;
    align-items: center;
    margin-top:80px;
    }
    .flow-image-div{
      overflow:auto;
    }
  }
  @media screen and (max-width: 900px) {
    .flow{
      flex-direction:column;
    }
    .flow .content ol{
    justify-content: space-between;
    align-items: center;
    min-width: 40%;
    margin-top:80px;
    }
    .flow .content li{ 
        margin-right:50px
    }
    .flow-image-div{
      overflow:auto;
    }
    .flow-image{
      margin-left:130px;
    }
  }
  @media screen and (max-width: 700px) {
    .flow{
      flex-direction:column;
    }
    .flow-image-div{
      overflow:auto;
    }
    .flow .content li{ 
        margin-right:50px
    }
    .flow-image{
      margin-left:250px;
    }
  }
  @media screen and (max-width: 650px) {
    .footer {
      margin: 1230px 0px 0px 20px;
    }
    .flow{
      flex-direction:column;
    }
    .flow-image-div{
      overflow:auto;
    }
    .flow .content li{ 
        margin-right:50px
    }
    .flow-image{
      margin-left:350px;
    }
  }
  @media screen and (max-width: 550px) {
    .footer {
      margin: 1350px 0px 0px 20px;
    }
    .flow{
        flex-direction:column;
    }
    .flow-image-div{
      overflow:auto;
    }
    .flow .content li{ 
        margin-right:50px
    }
    .flow-image{
      margin-left:450px;
    }
  }
  @media screen and (max-width: 400px) {
    .footer {
      margin: 1450px 0px 0px 20px;
    }
    .flow{
        flex-direction:column;
    }
    .flow-image-div{
      overflow:auto;
    }
    .flow .content li{ 
        margin-right:50px
    }
    .flow-image{
      margin-left:500px;
    }
  }
}
</style>
</head>
<body>
   <div style="margin-top:20px;margin-left: 40px;margin-bottom:40px;">
      <h2>Code Pattern: Authenticate users on your chatbot with SMS one time passcode</h2>
      <div style="margin-left:5px;font-size:14px;">
         <div>
            In this code pattern, learn how to authenticate users on your chatbot with an SMS one-time passcode (OTP).
         </div>
         </br>
         <div>
            After you have completed this code pattern, you understand how to:
         </div>
         <ul style="margin-left:-2px;">
            <li>Build conversational interfaces into any application, device, or channel.</li>
            <li>Run your application code without servers.</li>
            <li>Build APIs to authenticate users on your chatbot.</li>
            <li>Make external API calls through Watson Assistant.</li>
         </ul>
      </div>
   </div>
   <div class="flow">
      <div class="content">
         <h3>Flow</h3>
         <ol>
            <li> The user registers for a policy on the portal.</li>
            <li>User data is stored in the database, and policy details are sent to the user’s phone number in an SMS through the Twilio Messaging API.</li>
            <li>The user interacts with the chatbot and asks for confidential information that is related to the policy. Watson Assistant prompts the user to enter the OTP.</li>
            <li>The query is sent to Watson Assistant, which in turn invokes IBM Cloud Functions to make an API call to the user-defined, back-end API for retrieving information.</li>
            <li>The database is searched for the user’s phone number, and the OTP generated by the back-end API is sent to the user through Twilio.</li>
            <li>The user enters the OTP in the chat application to authenticate themselves.</li>
            <li>Watson Assistant validates the OTP by interacting with the back-end API.</li>
            <li>The user-requested confidential information is fetched from the database if the OTP is valid.</li>
            <li>IBM Cloud Functions returns the confidential information to Watson Assistant.</li>
            <li>Watson Assistant displays the user-requested confidential information.</li>
            <li>The user can see the confidential information in the chatbot.</li>
         </ol>
      </div>
      <div class="flow-image-div">
         <img class="flow-image" src="https://raw.githubusercontent.com/IBM/authenticate-users-on-your-chatbot-with-sms-otp/master/doc/source/images/architecture.png">
      </div>
   </div>
   <div class="timeline">
      <div class="container right">
         <div class="content">
            <p>Clone the GitHub repository</p>
            <a class="button is-dark is-medium" title="Clone the Repo" href="didact://?commandId=vscode.didact.sendNamedTerminalAString&text=nodejs%20terminal%202$$git%20clone%20https%3A%2F%2Fgithub.com%2FIBM%2Fauthenticate-users-on-your-chatbot-with-sms-otp.git%20%26%26%20cd%20authenticate-users-on-your-chatbot-with-sms-otp%2F%20%26%26%20cd%20custom-apis-for-authentication%20%26%26%20pip3%20install%20-r%20requirements.txt%20%26%26%20cd%20..%20%26%26%20cd%20node-web-application%20%20%26%26%20npm%20install%20%26%26%20cd%20..">Get Code</a>
         </div>
      </div>
      <div class="container right">
         <div class="content">
            <p>Create a <a href="https://www.twilio.com/try-twilio">Twilio service</a> account</p>
            <p>Verify caller IDs.</p>
            <p>Create the Twilio Trial Number.</p>
            <p>Copy Account SID, Auth Token and Phone Number.</p>
            <p style="margin-top:10px;">For detailed steps click?<a href="https://github.com/IBM/authenticate-users-on-your-chatbot-with-sms-otp#2-setup-twilio-messaging-service">here.</a></p>
         </div>
      </div>
      <div class="container right">
         <div class="content">
            <p>Build and Configure DB APIs</p>
            <p>
               You can build and run the Application within the Developer Playground, click on 
               <bold>Build and Run</bold>
               to start the application.
            </p>
            <a class="button is-dark is-medium" title="Build and Run" href="didact://?commandId=vscode.didact.sendNamedTerminalAString&text=nodejs%20terminal%202$$cd%20custom-apis-for-authentication%20%26%26%20python3%20app.py">Build and Run</a>
         </div>
      </div>
      <div class="container right">
         <div class="content">
            <p>Set up Cloud Functions</p>
            <p>Create a Cloud Function Action <a href="https://cloud.ibm.com/login?redirect=%2Ffunctions%2Fcreate%2Faction">here.</a></p>
            <p>Copy the code from <a href="https://github.com/IBM/authenticate-users-on-your-chatbot-with-sms-otp/blob/master/cloud-function-action/otp-auth.py">here </a>and paste as in the canvas for cloud function action.</p>
         </div>
      </div>
      <div class="container right">
         <div class="content">
            <p>Create Watson Assistant Services</p>
            <p>You need to be logged in to your IBM Cloud account in the Developer Playground to create and configure services.</p>
            <a class="button is-dark is-medium" title="Login to IBM Cloud" href="didact://?commandId=vscode.didact.sendNamedTerminalAString&text=nodejs%20terminal%203$$ibmcloud%20login%20--sso%20%26%26%20ibmcloud%20target%20--cf%20%26%26%20ibmcloud%20target%20-g%20Default">Login to IBM Cloud</a>
            <p style="margin-top:10px;">Navigate to Watson Assistant Instance from<a href="https://eu-gb.assistant.watson.cloud.ibm.com/instances"> here.</a></p>
            <p>Follow the steps <a href="https://github.com/IBM/authenticate-users-on-your-chatbot-with-sms-otp#6-import-watson-assistant-workspace">here </a>to import a Watson Assistant Skill and configure with Cloud Function URL.</p>
         </div>
      </div>
      <div class="container right">
         <div class="content">
            <p>Build and Run the Web App</p>
            <p>
               You can build and run the Application within the Developer Playground, click on 
               <bold>Build and Run</bold>
               to start the application.
            </p>
            <a class="button is-dark is-medium" title="Build and Run" href="didact://?commandId=vscode.didact.sendNamedTerminalAString&text=nodejs%20terminal%203$$cd%20authenticate-users-on-your-chatbot-with-sms-otp%2Fnode-web-application%20%26%26%20node%20server.js">Build and Run</a>
         </div>
      </div>
   </div>
   <div class="footer">
      <div class="content" style="padding:30px;padding-left:60px;padding-bottom: 0px;">
         <p>If you'd like to make changes and explore the application, make sure to stop it first!</p>
         <a class="button is-dark is-medium" href="didact://?commandId=vscode.didact.sendNamedTerminalCtrlC&text=nodejs%20terminal%202">Stop Running APIs</a>
         <a class="button is-dark is-medium" href="didact://?commandId=vscode.didact.sendNamedTerminalCtrlC&text=nodejs%20terminal%203">Stop Running Web App</a>
         <p style="margin-top:10px;">
            Completed the code pattern? Click on 
            <bold>Clean up</bold>
            to delete the IBM Cloud services that were created.
         </p>
         <a class="button is-dark is-medium" title="Delete services from IBM Cloud" href="didact://?commandId=vscode.didact.sendNamedTerminalAString&text=nodejs%20terminal%203$$servicename%3D%22cp-wa%22%20%26%26%20ibmcloud%20resource%20service-key-delete%20%22%24servicename-creds%22%20-f%20%26%26%20ibmcloud%20resource%20service-instance-delete%20%24servicename%20-f">Clean up</a>
         <p style="margin-top:10px;">Find the detailed steps <a href="https://github.com/IBM/authenticate-users-on-your-chatbot-with-sms-otp#4-create-a-cloud-function-action">here.</a></p>
         <p style="margin-top:10px;">You can also manage the services in <a href="https://cloud.ibm.com/resources">IBM Cloud Dashboard</a>.</p>
      </div>
      <div class="image-div">
         <p class="image-content">Want to explore this project more?
            <span style="font-size:15px;margin-top:0px;display:block;">Head over to the <a>Github Repository</a></span>
         </p>
         <a class="image-link" href="https://developer.ibm.com/patterns/authenticate-users-on-your-chatbot-with-sms-one-time-passcode-otp/" target="_blank">
         <div class="image-btn">
               <p class="image-link">View Product Details</p>
               <p class="image-link">   </p>
               <p class="image-link">
               <span>
                  <svg style="position: absolute; right: 1rem;" fill="#ffffff" focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/  svg" width="25" height="25" viewBox="0 0 32 32" aria-hidden="true">
                     <path d="M18 6L16.6 7.4 24.1 15 3 15 3 17 24.1 17 16.6 24.6 18 26 28 16z"></path>
                     <title>Arrow right</title>
                  </svg>
               </span>
               </p>
         </div>
         </a>
      </div>
   </div>
   <br><br>
</body>
</html>
