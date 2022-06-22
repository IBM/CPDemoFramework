<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="style.css">
  <style>
    .header {
      background-image: url('https://github.com/IBM/Developer-Playground/blob/master/didact/images/banner-image.jpg?raw=true');
    }
  </style>
</head>
<body>
  <div style="margin-top:2rem"></div>
  <div class="hidden-state">$workspace_id</div>
  <div class="header">
    <div class="left-content">
      <div class="apptitle">
        Geocoding and Search
      </div>
      <div class="subheading">
        Create location-based applications with the HERE Geocoding and Search API.
      </div>
    </div>
  </div>
  <div class="section" style="font-size:16px; margin-top:-1.25rem">
    <p>
      Geocoding is the process of transforming addresses (like "Taj Mahal in Agra, Uttar Pradesh, India") into
      geographic spatial coordinates (like latitude 27.1751° N and longitude 78.0421° E), which you can use to explore
      and position the map. Reverse geocoding is the process of converting geographic coordinates into a human-readable
      postal address. </p>
    <p>
      This application allows you to experiment with the HERE Geocoding and Search API to:
    </p>
    <ul>
      <li>Search for points of interest with 400+ categories and address objects at different levels (street, city,
        state, ...)</li>
      <li>Forward and reverse geocode address and geo-positions</li>
    </ul>
  </div>
  <div class="section">
    <p style="font-size: 24px;">Included APIs</p>
    <div>
      <p><a href="https://developer.ibm.com/apis/catalog/heremaps--geocoding-and-search-api-v7/Introduction">HERE
          Geocoding and Search API</a></p>
    </div>
  </div>
  <div class="section">
    <p style="font-size: 24px;">Pre-requisites</p>
    <div>
      <p><a href="https://developer.here.com/sign-up?create=Freemium-Basic&keepState=true&step=account">Subscribe </a>
        to
        the HERE Geocoding and Search API:</p>
      <ol>
        <li>Sign up for 'HERE Developer'.</li>
        <li>Login to your HERE account, navigate to Projects > REST.</li>
        <li>Go to OAuth2.0 > Generate App and click 'Create credentials'.</li>
        <li>'Access Key ID' and 'Access Key Secret' is your Client ID and Secret.</li>
        <li>Proceed to the 'API Keys' section and create your API Key.</li>
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
        href="didact://?commandId=extension.sendToTerminal&text=HEREGeocodingandSearch%7Cget-code%7CHEREGeocodingandSearch|git%20clone%20-b%20HERE%20--sparse%20https://github.com/IBM/Developer-Playground.git%20${CHE_PROJECTS_ROOT}/here-geocoding/%20%26%26%20cd%20${CHE_PROJECTS_ROOT}/here-geocoding/%20%26%26%20git%20sparse-checkout%20init%20--cone%20%26%26%20git%20sparse-checkout%20add%20HEREGeocodingandSearch">Get
        Code</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step install-dependencies">
      <div class="content">
        <p>Install required dependencies for executing application.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Build the Application"
        href="didact://?commandId=extension.sendToTerminal&text=HEREGeocodingandSearch%7CBUILD-APPLICATION%7CHEREGeocodingandSearch|cd%20${CHE_PROJECTS_ROOT}/here-geocoding/HEREGeocodingandSearch%20%26%26%20npm%20install%20--production">Install
        Dependencies</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step configure-application">
      <div class="content">
        <p>Configure the application. See pre-requisites.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Open the File"
        href="didact://?commandId=extension.openFile&text=HEREGeocodingandSearch%7Cconfigure-application%7C${CHE_PROJECTS_ROOT}/here-geocoding/HEREGeocodingandSearch/.env">Configure
        Application</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step launch-application">
      <div class="content">
        <p>Launch the application in the preview window.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Launch the Application"
        href="didact://?commandId=extension.sendToTerminal&text=HEREGeocodingandSearch%7Claunch-application%7CHEREGeocodingandSearch|cd%20${CHE_PROJECTS_ROOT}/here-geocoding/HEREGeocodingandSearch%20%26%26%20node%20token.js%20%26%26%20node%20server.js">Launch
        Application</a>
      <span class="dot"></span>
    </div>
  </div>
  <div class="footer">
    <div class="footer-cta">
      <div class="footer-step stop-application" style="background:transparent">
        <p>To edit or explore the application, make sure to stop it first.</p>
        <a class="button is-dark is-medium" title="Stop Application"
          href="didact://?commandId=vscode.didact.sendNamedTerminalCtrlC&text=HEREGeocodingandSearch">Stop
          Application</a>
      </div>
      <div class="footer-step explore-application" style="background:transparent">
        <p>Explore and update the code as per your requirement.</p>
        <a class="button is-dark is-medium" title="Explore the Code"
          href="didact://?commandId=extension.openFile&text=HEREGeocodingandSearch%7Cexplore-code%7C${CHE_PROJECTS_ROOT}/here-geocoding/HEREGeocodingandSearch/src/App.js">Explore
          Code</a>
      </div>
      <div class="footer-step re-launch-application" style="background:transparent">
        <p>Re-launch the application to view the changes made.</p>
        <a class="button is-dark is-medium" title="Re-Launch the Application"
          href="didact://?commandId=extension.sendToTerminal&text=HEREGeocodingandSearch%7Crelaunch-application%7CHEREGeocodingandSearch|cd%20${CHE_PROJECTS_ROOT}/here-geocoding/HEREGeocodingandSearch%20%26%26%20npm%20install%20%26%26%20export%20REACT_APP_mode=dev%20%26%26%20npm%20start">Re-Launch
          Application</a>
      </div>
      <div class="footer-step git-push" style="background:transparent">
        <p style="margin-top:0.625rem;">Click to push code to your own Github repository. You will need a personal
          access
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
            href="https://github.com/IBM/Developer-Playground/tree/HERE/HEREGeocodingandSearch" target="_blank">Github
            Repository</a></span>
        <span style="font-size:15px;margin-top:0px;display:block;">For further assistance reach out to <a
            href="https://github.com/IBM/Technology-Sandbox-Support/issues/new/choose" target="_blank"> Help &
            Support</a></span>
        <span style="font-size:15px;margin-top:0px;display:block;">Check out our <a
            href="https://ibm.github.io/Technology-Sandbox-Support/" target="_blank"> FAQs</a></span>
      </p>
      <div class="image-btn">
        <a class="image-link"
          href="didact://?commandId=extension.openURL&text=HEREGeocodingandSearch%7Cview-product-details%7Chttps://developer.here.com/documentation/geocoding-search-api/dev_guide/index.html"
          target="_blank">
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
          href="didact://?commandId=extension.openURL&text=HEREGeocodingandSearch%7Cbuy-this-product%7Chttps://developer.here.com/pricing"
          target="_blank">
          Buy this API
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
          href="didact://?commandId=extension.openURL&text=HEREGeocodingandSearch%7Cget-trial-subscription%7Chttps://developer.here.com/sign-up?create=Freemium-Basic&keepState=true&step=account"
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