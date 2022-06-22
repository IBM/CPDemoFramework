<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="style.css">
  <style>
    .header {
      background-image: url('https://github.com/IBM/Developer-Playground/blob/development/didact/images/weather.png?raw=true');
    }
  </style>
</head>
<body>
  <div style="margin-top:2rem"></div>
  <div class="hidden-state">$workspace_id</div>
  <div class="header">
    <div class="left-content">
      <div class="apptitle">
        Weather Data Assistant for Travel
      </div>
      <div class="subheading">
        Explore the weather and travel logistics with The Weather Company's APIs and HERE APIs.
      </div>
    </div>
  </div>
  <div class="section" style="font-size:16px; margin-top:-1.25rem">
    <p>
      Choosing a travel destination is an exciting part of trip planning. Understanding weather trends and conditions of
      a location helps you plan the best time to visit the destination. </p>
    <p>
      This application allows you to explore The Weather Company's APIs along with the HERE APIs so you can view the
      forecast, historical weather data and travel logistics simultaneously to make the best travel arrangements.
    </p>
  </div>
  <div class="section">
    <p style="font-size: 24px;">Execution flow</p>
    <ol>
      <li>Explore The Weather Company's Forecast and Historical APIs of a specific location by providing latitude and
        longitude values.</li>
      <li>Integrate HERE APIs into the application to:</li>
      <ul>
        <li> Render an interactive map of a specific location.</li>
        <li> Interact with the map dynamically, viewing the current and weekly local weather forecast.</li>
        <li> Explore the nearest hotels, transit stations, and airports.</li>
      </ul>
    </ol>
  </div>
  <div class="section">
    <p style="font-size: 24px;">Included APIs</p>
    <div>
      <ul>
        <li><a href="https://developer.ibm.com/apis/catalog/weather--weather-forecast-apis/Introduction">Weather
            Forecast APIs</a></li>
        <li><a
            href="https://developer.ibm.com/apis/catalog/weather--environmental-intelligence-suite_historical-apis/Introduction">Historical
            APIs</a></li>
        <li><a href="https://developer.ibm.com/apis/catalog/heremaps--geocoding-and-search-api-v7/Introduction">HERE
            Geocoding and Search API</a></li>
        <li><a href="https://developer.ibm.com/apis/catalog/heremaps--here-public-transit-api/Introduction">HERE Public
            Transit API</a></li>
        <li><a href="https://developer.here.com/documentation/map-tile/dev_guide/topics/quick-start.html">HERE Maps
            API</a></li>
      </ul>
    </div>
  </div>
  <div class="section">
    <p style="font-size: 24px;">Pre-requisites</p>
    <div>
      <ul>
        <li><a
            href="https://epwt-www.mybluemix.net/software/support/trial/cst/welcomepage.wss?siteId=1525&tabId=4159&w=1&_ga=2.232934494.1143069578.1643043347-1238955782.1642421092">Sign
            up </a>for The Weather Company Data trial (It might take up to 48 hours to get an API Key provisioned).</li>
        <li><a href="https://developer.here.com/sign-up?create=Freemium-Basic&keepState=true&step=account">Subscribe
          </a>to the HERE APIs:</li>
        <ol>
          <li>Sign up for 'HERE Developer'.</li>
          <li>Login to your HERE account, navigate to Projects > REST.</li>
          <li>Go to OAuth2.0 > Generate App and click 'Create credentials'.</li>
          <li>'Access Key ID' and 'Access Key Secret' is your Client ID and Secret.</li>
          <li>Proceed to the 'API Keys' section and create your API Key.</li>
        </ol>
      </ul>
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
        href="didact://?commandId=extension.sendToTerminal&text=weather%7Cget-code%7Cweather|git%20clone%20-b%20weather%20https://github.com/IBM/Developer-Playground.git%20${CHE_PROJECTS_ROOT}/weather/">Get
        Code</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step install-dependencies">
      <div class="content">
        <p>Install required dependencies for executing application.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Build the Application"
        href="didact://?commandId=extension.sendToTerminal&text=weather%7Cbuild-application%7Cweather%7Ccd%20${CHE_PROJECTS_ROOT}/weather/WeatherDataAssistant%20%26%26%20npm%20config%20set%20@here:registry%20https://repo.platform.here.com/artifactory/api/npm/maps-api-for-javascript/%20%26%26%20npm%20install%20--production">Install
        Dependencies</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step configure-application-wca">
      <div class="content">
        <p>Configure the application with The Weather Company API key (see pre-requisites) or use the demo key.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Open the File"
        href="didact://?commandId=extension.openFile&text=weather%7Cconfigure-application%7C${CHE_PROJECTS_ROOT}/weather/WeatherDataAssistant/.env">Use
        your Key</a>
      <p style="display:inline-block; margin-top:0.688rem;"> or </p>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Use demo key"
        href="didact://?commandId=extension.sendToTerminal&text=weather%7Cconfigure-application%7Cweather|cd%20${CHE_PROJECTS_ROOT}/weather/WeatherDataAssistant%20%26%26%20node%20key.js>.env">Use
        Demo Key</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step launch-application-wca">
      <div class="content">
        <p>Launch the application in the preview window.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Launch the Application"
        href="didact://?commandId=extension.sendToTerminal&text=weather%7Claunch-application%7Cweather|cd%20${CHE_PROJECTS_ROOT}/weather/WeatherDataAssistant%20%26%26%20cd%20${CHE_PROJECTS_ROOT}/weather/WeatherDataAssistant%20%26%26%20node%20server.js">Launch
        Application</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step integrate-here">
      <div class="content">
        <p>Explore travel logistics by integrating HERE API features into the application.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Install HERE Features"
        href="didact://?commandId=extension.sendToTerminal&text=weather%7Claunch-application%7Cweather|cd%20${CHE_PROJECTS_ROOT}/weather/WeatherDataAssistant%20%26%26%20cat%20here.txt%20>>.env%20%26%26%20mv%20here-components/airport.js%20here-components/hotels.js%20here-components/transit.js%20here-components/progcomp.js%20src/components%20%26%26%20cp%20here-components/App.js%20src/App.js">Integrate
        Features</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step configure-application-here">
      <div class="content">
        <p>Configure the application with HERE credentials. See pre-requisites.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Open the File"
        href="didact://?commandId=extension.openFile&text=weather%7Cconfigure-application%7C${CHE_PROJECTS_ROOT}/weather/WeatherDataAssistant/.env">Configure
        Application</a>
      <span class="dot"></span>
    </div>
    <div class="timeline step launch-application">
      <div class="content">
        <p>Launch the updated application.</p>
      </div>
      <input type="checkbox">
      <a id="step" class="button is-dark is-medium" title="Launch"
        href="didact://?commandId=extension.sendToTerminal&text=weather%7Crelaunch-application%7Cweather|cd%20${CHE_PROJECTS_ROOT}/weather/WeatherDataAssistant%20%26%26%20node%20token.js%20%26%26%20npm%20install%20%26%26%20export%20REACT_APP_mode=dev%20%26%26%20npm%20start">Re-Launch
        Application</a>
      <span class="dot"></span>
    </div>
  </div>
  <div class="footer">
    <div class="footer-cta">
      <div class="footer-step stop-application" style="background:transparent">
        <p>To edit or explore the application, make sure to stop it first.</p>
        <a class="button is-dark is-medium afterbutton" title="Stop Application"
          href="didact://?commandId=vscode.didact.sendNamedTerminalCtrlC&text=weather">Stop Application</a>
      </div>
      <div class="footer-step explore-application" style="background:transparent">
        <p class="afterbutton">Explore and update the code as per your requirement.</p>
        <a class="button is-dark is-medium afterbutton" title="Explore the Code"
          href="didact://?commandId=extension.openFile&text=weather%7Cexplore-code%7C${CHE_PROJECTS_ROOT}/weather/WeatherDataAssistant/src/App.js">Explore
          Code</a>
      </div>
      <div class="footer-step re-launch-application" style="background:transparent">
        <p class="afterbutton ">Re-launch the application to view the changes made.</p>
        <a class="button is-dark is-medium afterbutton" title="Re-Launch the Application"
          href="didact://?commandId=extension.sendToTerminal&text=weather%7Crelaunch-application%7Cweather|cd%20${CHE_PROJECTS_ROOT}/weather/WeatherDataAssistant%20%26%26%20npm%20install%20%26%26%20export%20REACT_APP_mode=dev%20%26%26%20npm%20start">Re-Launch
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
            href="https://github.com/IBM/Developer-Playground/tree/weather" target="_blank">Github
            Repository</a></span>
        <span style="font-size:15px;margin-top:0px;display:block;">For further assistance reach out to <a
            href="https://github.com/IBM/Technology-Sandbox-Support/issues/new/choose" target="_blank"> Help &
            Support</a></span>
        <span style="font-size:15px;margin-top:0px;display:block;">Check out our <a
            href="https://ibm.github.io/Technology-Sandbox-Support/" target="_blank"> FAQs</a></span>
      </p>
      <div class="image-btn">
        <a class="image-link"
          href="didact://?commandId=extension.openURL&text=weather%7Cview-product-details%7Chttps://docs.google.com/document/d/15Ru_3wdMgpbM4aOCm-4qNAnRfjx2w-Ruw3lnr8Hnodk/edit"
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
          href="didact://?commandId=extension.openURL&text=weather%7Cget-trial-subscription%7Chttps://epwt-www.mybluemix.net/software/support/trial/cst/welcomepage.wss?siteId=1525&tabId=4159&w=1&_ga=2.232934494.1143069578.1643043347-1238955782.1642421092"
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