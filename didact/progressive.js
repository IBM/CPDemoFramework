window.onload = function () {
    //CTAs to unlock together
    let ctaPairs = {
        "git-clone": ["explore-application"],
        "launch-application-wca": ["stop-application"],
        "create-services-ibmcloud": ["create-deploy-model"],
        "create-deployment-space": ["deploy-model", "error-ctas"],
        "create-deploy-model": ["create-cloud-function"],
        "create-cloud-function": ["create-assistant"],
        "create-assistant": ["configure-application-ctas"],
        "configure-application-ctas": ["launch-application"]
    }

    //Get name of the didact
    let didact = document.getElementsByClassName("apptitle")[0].textContent

    //Get Workspace ID and setup default data for localStorage
    let workspaceId = document.getElementsByClassName("hidden-state")[0].textContent
    let data = {
        workspaceId: workspaceId,
        ctasClicked: null
    }

    //Create localStorage item if didact name not present 
    if (localStorage[didact] === undefined) {
        localStorage[didact] = JSON.stringify(data)
    }

    //Reset localStorage to default data if workspace is changed
    if (JSON.parse(localStorage[didact]).workspaceId !== workspaceId) {
        localStorage[didact] = JSON.stringify(data)
    }

    //Get all timeline CTAs in the didact
    let steps = document.getElementsByClassName("step");

    //Activate the first CTA
    activate(steps[0])
    let completedCTAs = null;

    //Get current progress and enable those CTAs
    try {
        completedCTAs = JSON.parse(localStorage[didact]).ctasClicked;
        try {
            for (let i = 0; i < completedCTAs.length; i++) {
                enableCTA(Number(completedCTAs[i]))
            }
        } catch (e) {
            //Do Nothing
        }
    } catch {
        completedCTAs = null
    }

    //Add click event to CTAs
    for (let i = 0; i < steps.length; i++) {
        let anchor_tags = steps[i].getElementsByTagName("A")
        for (let j = 0; j < anchor_tags.length; j++) {
            if (anchor_tags[j].className.includes("button is-dark is-medium")) {
                anchor_tags[j].addEventListener("click", enableCTA)
            }
        }
    }

    //Get the index of CTA clicked
    function getNodeIndex(step) {
        let steps = document.getElementsByClassName("step");
        for (let i = 0; i < steps.length; i++) {
            if (steps[i].isSameNode(step))
                return i
        }
    }

    //Function to enable CTA
    function enableCTA(step) {
        //Get index of current CTA clicked and save it in localStorage
        let currentStep = 0
        if (isNaN(step)) {
            currentStep = getNodeIndex(step.target.parentElement)
            try {
                completedCTAs.push(currentStep)
            }
            catch {
                completedCTAs = [0]
            }
            let tempData = JSON.parse(localStorage[didact])
            tempData.ctasClicked = completedCTAs
            localStorage[didact] = JSON.stringify(tempData)
        } else {
            currentStep = step
        }
        //Check is any other CTAs needs to be unlocked on this particular CTA
        for (cta of Object.keys(ctaPairs)) {
            if (steps[currentStep].classList.contains(cta)) {
                for (let ctaPair of ctaPairs[cta]) {
                    try {
                        let pair = document.getElementsByClassName(ctaPair)[0];
                        activate(pair)
                    } catch {
                        //Do Nothing
                    }
                }
            }
        }
        //Add the checkmark icon to current CTA
        let checkbox = steps[currentStep].getElementsByTagName("INPUT")[0]
        checkbox.checked = true;
        //Enablke the next CTA
        if (currentStep + 1 != steps.length){
            activate(steps[currentStep + 1])
            steps[currentStep + 1].scrollIntoView({ block: "center" })
        }
        else {
            //if last CTA of timeline unlock the footer CTAs
            let footer = document.getElementsByClassName("footer-step")
            for (let i = 0; i < footer.length; i++) {
                activate(footer[i])
            }
        }

        //Add checkmark icon to dropdown if last CTA of dropdown clicked
        try {
            let parent = steps[currentStep].parentElement
            console.log(parent.tagName)
            if (parent.tagName === "DETAILS") {
                let dropdownSteps = parent.getElementsByClassName("step");
                if (dropdownSteps[dropdownSteps.length - 1] === steps[currentStep]) {
                    parent.parentElement.nextSibling.nextSibling.checked = true
                    parent.parentElement.nextSibling.nextSibling.nextSibling.nextSibling.classList.add("show-dot")
                    parent.removeAttribute("open");
                    parent.scrollIntoView({ block: "center" });
                }
            }
        } catch {
            //Do Nothing
        }
    }


    //Add required css to activate the CTAs
    function activate(step) {
        let anchor_tags = step.getElementsByTagName("A")
        try {
            let dot = step.getElementsByClassName("dot")[0]
            dot.classList.add("show-dot")
        } catch (e) {
            //Do Nothing
        }
        step.classList.add("enable");
        step.classList.add("allow-click")
        for (let i = 0; i < anchor_tags.length; i++) {
            anchor_tags[i].classList.add("allow-click")
            if (anchor_tags[i].className.includes("button is-dark is-medium") && i !== anchor_tags.length - 2)
                break
        }
    }
}