window.onload = function () {
  let env = document.getElementById("environment").textContent
  let compositeHref = "didact://?commandId=extension.compositeCommand&&text=terminal-for-sandbox-container:new%7Cvscode.didact.sendNamedTerminalAString%2Csandbox%20terminal%2Cgit clone https://github.com/IBM/CPDemoFramework -b $BRANCH --single-branch techzone;cd%20${CHE_PROJECTS_ROOT}/techzone/olm-utils;python3.8%20update-env-vars.py%20"
  compositeHref = compositeHref.replaceAll("$BRANCH",env)

  let prerequisite = ["server", "api_token", "kubeadmin_user", "kubeadmin_pass"]
  let services = {
    analyticsengine: 'Analytics Engine Powered by Apache Spark',
    bigsql: 'Db2 Big SQL',
    cde: 'Cognos Dashboards',
    cognos_analytics: 'Cognos Analytics',
    cpd_platform: 'Cloud Pak for Data Control Plane',
    cpfs: 'Cloud Pak Foundational Services(CPFS)',
    datagate: 'Data Gate',
    datarefinery: 'Data Refinery',
    datastage_ent: 'DataStage Enterprise',
    datastage_ent_plus: 'DataStage Enterprise Plus',
    db2aaservice: 'CPD db2 aas component',
    db2oltp: 'Db2',
    db2u: 'IBM Db2u',
    db2wh: 'Db2 Warehouse',
    dmc: 'Data Management Console',
    dods: 'Decision Optimization',
    dp: 'Data Privacy',
    dv: 'Data Virtualization',
    edb_cp4d: 'EnterpriseDB Postgres',
    hee: 'Execution Engine for Apache Hadoop',
    iis: "WKC's IIS component",
    informix: 'Informix install Operator',
    informix_cp4d: 'Informix deployment Operator',
    match360: 'Match 360 with Watson',
    model_train: 'IBM cloudpak operator for training with Model Train',
    mongodb: 'MongoDB Operator',
    mongodb_cp4d: 'MongoDB for Cloud Pak for Data',
    openpages: 'OpenPages',
    openpages_instance: 'OpenPages Instance',
    openscale: 'Watson OpenScale',
    planning_analytics: 'Planning Analytics',
    postgresql: 'Cloud Native PostgreSQL',
    productmaster: 'Product Master',
    productmaster_instance: 'Product Master Instance',
    rstudio: 'RStudio Server',
    scheduler: 'CPD Scheduler',
    spss: 'SPSS Modeler',
    voice_gateway: 'Voice Gateway',
    watson_assistant: 'Watson Assistant',
    watson_discovery: 'Watson Discovery',
    watson_gateway: 'IBM Watson Gateway Operator',
    watson_ks: 'Watson Knowledge Studio',
    watson_speech: 'Watson Speech to Text',
    wkc: 'Watson Knowledge Catalog',
    wml: 'Watson Machine Learning',
    wml_accelerator: 'Watson Machine Learning Accelerator',
    ws: 'Watson Studio',
    ws_pipelines: 'Watson Studio Pipelines',
    ws_runtimes: 'Watson Studio Runtimes',
    zen: 'Zen Service in CPFS'
  }
  let selectedServices = []
  let olmSelectedServices = []

  let didact = document.getElementsByClassName("apptitle")[0].textContent

  //Get Workspace ID and setup default data for localStorage
  let workspaceId = document.getElementById("workspaceID").textContent
  let data = {
    workspaceId: workspaceId,
    server: "",
    api_token: "",
    kubeadmin_user: "",
    kubeadmin_pass: "",
  }

  //Create localStorage item if didact name not present 
  if (localStorage[didact] === undefined) {
    localStorage[didact] = JSON.stringify(data)
  }

  //Reset localStorage to default data if workspace is changed
  if (JSON.parse(localStorage[didact]).workspaceId !== workspaceId) {
    localStorage[didact] = JSON.stringify(data)
  }

  //Fill input data from localStorage
  prerequisite.forEach(input => document.getElementsByName(input)[0].value = JSON.parse(localStorage[didact])[input])

  //Enable/Disable timeline
  let localData = JSON.parse(localStorage[didact])
  let timelineContainer = document.getElementsByClassName("timeline-container")[0]
  if ((localData.server.trim() === "" || localData.api_token.trim() === "" ) && (localData.kubeadmin_user.trim() === "" || localData.kubeadmin_pass.trim() === "")) {
    timelineContainer.style.opacity = 0.5;
    timelineContainer.style.cursor = "not-allowed";
    [...timelineContainer.getElementsByTagName("A")].forEach(ele => ele.style.pointerEvents = "none");
    [...timelineContainer.getElementsByTagName("INPUT")].forEach(ele => ele.style.pointerEvents = "none");
    [...timelineContainer.getElementsByTagName("DETAILS")].forEach(ele => ele.style.pointerEvents = "none");
    [...timelineContainer.getElementsByTagName("DIV")].forEach(ele => ele.style.pointerEvents = "none");
  }

  //default data
  let config = {
    server: localData.server,
    api_token: localData.api_token,
    kubeadmin_user: localData.kubeadmin_user,
    kubeadmin_pass: localData.kubeadmin_pass,
  }
  //Get env values
  let envVariables = document.getElementsByClassName('env-variables');
  [...envVariables].forEach((task) => {
    task.addEventListener("input", getEnvValues)
  });

  function getEnvValues(e) {
    console.log(e.target.name, e.target.value)
    config[e.target.name] = e.target.value
    let cta = document.getElementById("configure-env")
    cta.href = `${compositeHref}${Object.keys(config).map(val => `${val.toUpperCase()}=${config[val]}`).toString().replaceAll(",","%20")}`
    let tempData = JSON.parse(localStorage[didact])
    tempData[e.target.name] = e.target.value
    localStorage[didact] = JSON.stringify(tempData)
    let valid = true
    if((config.server.trim() === "" || config.api_token.trim() === "") && (config.kubeadmin_user.trim() === "" || config.kubeadmin_pass.trim() === ""))
      valid = false
    if (valid) {
      timelineContainer.style.opacity = 1;
      timelineContainer.style.cursor = "auto";
      [...timelineContainer.getElementsByTagName("A")].forEach(ele => ele.style.pointerEvents = "auto");
      [...timelineContainer.getElementsByTagName("INPUT")].forEach(ele => ele.style.pointerEvents = "auto");
      [...timelineContainer.getElementsByTagName("DETAILS")].forEach(ele => ele.style.pointerEvents = "auto");
      [...timelineContainer.getElementsByTagName("DIV")].forEach(ele => ele.style.pointerEvents = "auto");
    } else {
      timelineContainer.style.opacity = 0.5;
      timelineContainer.style.cursor = "not-allowed";
      [...timelineContainer.getElementsByTagName("A")].forEach(ele => ele.style.pointerEvents = "none");
      [...timelineContainer.getElementsByTagName("INPUT")].forEach(ele => ele.style.pointerEvents = "none");
      [...timelineContainer.getElementsByTagName("DETAILS")].forEach(ele => ele.style.pointerEvents = "none");
      [...timelineContainer.getElementsByTagName("DIV")].forEach(ele => ele.style.pointerEvents = "none");
    }
  }


  document.getElementById("existing_service").addEventListener("click", existing_service);

  function existing_service() {
    let artifacts = document.getElementById("cpd_instance_value").value;
    //samplevalue cpd-inst-01
    document.getElementById("command_exec").href =
      "didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$run_utils get-cr-status --cpd_instance_ns=" + artifacts;
    document.getElementById("command_exec").click();
  }

  document.getElementById("install_olm").addEventListener("click", install_olm);

  function install_olm() {
    let component_list = olmSelectedServices.toString()
    let release_version = document.getElementById("olm_release_version").value;
    let preview_value = document.getElementById('olm_preview_value').value;
    document.getElementById("command_exec").href =
      "didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$run_utils apply-olm --preview=" +
      preview_value +
      " --release=" +
      release_version +
      " --components=" +
      component_list;
    document.getElementById("command_exec").click();
  }

  document.getElementById("install_cr").addEventListener("click", install_cr);

  function install_cr() {
    let component_list = selectedServices.toString()
    let release_version = document.getElementById("cr_release_version").value;
    let preview_value = document.getElementById('cr_preview_value').value;
    select = document.getElementById('cr_license_acceptance');
    let license_acceptance = select.options[select.selectedIndex].text;
    let cr_cpd_instance = document.getElementById("cr_cpd_instance").value;
    let cr_storage_class = document.getElementById("cr_storage_class").value;
    let cr_storage_value = document.getElementById("cr_storage_value").value;
    let storage = ""
    if (cr_storage_class === "storage_class") {
      storage = " --storage_class=" + cr_storage_value
    } else {
      storage = " --storage_vendor=" + cr_storage_value
    }

    document.getElementById("command_exec").href =
      "didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$run_utils apply-cr --preview=" +
      preview_value +
      " --release=" +
      release_version +
      " --components=" +
      component_list +
      " --license_acceptance=" +
      license_acceptance +
      " --cpd_instance_ns=" +
      cr_cpd_instance +
      storage;
    document.getElementById("command_exec").click();
  }
  // Preview logic
  document.getElementById("get_preview").addEventListener("click", get_preview);
  document.getElementById("get_preview_2").addEventListener("click", get_preview);
  function get_preview() {
    document.getElementById("command_exec").href =
      "didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$get_preview"
    document.getElementById("command_exec").click();
    document.getElementById("command_exec").href =
      "didact://?commandId=vscode.open&projectFilePath=/projects/techzone-demo/olm-utils/preview.sh"
    document.getElementById("command_exec").click();
  }


  // Get the dropdown elements
  let olmServiceList = document.getElementById('olm-service-list');
  let serviceList = document.getElementById('cr-service-list');

  //Open close dropdowns
  document.onclick = function (e) {
    if (e.target.parentElement !== olmServiceList && e.target.name !== "olm-services" && e.target.parentElement !== serviceList && e.target.name !== "cr-services" && e.target.nodeName !== "LI" && e.target.nodeName !== "INPUT") {
      serviceList.classList.remove('visible');
      olmServiceList.classList.remove('visible');
    }
  };
  serviceList.getElementsByClassName('anchor')[0].onclick = function (evt) {
    if (serviceList.classList.contains('visible'))
      serviceList.classList.remove('visible');
    else
      serviceList.classList.add('visible');
  }
  olmServiceList.getElementsByClassName('anchor')[0].onclick = function (evt) {
    if (olmServiceList.classList.contains('visible'))
      olmServiceList.classList.remove('visible');
    else
      olmServiceList.classList.add('visible');
  }

  //populate the respective dropdown lists
  let olmServicesList = document.getElementById("olm-git-services");
  let gitServicesList = document.getElementById("cr-git-services");
  Object.keys(services).forEach(id => {
    let li = document.createElement("li");
    let input = document.createElement("input");
    input.setAttribute("value", id)
    input.setAttribute("name", "cr-services")
    input.setAttribute("type", "checkbox")
    li.appendChild(input)
    li.appendChild(document.createTextNode(services[id]));
    gitServicesList.appendChild(li);
    li = document.createElement("li");
    input = document.createElement("input");
    input.setAttribute("value", id)
    input.setAttribute("name", "olm-services")
    input.setAttribute("type", "checkbox")
    li.appendChild(input)
    li.appendChild(document.createTextNode(services[id]));
    olmServicesList.appendChild(li);

  })

  //Get selected values
  let gitServices = document.getElementsByName("cr-services");
  let olmServices = document.getElementsByName("olm-services");
  gitServices.forEach((task) => task.addEventListener("click", updateSelectedServices));
  olmServices.forEach((task) => task.addEventListener("click", updateOlmSelectedServices));

  function updateSelectedServices(e) {
    if (e.target.checked) {
      selectedServices.push(e.target.value)
      gitServicesList.insertBefore(e.target.parentElement, gitServicesList.firstChild);
    } else {
      selectedServices.indexOf(e.target.value) !== -1 && selectedServices.splice(selectedServices.indexOf(e.target.value), 1)
      gitServicesList.insertBefore(e.target.parentElement, gitServices[Object.keys(services).indexOf(e.target.value)].parentElement);

    }
    let showSeleted = document.getElementById("cr-selected-services")
    showSeleted.textContent = selectedServices.toString().replaceAll(",", ", ")
  }

  function updateOlmSelectedServices(e) {
    if (e.target.checked) {
      olmSelectedServices.push(e.target.value)
      olmServicesList.insertBefore(e.target.parentElement, olmServicesList.firstChild);
    } else {
      olmSelectedServices.indexOf(e.target.value) !== -1 && olmSelectedServices.splice(olmSelectedServices.indexOf(e.target.value), 1)
      olmServicesList.insertBefore(e.target.parentElement, olmServices[Object.keys(services).indexOf(e.target.value)].parentElement);

    }
    let showSeleted = document.getElementById("olm-selected-services")
    showSeleted.textContent = olmSelectedServices.toString().replaceAll(",", ", ")
  }


  //Search in the dropdown
  let searchItem = document.getElementById("cr-services-search")
  searchItem.addEventListener("input", filterServiceList)
  let olmSearchItem = document.getElementById("olm-services-search")
  olmSearchItem.addEventListener("input", filterServiceList)

  function filterServiceList(e) {
    let currServices = []
    if (e.target.id === "cr-services-search") {
      currServices = gitServices
    } else {
      currServices = olmServices
    }
    let listServices = [...currServices].map(service => service.value)
    listServices.forEach((res, idx) => {
      if (res.toLowerCase().includes(e.target.value.toLowerCase()) || services[res].toLowerCase().includes(e.target.value.toLowerCase())) {
        currServices[idx].parentElement.style.display = "block"
      } else {
        currServices[idx].parentElement.style.display = "none"
      }
    })
  }
};
