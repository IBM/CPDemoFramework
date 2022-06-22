window.onload = function funLoad() {

  let env = document.getElementById("environment").textContent
  let compositeHref = "didact://?commandId=extension.compositeCommand&&text=terminal-for-sandbox-container:new%7Cvscode.didact.sendNamedTerminalAString%2Csandbox%20terminal%2Cgit%20clone%20-b%20$BRANCH%20https%3A%2F%2Fgithub.com%2FIBM%2FCPDemoFramework%20%24%7BCHE_PROJECTS_ROOT%7D%2Ftechzone-demo%2C%2Fprojects%7Cvscode.didact.sendNamedTerminalAString%2Csandbox%20terminal%2Ccd%20${CHE_PROJECTS_ROOT}/techzone-demo;pip3.8%20install%20-r%20requirements.txt%3Bcd%20%2Fprojects%2Ftechzone-demo%2Fsandbox%2F%3Bpython3.8%20update-env.py%20"
  compositeHref = compositeHref.replaceAll("$BRANCH",env)

  let prerequisite = ["hostname", "wkcuser", "password"]
  let pushToGitRequiredFields = ["demoname","tags","author","desc"]
  requiredVals={
    demoname:"",
    tags:"",
    author:"",
    desc: "",
  }
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

  let industries = [
    { id: 'hospitality', value: 'Hospitality' },
    { id: 'healthcare', value: 'Healthcare' },
    { id: 'e-commerce', value: 'E-commerce' },
    { id: 'banking', value: 'Banking and financial services' },
    { id: 'insurance', value: 'Insurance' },
    { id: 'retail', value: 'Retail' },
    { id: 'software', value: 'Software' },
    { id: 'telecommunications', value: 'Telecommunications' },
    { id: 'transportation', value: 'Transportation' },
    { id: 'utilities', value: 'Utilities' },
    { id: 'other', value: 'Other' }
  ]

  function getIndustry(industry){
    return industries.find(({id, value}) => value===industry).id
    }

  let selectedServices = []
  let selecetdIndustry = ""
  let didact = document.getElementsByClassName("apptitle")[0].textContent

  //Get Workspace ID and setup default data for localStorage
  let workspaceId = document.getElementById("workspaceID").textContent
  let data = {
    workspaceId: workspaceId,
    hostname: "",
    wkcuser: "",
    password: "",
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

  // .push related code
  document.getElementById("pushToGit").addEventListener("click", pushToGit);
  function pushToGit() {
    let industry = selecetdIndustry//document.getElementById("industry").value || ""
    let tags = document.getElementById("tags").value || ""
    let author = document.getElementById("author").value || ""
    let services = selectedServices.toString()//document.getElementById("services").value
    let demoName = document.getElementById("demoname").value || ""
    let desc = document.getElementById("desc").value || "Update"
    let userID=document.getElementById("userID").textContent || author
    tags = tags.split(",")
    services = services.split(",")
    industry = industry.split(",")
    // JSON ARRAY
    let metadata = {
      "industries": industry,
      "tags": tags,
      "author": author,
      "services": services,
      "demoName": userID.replace(/ /g,'')+"-"+demoName.replace(/ /g,''),
      "displayName":demoName,
      "desc": desc
    }
    // let metadata=`{"industry":"${industry}","tags":"${["tags","asddsa","dsa"]}","author":"${author}","services":"${services}","demoName":"${demoName}"}`
    metadata = '\'' + JSON.stringify(metadata) + '\''
    document.getElementById("command_exec").href =
      "didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$bash /projects/techzone-demo/sandbox/github.sh " + "\""+demoName.replace(/ /g,'')+ "\""+" " + metadata + " " + "\""+ userID.replace(/ /g,'')+ "\""+ " "+ "\""+desc+ "\"";

    document.getElementById("command_exec").click();

  }

  //Enable/Disable timeline
  let localData = JSON.parse(localStorage[didact])
  let timelineContainer = document.getElementsByClassName("timeline-container")[0]
  if (localData.hostname.trim() === "" || localData.wkcuser.trim() === "" || localData.password.trim() === "") {
    timelineContainer.style.opacity = 0.5;
    timelineContainer.style.cursor = "not-allowed";
    [...timelineContainer.getElementsByTagName("A")].forEach(ele => ele.style.pointerEvents = "none");
    [...timelineContainer.getElementsByTagName("INPUT")].forEach(ele => ele.style.pointerEvents = "none");
    [...timelineContainer.getElementsByTagName("DETAILS")].forEach(ele => ele.style.pointerEvents = "none");
  }

  //default data
  let config = {
    hostname: localData.hostname,
    wkcuser: localData.wkcuser,
    password: localData.password,
  }

  //Modify configure-env with localstorage values
  let cta = document.getElementById("configure-env")
  cta.href = `${compositeHref}${Object.values(config).toString().replaceAll(",", "%20")}`


  //open/close industry dropdown
  let industryList = document.getElementById('industry-list');
  industryList.getElementsByClassName('anchor')[0].onclick = function (evt) {
    if (industryList.classList.contains('visible'))
      industryList.classList.remove('visible');
    else
      industryList.classList.add('visible');
  }

  //modify cta with selected industry value
  let options = industryList.getElementsByTagName('LI');
  [...options].forEach(option => option.addEventListener("click", selectOption))
  function selectOption(e) {
    document.getElementById("selected-industry").textContent = e.target.textContent
    selecetdIndustry = getIndustry(e.target.textContent);
    industryList.classList.remove('visible');
    let cta = document.getElementById("pushToGit")
    if(Object.values(requiredVals).map(val => val.trim()).includes("") || selectedServices.length === 0 || selecetdIndustry.trim() === ""){
      cta.classList.remove("enable")
      cta.classList.add("disable")
      cta.classList.remove("allow-click")
      cta.classList.add("no-click")
    }else{
      cta.classList.remove("disable")
      cta.classList.add("enable")
      cta.classList.remove("no-click")
      cta.classList.add("allow-click")
    }
  }

  //open/close gov-artifacts dropdown
  let checkList = document.getElementById('list1');
  checkList.getElementsByClassName('anchor')[0].onclick = function (evt) {
    if (checkList.classList.contains('visible'))
      checkList.classList.remove('visible');
    else
      checkList.classList.add('visible');
  }

  //Get env values
  let envVariables = document.getElementsByClassName('env-variables');
  [...envVariables].forEach((task) => {
    task.addEventListener("input", getEnvValues)
  });

  function getEnvValues(e) {
    if (e.target.name === "hostname") {
      e.target.value = e.target.value.replace(/(^\w+:|^)\/\//, '');
    }
    config[e.target.name] = e.target.value
    let cta = document.getElementById("configure-env")
    cta.href = `${compositeHref}${Object.values(config).toString().replaceAll(",", "%20")}`
    let tempData = JSON.parse(localStorage[didact])
    tempData[e.target.name] = e.target.value
    localStorage[didact] = JSON.stringify(tempData)
    valid = true
    for (val of Object.values(config)) {
      if (val.trim() === "")
        valid = false
    }
    if (valid) {
      timelineContainer.style.opacity = 1;
      timelineContainer.style.cursor = "auto";
      [...timelineContainer.getElementsByTagName("A")].forEach(ele => ele.style.pointerEvents = "auto");
      [...timelineContainer.getElementsByTagName("INPUT")].forEach(ele => ele.style.pointerEvents = "auto");
      [...timelineContainer.getElementsByTagName("DETAILS")].forEach(ele => ele.style.pointerEvents = "auto");
    } else {
      timelineContainer.style.opacity = 0.5;
      timelineContainer.style.cursor = "not-allowed";
      [...timelineContainer.getElementsByTagName("A")].forEach(ele => ele.style.pointerEvents = "none");
      [...timelineContainer.getElementsByTagName("INPUT")].forEach(ele => ele.style.pointerEvents = "none");
      [...timelineContainer.getElementsByTagName("DETAILS")].forEach(ele => ele.style.pointerEvents = "none");
    }
  }


  //enable managemnet dropdowns
  let tasks = document.querySelectorAll("[id^='task']");
  tasks.forEach((task) => (task.style.display = "none"));

  let selectedTasks = document.getElementsByName("checkboxtask");
  selectedTasks.forEach((task) => task.addEventListener("click", showTasks));
  function showTasks(e) {

    if (e.target.checked) {
      document.getElementById(e.target.value).style.display = "block";
    } else {
      document.getElementById(e.target.value).style.display = "none";
    }
  }


  //Get selected values
  let govArtifacts = document.getElementsByName("governance-artifacts");
  govArtifacts.forEach((task) => task.addEventListener("click", UpdateExport));
  let selectedArtifacts = ["all"]
  function UpdateExport(e) {
    /*if(e.target.value==="select-all") {
      if(e.target.checked ===true){ 
      govArtifacts.forEach((task) => {
        if(task.value!=="select-all"){
          selectedArtifacts.push(task.value);
          task.checked = true
        }
      }) }
      else{
        govArtifacts.forEach((task) => {
            task.checked = false
          })
       selectedArtifacts = []
      }
    }*/
    if (e.target.checked) {
      selectedArtifacts.push(e.target.value)
    } else {
      selectedArtifacts.indexOf(e.target.value) !== -1 && selectedArtifacts.splice(selectedArtifacts.indexOf(e.target.value), 1)
    }
    let task = document.getElementById("export-task")
    let cta = task.getElementsByTagName("A")[0]
    if (selectedArtifacts.length === 0) {
      task.classList.remove("enable")
      task.classList.add("disable")
      cta.classList.remove("allow-click")
      cta.classList.add("no-click")
    } else {
      task.classList.remove("disable")
      task.classList.add("enable")
      cta.classList.remove("no-click")
      cta.classList.add("allow-click")
    }
    cta.href = `didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$cd /projects/techzone-demo/sandbox/;python3.8 exportGovArtifacts.py governance_artifacts.zip ${selectedArtifacts.toString()};unzip governance_artifacts.zip -d governance_artifacts`
    if (selectedArtifacts.indexOf("rule") >= 0 || selectedArtifacts.indexOf("all") >= 0) {
      cta.href = cta.href + ";python3.8 exportDataProtectionRules.py data_protection_rules.json"
    }
    let showSeleted = document.getElementById("selected")
    showSeleted.textContent = selectedArtifacts.toString().replaceAll(",", ", ")
  }

  //Open Close services dropdowns
  let serviceList = document.getElementById('service-list');
  serviceList.getElementsByClassName('anchor')[0].onclick = function (evt) {
    if (serviceList.classList.contains('visible'))
      serviceList.classList.remove('visible');
    else
      serviceList.classList.add('visible');
  }
  // Populate the dropdown
  let gitServicesList = document.getElementById("git-services");
  Object.keys(services).forEach(id => {
    let li = document.createElement("li");
    let input = document.createElement("input");
    input.setAttribute("value", id)
    input.setAttribute("name", "services")
    input.setAttribute("type", "checkbox")
    li.appendChild(input)
    li.appendChild(document.createTextNode(services[id]));
    gitServicesList.appendChild(li);
  })

  //Get selected values
  let gitServices = document.getElementsByName("services");
  gitServices.forEach((task) => task.addEventListener("click", updateSelectedServices));
  function updateSelectedServices(e) {
    if (e.target.checked) {
      selectedServices.push(e.target.value)
      gitServicesList.insertBefore(e.target.parentElement, gitServicesList.firstChild);
    } else {
      selectedServices.indexOf(e.target.value) !== -1 && selectedServices.splice(selectedServices.indexOf(e.target.value), 1)
      gitServicesList.insertBefore(e.target.parentElement, gitServices[Object.keys(services).indexOf(e.target.value)].parentElement);

    }
    let showSeleted = document.getElementById("selected-services")
    showSeleted.textContent = selectedServices.toString().replaceAll(",", ", ")
    let cta = document.getElementById("pushToGit")
    if(Object.values(requiredVals).map(val => val.trim()).includes("") || selectedServices.length === 0 || selecetdIndustry.trim() === ""){
      cta.classList.remove("enable")
      cta.classList.add("disable")
      cta.classList.remove("allow-click")
      cta.classList.add("no-click")
    }else{
      cta.classList.remove("disable")
      cta.classList.add("enable")
      cta.classList.remove("no-click")
      cta.classList.add("allow-click")
    }
  }

  //Search in dropdown
  let searchItem = document.getElementById("services-search")
  searchItem.addEventListener("input", filterServiceList)

  function filterServiceList(e) {
    let filteredServices = {}
    let htmlServices = document.getElementsByName("services")
    let listServices = [...htmlServices].map(service => service.value)
    listServices.forEach((res, idx) => {
      if (res.toLowerCase().includes(e.target.value.toLowerCase()) || services[res].toLowerCase().includes(e.target.value.toLowerCase())) {
        filteredServices[res] = services[res]
        htmlServices[idx].parentElement.style.display = "block"
      } else {
        htmlServices[idx].parentElement.style.display = "none"
      }
    })
  }


  //close dropdowns when clicked outside
  document.onclick = function (e) {
    if (e.target.parentElement !== industryList && e.target.parentElement !== checkList && e.target.name !== "governance-artifacts" && e.target.parentElement !== serviceList && e.target.name !== "services" && e.target.nodeName !== "LI" && e.target.nodeName !== "INPUT") {
      serviceList.classList.remove('visible');
      checkList.classList.remove('visible');
      industryList.classList.remove('visible');
    }
  };

  //Enable/Disable PushToGit CTA
  pushToGitRequiredFields.forEach(id => document.getElementById(id).addEventListener("input", setPushToGitCTA))

  function setPushToGitCTA(e) {
    requiredVals[e.target.id] = e.target.value
    let cta = document.getElementById("pushToGit")
    if(Object.values(requiredVals).map(val => val.trim()).includes("") || selectedServices.length === 0 || selecetdIndustry.trim() === ""){
      cta.classList.remove("enable")
      cta.classList.add("disable")
      cta.classList.remove("allow-click")
      cta.classList.add("no-click")
    }else{
      cta.classList.remove("disable")
      cta.classList.add("enable")
      cta.classList.remove("no-click")
      cta.classList.add("allow-click")
    }
  }

};
