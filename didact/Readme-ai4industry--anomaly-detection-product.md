<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="style.css">
    <style>
        .header{
            background-image: url('https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/anomaly.jpeg');
        }
    </style>
</head>
<body>
    <div style="margin-top:2rem"></div>
    <div class="hidden-state">$workspace_id</div>
    <div class="header">
        <div class="left-content">
            <div class="apptitle">
                Anomaly Detection
            </div>
            <div class="subheading">
                Perform anomaly detection on a time-series dataset.
            </div>
        </div>
    </div>
    <div class="section" style="font-size:16px; margin-top:-1.25rem">
        <p>Industrial applications need to be able to detect anomalies from unlabelled time series data which can be a
            painful process. Machine learning tools use anomaly detection to identify data points, events, and
            observations
            that deviate from a dataset’s normal behavior.</p>
        <p>This anomaly detection API service can help users detect anomalies from the entire time series or predict
            anomaly
            status of the last data input. Currently the service supports both univariate and multivariate time
            series.This
            application allows you to experiment with the Anomaly Detection API on both univariate and multivariate time
            series datasets. The Anomaly Detection API packages state-of-the-art techniques for doing anomaly detection
            for a
            time-series dataset along with a unified framework to access these techniques.</p>
    </div>
    <div class="section">
        <p style="font-size:24px">Learning Resources</p>
        <div>
            <a href="https://developer.ibm.com/learningpaths/get-started-anomaly-detection-api/">Get Started with
                Anomaly
                Detection API</a></br>
        </div>
    </div>
    <div class="section">
        <p style="font-size:24px">Included APIs</p>
        <div>
            <p><a href="https://developer.ibm.com/apis/catalog/ai4industry--anomaly-detection-product/Introduction">Anomaly
                    Detection API</a></p>
        </div>
    </div>
    <div class="section">
        <p style="font-size:24px">Pre-requisites</p>
        <div>
            <ol>
                <li>
                    <p>IBM Account - <a
                            href="https://ibm.com/registration?cm_sp=ibmdev--developer-sandbox--cloudreg">Create</a>
                        one for free.</p>
                </li>
                <li>Obtain API credentials </li>
                <ul>
                    <li><a href="https://www.ibm.com/account/reg/us-en/signup?formid=urx-51009">Subscribe</a> to the
                        Anomaly
                        Detection API.</li>
                    <li>Check your <a href="https://developer.ibm.com/profile/myapis"> API Subscriptions</a>.</li>
                    <li>Select subscription for Anomaly Detection API to proceed.</li>
                    <li>Get the Client ID/Secret, if not, Generate an API Key.</li>
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
            <input type="checkbox"><a id="step" class="button is-dark is-medium" title="Get the Code"
                href="didact://?commandId=extension.sendToTerminal&text=AnomalyDetection%7Cclone%7Canomaly|git%20clone%20-b%20anomaly%20https://github.com/IBM/Developer-Playground.git%20${CHE_PROJECTS_ROOT}/anomaly"
                target="_blank">Get Code</a>
            <span class="dot"></span>
        </div>
        <div class="timeline step install-dependencies">
            <div class="content">
                <p>Install required dependencies for executing application.</p>
            </div>
            <input type="checkbox"><a id="step" class="button is-dark is-medium" title="Build the Application"
                href="didact://?commandId=extension.sendToTerminal&text=AnomalyDetection%7Cbuild%7Canomaly|cd%20${CHE_PROJECTS_ROOT}/anomaly%20%26%26%20npm%20install%20--production"
                target="_blank">Install Dependencies</a>
            <span class="dot"></span>
        </div>
        <div class="timeline step configure-application">
            <div class="content">
                <p>Configure the application. See prerequisites.</p>
            </div>
            <input type="checkbox"><a id="step" class="button is-dark is-medium" title="Open the File"
                href="didact://?commandId=extension.openFile&text=AnomalyDetection%7Cconfigure-application%7C${CHE_PROJECTS_ROOT}/anomaly/.env"
                target="_blank">Configure Application</a>
            <span class="dot"></span>
        </div>
        <div class="timeline step launch-application">
            <div class="content">
                <p>Launch the application in the preview window.</p>
            </div>
            <input type="checkbox"><a id="step" class="button is-dark is-medium" title="Launch the Application"
                href="didact://?commandId=extension.sendToTerminal&text=AnomalyDetection%7Claunch%7Canomaly|cd%20${CHE_PROJECTS_ROOT}/anomaly/%20%26%26%20npm%20run%20server"
                target="_blank">Launch Application</a>
            <span class="dot"></span>
        </div>
    </div>
        <div class="footer">
            <div class="footer-cta">
            <div class="footer-step stop-application" style="background:transparent">
                <p>To edit or explore the application, make sure to stop it first.</p>
                <a class="button is-dark is-medium" title="Stop Application"
                    href="didact://?commandId=vscode.didact.sendNamedTerminalCtrlC&text=anomaly">Stop Application</a>
            </div>
             <div class="footer-step explore-application" style="background:transparent">
                <p>Explore and update the code as per your requirement.</p>
                <a class="button is-dark is-medium" title="Explore the Code"
                    href="didact://?commandId=extension.openFile&text=AnomalyDetection%7Cexplore-code%7C${CHE_PROJECTS_ROOT}/anomaly/src/App.js">Explore
                    Code</a>
            </div>
             <div class="footer-step re-launch-application" style="background:transparent">
                <p>Re-launch the application to view the changes made.</p>
                <a class="button is-dark is-medium" title="Re-Launch the Application"
                    href="didact://?commandId=extension.sendToTerminal&text=AnomalyDetection%7Cre-launch%7Canomaly|cd%20${CHE_PROJECTS_ROOT}/anomaly%20%26%26%20npm%20install%20--only=dev%20%26%26%20rm%20-rf%20build%20%26%26%20npm%20run%20build%20%26%26%20npm%20run%20server">Re-Launch
                    Application</a>
            </div>
            </div>
            <div class="image-div">
                <p class="image-content">Want to explore this project more?
                    <span style="font-size:15px;margin-top:0px;display:block;">Head over to the <a
                            href="https://github.com/IBM/Developer-Playground/tree/anomaly" target="_blank">Github
                            Repository</a></span>
                    <span style="font-size:15px;margin-top:0px;display:block;">For further assistance reach out to <a
                            href="https://github.com/IBM/Technology-Sandbox-Support/issues/new/choose" target="_blank">
                            Help &
                            Support</a></span>
                    <span style="font-size:15px;margin-top:0px;display:block;">Check out our <a
                            href="https://ibm.github.io/Technology-Sandbox-Support/" target="_blank">FAQs</a></span>
                </p>
                <div class="image-btn">
                    <a class="image-link"
                        href="didact://?commandId=extension.openURL&text=anomaly%7Cview-product-details%7Chttps://www.ibm.com/products"
                        target="_blank">
                        View Product Details
                        <span>
                            <svg style="position: absolute; right: 0.625rem;" fill="#ffffff" focusable="false"
                                preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/  svg" width="25"
                                height="25" viewBox="0 0 32 32" aria-hidden="true">
                                <path d="M18 6L16.6 7.4 24.1 15 3 15 3 17 24.1 17 16.6 24.6 18 26 28 16z"></path>
                                <title>Arrow right</title>
                            </svg>
                        </span>
                    </a>
                    <a class="image-link"
                        href="didact://?commandId=extension.openURL&text=anomaly%7Cget-trial-subscription%7Chttps://www.ibm.com/account/reg/us-en/signup?formid=urx-51009"
                        target="_blank">
                        Get Trial Subcription
                        <span>
                            <svg style="position: absolute; right: 0.625rem;" fill="#ffffff" focusable="false"
                                preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/  svg" width="25"
                                height="25" viewBox="0 0 32 32" aria-hidden="true">
                                <path d="M18 6L16.6 7.4 24.1 15 3 15 3 17 24.1 17 16.6 24.6 18 26 28 16z"></path>
                                <title>Arrow right</title>
                            </svg>
                        </span>
                    </a>
                    <a class="image-link no-hover"></a>
                </div>
            </div>
        </div>
</body>
<script src="progressive.js"></script>
</html>
