#!/bin/bash  
demo_name=$1
private_git_token=$2
project_name=ibmtechzone-demo-artifacts 
branch="main"
if [[ $PLAYGROUND_ENVIRONMENT == *"development"* ]]; then
      branch="development" 
fi
if [[ $PLAYGROUND_ENVIRONMENT == *"staging"* ]]; then
      branch="staging" 
fi
if [[ $PLAYGROUND_ENVIRONMENT == *"techzone"* ]]; then
      branch="techzone" 
fi
github_url=https://github.com/IBM/ibmtechzone-demo-artifacts
cd /projects/techzone-demo/sandbox
rm -rf /projects/techzone-demo/sandbox/$project_name
git clone --single-branch --branch $branch --sparse $github_url 
cd /projects/techzone-demo/sandbox/$project_name
git sparse-checkout set $demo_name
# cd /projects/techzone-demo/sandbox/

if [ -d "$demo_name" ]; then
  # Control will enter here if $DIRECTORY doesn't exist.
    echo "$demo_name DemoName Found!"
    cp -a /projects/techzone-demo/sandbox/$project_name/$demo_name/. /projects/techzone-demo/sandbox/
    rm -rf /projects/techzone-demo/sandbox/$project_name
    echo "Demo loaded successfully!"

    isPrivate=`cat /projects/techzone-demo/sandbox/readme.json | jq '.isPrivate'`
    if [ $isPrivate = "true" ]; then
      echo "This is a private demo. Lets retrieve the demo files from the private github repo"
      privateGitRepoUrl=`cat /projects/techzone-demo/sandbox/readme.json | jq '.privateGitRepoUrl'`
      cd /projects/techzone-demo/sandbox

      #if privateGitRepoUrl starts with a " remove it. 
      if [ ${privateGitRepoUrl:0:1}='"' ]; then
        privateGitRepoUrl="${privateGitRepoUrl:1:-1}"
      fi

      #If the git token is provided, lets add it to the git url. 
      if [ "$private_git_token" ]; then
        private_github_url="${private_github_url:0:8}$private_git_token@${private_github_url:8}"
      fi
      git clone --sparse $privateGitRepoUrl $project_name
      cd /projects/techzone-demo/sandbox/$project_name
      git sparse-checkout set $demo_name
      if [ -d "$demo_name" ]; then
        cp -a /projects/techzone-demo/sandbox/$project_name/$demo_name/* /projects/techzone-demo/sandbox/
        rm -rf /projects/techzone-demo/sandbox/$project_name
      else
        echo "Private Demo not found"
      fi
    fi
    exit 2
fi
echo "DemoName Not Found!"
echo "File loading failed!"
rm -rf /projects/techzone-demo/sandbox/$project_name