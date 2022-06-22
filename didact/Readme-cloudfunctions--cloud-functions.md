<html>
<style>
.boxed 
{
  border: 1px solid blue ;
}
</style>
<style>
.btn {
  border: 2px solid gray;
  background-color: #202020;
  color: white;
  padding: 10px 15px;
  font-size: 16px;
  cursor: pointer;
}
.info {
  border-color: gray;
  color: gray;
  
}
<style>
html,div,body{
    background-color:#1a1a1a;
    font-family: 'IBM Plex Sans', sans-serif;
}

.content p{
  font-family: 'IBM Plex Sans', sans-serif;  
  font:15px;
  color: #fff;
}
pre{
    background-color:#d9dbde;
    color:#000;
    font-family: 'IBM Plex Sans', sans-serif;
    font:12px;
}
.content h4{
    color:#fff;
}
.content h6{
    font-family: 'IBM Plex Sans', sans-serif;
    background-color:#1a1a1a;
    color:#fff;
}
.content h3{
    font-family: 'IBM Plex Sans', sans-serif;
    color: #2a67f5;
    background-color:#1a1a1a;
}
.h3{
    font-family: 'IBM Plex Sans', sans-serif;
    color: #2a67f5;
    background-color:#1a1a1a;
}
ul, ol,b{ 
    font-family: 'IBM Plex Sans', sans-serif;
    color: #fff;
}
#ul1{
  font-family: 'IBM Plex Sans', sans-serif;
    color: #fff;
}
.button.is-dark.is-medium {
  font-family: 'IBM Plex Sans', sans-serif;
  background-color: #1a1a1a;
  border-color: white;
  color: #fff;
}
.button.is-dark.is-medium:hover {
  font-family: 'IBM Plex Sans', sans-serif;
  background-color: #2a67f5;
  border-color: white;
  color: #fff;
}
.title.is-3{
  font-family: 'IBM Plex Sans', sans-serif;
  color:#fff;
}
.subtitle.is-4{
    font-family: 'IBM Plex Sans', sans-serif;
    color:#fff;
}
​
</style>
<body style="font-family: 'IBM Plex Sans', sans-serif;background-color:#1a1a1a;">
<div style="font-family: 'IBM Plex Sans', sans-serif;background-color:#1a1a1a;">
​
</style>
​
<body>

<img src = "https://github.com/IBM/Developer-Playground/raw/475f1649ea46e4b31f7e9f4a8cb1760e59f03d55/didact/images/unnamed.jpg" width = "500" height= "500">


<h2 class="title is-3 ">Cloud Pak Sample App</h2>

<p> This sample app aims to showcase the functionalities available on the Cloud Pak platform, with regards to Cloud Pak for Data and Cloud Pak for Integration
</p>

<h3> Getting Started</h3></span>

<span style="color:grey"><h2>1. Create an account on IBM's Cloud Platform</h2></span>

To ensure a completely immersive experience with Cloud Pak services, create an account on IBM's cloud platform.

<a class="button is-dark is-medium" title="Build the App" href="didact://?commandId=terminal-for-nodejs-container:new">Open Terminal</a><br>

<p>On click of the below button will help you login through IBM cloud CLI commands.</p>

<a class="button is-dark is-medium" title="Log in here" href="didact://?commandId=vscode.didact.sendNamedTerminalAString&text=nodejs%20terminal%201$$cd ${CHE_PROJECTS_ROOT}/LoanAPP-MQ ;ibmcloud%20login%20-r%20eu-gb%20--sso%20%26%26%20ibmcloud%20target%20--cf%20%26%26%20ibmcloud%20target%20-g%20Default">Log in here</a><br>



<span style="color:grey"><h2> 2. Check prerequisites linked to Cloud account</h2></span>

<p> This sample app requires the user to avail certain instances present in the Services catalog. The lite version of these services will suffice. The instances are listed below:</p>


<h4>2.1 IBM MQ</h4>

<p>IBM MQ(Message Queue) provides proven, enterprise-grade messaging capabilities, such as point-to-point and publish/subscribe models, to facilitate the flow of information between applications.It enables asynchronous messaging.</p>

<h5>Follow the below steps to create an IBM MQ instance and connect your application data to IBM MQ.</h5>

<p>Step1: Click the below button to create IBM MQ instance through IBM cloud CLI commands.</p>
<a class="button is-dark is-medium" title="IBM MQ" href="didact://?commandId=vscode.didact.sendNamedTerminalAString&text=nodejs terminal 1$$ibmcloud resource service-instance-create mqinstance mqcloud lite eu-gb">IBM MQ</a><br><br>
<p>Step 2 : Go to <a href='https://cloud.ibm.com/resources'>IBM cloud resources</a>.Expand the <b>services</b> row and click the <b>mqinstace</b> that has been created.
 </p>
<img src = "https://github.com/IBM/Developer-Playground/raw/d74eff025600d4cab158f2c7926946275984cfbc/didact/images/IBM-cloud-resourceList.png" width = "750" height= "750">
<p>Step 3 : On clicking the instance you will be re-directed to a page as shown below.click on create button to create queue manager.
 </p>
<img src = "https://github.com/IBM/Developer-Playground/raw/475f1649ea46e4b31f7e9f4a8cb1760e59f03d55/didact/images/MQ-step2.png" width = "750" height= "750">
<p>Step 4 : Give queue manager a name and click on create.</p>
<img src = "https://github.com/IBM/Developer-Playground/raw/475f1649ea46e4b31f7e9f4a8cb1760e59f03d55/didact/images/MQ-step3.png" width = "750" height= "750">

<p>Step 5 : Creating queue manager takes some time. When the status changes to running it indicates that queue manager is ready to use.</p>
<img src = "https://github.com/IBM/Developer-Playground/raw/475f1649ea46e4b31f7e9f4a8cb1760e59f03d55/didact/images/MQ-step4.png" width = "750" height= "750">

<p>Step 6 : Click on Application credentials and click on Add.</p>
<img src = "https://github.com/IBM/Developer-Playground/raw/475f1649ea46e4b31f7e9f4a8cb1760e59f03d55/didact/images/MQ-step5.png" width = "750" height= "750">
<p>Step 7 : Give a display name and click in add and generate API Key.Download the file</p>
<img src = "https://github.com/IBM/Developer-Playground/raw/475f1649ea46e4b31f7e9f4a8cb1760e59f03d55/didact/images/MQ-step6.png" width = "750" height= "750">
<p>Step 8 : Go to <b>Queue managers</b> tab and click on the queue manager that you have created in step in step3.</p>
<img src = "https://github.com/IBM/Developer-Playground/raw/475f1649ea46e4b31f7e9f4a8cb1760e59f03d55/didact/images/MQ-step7.png" width = "750" height= "750">
<p>Step 9 : Download the connection information as shown in the below image.</p>
<img src = "https://github.com/IBM/Developer-Playground/raw/475f1649ea46e4b31f7e9f4a8cb1760e59f03d55/didact/images/MQ-step8.png" width = "750" height= "750">
<br/>
<br/>
<br/>
<h4>2.2 Waston Machine Learning </h4>
<p>IBM Watson Machine Learning helps data scientists and developers accelerate AI and machine learning deployment on IBM Cloud Pak for Data.With watson machine learning you can deploy AI models at scale across any cloud on an open.</p>

<p>Click on the below button to create a machine learning instance on IBM cloud .</p>

<a class="button is-dark is-medium" title="Machine Learning" href="https://dataplatform.cloud.ibm.com/data/catalog/pm-20?context=cpdaas&target=services">Machine Learning</a>
<br>

<p>On clicking the above button you will be redirected to a page as shown in the below figure.</p>
<img src = "https://github.com/IBM/Developer-Playground/raw/475f1649ea46e4b31f7e9f4a8cb1760e59f03d55/didact/images/machineLearning-instance.png" width = "750" height= "750">
<br/>
<br/>̌
<h4>2.3 MongoDB on IBM cloud</h4>
<p>Click on the below button to create a MongoDB instance on IBM cloud .</p>
<a class="button is-dark is-medium" title="Databases for MongoDB" href="https://dataplatform.cloud.ibm.com/data/catalog/databases-for-mongodb?context=cpdaas&target=services">Databases for MongoDB</a><br>
<p>On clicking the above button you will be redirected to a page as shown in the below figure.</p>
<img src = "https://github.com/IBM/Developer-Playground/raw/475f1649ea46e4b31f7e9f4a8cb1760e59f03d55/didact/images/Mongo-instance.png" width = "750" height= "750">
<br>
</body>



<span style="color:grey"><h2>3. Clone the GitHub repo for this Sample App</h2></span>

<p>This Sample app needs to be cloned onto the Developer playground. It only takes a few minutes to do so.</p>


<p href="didact://?commandId=send">
<a class="button is-dark is-medium" title="Get the code" href="didact://?commandId=vscode.didact.sendNamedTerminalAString&text=nodejs terminal 1$$git+clone+https://github.ibm.com/SUMANVITA-K/LoanAPP-MQ">Get the code</a><br>

<span style="color:grey"><h2>4.Deploy AutoAI Model</h2></span>

<p>To deploy the AutoAI model to deployment space the program will require API key and space id</p>
<ul><h6>Steps to generate API Key</h6>
<li>
<p>Step 1 : Haven't logged in to IBM Cloud ? then click  <a  href="didact://?commandId=vscode.didact.sendNamedTerminalAString&text=nodejs%20terminal%201$$cd ${CHE_PROJECTS_ROOT}/LoanAPP-MQ ;ibmcloud%20login%20-r%20eu-gb%20--sso%20%26%26%20ibmcloud%20target%20--cf%20%26%26%20ibmcloud%20target%20-g%20Default">login to ibm cloud</a>
 </p>

</li>
<li>

<p>Step 2 :  Click the below button to generate api key through IBM cloud CLI commands.</p><br>
<a class="button is-dark is-medium" title="Generate API key" href="didact://?commandId=vscode.didact.sendNamedTerminalAString&text=nodejs%20terminal%201$$cd ${CHE_PROJECTS_ROOT}/LoanAPP-MQ ; ibmcloud%20iam%20api-key-create%20ApiKey-LoanApp-MQ%20-d%20'this is API key for loanapp-MQ'%20--file ${CHE_PROJECTS_ROOT}/LoanAPP-MQ/key_file">Generate api key</a><br> 
<p>This will generate API key with name <b>ApiKey-LoanApp-MQ</b> and the value of API key will be stored in <b>key_file</b> file in the main directory of the project.</p>
</li>
</ul>

<ul><h6>Steps to generate deployment space</h6>
<li>
<p>Step 1 : Go to <a href="https://dataplatform.cloud.ibm.com/">IBM CloudPak for data</a> and login with your mail id. Once you login click on view all spaces button as shown in the figure below.
 </p>
<img src = "https://github.com/IBM/Developer-Playground/raw/475f1649ea46e4b31f7e9f4a8cb1760e59f03d55/didact/images/step1-spaceId.png" width = "750" height= "750">
</li>
<li>
<p>Step 2 :  Click on create deployment space.</p>
<img src = "https://github.com/IBM/Developer-Playground/raw/475f1649ea46e4b31f7e9f4a8cb1760e59f03d55/didact/images/step2-spaceId.png" width = "750" height= "750">
</li>
<li><p>Step 3 : Give the deployment a name and add a machine learning instance that you have earlier created.Click on create button after filling the details.</p>
<img src = "https://github.com/IBM/Developer-Playground/raw/475f1649ea46e4b31f7e9f4a8cb1760e59f03d55/didact/images/step3-spaceID.png" width = "750" height= "750">
</li>
<li>
<p>Step 4 : Click on view deployement space and then select manage tab.Under this tab, copy the space GUID.</p>

</li>
</ul>


<a class="button is-dark is-medium" title="Deploy the model" href="didact://?commandId=vscode.didact.sendNamedTerminalAString&text=nodejs terminal 1$$cd ${CHE_PROJECTS_ROOT}/LoanAPP-MQ ; pip3.8+install+-r+requirements.txt;python3.8+./DeployModel/DeployMLModel.py">Deploy Model</a><br>


<span style="color:grey"><h2>5. Build the App</h2></span>

<p> Build the application to explore it's functionalities within the given terminal.</p>
<a class="button is-dark is-medium" title="Build the App" href="didact://?commandId=vscode.didact.sendNamedTerminalAString&text=nodejs terminal 1$$cd ${CHE_PROJECTS_ROOT}/LoanAPP-MQ ;npm+install">Build the App</a><br>

<span style="color:grey"><h4>6.Adding credentials to the App</h4></span>

<p>CLick the below button to open the .env file. </p>

<a class="button is-dark is-medium" title="Edit environment variables" href="didact://?commandId=vscode.open&projectFilePath=LoanAPP-MQ/.env">Edit Environment Variables</a><br>
<br/>
<b>Follow the below instructions to plugin the correct values in the env file.</b>
<br/>
<p>Open the connection information file that you have downloaded from section 2.1 step8.Replace the values of <b>host_name</b>, <b>queue_manager_name</b> in .env file with <b>hostname</b>, <b>queueManagerName</b> </p> of connection_info.json file respectively.Now open the Application API key file that you have downloaded from section2.1 step 6.Replace <b>user_name</b>, <b>api_key_mq</b> of .env file with the <b>mqUsername</b>, <b>apiKey</b> of applicationApiKey.json file respectively.

<br/>


<span style="color:grey"><h2>7.Launch the Application</h2></span>

<p>Upon launching the app,the application will start running. </p>

<a class="button is-dark is-medium" title="Launch the Application" href="didact://?commandId=vscode.didact.sendNamedTerminalAString&text=nodejs terminal 1$$cd ${CHE_PROJECTS_ROOT}/LoanAPP-MQ ; npm+start">Launch the Application</a><br>

<!-- <span style="color:grey"><h2>7. Explore the Code.</h2></span>

<a class="button is-dark is-medium" title="Explore the Code" href="didact://?commandId=workbench.view.explorer">Explore the Code</a><br><br>

<p> -->
<span style="color:grey"><h2>8.Stop the application</h2></span>

<a class="button is-dark is-medium" title="Stop terminal" href="didact://?commandId=vscode.didact.sendNamedTerminalCtrlC&text=nodejs%20terminal%201">Stop Terminal</a><br>

<span style="color:grey"><h2>9.Delete Deployment</h2></span>

<p>Deleting deployment will help you save CUH.</p>

<a class="button is-dark is-medium" title="Delete deployment" href="didact://?commandId=vscode.didact.sendNamedTerminalAString&text=nodejs terminal 1$$cd ${CHE_PROJECTS_ROOT}/LoanAPP-MQ ;python3.8+./DeleteDeploy/deleteDeploy.py">Delete Deployment</a><br>
  
<span style="color:grey"><h2>10.Delete API key</h2></span>

<p>Click the below button to delete API key generated in step 4 through IBM cloud CLI command both from the sample app and IBM cloud.</p>
<a class="button is-dark is-medium" title="Delete API Key" href="didact://?commandId=vscode.didact.sendNamedTerminalAString&text=nodejs terminal 1$$cd ${CHE_PROJECTS_ROOT}/LoanAPP-MQ ;ibmcloud iam api-key-delete ApiKey-LoanApp-MQ ; rm ${CHE_PROJECTS_ROOT}/LoanAPP-MQ/key_file">Delete API Key</a><br>
