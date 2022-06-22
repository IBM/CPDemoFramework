<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="style.css">
    <style>
        .header {
            background-image: url('https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/aws-healthcare-header.jpg');
        }
    </style>
</head>
<body>
    <div style="margin-top:2rem"></div>
    <div class="hidden-state">$workspace_id</div>
    <div class="header">
        <div class="left-content">
            <div class="apptitle">
                Proactive Healthcare Management System
            </div>
            <div class="subheading">
                Predicting cardiac events based on real-time monitoring of patients health data using IBM Cloud pak for Data technology along with AWS Cloud.
            </div>
        </div>
    </div>
    <div class="section" style="font-size:16px; margin-top:-1.25rem">
        <p>In the healthcare domain, there is a lot of real-time data that is generated. This real-time data needs to be monitored to generate predictions and alerts for healthcare professionals. A manual monitoring of such data is difficult. Hence in this code pattern we add AI based predictions and automate the monitoring of healthcare data.</p>
        <p>In this code pattern, you will learn to build a machine learning model with no code on IBM Cloud Pak for Data, create a streaming flow on AWS Cloud and invoke the model to get predictions in real-time.</p>
    </div>
    <div class="section">
        <p style="font-size:24px">Architecture Diagram</p>
        <img class="flow-image" src="https://raw.githubusercontent.com/IBM/Developer-Playground/aws-healthcare/doc/source/images/architecture-no-spss.png"/>
    </div>
    <div class="section">
        <p style="font-size:24px">Execution Flow</p>
        <ol>
            <li>Healthcare data is dumped into a S3 bucket on AWS.</li>
            <li>A producer lambda function is triggered to encrypt the data and stream it to AWS Kinesis.</li>
            <li>A pretrained machine learning model is deployed in Watson Studio Machine Learning.</li>
            <li>A consumer lambda function reads the data from kinesis streams.</li>
            <li>The consumer function invokes the model from Watson Studio Machine Learning with the data received from kinesis streams.</li>
            <li>The data streamed from the kinesis along with the predictions received from the Watson Studio Machine Learning are then visualized in AWS CloudWatch.</li>
        </ol>
    </div>
    <div class="section">
        <p style="font-size:24px">Learning Resources</p>
        <div>
            <a href="https://github.com/IBM/proactive-healthcare-management-cpd-aws.git">Proactive Healthcare Management System</a></br>
        </div>
    </div>
    <div class="section">
        <p style="font-size:24px">Included Components</p>
        <div>
            <p>This  application uses the following <a href="https://www.ibm.com/products/cloud-pak-for-data">IBM Cloud Pak for Data services</a>:</p>
            <p><a href="https://cloud.ibm.com/objectstorage">Cloud Object Storage</a>: IBM Cloud Object Storage is a highly scalable cloud storage service, designed for high durability, resiliency and security.</p>
            <p><a href="https://cloud.ibm.com/catalog/services/machine-learning">Watson Machine Learning</a>: Deploy, manage and integrate machine learning models into your applications and services in as little as one click.</p>
            <p><a href="https://cloud.ibm.com/catalog/services/watson-studio">Watson Studio</a>: Develop sophisticated machine learning models using Notebooks and code-free tools to infuse AI throughout your business.</p>
            <p>This Asset uses the following <a href="https://aws.amazon.com/products/">AWS Services</a>:</p>
            <p><a hrefy="https://aws.amazon.com/iam">IAM Roles</a>: AWS Identity and Access Management (IAM) provides fine-grained access control across all of AWS.</p>
            <p><a href="https://aws.amazon.com/kinesis">Kinesis</a>: Amazon Kinesis makes it easy to collect, process, and analyze real-time, streaming data so you can get timely insights and react quickly to new information.</p>
            <p><a href="https://aws.amazon.com/lambda">Lambda</a>: AWS Lambda is a serverless, event-driven compute service that lets you run code for virtually any type of application or backend service without provisioning or managing servers. </p>
            <p><a href="https://aws.amazon.com/cloudwatch">CloudWatch</a>: Amazon CloudWatch is a monitoring and observability service built for DevOps engineers, developers, site reliability engineers (SREs), IT managers, and product owners.</p>
            <p><a href="https://aws.amazon.com/s3">S3</a>: Amazon Simple Storage Service (Amazon S3) is an object storage service offering industry-leading scalability, data availability, security, and performance.</p>
        </div>
    </div>
    <div class="section">
        <p style="font-size:24px">Pre-requisites</p>
        <div>
            <p>AWS Account -  <a href="https://portal.aws.amazon.com/billing/signup#/start">Login</a> or <a href="https://portal.aws.amazon.com/billing/signup">Create</a> one for free</p>
            <p>IBM Cloud Pak for Data Account - <a href="https://dataplatform.cloud.ibm.com/home2?context=cpdaas?cm_sp=ibmdev--developer-sandbox--cloudreg">Login </a> or<a href="https://dataplatform.cloud.ibm.com/registration/stepone?context=cpdaas&apps=all?cm_sp=ibmdev--developer-sandbox--cloudreg"> Create</a> one for free.</p>
        </div>
    </div>
    <div class="section">
        <p style="font-size:24px">Instructions</p>
        <p>Please follow all the below steps in proper sequence.</p>
    </div>   
    <div class="timeline-container">
        <div class="timeline step git-clone">
            <div class="content">
                <p>Clone the GitHub repository and install required dependencies for executing python scripts.</p>
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="Configure Resources"
                href="didact://?commandId=extension.compositeCommand&&text=terminal-for-sandbox-container:new%7Cvscode.didact.sendNamedTerminalAString%2Csandbox%20terminal%2Cgit%20clone%20-b%20aws-healthcare%20https%3A%2F%2Fgithub.com%2FIBM%2FDeveloper-Playground%20%24%7BCHE_PROJECTS_ROOT%7D%2Faws-healthcare%2C%2Fprojects%7Cvscode.didact.sendNamedTerminalAString%2Csandbox%20terminal%2Ccd%20${CHE_PROJECTS_ROOT}/aws-healthcare/proactive-healthcare-management/;pip3.8%20install%20-r%20requirements.txt">Configure Environment</a>
            <span class="dot"></span>
        </div>
        <div class="timeline step login-ibmcloud">
            <div class="content">
                <p>Log in to your IBM Cloud account. You will be provided a link to get your one-time passcode which you will need to copy and paste to proceed with authorization.</p>
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="Login to IBM Cloud" href="didact://?commandId=extension.sendToTerminal&text=AwsHealthcare%7Cibm-login%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/aws-healthcare/proactive-healthcare-management/ibm/scripts/%20%26%26%20chmod%20%2Bx%20.%2Flogin.sh%20%26%26%20.%2Flogin.sh">Login to IBM Cloud</a>
            <span class="dot"></span>
        </div>
        <div class="timeline step generate-api-key">
            <div class="content">
                <p>Create services on IBM Cloud and generate an API Key to access the Watson Machine Learning service.</p>
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="create IBM service and API key" href="didact://?commandId=extension.sendToTerminal&text=AwsHealthcare%7Csetup-ibm-cloud%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/aws-healthcare/proactive-healthcare-management/ibm/scripts/%20%26%26%20chmod%20%2Bx%20.%2Fcreate-ibm-cloud-services.sh%20%26%26%20.%2Fcreate-ibm-cloud-services.sh;cd%20${CHE_PROJECTS_ROOT}/aws-healthcare/proactive-healthcare-management/ibm/;ibmcloud%20iam%20api-key-create%20ApiKey-AwsHealthcare%20-d%20'this is API key for AwsHealthcare'%20--file%20${CHE_PROJECTS_ROOT}/aws-healthcare/proactive-healthcare-management/ibm/key_file">Setup IBM Cloud</a>
            <span class="dot"></span>
        </div>
        <div class="timeline step configure-aws">
            <div class="content">
                <p>Log in to your <a href="https://console.aws.amazon.com/iam/home#/security_credentials$access_key">AWS account</a> and create access key.</p>
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="Configure AWS Account" href="didact://?commandId=extension.sendToTerminal&text=AwsHealthcare%7Cconfigure-aws%7Csandbox%20terminal|export AWS_PAGER='';cd%20${CHE_PROJECTS_ROOT}/aws-healthcare/proactive-healthcare-management/%20%26%26%20aws%20configure">Configure AWS Account</a>
            <span class="dot"></span>
        </div>
        <div class="timeline step create-s3-bucket">
            <div class="content">
                <p>Create an S3 bucket to dump the healthcare data.</p>
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="Create Bucket" href="didact://?commandId=extension.sendToTerminal&text=AwsHealthcare%7Ccreate-bucket%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/aws-healthcare/proactive-healthcare-management/aws/scripts%20%26%26%20chmod%20%2Bx%20.%2Fcreate-s3-bucket.sh%20%26%26%20.%2Fcreate-s3-bucket.sh">Create Bucket</a>
            <span class="dot"></span>
        </div>
        <div class="timeline step create-kinesis-stream">
            <div class="content">
                <p>Create an Kinesis Stream between the producer and consumer lambda functions.</p>
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="Create Kinesis" href="didact://?commandId=extension.sendToTerminal&text=AwsHealthcare%7Ccreate-kinesis%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/aws-healthcare/proactive-healthcare-management/aws/scripts%20%26%26%20chmod%20%2Bx%20.%2Fcreate-kinesis.sh%20%26%26%20.%2Fcreate-kinesis.sh">Create Kinesis</a>
            <span class="dot"></span>
        </div>
        <div class="timeline step create-iam-role">
            <div class="content">
                <p>Create an IAM Role to AWS services.</p>
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="Create IAM Role" href="didact://?commandId=extension.sendToTerminal&text=AwsHealthcare%7Ccreate-iam-role%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/aws-healthcare/proactive-healthcare-management/aws/scripts%20%26%26%20chmod%20%2Bx%20.%2Fcreate-iam-role.sh%20%26%26%20.%2Fcreate-iam-role.sh">Create IAM Role</a>
            <span class="dot"></span>
        </div>
        <div class="timeline step create-lambda-function">
            <div class="content">
                <p>Create Producer Lambda Function to encrypt the healthcare data.</p>
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="Create Lambda" href="didact://?commandId=extension.sendToTerminal&text=AwsHealthcare%7Ccreate-function%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/aws-healthcare/proactive-healthcare-management/aws/%20%26%26%20python3.8%20create-lambda-producer-function.py">Create Lambda Function</a>
            <span class="dot"></span>
        </div>
        <div class="timeline step create-event-notification">
            <div class="content">
                <p>Create an event notification to trigger functions on adding data to the S3 bucket.</p>
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="Create Event Notification" href="didact://?commandId=extension.sendToTerminal&text=AwsHealthcare%7Ccreate-event-notification%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/aws-healthcare/proactive-healthcare-management/aws/scripts%20%26%26%20chmod%20%2Bx%20.%2Fcreate-event-notification.sh%20%26%26%20.%2Fcreate-event-notification.sh">Create Event Notification</a>
            <span class="dot"></span>
        </div>
        <div class="timeline step create-deployment-space">
            <div class="content">
                <p>Create a new deployment space with the pre-loaded model. Make sure your <a href="https://dataplatform.cloud.ibm.com?cm_sp=ibmdev--developer-sandbox--cloudreg">IBM Cloud Pak for Data</a> account is active.</p>
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="Create Deployment Space" href="didact://?commandId=extension.sendToTerminal&text=AwsHealthcare%7Ccreate-deployment-space%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/aws-healthcare/proactive-healthcare-management/ibm/deployment-files/%20%26%26%20python3.8%20create_space.py">Create Deployment Space</a>
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
                        <a id="step" class="button is-dark is-medium" href="https://github.com/IBM/Developer-Playground/raw/aws-healthcare/proactive-healthcare-management/Model/aws-healthcare.zip">Download</a>
                        <span class="dot"></span>
                    </div>
                    <div class="timeline step">
                        <div class="content">
                            <p>Step 2 : Login to your <a href="https://dataplatform.cloud.ibm.com?cm_sp=ibmdev--developer-sandbox--cloudreg">IBM CloudPak for Data</a> account with the <b>Region</b> given in your sandbox terminal. Click on <b>Create a Project</b>.</p>
                            <img src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/bank-loan-didact1.png" width="750" height="750">
                        </div>
                        <input type="checkbox">
                        <a id="step" class="button is-dark is-medium">Mark as Complete</a>
                        <span class="dot"></span>
                    </div>
                    <div class="timeline step">
                        <div class="content">
                            <p>Step 3 : Click on <b>Create a project from sample or file.</b></p>
                            <img src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/bank-loan-didact2.png" width="750" height="750">
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
                            <img src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/aws-healthcare-didact3.png" width="750" height="750">
                        </div>
                        <input type="checkbox">
                        <a id="step" class="button is-dark is-medium">Mark as Complete</a>
                        <span class="dot"></span>
                    </div>
                    <div class="timeline step">
                        <div class="content">
                            <p>Step 5 : After the project is created, click on <b>View new project</b>.</p>
                            <img src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/aws-healthcare-didact4.png" width="750" height="750">
                        </div>
                        <input type="checkbox">
                        <a id="step" class="button is-dark is-medium">Mark as Complete</a>
                        <span class="dot"></span>
                    </div>
                    <div class="timeline step">
                        <div class="content">
                            <p>Step 6 : Click on the <b>Assets</b> tab.</p>
                            <img src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/aws-healthcare-didact5.png" width="750" height="750">
                        </div>
                        <input type="checkbox">
                        <a id="step" class="button is-dark is-medium">Mark as Complete</a>
                        <span class="dot"></span>
                    </div>
                    <div class="timeline step">
                        <div class="content">
                            <p>Step 7 : Click on the <b>(⋮)</b> icon right hand side of the <b>Model</b> and Click on <b>Promote</b>.</p>
                            <img src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/aws-healthcare-didact6.png" width="750" height="750">
                        </div>
                        <input type="checkbox">
                        <a id="step" class="button is-dark is-medium">Mark as Complete</a>
                        <span class="dot"></span>
                    </div>
                    <div class="timeline step">
                        <div class="content">
                            <p>Step 8 : On the <b>Target Space</b> drop-down menu, select the deployment space you created (To get the deployment space name check your sandbox terminal), Once done click <b>Promote</b>.</p>
                            <img src="https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/aws-healthcare-didact7.png" width="750" height="750">
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
                <p>Deploy the model on Cloud Pak for Data.</p>
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="Deploy Model" href="didact://?commandId=extension.sendToTerminal&text=AwsHealthcare%7Cdeploy-model%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/aws-healthcare/proactive-healthcare-management/ibm/deployment-files/%20%26%26%20python3.8%20DeploySavedModel.py">Deploy Model</a>
            <span class="dot"></span>
        </div>
        <div class="timeline step create-lambda-function">
            <div class="content">
                <p>Create Consumer Lambda Function to invoke the model from Cloud Pak for Data with the data received from kinesis streams.</p>
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="Create Lambda" href="didact://?commandId=extension.sendToTerminal&text=AwsHealthcare%7Ccreate-function%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/aws-healthcare/proactive-healthcare-management/aws/%20%26%26%20python3.8%20create-lambda-consumer-function.py">Create Consumer Function</a>
            <span class="dot"></span>
        </div>
        <div class="timeline step upload-to-s3">
            <div class="content">
                <p>Upload healthcare data to S3 bucket.</p>
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="Upload Data" href="didact://?commandId=extension.sendToTerminal&text=AwsHealthcare%7Cupload-data%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/aws-healthcare/proactive-healthcare-management/aws/scripts%20%26%26%20chmod%20%2Bx%20.%2Fupload-data.sh%20%26%26%20.%2Fupload-data.sh">Upload Data</a>
            <span class="dot"></span>
        </div>
        <div class="timeline step get-cloudwatch-logs">
            <div class="content">
                <p>From AWS CloudWatch, get the Consumer Logs having the data streamed from the Kinesis and the predictions received from the Watson ML. Fetching the logs might take some time. Please check the sandbox terminal for completion message.</p>
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="Get logs" href="didact://?commandId=extension.sendToTerminal&text=AwsHealthcare%7Cget-logs%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/aws-healthcare/proactive-healthcare-management/aws/;python3.8%20print-logs.py">Get Logs</a>
            <span class="dot"></span>
        </div>
        <div class="timeline step open-cloudwatch-logs">
            <div class="content">
                <p>Open the Logs in Sandbox.</p>
            </div>
            <input type="checkbox">
            <a id="step" class="button is-dark is-medium" title="Open logs" href="didact://?commandId=extension.openFile&text=AwsHealthcare%7Copen-file%7C${CHE_PROJECTS_ROOT}/aws-healthcare/proactive-healthcare-management/aws/logs.txt">Open Logs</a>
            <span class="dot"></span>
        </div>
    </div>
    <div class="footer">
        <div class="footer-cta">
            <div class="footer-step clean-up-services" style="background:transparent">  
                <p style="margin-top:0.625rem;">Click on Clean up to delete the AWS services that were created.</p>
                <a class="button is-dark is-medium" title="Delete services from AWS" href="didact://?commandId=extension.sendToTerminal&text=AwsHealthcare%7Caws-clean-up%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/aws-healthcare/proactive-healthcare-management/aws/;python3.8%20delete-aws-services.py">AWS Clean Up</a>
                <p style="margin-top:0.625rem;">You can also manage the AWS services in <a href="https://console.aws.amazon.com">AWS Console</a></p>
            </div>
            <div class="footer-step clean-up-services" style="background:transparent"> 
                <p style="margin-top:0.625rem;">Click on Clean up to delete the IBM Cloud services that were created.</p>
                <a class="button is-dark is-medium" title="Delete services from IBM Cloud" href="didact://?commandId=extension.sendToTerminal&text=AwsHealthcare%7Cibm-clean-up%7Csandbox%20terminal|cd%20${CHE_PROJECTS_ROOT}/aws-healthcare/proactive-healthcare-management/ibm/scripts;chmod%20%2Bx%20.%2Fdeleteservice.sh%20%26%26%20.%2Fdeleteservice.sh">IBM Clean Up</a>
                <p style="margin-top:0.625rem;">You can also manage the IBM services in <a href="https://cloud.ibm.com/resources">IBM Cloud Dashboard</a></p>
                <p style="margin-top:0.625rem;"></p>
            </div>
            <div class="footer-step git-push" style="background:transparent">
                <p style="margin-top:0.625rem;">Click to push code to your own Github repository. You will need a personal access
                token to complete this action via the CLI. Refer to this <a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token">guide</a> for generating your personal access token.</p>
                <a class="button is-dark is-medium" title="Delete services from IBM Cloud" href="didact://?commandId=extension.sendToTerminal&text=sandbox%20terminal$$sh%20/github.sh ">Push to Github</a>
            </div>
        </div>
        <div class="image-div">
            <p class="image-content">Want to explore this project more?
            <span style="font-size:15px;margin-top:0px;display:block;">Head over to the <a href="https://github.com/IBM/Developer-Playground/tree/aws-healthcare">Github Repository</a></span>
            <span style="font-size:15px;margin-top:0px;display:block;">For further assistance reach out to <a href="https://github.com/IBM/Technology-Sandbox-Support/issues/new/choose" target="_blank"> Help & Support</a></span>
            <span style="font-size:15px;margin-top:0px;display:block;">Check out our <a href="https://ibm.github.io/Technology-Sandbox-Support/" target="_blank">FAQs</a></span></p>
            <a class="image-link" href="https://developer.ibm.com/patterns/proactive-healthcare-management-system-with-aws-streams-and-ibm-cpd-analytics/" target="_blank">
                <div class="image-btn">
                    <p class="image-link">View Product Details
                        <p style="padding-top: 14px"></p>
                        <span>
                            <svg style="position: absolute; right: 10px;" fill="#ffffff" focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/  svg" width="25" height="25" viewBox="0 0 32 32" aria-hidden="true">
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
<script src="progressive.js"></script>
</html>
