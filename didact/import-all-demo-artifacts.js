window.onload = function funLoad() {
  let env = document.getElementById("environment").textContent
  let compositeHref = "didact://?commandId=extension.compositeCommand&&text=terminal-for-sandbox-container:new%7Cvscode.didact.sendNamedTerminalAString%2Csandbox%20terminal%2Cgit%20clone%20-b%20$BRANCH%20https%3A%2F%2Fgithub.com%2FIBM%2FCPDemoFramework%20%24%7BCHE_PROJECTS_ROOT%7D%2Ftechzone-demo%2C%2Fprojects%7Cvscode.didact.sendNamedTerminalAString%2Csandbox%20terminal%2Cbash%20/projects/techzone-demo/sandbox/getDemoFiles.sh%20demo_name%7Cvscode.didact.sendNamedTerminalAString%2Csandbox%20terminal%2Ccd%20${CHE_PROJECTS_ROOT}/techzone-demo;pip3.8%20install%20-r%20requirements.txt%3Bcd%20%2Fprojects%2Ftechzone-demo%2Fsandbox%2F%3Bpython3.8%20update-env.py%20"
  compositeHref = compositeHref.replaceAll("$BRANCH",env)
  
  let prerequisite = ["hostname", "wkcuser", "password"]
  let didact = document.getElementsByClassName("apptitle")[0].textContent

  //Get Workspace ID and setup default data for localStorage
  let workspaceId = document.getElementById("workspaceID").textContent
  let data = {
    workspaceId: workspaceId,
    hostname: "",
    wkcuser: "",
    password: "",
    demo: ""
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


  //Disable timeline
  let localData = JSON.parse(localStorage[didact])
  let timelineContainer = document.getElementsByClassName("timeline-container")[0]
  if (localData.hostname.trim() === "" || localData.wkcuser.trim() === "" || localData.password.trim() === "") {
    timelineContainer.style.opacity = 0.5;
    timelineContainer.style.cursor = "not-allowed";
    [...timelineContainer.getElementsByTagName("A")].forEach(ele => ele.style.pointerEvents = "none");
    [...timelineContainer.getElementsByTagName("INPUT")].forEach(ele => ele.style.pointerEvents = "none");
    [...timelineContainer.getElementsByTagName("DETAILS")].forEach(ele => ele.style.pointerEvents = "none");
    let checkList = document.getElementById('list1');
    checkList.style.pointerEvents = "none";


  }

  //Store Config data
  let config = {
    hostname: localData.hostname,
    wkcuser: localData.wkcuser,
    password: localData.password,
  }
  let demo = localData.demo

  //modify cta with localStorage data
  let cta = document.getElementById("configure-env")
  cta.href = `${compositeHref.replace("demo_name", demo)}${Object.values(config).toString().replaceAll(",", "%20")}`

  if (demo.trim() !== "") {
    document.getElementById("selected").textContent = demo
    document.getElementById("import-project").href = `didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$cd /projects/techzone-demo/sandbox/;python3.8 importProject.py project_assets ${demo}`
  }


  //open/close demo dropdown
  let checkList = document.getElementById('list1');
  document.onclick = function (e) {
    if (e.target.parentElement !== checkList && e.target.name !== "governance-artifacts" && e.target.nodeName !== "LI") {
      checkList.classList.remove('visible');
    }
  };
  checkList.getElementsByClassName('anchor')[0].onclick = function (evt) {
    if (checkList.classList.contains('visible'))
      checkList.classList.remove('visible');
    else
      checkList.classList.add('visible');
  }

  //modify cta with selected demo value
  let options = checkList.getElementsByTagName('LI');
  [...options].forEach(option => option.addEventListener("click", selectOption))
  function selectOption(e) {
    document.getElementById("selected").textContent = e.target.textContent
    demo = e.target.textContent
    cta.href = `${compositeHref.replace("demo_name", e.target.textContent)}${Object.values(config).toString().replaceAll(",", "%20")}`
    document.getElementById("import-project").href = `didact://?commandId=vscode.didact.sendNamedTerminalAString&&text=sandbox terminal$$cd /projects/techzone-demo/sandbox/;python3.8 importProject.py project_assets ${e.target.textContent}`
    checkList.classList.remove('visible');
    let tempData = JSON.parse(localStorage[didact])
    tempData["demo"] = e.target.textContent
    localStorage[didact] = JSON.stringify(tempData)
  }

  //get env values
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
    cta.href = `${compositeHref.replace("demo_name", demo)}${Object.values(config).toString().replaceAll(",", "%20")}`
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
      let checkList = document.getElementById('list1');
      checkList.style.pointerEvents = "auto";
    } else {
      timelineContainer.style.opacity = 0.5;
      timelineContainer.style.cursor = "not-allowed";
      [...timelineContainer.getElementsByTagName("A")].forEach(ele => ele.style.pointerEvents = "none");
      [...timelineContainer.getElementsByTagName("INPUT")].forEach(ele => ele.style.pointerEvents = "none");
      [...timelineContainer.getElementsByTagName("DETAILS")].forEach(ele => ele.style.pointerEvents = "none");
      let checkList = document.getElementById('list1');
      checkList.style.pointerEvents = "none";
    }
  }
}
