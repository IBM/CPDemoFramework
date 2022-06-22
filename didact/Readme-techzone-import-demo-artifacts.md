<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="import-demo-artifacts.css">
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
            <div class="apptitle">Recreate shared demo assets on your CPD cluster</div>
            <div class="subheading">Demo assets include different types of artifacts such as Users, Governance artifacts, Analytics projects, Data integration projects etc.</br>Enter your CPD credentials and select one or more artifacts to recreate into your CPD cluster.</div>
        </div>
    </div>
    <div class="section">
        <p style="font-size:24px">Pre-requisites</p>
        <div>
            <p>Enter your cp4d details.</p>
            <div class="env-config">
                <label>Hostname: </label><input class="env-variables" name="hostname" type="text" />
                <label>User: </label><input class="env-variables" name="wkcuser" type="text" />
                <label>Password: </label><input class="env-variables" name="password" type="password" />
            </div>
        </div>
    </div>
    <div class="section">
        <p style="font-size:24px">Instructions</p>
        <p>Please follow all the below steps in proper sequence.</p>
    </div>
    <div class="timeline-container">
        <div class="timeline timelinestep">
            <div class="content">
                <p>Demo Name: <b id="selected-demo">$demo_name</b></p>
            </div>
            <span class="dot"></span>
        </div>
        <div class="timeline timelinestep">
            <div class="content">
                <p>Get the resources required and update the cp4d details in .env file.</p>
            </div>
            <a id="configure-env" class="button is-dark is-medium" title="Configure Resources"
                href="didact://?commandId=extension.compositeCommand&&text=terminal-for-sandbox-container:new%7Cvscode.didact.sendNamedTerminalAString%2Csandbox%20terminal%2Cgit%20clone%20-b%20techzone%20https%3A%2F%2Fgithub.com%2FIBM%2FDeveloper-Playground%20%24%7BCHE_PROJECTS_ROOT%7D%2Ftechzone-demo%2C%2Fprojects%7Cvscode.didact.sendNamedTerminalAString%2Csandbox%20terminal%2Csh%20/projects/techzone-demo/sandbox/getDemoFiles.sh%20demo_name%7Cvscode.didact.sendNamedTerminalAString%2Csandbox%20terminal%2Ccd%20${CHE_PROJECTS_ROOT}/techzone-demo;pip3.8%20install%20-r%20requirements.txt%3Bcd%20%2Fprojects%2Ftechzone-demo%2Fsandbox%2F">Configure Environment</a>
            <span class="dot"></span>
        </div>
        <div class="timeline" id="task1">
            <div class="content">
                <details>
                    <summary>User management<span class="arrow"></span></summary>
                    <br><br>
                    <div>
                        <div class="content">
                            <p>Create users in the configured cp4d instance.</p>
                        </div>
                        <a class="button is-dark is-medium" title="Create Users"
                            href="didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$cd /projects/techzone-demo/sandbox/;python3.8 createUsers.py users.csv">Create
                            Users</a>
                    </div>
                </details>
            </div>
            <span class="dot"></span>
        </div>
        <div class="timeline" id="task2">
            <div class="content">
                <details>
                    <summary>Governance Artifacts<span class="arrow"></span></summary>
                    <br><br>
                    <div>
                        <div class="content">
                            <p>Import Governance Artifacts</p>
                        </div>
                        <a class="button is-dark is-medium" title="Import Gov Artifacts"
                            href="didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$cd /projects/techzone-demo/sandbox/;python3.8 importGovArtifacts.py governance_artifacts.zip">Import
                            Artifacts</a>
                    </div>
                </details>
            </div>
            <span class="dot"></span>
        </div>
        <!--<div class="timeline" id="task2">
            <div class="content">
                            <p>Validate</p>
                        </div>
                        <a class="button is-dark is-medium" title="Export Gov Artifacts"
                            href="didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$cd /projects/techzone-demo/sandbox/;">Validate</a>
            <span class="dot"></span>
        </div>-->
        <div class="timeline" id="task3">
            <div class="content">
                <details>
                    <summary>Project management<span class="arrow"></span></summary>
                    <br><br>
                    <div>
                        <div class="content">
                            <p>Import project</p>
                        </div>
                        <a id="import-project" class="button is-dark is-medium" title="Import Project"
                            href="didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$cd /projects/techzone-demo/sandbox/;python3.8 importProject.py project_assets ">Import
                            Project</a>
                        <span class="dot"></span>
                    </div>
                </details>
            </div>
            <span class="dot"></span>
        </div>
    </div>
    </div>
    </div>
</body>
<script src="import-demo-artifacts.js"></script>

</html>
