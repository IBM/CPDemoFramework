<html>

<head>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <script src="olm-utils.js">
  </script>
  <link rel="stylesheet" href="olm-utils.css">
  <style>
    .header {
      background-image: url("https://raw.githubusercontent.com/IBM/Developer-Playground/master/didact/images/video_insights.jpeg");
    }
  </style>

</head>

<body>
  <div style="margin-top:2rem"></div>
  <div id="workspaceID" class="hidden-state">$workspace_id</div>
  <div id="userID" class="hidden-state">$user_id</div>
  <div id="environment" class="hidden-state">$environment</div>
  <div class="header">
    <div class="left-content">
      <div class="apptitle">Self-service customizable CP4D environment setup</div>
      <div class="subheading">Cloud Pak for Data (CP4D) v4 adopted the Operator based installation & management pattern.
        This gives us flexibility to custom build a demo environment based on our needs. If we are doing a simple data
        science demo with services WS, WML you can choose to just install those 2 services in a self-service fashion on
        an appropriately sized cluster for more cost effectiveness in addition to better performance as you would have
        installed just services you need for your demo. This interface uses standard engineering-supported install
        utility/mechanism for ongoing support/maintainability.</div>
    </div>
  </div>
  <div class="section">
    <p style="font-size:24px">Pre-requisites</p>
    <div>
      <p>Configure Openshift credentials (either use combination of server, user/password (OR) server, token).<br>
        Openshift server name (including https://) and token can be obtained using one of two methods
      <ol>
        <li>From Openshift console, select your profile on top right and select “Copy login command”</li>
        <li>From oc cli, run “oc config view --minify|grep server” to get server name and “oc whoami -t” to get token
        </li>
      </ol>
      You can get the ICR KEY by logging onto <a href="https://myibm.ibm.com">myibm.ibm.com</a> using your IBM ID.
      </p>
      <div class="env-config">
        <label>Server: </label><input class="env-variables" name="server" type="text" />
        <label>API Token: </label><input class="env-variables" name="api_token" type="text" />
        <p>-------OR-------</p>
        <p></p>
        <label>Kube Admin User: </label><input class="env-variables" name="kubeadmin_user" type="text" />
        <label>Kube Admin Password: </label><input class="env-variables" name="kubeadmin_pass" type="password" />
      </div>
    </div>
  </div>
  <div class="section">
    <p style="font-size: 24px">Instructions</p>
    Please follow all the below steps in proper sequence<br>
    At a high level the installation steps include:
    <ol>
      <li>Deploy Operator Lifecycle Manager (OLM )objects for selected Cloud Pak for Data(CP4D) services.</li>
      <li>Deploy custom resources for selected CP4D services.</li>
    </ol>
    Please follow steps below as appropriate, some steps are optional depending on what needs to be done. Mandatory
    steps are indicated using *<br><br>
  </div>
  <div class="timeline-container">
    <!--<div class="timeline">
      <div class="content">
        <p>Open the sandbox terminal.</p>
      </div>
      <a class="button is-dark is-medium" title="Open Terminal"
        href="didact://?commandId=terminal-for-sandbox-container:new">Open Terminal *</a>
      <span class="dot"></span>
    </div>-->
    <div class="timeline">
      <div class="content">
        <p>Get the resources required to deploy CP4D services and configure the openshift credentials.</p>
      </div>
      <a class="button is-dark is-medium" id="configure-env" title="Configure Environment"
        href="didact://?commandId=extension.compositeCommand&&text=terminal-for-sandbox-container:new%7Cvscode.didact.sendNamedTerminalAString%2Csandbox%20terminal%2Cgit clone https://github.com/IBM/Developer-Playground -b techzone --single-branch techzone;cd%20${CHE_PROJECTS_ROOT}/techzone/olm-utils;python3.8%20update-env-vars.py%20">Configure
        Environment *</a>
      <span class="dot"></span>
    </div>
    <!--<div class="timeline">
      <div class="content">
        <p>Configure Openshift credentials (either use combination of server, user/password (OR) server, token).<br>
          Openshift server name (including https://) and token can be obtained using one of two methods
        <ol>
          <li>From Openshift console, select your profile on top right and select “Copy login command”</li>
          <li>From oc cli, run “oc config view --minify|grep server” to get server name and “oc whoami -t” to get token
          </li>
        </ol>
        You can get the ICR KEY by logging onto <a href="https://myibm.ibm.com">myibm.ibm.com</a> using your IBM ID.
        </p>
      </div>
      <a class="button is-dark is-medium" title="open env file"
        href="didact://?commandId=vscode.open&projectFilePath=/projects/techzone/olm-utils/env.sh">Configure *
      </a>
      <span class="dot"></span>
    </div>-->
    <div class="timeline">
      <div class="content">
        <p>Deploy CP4D installation utility </p>
      </div>
      <a class="button is-dark is-medium" title="open env file"
        href="didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$source env.sh">Deploy
        *
      </a>
      <span class="dot"></span>
    </div>
    <div class="timeline">
      <div class="content">
        <p>Check the status of the installation utility deployment, it might take upto 45 seconds for the deployment to
          be ready, you are ready to proceed to the next step when the olm-utils pod is in running state </p>
      </div>
      <a class="button is-dark is-medium" title="Check Pod State"
        href="didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$get_pods">Check Pod
        State
      </a>
      <span class="dot"></span>
    </div>
    <!-- <div class="timeline">
      <div class="content">
        <p>Run Utils Login to OC</p>
        <a class="button is-dark is-medium" title="Check Pod State"
          href="didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$oclogin_auto">oclogin
        </a>
      </div>
    </div> -->
    <div class="timeline">
      <div class="content">
        <p>Installation of CP4D services requires the correct service code/name to be used, you can get the services
          code/name by listing components. The subsequent steps have a “components” field where you can provide one or
          more service code(s) in a comma-separated list </p>
      </div>
      <a class="button is-dark is-medium" title="Check Pod State"
        href="didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$run_utils list-components --release=4.0.5">List
        Components
      </a>
      <span class="dot"></span>
    </div>
    <div class="timeline">
      <div class="content">
        <p>Check currently installed CP4D services on the cluster in the selected namespace. If this is a new
          cluster/namespace, there will be no CP4D services installed</p>
        <label>CPD instance namespace</label>
        <input type="text" id="cpd_instance_value" value="cpd-instance">
      </div>
      <a class="button is-dark is-medium" title="Execute" id="existing_service">Execute
      </a>
      <span class="dot"></span>
    </div>
    <div class="timeline">
      <div class="content">
        <p>Deploy OLM (Catalog source, Subscription, Cluster service version, Install Plan) objects for selected CP4D
          services</p>
        <div class="env-config">
          <label>Preview</label>
          <select id="olm_preview_value">
            <option value="true">true</option>
            <option value="false">false</option>
          </select>
          <label>Release Version</label>
          <input type="text" id="olm_release_version" placeholder="4.0.5">
          <label>Components list</label>
          <div id="olm-service-list" class="dropdown-check-list" tabindex="100">
            <span class="anchor">Select Components</span>
            <div class="items">
              <input id="olm-services-search" type="search" placeholder="Search components" style="width: 100%" />
              <ul id="olm-git-services">
              </ul>
            </div>
          </div>
        </div>
        <p style="margin-top:1rem"><b>Selected Services: </b><span id="olm-selected-services"></span></p>
        <!--<input type="text" id="olm_component_list" placeholder="cpfs,cpd_platform"><br><br>-->
      </div>
      <a class="button is-dark is-medium" title="Execute" id="install_olm">Execute
      </a>
      <br />
      <br />
      <a class="button is-dark is-medium" title="open the preview file" id="get_preview">Open Preview File
      </a>
      <span class="dot"></span>
    </div>
    <div class="timeline">
      <div class="content">
        <p>Deploy custom resources for selected CP4D services</p>
        <div class="env-config">
          <label>Preview</label>
          <select id="cr_preview_value">
            <option value="true">true</option>
            <option value="false">false</option>
          </select>
          <label>Release version</label>
          <input type="text" id="cr_release_version" placeholder="4.0.5">
          <label>Components list
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
          <div id="cr-service-list" class="dropdown-check-list" tabindex="100">
            <span class="anchor">Select Components</span>
            <div class="items">
              <input id="cr-services-search" type="search" placeholder="Search components" style="width: 100%" />
              <ul id="cr-git-services">
              </ul>
            </div>
          </div>
        </div>
        <p style="margin-top:1rem"><b>Selected Services: </b><span id="cr-selected-services"></span></p>
        <p></p>
        <!--<input type="text" id="cr_component_list" placeholder="cpfs,cpd_platform">-->
        <div class="env-config">
          <label>license_acceptance</label>
          <select id="cr_license_acceptance">
            <option value="true">true</option>
            <option value="false">false</option>
          </select>
          <label>Select Storage Type</label>
          <div>
            <select id="cr_storage_class">
              <option value="storage_class">Storage Class</option>
              <option value="storage_vendor">Storage Vendor</option>
            </select>
            <input type="text" id="cr_storage_value" placeholder="Storage Value">
          </div>
          <label>CPD instance namespace</label>
          <input type="text" id="cr_cpd_instance" value="cpd-instance">
        </div>
      </div>
      <a class="button is-dark is-medium" title="Execute" id="install_cr">Execute
      </a>
      <br />
      <br />
      <a class="button is-dark is-medium" title="open the preview file" id="get_preview_2">Open Preview File
      </a>
      <span class="dot"></span>
    </div>
    <div class="timeline">
      <div class="content">
        <p>Cleanup install utility artifacts</p>
      </div>
      <a class="button is-dark is-medium" title="Check Pod State"
        href="didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$sh delete.sh">Clean
        up
      </a>
      <span class="dot"></span>
    </div>
  </div>
  <a id="command_exec" ,href=""></a>
</body>

</html>