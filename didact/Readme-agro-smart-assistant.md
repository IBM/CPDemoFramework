<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="style.css">
  <style>
    .header {
      background-image: url('https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/agro-chatbot.jpeg');
    }
  </style>
</head>

<body>
  <div style="margin-top:2rem"></div>
  <div class="hidden-state">$workspace_id</div>
  <div class="header">
    <div class="left-content">
      <div class="apptitle">
        Agro Smart Assistant
      </div>
      <div class="subheading">
        Use machine learning in a virtual assistant to get crop recommendations.
      </div>
    </div>
  </div>
  <div class="section" style="font-size:16px; margin-top:-1.25rem">
    <p>
      Precision agriculture is a technology-enabled approach to farming management that helps farmers make well-informed
      decisions about where and when to plant crops. This practice uses research data related to soil characteristics,
      soil types, and crop-yield data to help farmers determine the right crop to plant based on the location, weather,
      and soil-specific parameters.
    </p>
    <p>
      Often, machine learning models are used to garner recommendations for what crop choice would increase
      productivity.
    </p>
    <p>
      This application uses a chatbot to gather the soil characteristics and a machine learning model to provide the
      best crop recommendation.
    </p>
  </div>
  <div class="section">
    <p style="font-size:24px">Execution Flow</p>
    <ol>
      <li>Use the IBM Cloud CLI to login to your IBM Cloud account.</li>
      <li>Create IBM Cloud services instances for Cloud Object Storage, Watson Machine
        Learning, Watson Assistant, and Watson Studio in IBM Cloud Pak for Data.</li>
      <li>Deploy our Crop Recommender model in Watson Studio.</li>
      <li>Create a Cloud Function to get output from the model using the model URL.</li>
      <li>Create a chatbot in Watson Assistant and integrate with the Cloud Function.</li>
      <li>Prompt the user for soil characteristics via the chatbot.</li>
      <li>The chatbot will use the Cloud Funtion to pass user responses to the model and return crop recommendations to
        the user.</li>
    </ol>
  </div>
  <div class="section">
    <p style="font-size:24px">Learning Resources</p>
    <div>
      <a href="https://developer.ibm.com/articles/what-is-machine-learning/">Build robust machine learning-based
        solutions</a></br>
      <a href="https://developer.ibm.com/learningpaths/get-started-watson-assistant/">Get Started with Watson
        Assistant</a></br>
    </div>
  </div>
  <div class="section">
    <p style="font-size:24px">Included Components</p>
    <div>
      <p>This application uses the following <a href="https://cloud.ibm.com">IBM Cloud services</a>:</p>
      <p><a href="https://www.ibm.com/products/cloud-pak-for-data">IBM Cloud Pak for Data</a>: An integrated platform
        for data and AI.</p>
      <p><a href="https://cloud.ibm.com/objectstorage">Cloud Object Storage</a>: IBM Cloud Object Storage is a highly
        scalable cloud storage service, designed for high durability, resiliency and security.</p>
      <p><a href="https://cloud.ibm.com/catalog/services/watson-assistant">Watson Assistant</a>: Watson Assistant lets
        you build conversational interfaces into any application, device, or channel.</p>
      <p><a href="https://cloud.ibm.com/catalog/services/watson-studio">Watson Studio</a>: Develop sophisticated machine
        learning models using Notebooks and code-free tools to infuse AI throughout your business.</p>
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
      <a id="step" class="button is-dark is-medium" title="Get the Code"
        href="didact://?commandId=extension.sendToTerminal&text=AgroSmartAssistant%7Cclone-repo%7Csandbox%20terminal|git%20clone%20-b%20agro-chatbot%20https://github.com/IBM/Developer-Playground.git%20${CHE_PROJECTS_ROOT}/cp4d-smart-virtual-assistant">Get
        Code</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step install-dependencies">
      <div class="content">
        <p>Install required dependencies for executing python scripts and the node chatbot application
        </p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Build the Application"
        href="didact://?commandId=extension.sendToTerminal&text=AgroSmartAssistant%7Cbuild%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/cp4d-smart-virtual-assistant/Agro-Smart-Assistant/chatbot%20%26%26%20npm%20install%26%26cd%20${CHE_PROJECTS_ROOT}/cp4d-smart-virtual-assistant%20%26%26%20pip3.8%20install%20-r%20requirements.txt">Install
        Dependencies</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step login-ibmcloud">
      <div class="content">
        <p>Log in to your IBM Cloud account. You will be provided a link to get your one-time passcode which you will
          need to copy
          and paste to proceed with authorization.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Login to IBM Cloud"
        href="didact://?commandId=extension.sendToTerminal&text=AgroSmartAssistant%7Cibm-login%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/cp4d-smart-virtual-assistant/Agro-Smart-Assistant/scripts%20%26%26%20chmod%20%2Bx%20.%2Flogin.sh%20%26%26%20.%2Flogin.sh">Login
        to IBM Cloud</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step create-services-ibmcloud">
      <div class="content">
        <p>Create services on IBM Cloud.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Create IBM Watson Services"
        href="didact://?commandId=extension.sendToTerminal&text=AgroSmartAssistant%7Ccreate-services%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/cp4d-smart-virtual-assistant/Agro-Smart-Assistant/scripts%20%26%26%20chmod%20%2Bx%20.%2Fcreate-ibm-services.sh%20%26%26%20.%2Fcreate-ibm-services.sh">Create
        Services</a>
      <p style="margin-top:50px">Follow the below steps to download and deploy the Watson Machine Learning model.</p>
      <span class="dot"></span>
    </div>
    <div class="timeline dropdown-ctas create-deploy-model step">
      <div class="content">
        <details>
          <summary>Create a New Deployment Space and Deploy the Model using Watson Machine
            Learning<span class="arrow"></span></summary></br></br>
          <div class="timeline step" style="opacity:1">
            <div class="content">
              <p>Step 1 : Generate an API Key in the IBM account. This is required to access the model for our Cloud
                Function.</p>
            </div><input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="Generate API key"
              href="didact://?commandId=extension.sendToTerminal&text=AgroSmartAssistant%7Cgenerate-api-token%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/cp4d-smart-virtual-assistant;ibmcloud%20iam%20api-key-create%20ApiKey-SVA%20-d%20'this is API key for Smart Virtual Assitant'%20--file%20${CHE_PROJECTS_ROOT}/cp4d-smart-virtual-assistant/key_file">Generate
              API key</a><span class="dot"></span>
          </div>
          <div class="timeline step create-deployment-space">
            <div class="content">
              <p>Step 2 : Create a new deployment space with the pre-loaded model. Make sure your <a
                  href="https://dataplatform.cloud.ibm.com?cm_sp=ibmdev--developer-sandbox--cloudreg">IBM Cloud Pak for
                  Data</a> account is active in the region given in sandbox terminal.</p>
            </div><input type="checkbox">
            <a id="step" class="button is-dark is-medium"
              href="didact://?commandId=extension.sendToTerminal&text=AgroSmartAssistant%7Ccreate-space%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/cp4d-smart-virtual-assistant/Agro-Smart-Assistant/deployment-files%20%26%26%20python3.8%20create_space.py">Create
              Deployment Space</a>
            <span class="dot"></span>
          </div>
          <div class="timeline dropdown-ctas error-ctas">
            <div class="content">
              <details>
                <summary>Incase your model import failed, do the following steps<span class="arrow"></span></summary>
                </br></br>
                <div class="timeline step" style="opacity:1">
                  <div class="content">
                    <p>Step 1 : Download the project zip file.</p>
                  </div><input type="checkbox">
                  <a id="step" class="button is-dark is-medium"
                    href="https://github.com/IBM/Developer-Playground/raw/agro-chatbot/Agro-Smart-Assistant/data/crop-recommendation.zip">Download</a>
                  <span class="dot"></span>
                </div>
                <div class="timeline step">
                  <div class="content">
                    <p>Step 2 : Login to your <a
                        href="https://dataplatform.cloud.ibm.com?cm_sp=ibmdev--developer-sandbox--cloudreg">IBM Cloud
                        Pak
                        for Data</a> account with the region given in your sandbox terminal. Click on "Create a
                      Project".
                    </p>
                    <img
                      src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/section_error_1.png"
                      width="750" height="750">
                  </div>
                  <input type="checkbox">
                  <a id="step" class="button is-dark is-medium">Mark as Complete</a>
                  <span class="dot"></span>
                </div>
                <div class="timeline step">
                  <div class="content">
                    <p>Step 3 : Click on "Create a project from sample or file".</p>
                    <img
                      src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/section_error_2.png"
                      width="750" height="750">
                  </div>
                  <input type="checkbox">
                  <a id="step" class="button is-dark is-medium">Mark as Complete</a>
                  <span class="dot"></span>
                </div>
                <div class="timeline step">
                  <div class="content">
                    <p>Step 4: Upload the zip file that was just downloaded in Step 1 > Enter a project name > click
                      "Create".</p>
                    <img
                      src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/section_error_3.png"
                      width="750" height="750">
                  </div>
                  <input type="checkbox">
                  <a id="step" class="button is-dark is-medium">Mark as Complete</a>
                  <span class="dot"></span>
                </div>
                <div class="timeline step">
                  <div class="content">
                    <p>Step 5 : After the project is created, click on "View new project".</p>
                    <img
                      src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/section_error_4.png"
                      width="750" height="750">
                  </div>
                  <input type="checkbox">
                  <a id="step" class="button is-dark is-medium">Mark as Complete</a>
                  <span class="dot"></span>
                </div>
                <div class="timeline step">
                  <div class="content">
                    <p>Step 6 : Click on the Assets tab.</p>
                    <img
                      src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/section_error_5.png"
                      width="750" height="750">
                  </div>
                  <input type="checkbox">
                  <a id="step" class="button is-dark is-medium">Mark as Complete</a>
                  <span class="dot"></span>
                </div>
                <div class="timeline step">
                  <div class="content">
                    <p>Step 7 : Click on the (⋮) on right hand side of the Model and Click on "Promote" button.</p>
                    <img
                      src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/section_error_6.png"
                      width="750" height="750">
                  </div>
                  <input type="checkbox">
                  <a id="step" class="button is-dark is-medium">Mark as Complete</a>
                  <span class="dot"></span>
                </div>
                <div class="timeline step">
                  <div class="content">
                    <p>Step 8 : On the "Target Space" drop-down menu, select the deployment space you created (To get
                      the
                      deployment space name check your sandbox terminal), Once done click "Promote".</p>
                    <img
                      src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/section_error_7.png"
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
              <p>Step 3 : Deploy the model.</p>
            </div><input type="checkbox">
            <a id="step" class="button is-dark is-medium"
              href="didact://?commandId=extension.sendToTerminal&text=AgroSmartAssistant%7Cdeploy-model%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/cp4d-smart-virtual-assistant/Agro-Smart-Assistant/deployment-files%20%26%26%20python3.8%20deploy_model.py">Deploy</a>
            <span class="dot"></span>
          </div>
          <div class="timeline step">
            <div class="content">
              <p>Step 4 : Run the script to update the code file with Model URL.</p>
            </div><input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="Update Model URL"
              href="didact://?commandId=extension.sendToTerminal&text=AgroSmartAssistant%7Cupdate-model-url%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/cp4d-smart-virtual-assistant/Agro-Smart-Assistant/scripts%20%26%26%20chmod%20%2Bx%20.%2Fadd_model_url.sh%20%26%26%20.%2Fadd_model_url.sh">Update
              Model URL</a><span class="dot"></span>
          </div>
        </details>
      </div>
      <input type="checkbox">
      <span class="dot"></span>
    </div>
    <div class="timeline dropdown-ctas create-cloud-function step">
      <div class="content">
        <details>
          <summary>Configure Cloud Functions to access the model<span class="arrow"></span></summary></br></br>
          <div class="timeline step" style="opacity:1">
            <div class="content">
              <p>Step 1 : Create an Action in cloud functions with web action enabled.</p>
            </div><input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="Create Action"
              href="didact://?commandId=extension.sendToTerminal&text=AgroSmartAssistant%7Ccreate-action%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/cp4d-smart-virtual-assistant/Agro-Smart-Assistant/scripts%20%26%26%20python3.8%20create_action.py">Create
              Action</a><span class="dot"></span>
          </div>
          <div class="timeline step">
            <div class="content">
              <p>Step 2 : Run the script to add API Key parameter to the Action.</p>
            </div><input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="Create Parameter"
              href="didact://?commandId=extension.sendToTerminal&text=AgroSmartAssistant%7Cadd-parameter%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/cp4d-smart-virtual-assistant/Agro-Smart-Assistant/scripts%20%26%26%20chmod%20%2Bx%20.%2Fadd_parameter.sh%20%26%26%20.%2Fadd_parameter.sh">Add
              Parameter</a><span class="dot"></span>
          </div>
          <div class="timeline step">
            <div class="content">
              <p>Step 3 : Run the script to update the Watson Assistant Dialog skill file with the webhook URL to access
                the Cloud Function.</p>
            </div><input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="Update"
              href="didact://?commandId=extension.sendToTerminal&text=AgroSmartAssistant%7Cupdate-webhook-url%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/cp4d-smart-virtual-assistant/Agro-Smart-Assistant/scripts%20%26%26%20chmod%20%2Bx%20.%2Fupdate_dialog.sh%20%26%26%20.%2Fupdate_dialog.sh">Update
              Dialog Skill</a><span class="dot"></span>
          </div>
        </details>
      </div>
      <input type="checkbox">
      <span class="dot"></span>
    </div>
    <div class="timeline dropdown-ctas create-assistant step">
      <div class="content">
        <details>
          <summary>Integrate the Machine Learning Model with Watson Assistant<span class="arrow"></span></summary>
          </br></br>
          <div class="timeline step" style="opacity:1">
            <div class="content">
              <p>Step 1 : Create the Dialog Skill.</p>
            </div><input type="checkbox">
            <a id="step" class="button is-dark is-medium"
              href="didact://?commandId=extension.sendToTerminal&text=AgroSmartAssistant%7Ccreate-skill%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/cp4d-smart-virtual-assistant/Agro-Smart-Assistant/chatbot%20%26%26%20python3.8%20watson-assistant.py">Create
              Skill</a><span class="dot"></span>
          </div>
          <div class="timeline step">
            <div class="content">
              <p>Step 2 : Open the Assistant URL given in sandbox terminal in a new tab. Avoid using the shortcut to
                open
                the URL just copy paste the URL in new tab.</p>
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium">Mark as Complete</a>
            <span class="dot"></span>
          </div>
          <div class="timeline step">
            <div class="content">
              <p>Step 3 : If the below screen is displayed, click on the profile icon and select "Switch to classic
                experience".</p>
              <img
                src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/section_4.2_assistant.png"
                width="750" height="750">
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium">Mark as Complete</a>
            <span class="dot"></span>
          </div>
          <div class="timeline step">
            <div class="content">
              <p>Step 4 : Click on "Create assistant".</p>
              <img
                src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/section_4.3_assistant.png"
                width="550" height="550">
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium">Mark as Complete</a>
            <span class="dot"></span>
          </div>
          <div class="timeline step">
            <div class="content">
              <p>Step 5 : Enter the name of the assistant and click "Create assistant".</p>
              <img
                src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/section_4.4_assistant.png"
                width="550" height="550">
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium">Mark as Complete</a>
            <span class="dot"></span>
          </div>
          <div class="timeline step">
            <div class="content">
              <p>Step 6 : Once the Assistant is created, click on "Add dialog skill".</p>
              <img
                src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/section_4.5_assistant.png"
                width="750" height="750">
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium">Mark as Complete</a>
            <span class="dot"></span>
          </div>
          <div class="timeline step">
            <div class="content">
              <p>Step 7
                : In the "Add dialog skill" window, select the "Add Existing Skill" file and click on the "Crop
                Recommender" Skill.</p>
              <img
                src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/section_4.6_assistant.png"
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
    <div class="timeline dropdown-ctas configure-application-ctas step">
      <div class="content">
        <details>
          <summary>Configure the application<span class="arrow"></span></summary></br></br>
          <div class="timeline step" style="opacity:1">
            <div class="content">
              <p>Step 1 : Once the skill is created, click on (⋮) on top right and Click on "Assitant Settings".</p>
              <img
                src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/section_5.1_chatbot.png"
                width="450" height="450">
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium">Mark as Complete</a>
            <span class="dot"></span>
          </div>
          <div class="timeline step">
            <div class="content">
              <p>Step 2 : Copy the Assistant ID and Assistant URL in .env file.</p>
              <img
                src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/section_5.2_chatbot.png"
                width="750" height="750">
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium">Mark as Complete</a>
            <span class="dot"></span>
          </div>
          <div class="timeline step">
            <div class="content">
              <p>Step 3 : Paste it in .env file.</p>
            </div><input type="checkbox">
            <a id="step" class="button is-dark is-medium"
              href="didact://?commandId=extension.openFile&text=AgroSmartAssistant%7Cload-skill%7C${CHE_PROJECTS_ROOT}/cp4d-smart-virtual-assistant/.env">Open
              file</a><span class="dot"></span>
          </div>
        </details>
      </div>
      <input type="checkbox">
      <span class="dot"></span>
    </div>
    <div class="timeline step launch-application">
      <div class="content">
        <p>Launch the application in the preview window.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Launch the Application"
        href="didact://?commandId=extension.sendToTerminal&text=AgroSmartAssistant%7Claunch%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/cp4d-smart-virtual-assistant/Agro-Smart-Assistant/chatbot%20%26%26%20npm%20start">Launch
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
        <a class="button is-dark is-medium" title="Explore the Code"
          href="didact://?commandId=extension.openFile&text=AgroSmartAssistant%7Copen-file%7C${CHE_PROJECTS_ROOT}/cp4d-smart-virtual-assistant/Agro-Smart-Assistant/chatbot/public/index.html">Explore
          Code</a></div>
        <div class="footer-step re-launch-application" style="background:transparent">
          <p>Re-launch the application to view the changes made.</p>
          <a class="button is-dark is-medium" title="Launch the Application"
            href="didact://?commandId=extension.sendToTerminal&text=AgroSmartAssistant%7Cre-launch%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/cp4d-smart-virtual-assistant/Agro-Smart-Assistant/chatbot%20%26%26%20npm%20start">Re-Launch
            Application</a>
        </div>
        <div class="footer-step clean-up-services" style="background:transparent">
          <p style="margin-top:0.625rem;">Click on
            <bold>Clean up</bold> to delete the IBM Cloud services that were created. Make sure to stop the application
            first.
          </p>
          <a class="button is-dark is-medium" title="Delete services from IBM Cloud"
            href="didact://?commandId=extension.sendToTerminal&text=AgroSmartAssistant%7Cdelete-services%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/cp4d-smart-virtual-assistant/Agro-Smart-Assistant/scripts%20%26%26%20chmod%20%2Bx%20.%2Fdelete_services.sh%20%26%26%20.%2Fdelete_services.sh">Clean
            Up</a>
            <p style="margin-top:0.625rem;">You can also manage the services in
            <a href="https://cloud.ibm.com/resources">IBM Cloud Dashboard</a>.
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
          <span style="font-size:15px;margin-top:0px;display:block;">Head over to the <a
              href="https://github.com/IBM/Developer-Playground/tree/agro-chatbot" target="_blank">Github
              Repository</a></span>
          <span style="font-size:15px;margin-top:0px;display:block;">For further assistance reach out to <a
              href="https://github.com/IBM/Technology-sandbox-Support/issues/new/choose" target="_blank"> Help &
              Support</a></span>
          <span style="font-size:15px;margin-top:0px;display:block;">Check out our <a
              href="https://ibm.github.io/Technology-Sandbox-Support/" target="_blank">FAQs</a></span>
        </p>
      </div>
    </div>
    <br><br>
</body>
<script src="progressive.js"></script>

</html>