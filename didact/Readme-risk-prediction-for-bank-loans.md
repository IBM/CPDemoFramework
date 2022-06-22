<html>

<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="style.css">
  <style>
    .header {
      background-image: url('https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/bank-loan-header.jpg');
    }
  </style>
</head>

<body>
  <div style="margin-top:2rem"></div>
  <div class="hidden-state">$workspace_id</div>
  <div class="header">
    <div class="left-content">
      <div class="apptitle">
        Risk Prediction for Bank Loans Application
      </div>
      <div class="subheading">
        Use machine learning to predict risks involved when approving a loan application.
      </div>
    </div>
  </div>
  <div class="section" style="font-size:16px; margin-top:-1.25rem">
    In a typical bank loan department, the loan agent receives an application from a customer. The agent then considers
    several factors to decide whether the loan should be approved or rejected. Loan agents can use machine learning to
    improve the decision-making process. This bank loan application uses a machine learning model deployed on Cloud Pak
    for Data to predict the risk of a loan application.
  </div>
  <div class="section">
    <p style="font-size:24px">Execution Flow </p>
    <div>
      <ol>
        <li>Create a deployment space using Watson Machine Learning in IBM Cloud Pak for Data platform and deploy a
          pre-trained machine learning model.</li>
        <li>Prompt the user for application details.</li>
        <li>Make a Watson Machine Learning REST API call to invoke the machine learning model with the specified input.
        </li>
        <li>Return the risk associated with the loan application.</li>
      </ol>
    </div>
  </div>
  <div class="section">
    <p style="font-size:24px">Learning Resources</p>
    <div>
      <a href="https://developer.ibm.com/articles/modernizing-your-bank-loan-department/">Modernizing a loan bank
        department</a></br>
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
      <p><a href="https://cloud.ibm.com/catalog/services/watson-studio">Watson Studio</a>: Develop sophisticated machine
        learning models using Notebooks and code-free tools to infuse AI throughout your business.</p>
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
        href="didact://?commandId=terminal-for-sandbox-container:new">Open Terminal</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step git-clone">
      <div class="content">
        <p>Clone the GitHub repository.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Clone the Repo"
        href="didact://?commandId=extension.sendToTerminal&text=BankLoanApp%7Cget-code%7Csandbox%20terminal|git%20clone%20-b%20bank-loan%20https://github.com/IBM/Developer-Playground.git ${CHE_PROJECTS_ROOT}/bank-loan/ && cd ${CHE_PROJECTS_ROOT}/bank-loan/bankloan">Get
        Code</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step install-dependencies">
      <div class="content">
        <p>Install required dependencies for executing python scripts.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Install Dependencies"
        href="didact://?commandId=extension.sendToTerminal&text=BankLoanApp%7Cinstall-dependencies%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/bank-loan/bankloan;pip3.8%20install%20-r%20requirements.txt">Install
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
        href="didact://?commandId=extension.sendToTerminal&text=BankLoanApp%7Cibm-login%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/bank-loan/bankloan/script%20%26%26%20chmod%20%2Bx%20.%2Flogin.sh%20%26%26%20.%2Flogin.sh">Login
        to IBM Cloud</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step create-services-ibmcloud">
      <div class="content">
        <p>Create services on IBM Cloud.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Create Services"
        href="didact://?commandId=extension.sendToTerminal&text=BankLoanApp%7Ccreate-ibm-services%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/bank-loan/bankloan/script%20%26%26%20chmod%20%2Bx%20.%2Fcreate-ibm-cloud-services.sh%20%26%26%20.%2Fcreate-ibm-cloud-services.sh">Create
        Services</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step generate-apikey">
      <div class="content">
        <p>Generate an API Key in the IBM account. This is required to access the model.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Generate API key"
        href="didact://?commandId=extension.sendToTerminal&text=BankLoanApp%7Cgenerate-api-token%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/bank-loan/bankloan;ibmcloud%20iam%20api-key-create%20ApiKey-bankLoan%20-d%20'this is API key for bankLoan'%20--file%20${CHE_PROJECTS_ROOT}/bank-loan/bankloan/key_file">Generate
        API key</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step create-deployment-space">
      <div class="content">
        <p>Create a new deployment space with the pre-loaded model. Make sure your <a
            href="https://dataplatform.cloud.ibm.com?cm_sp=ibmdev--developer-sandbox--cloudreg">IBM Cloud Pak for
            Data</a> account is active.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium"
        href="didact://?commandId=extension.sendToTerminal&text=BankLoanApp%7Ccreate-deployment-space%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/bank-loan/bankloan/deployment-files%20%26%26%20python3.8%20create_space.py">Create
        Deployment Space</a>
      <span class="dot"></span>
    </div>
    <div class="timeline dropdown-ctas error-ctas step">
      <div class="content">
        <details>
          <summary>Incase Importing the Model Fails, do the following steps<span class="arrow"></span></summary></br></br>
          <div class="timeline step" style="opacity:1">
            <div class="content">
              <p>Step 1 : Download the project zip file.</p>
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium"
              href="https://github.com/IBM/Developer-Playground/raw/bank-loan/bankloan/data/bankLoan.zip">Download</a>
            <span class="dot"></span>
          </div>
          <div class="timeline step">
            <div class="content">
              <p>Step 2 : Login to your <a
                  href="https://dataplatform.cloud.ibm.com?cm_sp=ibmdev--developer-sandbox--cloudreg">IBM CloudPak for
                  Data</a> account with the <b>Region</b> given in your sandbox terminal. Click on <b>Create a
                  Project</b>.</p>
              <img
                src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/bank-loan-didact1.png"
                width="750" height="750">
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium">Mark as Complete</a>
            <span class="dot"></span>
          </div>
          <div class="timeline step">
            <div class="content">
              <p>Step 3 : Click on <b>Create a project from sample or file.</b></p>
              <img
                src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/bank-loan-didact2.png"
                width="750" height="750">
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium">Mark as Complete</a>
            <span class="dot"></span>
          </div>
          <div class="timeline step">
            <div class="content">
              <p>Step 4: Upload the zip file that was just downloaded in Step 1 > Enter a project <b>Name</b> > click
                <b>Create</b>.
              </p>
              <img
                src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/bank-loan-didact3.png"
                width="750" height="750">
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium">Mark as Complete</a>
            <span class="dot"></span>
          </div>
          <div class="timeline step">
            <div class="content">
              <p>Step 5 : After the project is created, click on <b>View new project</b>.</p>
              <img
                src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/bank-loan-didact4.png"
                width="750" height="750">
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium">Mark as Complete</a>
            <span class="dot"></span>
          </div>
          <div class="timeline step">
            <div class="content">
              <p>Step 6 : Click on the <b>Assets</b> tab.</p>
              <img
                src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/bank-loan-didact5.png"
                width="750" height="750">
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium">Mark as Complete</a>
            <span class="dot"></span>
          </div>
          <div class="timeline step">
            <div class="content">
              <p>Step 7 : Click on the <b>(⋮)</b> icon right hand side of the <b>Model</b> and Click on <b>Promote</b>.
              </p>
              <img
                src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/bank-loan-didact6.png"
                width="750" height="750">
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium">Mark as Complete</a>
            <span class="dot"></span>
          </div>
          <div class="timeline step">
            <div class="content">
              <p>Step 8 : On the <b>Target Space</b> drop-down menu, select the deployment space you created (To get the
                deployment space name check your sandbox terminal), Once done click <b>Promote</b>.</p>
              <img
                src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/bank-loan-didact7.png"
                width="750" height="750">
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium">Mark as Complete</a>
            <span class="dot"></span>
          </div>
        </details>
      </div>
      <input type="checkbox">
      <span class="dot"></span>
    </div>
    <div class="timeline step deploy-model">
      <div class="content">
        <p>Deploy the model.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Deploy Model"
        href="didact://?commandId=extension.sendToTerminal&text=BankLoanApp%7Cdeploy-model%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/bank-loan/bankloan/deployment-files%20%26%26%20python3.8%20DeploySavedModel.py">Deploy
        Model</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step launch-application">
      <div class="content">
        <p>Launch the application in the preview window.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Launch Application"
        href="didact://?commandId=extension.sendToTerminal&text=BankLoanApp%7Cstart-app%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/bank-loan/bankloan;python3.8%20app.py">Launch
        Application</a>
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
          href="didact://?commandId=extension.openFile&text=BankLoanApp%7Copen-file%7C${CHE_PROJECTS_ROOT}/bank-loan/bankloan/templates/input.html">Explore
          Code</a>
      </div>
      <div class="footer-step re-launch-application" style="background:transparent">
        <p>Re-launch the application to view the changes made.</p>
        <a class="button is-dark is-medium" title="Re-Launch Application"
          href="didact://?commandId=extension.sendToTerminal&text=BankLoanApp%7Crestart-app%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/bank-loan/bankloan/;python3.8%20app.py">Re-Launch
          Application</a>
      </div>
      <div class="footer-step clean-up-services" style="background:transparent">
        <p style="margin-top:0.625rem;">Click on Clean up to delete the IBM Cloud services that were created. Make sure to
          stop the application first!
        </p>
        <a class="button is-dark is-medium" title="Delete services from IBM Cloud"
          href="didact://?commandId=extension.sendToTerminal&text=BankLoanApp%7Cclean-up%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/bank-loan/bankloan/script;chmod%20%2Bx%20.%2Fdeleteservice.sh%20%26%26%20.%2Fdeleteservice.sh">Clean
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
          <a href="https://github.com/IBM/Developer-Playground/tree/bank-loan" target="_blank">Github Repository</a>
        </span>
        <span style="font-size:15px;margin-top:0px;display:block;">For further assistance reach out to <a
            href="https://github.com/IBM/Technology-Sandbox-Support/issues/new/choose" target="_blank"> Help &
            Support</a></span>
        <span style="font-size:15px;margin-top:0px;display:block;">Check out our <a
            href="https://ibm.github.io/Technology-Sandbox-Support/" target="_blank">FAQs</a></span>
      </p>
      <a class="image-link"
        href="https://developer.ibm.com/patterns/create-a-web-based-intelligent-bank-loan-application-for-a-loan-agent/"
        target="_blank">
        <div class="image-btn">
          <p class="image-link">View Product Details
          <p style="padding-top: 14px"></p>
          <span>
            <svg style="position: absolute; right: 10px;" fill="#ffffff" focusable="false"
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
