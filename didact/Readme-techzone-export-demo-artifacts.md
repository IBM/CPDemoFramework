<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="export-demo-artifacts.css">
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
            <div class="apptitle">Save/Share demo assets with community</div>
            <div class="subheading">Save demo artifacts to a centralized location (Shared GitHub repository). This will
                enable you to recreate your demo assets onto a different/new infrastructure (potentially on a newer
                version of Cloud Pak for Data). The centralized collection of demo assets can be leveraged by the
                broader community so we all benefit from each others work.</div>
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
                <p>Get the resources required and update the cp4d details in .env file.</p>
            </div>
            <a id="configure-env" class="button is-dark is-medium" title="Configure Resources"
                href="didact://?commandId=extension.compositeCommand&&text=terminal-for-sandbox-container:new%7Cvscode.didact.sendNamedTerminalAString%2Csandbox%20terminal%2Cgit%20clone%20-b%20techzone%20https%3A%2F%2Fgithub.com%2FIBM%2FDeveloper-Playground%20%24%7BCHE_PROJECTS_ROOT%7D%2Ftechzone-demo%2C%2Fprojects%7Cvscode.didact.sendNamedTerminalAString%2Csandbox%20terminal%2Ccd%20${CHE_PROJECTS_ROOT}/techzone-demo;pip3.8%20install%20-r%20requirements.txt%3Bcd%20%2Fprojects%2Ftechzone-demo%2Fsandbox%2F%7C">Configure
                Environment</a>
            <span class="dot"></span>
        </div>
        <div class="timeline timelinestep">
            <div class="content">
                <p>Select the required tasks</p>
                <div class="checkbox-group">
                    <div style="float:left;padding: 0.2rem;flex: 1 1 31%;">
                        <input type="checkbox" name="checkboxtask" value="task1" />
                        <label for="task1">User Management</label>
                    </div>
                    <div style="float:left;padding: 0.2rem;flex: 1 1 31%;">
                        <input type="checkbox" name="checkboxtask" value="task2" />
                        <label for="task2">Governance Artifacts</label>
                    </div>
                    <div style="float:left;padding: 0.2rem;flex: 1 1 31%;">
                        <input type="checkbox" name="checkboxtask" value="task3" />
                        <label for="task3">Project Management</label>
                    </div>
                </div>
                <span class="dot"></span>
            </div>
        </div>
        <div class="timeline" id="task1">
            <div class="content">
                <details>
                    <summary>User management<span class="arrow"></span></summary>
                    <br><br>
                    <div>
                        <div class="content">
                            <p>Export User List to the csv file</p>
                        </div>
                        <a class="button is-dark is-medium" title="Export User List"
                            href="didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$cd /projects/techzone-demo/sandbox/;python3.8 exportUsers.py users.csv">Export
                            User List</a>
                        <span class="dot"></span>
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
                    <div class="content">
                        <p>Select the action to perform in the configured cp4d instance</p>
                        <div id="list1" class="dropdown-check-list" tabindex="100">
                            <span class="anchor">Select Artifacts</span>
                            <ul class="items">
                                <li><input type="checkbox" name="governance-artifacts" value="all" checked />All </li>
                                <li><input type="checkbox" name="governance-artifacts" value="category" />Category
                                </li>
                                <li><input type="checkbox" name="governance-artifacts"
                                        value="classification" />Classification
                                </li>
                                <li><input type="checkbox" name="governance-artifacts" value="data_class" />Data
                                    Class
                                </li>
                                <li><input type="checkbox" name="governance-artifacts" value="glossary_term" />Glossary
                                    Terms
                                </li>
                                <li><input type="checkbox" name="governance-artifacts" value="policy" />Policy
                                </li>
                                <li><input type="checkbox" name="governance-artifacts"
                                        value="reference_data" />Reference Data
                                </li>
                                <li><input type="checkbox" name="governance-artifacts" value="rule" />Rule</label>
                                </li>
                            </ul>
                        </div>
                        <p style="margin-top:1rem;"><b>Selected Artifacts: </b><span id="selected">all</span></p>
                    </div>
                    <br>
                    <div id="export-task">
                        <div class="content">
                            <p>Export Governance Artifacts</p>
                        </div>
                        <a class="button is-dark is-medium" title="Export Governance Artifacts"
                            href="didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$cd /projects/techzone-demo/sandbox/;python3.8 exportGovArtifacts.py governance_artifacts.zip all;unzip governance_artifacts.zip -d governance_artifacts;python3.8 exportDataProtectionRules.py data_protection_rules.json">Export
                            Artifacts</a>
                        <span class="dot"></span>
                    </div>
                </details>
            </div>
            <span class="dot"></span>
        </div>
        <div class="timeline" id="task3">
            <div class="content">
                <details>
                    <summary>Project management<span class="arrow"></span></summary>
                    <br><br>
                    <div>
                        <div class="content">
                            <p>Export project from the configured cp4d instance</p>
                        </div>
                        <a class="button is-dark is-medium" title="Export Project"
                            href="didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$cd /projects/techzone-demo/sandbox/;python3.8 exportProject.py project_assets.zip">Export
                            Project</a>
                        <span class="dot"></span>
                    </div>
                </details>
            </div>
            <span class="dot"></span>
        </div>
        <div class="timeline">
            <div class="content">
                <details>
                    <summary>Push to Github<span class="arrow"></span></summary>
                    <br><br>
                    <div class="content">
                        <!-- <p>Select the action to perform in the configured cp4d instance</p> -->
                        <div class="env-config">
                            <label>Demo Name*</label>
                            <input type="text" id="demoname">
                            <label>Industry*</label>
                            <!--<input type="text" id="industry">-->
                            <div id="industry-list" class="dropdown-check-list" tabindex="100">
                                <span id="selected-industry" class="anchor">Select Industry</span>
                                <ul class="items">
                                    <li>Banking and financial services</li>
                                    <li>E-commerce</li>
                                    <li>Healthcare</li>
                                    <li>Hospitality</li>
                                    <li>Insurance</li>
                                    <li>Retail</li>
                                    <li>Software</li>
                                    <li>Telecommunications</li>
                                    <li>Transportation</li>
                                    <li>Utilities</li>
                                    <li>Other</li>
                                    </select>
                                </ul>
                            </div>
                            <label>Tags(comma separated)*</label>
                            <input type="text" id="tags">
                            <label>Author*</label>
                            <input type="text" id="author">
                            <label>Description</label>
                            <input type="text" id="desc">
                            <label>Services*</label>
                            <!--<input type="text" id="services">-->
                            <div id="service-list" class="dropdown-check-list" tabindex="100">
                                <span class="anchor">Select Services</span>
                                <div class="items">
                                    <input id="services-search" type="search" placeholder="Search services"
                                        style="width: 100%" />
                                    <ul id="git-services">
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <p style="margin-top:1rem;"><b>Selected Services: </b><span id="selected-services"></span></p>
                    </div>
                    <button class="button is-dark is-medium no-click disable" title="Push to github" id="pushToGit">Push
                        to GitHub</button>
            </div>
            <span class="dot"></span>
        </div>
    </div>
    </div>
    <a id="command_exec" ,href=""></a>
    </div>
</body>
<script src="export-demo-artifacts.js"></script>

</html>