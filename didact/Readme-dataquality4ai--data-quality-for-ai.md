<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="style.css">
  <style>
    .header {
      background-image: url('https://github.com/IBM/Developer-Playground/blob/master/didact/images/data-quality.png?raw=true');
    }
  </style>
</head>
<body>
  <div style="margin-top:2rem"></div>
  <div class="hidden-state">$workspace_id</div>
  <div class="header">
    <div class="left-content">
      <div class="apptitle">
        Data Quality for AI
      </div>
      <div class="subheading">
        Assess the quality of data sets for AI models.
      </div>
    </div>
  </div>
  <br>
  <br>
  <div class="section" style="font-size:16px; margin-top:-1.25rem">
    <p>
      Access to quality data can significantly reduce model building time, streamline data preparation efforts, and
      improve the overall reliability of the AI pipeline.</p>
    <p>
      The Data Quality for AI integrated toolkit provides various data profiling and quality estimation metrics to
      assess the quality of ingested data in a systematic and objective manner. This application allows you to
      experiment with the Data Quality for AI toolkit to assess the quality of your dataset.
    </p>
  </div>
  <div class="section">
    <p style="font-size:24px">Learning Resources</p>
    <div>
      <a href="https://developer.ibm.com/learningpaths/data-quality-ai-toolkit/">Get started with Data Quality for
        AI</a></br>
    </div>
  </div>
  <div class="section">
    <p style="font-size:24px">Included APIs</p>
    <div>
      <p><a href="https://developer.ibm.com/apis/catalog/dataquality4ai--data-quality-for-ai/Introduction">Data Quality
          for AI API</a></p>
    </div>
  </div>
  <div class="section">
    <p style="font-size:24px">Pre-requisites</p>
    <div>
      <ol>
        <li>
          <p>IBM Account - <a href="https://ibm.com/registration?cm_sp=ibmdev--developer-sandbox--cloudreg">Create</a>
            one for free.</p>
        </li>
        <li>Obtain API credentials </li>
        <ul>
          <li><a href="https://www.ibm.com/account/reg/us-en/signup?formid=urx-50307">Subscribe </a> to the Data Quality
            for AI.</li>
          <li>Check your <a href="https://developer.ibm.com/profile/myapis"> API Subscriptions</a>.</li>
          <li>Select the subscription for Data Quality for AI to proceed.</li>
          <li>You can obtain your Client ID/Secret from here. Else, you can "Generate API Key".</li>
        </ul>
      </ol>
    </div>
  </div>
  <div class="section">
    <p style="font-size:24px">Instructions</p>
    <p>Please follow all the below steps in proper sequence.</p>
  </div>
  <div class="timeline-container">
    <div class="timeline step git-clone">
      <div class="content">
        <p>Clone the GitHub repository.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Get the Code"
        href="didact://?commandId=extension.sendToTerminal&text=data-quality%7Cget-code%7Cdata-quality|git%20clone%20-b%20DART%20https://github.com/IBM/Developer-Playground.git%20${CHE_PROJECTS_ROOT}/data-quality/">Get
        Code</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step install-dependencies">
      <div class="content">
        <p>Install required dependencies for executing application.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Build the Application"
        href="didact://?commandId=extension.sendToTerminal&text=data-quality%7Cbuild-application%7Cdata-quality|cd%20${CHE_PROJECTS_ROOT}/data-quality/DataQuality%20%26%26%20npm%20install%20--production">Install
        Dependencies</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step configure-application">
      <div class="content">
        <p>Configure the application. See pre-requisites.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Open the File"
        href="didact://?commandId=extension.openFile&text=data-quality%7Cconfigure-application%7C${CHE_PROJECTS_ROOT}/data-quality/DataQuality/.env">Configure
        Application</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step launch-application">
      <div class="content">
        <p>Launch the application in the preview window.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Launch the Application"
        href="didact://?commandId=extension.sendToTerminal&text=data-quality%7Claunch-application%7Cdata-quality|cd%20${CHE_PROJECTS_ROOT}/data-quality/DataQuality%20%26%26%20node%20server.js">Launch
        Application</a>
      <span class="dot"></span>
    </div>
  </div>
  <br>
  <div class="footer">
    <div class="footer-cta">
      <div class="footer-step stop-application" style="background:transparent">
        <p>To edit or explore the application, make sure to stop it first.</p>
        <a class="button is-dark is-medium" title="Stop Application"
          href="didact://?commandId=vscode.didact.sendNamedTerminalCtrlC&text=data-quality">Stop Application</a>
      </div>
      <div class="footer-step explore-application" style="background:transparent">
        <p>Explore and update the code as per your requirement.</p>
        <a class="button is-dark is-medium" title="Explore the Code"
          href="didact://?commandId=extension.openFile&text=data-quality%7Cexplore-code%7C${CHE_PROJECTS_ROOT}/data-quality/DataQuality/src/App.js">Explore
          Code</a>
      </div>
      <div class="footer-step re-launch-application" style="background:transparent">
        <p>Re-launch the application to view the changes made.</p>
        <a class="button is-dark is-medium" title="Re-Launch the Application"
          href="didact://?commandId=extension.sendToTerminal&text=data-quality%7Crelaunch-application%7Cdata-quality|cd%20${CHE_PROJECTS_ROOT}/data-quality/DataQuality%20%26%26%20npm%20install%20--only=dev%20%26%26%20rm%20-rf%20build%20%26%26%20npm%20run%20build%20%26%26%20node%20server.js">Re-Launch
          Application</a>
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
            href="https://github.com/IBM/Developer-Playground/tree/DART" target="_blank">Github Repository</a></span>
        <span style="font-size:15px;margin-top:0px;display:block;">For further assistance reach out to <a
            href="https://github.com/IBM/Technology-Sandbox-Support/issues/new/choose" target="_blank"> Help &
            Support</a></span>
        <span style="font-size:15px;margin-top:0px;display:block;">Check out our <a
            href="https://ibm.github.io/Technology-Sandbox-Support/" target="_blank"> FAQs</a></span>
      </p>
      <div class="image-btn">
        <a class="image-link" href="didact://?commandId=extension.openURL&text=data-quality%7Cview-product-details%7Chttps://www.ibm.com/products/dqaiapi
               " target="_blank">
          View Product Details
          <span>
            <svg style="position: absolute; right: 0.625rem;" fill="#ffffff" focusable="false"
              preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/  svg" width="25" height="25"
              viewBox="0 0 32 32" aria-hidden="true">
              <path d="M18 6L16.6 7.4 24.1 15 3 15 3 17 24.1 17 16.6 24.6 18 26 28 16z"></path>
              <title>Arrow right</title>
            </svg>
          </span>
        </a>
        <a class="image-link"
          href="didact://?commandId=extension.openURL&text=data-quality%7Cget-trial-subscription%7Chttps://www.ibm.com/account/reg/us-en/signup?formid=urx-50307"
          target="_blank">
          Get Trial Subscription
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