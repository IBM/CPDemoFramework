<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="style.css">
  <style>
    .header {
      background-image: url('https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/video_insights.jpeg');
    }
  </style>
</head>
<body>
  <div style="margin-top:2rem"></div>
  <div class="hidden-state">$workspace_id</div>
  <div class="header">
    <div class="left-content">
      <div class="apptitle">
        Video Analysis Application
      </div>
      <div class="subheading">
        Extract meaningful insights from video files using Watson Speech to Text, Natural Language Processing, and Tone
        Analyzer services.
      </div>
    </div>
  </div>
  <div class="section" style="font-size:16px; margin-top:-1.25rem">
    <p>The benefit of a virtually connected world is that important meetings and classes can be recorded, giving
      attendees more opportunities to stay connected and tune into important events. But with so much content to
      process, listening or watching all of this recorded content can be time-consuming and tedious.</p>
    <p>This application uses IBM Watson Services to analyze a video recording and to generate a detailed report
      highlighting its key points.</p>
  </div>
  <div class="section">
    <p style="font-size:24px">Architecture Diagram</p>
    <img class="flow-image"
      src="https://developer.ibm.com/developer/default/patterns/extract-textual-insights-from-a-given-video/images/extract-textual-insights-from-a-given-video-flow.png">
  </div>
  <div class="section">
    <p style="font-size:24px">Execution Flow</p>
    <ol>
      <li>User uploads recorded video file of the virtual meeting or a virtual classroom in the application.</li>
      <li>FFMPG Library extracts audio from the video file.</li>
      <li>Watson Speech To Text transcribes the audio to give a diarized textual output.</li>
      <li>Watson Language Translator (Optionally) translates other languages into English transcript.</li>
      <li>Watson Tone Analyzer analyses the transcript and highlights the top positive statements from the transcript.
      </li>
      <li>Watson Natural Language Understanding reads the transcript to identify key points and record the sentiments
        and emotions.</li>
      <li>The key points and a summary of the video is then presented to the user in the application.</li>
      <li>The user can then download the textual insights.</li>
    </ol>
  </div>
  <div class="section">
    <p style="font-size:24px">Learning Resources</p>
    <div>
      <a href="https://developer.ibm.com/articles/text-mining-and-analysis-from-webex-recordings/">Understanding the
        Extract insights from videos Asset</a>
    </div>
  </div>
  <div class="section">
    <p style="font-size:24px">Included Components</p>
    <div>
      <p>This Asset uses the following IBM Watson Services:</p>
      <p><a href="https://cloud.ibm.com/catalog/services/natural-language-understanding">Watson Natural Language
          Understanding</a>: Use advanced NLP to analyze text and extract meta-data from content such as concepts,
        entities, keywords, categories, sentiment, emotion, relations, and semantic roles.</p>
      <p><a href="https://cloud.ibm.com/catalog/services/speech-to-text">Watson Speech to Text</a>: The Speech to Text
        service converts the human voice into the written word.</p>
    </div>
  </div>
  <div class="section">
    <p style="font-size:24px">Pre-requisites</p>
    <div>
      <p>IBM Cloud Account - <a
          href="https://cloud.ibm.com/registration/trial?cm_sp=ibmdev--developer-sandbox--cloudreg"> Create</a> one for
        free.</p>
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
      <input type="checkbox"><a id="step" class="button is-dark is-medium" title="Open Terminal"
        href="didact://?commandId=terminal-for-sandbox-container:new">Open Terminal</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step git-clone">
      <div class="content">
        <p>Clone the GitHub repository.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Clone the Repo"
        href="didact://?commandId=extension.sendToTerminal&text=VideoAnalysis%7Cget-code%7Csandbox%20terminal%7Cgit%20clone%20-b%20video-insights%20https%3A%2F%2Fgithub.com%2FIBM%2FDeveloper-Playground.git%20${CHE_PROJECTS_ROOT}/video-analysis">Get
        Code</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step install-dependencies">
      <div class="content">
        <p>Install required dependencies.
        </p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Build the Application"
        href="didact://?commandId=extension.sendToTerminal&text=VideoAnalysis%7Cbuild%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/video-analysis%20%26%26%20pip3.8%20install%20-r%20requirements.txt">Install
        Dependencies</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step login-ibmcloud">
      <div class="content">
        <p>Log in to your IBM Cloud account.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Login to IBM Cloud"
        href="didact://?commandId=extension.sendToTerminal&text=VideoAnalysis%7Clogin-ibm-cloud%7Csandbox%20terminal%7Ccd%20${CHE_PROJECTS_ROOT}/video-analysis/video-insights%20%26%26%20chmod%20%2Bx%20.%2Flogin.sh%20%26%26%20.%2Flogin.sh">Login
        to IBM Cloud</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step create-services-ibmcloud">
      <div class="content">
        <p>Create services on IBM Cloud.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Create IBM Watson Services"
        href="didact://?commandId=extension.sendToTerminal&text=VideoAnalysis%7Ccreate-ibm-watson-service%7Csandbox%20terminal%7Ccd%20${CHE_PROJECTS_ROOT}/video-analysis/video-insights%20%26%26%20chmod%20%2Bx%20.%2Fcreate-ibm-cloud-services.sh%20%26%26%20.%2Fcreate-ibm-cloud-services.sh">Create
        Services</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step launch-application">
      <div class="content">
        <p>Launch the application in the preview window.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Launch the Application"
        href="didact://?commandId=extension.sendToTerminal&text=VideoAnalysis%7Claunch-application%7Csandbox%20terminal%7Ccd%20${CHE_PROJECTS_ROOT}/video-analysis/video-insights%20%26%26%20python3.8%20app.py">Launch
        Application</a>
      <span class="dot"></span>
    </div>
  </div>
  <div class="footer">
    <div class="footer-cta">
      <div class="footer-step stop-application" style="background:transparent">
        <p>To edit or explore the application, make sure to stop it first.</p>
        <a class="button is-dark is-medium" title="stop application"
          href="didact://?commandId=vscode.didact.sendNamedTerminalCtrlC&text=sandbox%20terminal">Stop Application</a>
      </div>
      <div class="footer-step explore-application" style="background:transparent">
        <p>Explore and update the code as per your requirement.</p>
        <a class="button is-dark is-medium" title="Explore the Code"
          href="didact://?commandId=extension.openFile&text=VideoAnalysis%7Copen-file%7C${CHE_PROJECTS_ROOT}/video-analysis/video-insights/app.py">Explore
          Code</a>
      </div>
      <div class="footer-step re-launch-application" style="background:transparent">
        <p>Re-launch the application to view the changes made.</p>
        <a class="button is-dark is-medium" title="Launch the Application"
          href="didact://?commandId=extension.sendToTerminal&text=VideoAnalysis%7Cre-launch%7Csandbox%20terminal%7Ccd%20${CHE_PROJECTS_ROOT}/video-analysis/video-insights%20%26%26%20python3.8%20app.py">Re-Launch
          Application</a>
      </div>
      <div class="footer-step clean-up-services" style="background:transparent">
        <p style="margin-top:0.625rem;">
          Click on <bold>Clean up</bold> to delete the IBM Cloud services that were created.
        </p>
        <a class="button is-dark is-medium" title="Delete services from IBM Cloud"
          href="didact://?commandId=extension.sendToTerminal&text=VideoAnalysis%7Cdelete-services%7Csandbox%20terminal%7Ccd%20${CHE_PROJECTS_ROOT}/video-analysis/video-insights%20%26%26%20chmod%20%2Bx%20.%2Fdeleteservice.sh%20%26%26%20.%2Fdeleteservice.sh">Clean
          Up</a>
          <p style="margin-top:0.625rem;">You can also manage the services in <a href="https://cloud.ibm.com/resources">IBM
            Cloud Dashboard</a>.</p>
      </div>
      <div class="footer-step git-push" style="background:transparent">
        <p style="margin-top:0.625rem;">Click to push code to your own Github repository. You will need a personal
          access token to complete this action via the CLI. Refer to this </p><a
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
            href="https://github.com/IBM/Developer-Playground/tree/video-insights">Github Repository</a></span>
        <span style="font-size:15px;margin-top:0px;display:block;">For further assistance reach out to <a
            href="https://github.com/IBM/Technology-Sandbox-Support/issues/new/choose" target="_blank"> Help &
            Support</a></span>
        <span style="font-size:15px;margin-top:0px;display:block;">Check out our <a
            href="https://ibm.github.io/Technology-Sandbox-Support/" target="_blank">FAQs</a></span>
      </p>
      <a class="image-link" href="https://developer.ibm.com/patterns/extract-textual-insights-from-a-given-video/"
        target="_blank">
        <div class="image-btn">
          <p class="image-link">View Product Details</p>
          <p class="image-link"> </p>
          <p class="image-link">
            <span>
              <svg style="position: absolute; right: 0.625rem;" fill="#ffffff" focusable="false"
                preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/  svg" width="25" height="25"
                viewBox="0 0 32 32" aria-hidden="true">
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
<script src="progressive.js"></script>
</html>