<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="style.css">
  <style>
    .header {
      background-image: url('https://raw.githubusercontent.com/IBM/Developer-Playground/development/didact/images/churnHeader.jpeg');
    }
  </style>
</head>
<body>
  <div style="margin-top:2rem"></div>
  <div class="hidden-state">$workspace_id</div>
  <div class="header">
    <div class="left-content">
      <div class="apptitle">
        Customer Churn Prediction
      </div>
      <div class="subheading">
        Solve a business problem and predict customer churn using a Telco customer churn data set by using IBM Watson
        machine learning.
      </div>
    </div>
  </div>
  <div class="section" style="font-size:16px; margin-top:-1.25rem">
    Customer churn is a phenomenon when a customer ends their relationship or stops doing business with a company. This
    basic factor helps a business determine the revenue loss for a given period. This application uses a machine
    learning model deployed on Cloud Pak for Data to predict whether a telecommunications customer is at risk of leaving
    the business.
  </div>
  <div class="section">
    <p style="font-size:24px">Execution Flow </p>
    <ol>
      <li>Create a deployment space using Watson Machine Learning in IBM Cloud Pak for Data platform.</li>
      <li>Train and deploy a machine learning model.</li>
      <li>Prompt the user for application details.</li>
      <li>Make a Watson Machine Learning REST API call to invoke the machine learning model with the specified input.
      </li>
      <li>Return the churn prediction associated with a customer's detail.</li>
    </ol>
  </div>
  <div class="section">
    <p style="font-size:24px">Learning Resources</p>
    <div>
      <a href="https://developer.ibm.com/articles/what-is-machine-learning/">Build robust machine learning-based
        solutions</a></br>
    </div>
  </div>
  <div class="section">
    <p style="font-size:24px">Included Components</p>
    <div>
      <p>This application uses the following <a href="https://www.ibm.com/products/cloud-pak-for-data">IBM Cloud Pak for
          Data services</a>:</p>
      <p><a href="https://cloud.ibm.com/objectstorage">Cloud Object Storage</a>: IBM Cloud Object Storage is a highly
        scalable cloud storage service, designed for high durability, resiliency and security.</p>
      <p><a href="https://cloud.ibm.com/catalog/services/machine-learning">Watson Machine Learning</a>: Deploy, manage
        and integrate machine learning models into your applications and services in as little as one click.</p>
    </div>
  </div>
  <div class="section">
    <p style="font-size:24px">Pre-requisites</p>
    <div>
      <p>IBM Cloud Account - <a
          href="https://cloud.ibm.com/registration/trial?cm_sp=ibmdev--developer-sandbox--cloudreg"> Create</a> one for
        free.</p>
      <p>IBM Cloud Pak for Data Account - <a
          href="https://dataplatform.cloud.ibm.com/home2?context=cpdaas?cm_sp=ibmdev--developer-sandbox--cloudreg">Login
        </a> or<a
          href="https://dataplatform.cloud.ibm.com/registration/stepone?context=cpdaas&apps=all?cm_sp=ibmdev--developer-sandbox--cloudreg">
          Create</a> one for free.</p>
    </div>
  </div>
  <div class="section">
    <p style="font-size:24px">Instructions</p>
    <p>Please follow all the below steps in proper sequence.</p>
  </div>
  <div class="timeline-container">
    <div class="timeline step open-terminal">
      <div class="content">
        <p>Open the sandbox terminal.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Open Terminal"
        href="didact://?commandId=terminal-for-sandbox-container:new">Open Terminal</a><br>
      <span class="dot"></span>
    </div>
    <div class="timeline step git-clone">
      <div class="content">
        <p>Clone the GitHub repository.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Clone the Repo"
        href="didact://?commandId=extension.sendToTerminal&text=ChurnPrediction%7Cget-code%7Csandbox%20terminal|git%20clone%20-b%20churn-prediction%20https://github.com/IBM/Developer-Playground.git%20${CHE_PROJECTS_ROOT}/churn-prediction/%20%26%26%20cd%20${CHE_PROJECTS_ROOT}/churn-prediction/">Get
        Code</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step install-dependencies">
      <div class="content">
        <p>Install required dependencies for executing python scripts and the node customer churn prediction
          application.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Install Dependencies"
        href="didact://?commandId=extension.sendToTerminal&text=ChurnPrediction%7Cinstall-requirements%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/churn-prediction;pip3.8%20install%20-r%20requirements.txt;npm%20install;">Install
        Dependencies</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step login-ibmcloud">
      <div class="content">
        <p>Log in to your IBM Cloud account. You will be provided a link to get your one-time passcode which you will
          need to copy and paste to proceed with authorization.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Login to IBM Cloud"
        href="didact://?commandId=extension.sendToTerminal&text=ChurnPrediction%7Cibm-login%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/churn-prediction%20%26%26%20chmod%20%2Bx%20.%2Flogin.sh%20%26%26%20.%2Flogin.sh">Login
        to IBM Cloud</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step create-services-ibmcloud">
      <div class="content">
        <p>Create services on IBM Cloud.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Create Services"
        href="didact://?commandId=extension.sendToTerminal&text=ChurnPrediction%7Ccreate-ibm-services%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/churn-prediction;chmod%20%2Bx%20.%2Fcreate-ibm-cloud-services.sh%20%26%26%20.%2Fcreate-ibm-cloud-services.sh">Create
        Services</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step generate-api-key">
      <div class="content">
        <p>Generate an API Key in the IBM account. This is required to access the model.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Generate API key"
        href="didact://?commandId=extension.sendToTerminal&text=ChurnPrediction%7Cgenerate-api-token%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/churn-prediction;ibmcloud%20iam%20api-key-create%20ApiKey-churnPred%20-d%20'this is API key for churnPred'%20--file%20${CHE_PROJECTS_ROOT}/churn-prediction/key_file">Generate
        API key</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step create-deployment-space">
      <div class="content">
        <p>Create a new empty deployment space. Make sure your <a
            href="https://dataplatform.cloud.ibm.com?cm_sp=ibmdev--developer-sandbox--cloudreg">IBM Cloud Pak for
            Data</a> account is active.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Create Deployment Space"
        href="didact://?commandId=extension.sendToTerminal&text=ChurnPrediction%7Ccreate-deployment-space%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/churn-prediction;python3.8%20create_space.py">Create
        Deployment Space</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step deploy-model">
      <div class="content">
        <p>Train and deploy the model.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Deploy Model"
        href="didact://?commandId=extension.sendToTerminal&text=ChurnPrediction%7Cdeploy-model%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/churn-prediction;python3.8%20DeployModel/DeployMLModel.py">Deploy
        Model</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step launch-application">
      <div class="content">
        <p>Launch the application in the preview window.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Launch Application"
        href="didact://?commandId=extension.sendToTerminal&text=ChurnPrediction%7Cstart-app%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/churn-prediction;npm%20start">Launch
        Application</a><br>
      <span class="dot"></span>
    </div>
  </div>
  <div class="footer">
    <div class="footer-cta">
      <div class="footer-step stop-application" style="background:transparent">
        <p>To edit or explore the application, make sure to stop it first.</p>
        <a class="button is-dark is-medium" title="Stop Application"
          href="didact://?commandId=vscode.didact.sendNamedTerminalCtrlC&text=sandbox%20terminal">Stop Application</a>
      </div>
      <div class="footer-step explore-application" style="background:transparent">
        <p>Explore and update the code as per your requirement.</p>
        <a class="button is-dark is-medium" title="Explore Code"
          href="didact://?commandId=extension.openFile&text=ChurnPrediction%7Copen-file%7C${CHE_PROJECTS_ROOT}/churn-prediction/client/src/App.js">Explore
          Code</a>
      </div>
      <div class="footer-step re-launch-application" style="background:transparent">
        <p>Re-launch the application to view the changes made.</p>
        <a class="button is-dark is-medium" title="Re-Launch Application"
          href="didact://?commandId=extension.sendToTerminal&text=ChurnPrediction%7Crestart-app%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/churn-prediction;cd%20client;npm%20install;npm%20run%20build;cd%20..;npm%20start">Re-Launch
          Application</a>
      </div>
      <div class="footer-step clean-up-services" style="background:transparent">
        <p style="margin-top:0.625rem;">Click on Clean up to delete the IBM Cloud services that were created. Make sure to
          stop the application first!
        </p>
        <a class="button is-dark is-medium" title="Delete services from IBM Cloud"
          href="didact://?commandId=extension.sendToTerminal&text=ChurnPrediction%7Cclean-up%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/churn-prediction;chmod%20%2Bx%20.%2Fdeleteservice.sh%20%26%26%20.%2Fdeleteservice.sh">Clean
          Up</a>
          <p style="margin-top:0.625rem;">You can also manage the services in
            <a href="https://cloud.ibm.com/resources">IBM Cloud Dashboard</a>
          </p>
      </div>
      <div class="footer-step git-push" style="background:transparent">
        <p style="margin-top:0.625rem;">Click to push code to your own Github repository. You will need a personal access
          token to complete this action via the CLI. Refer to this <a
            href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token">guide</a>
          for generating your personal access token.</p>
        <a class="button is-dark is-medium" title="Delete services from IBM Cloud"
          href="didact://?commandId=vscode.didact.sendNamedTerminalAString&text=sandbox%20terminal$$sh%20/github.sh ">Push
          to Github</a>
      </div>
    </div>
    <div class="image-div">
      <p class="image-content">Want to explore this project more?
        <span style="font-size:15px;margin-top:0px;display:block;">Head over to the
          <a href="https://github.com/IBM/Developer-Playground/tree/churn-prediction" target="_blank">Github
            Repository</a>
        </span>
        <span style="font-size:15px;margin-top:0px;display:block;">For further assistance reach out to <a
            href="https://github.com/IBM/Technology-Sandbox-Support/issues/new/choose" target="_blank"> Help &
            Support</a></span>
        <span style="font-size:15px;margin-top:0px;display:block;">Check out our <a
            href="https://ibm.github.io/Technology-Sandbox-Support/" target="_blank"> FAQs</a></span>
      </p>
      <a class="image-link"
        href="https://developer.ibm.com/patterns/predict-customer-churn-using-watson-studio-and-jupyter-notebooks/?mhsrc=ibmsearch_a&mhq=%20churn%20prediction"
        target="_blank">
        <div class="image-btn">
          <p class="image-link">View Product Details
          <p style="padding-top: 14px"></p>
          <span>
            <svg style="position: absolute; right: 0.625rem;" fill="#ffffff" focusable="false"
              preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/  svg" width="25" height="25"
              viewBox="0 0 32 32" aria-hidden="true">
              <path d="M18 6L16.6 7.4 24.1 15 3 15 3 17 24.1 17 16.6 24.6 18 26 28 16z"></path>
              <title>Arrow right</title>
            </svg>
          </span>
      </a>
    </div>
  </div>
  </div>
</body>
<script src="progressive.js"></script>
</html>