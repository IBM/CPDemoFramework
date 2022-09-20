#!/bin/bash  
demo_name=$1
isPrivate=$2
privateGitRepoUrl=$3
privateGitToken=$4
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

cd /projects/techzone-demo/sandbox
rm -rf /projects/techzone-demo/sandbox/$project_name

if [ $isPrivate == "true" ]; then
  echo "This is a private demo. Lets retrieve the demo files from the private github repo"

  #If the git token is provided, lets add it to the git url and clone. 
  if [ "$privateGitToken" ]; then
    privateGitRepoUrl="${privateGitRepoUrl:0:8}$privateGitToken@${privateGitRepoUrl:8}"
    git clone --sparse $privateGitRepoUrl $project_name
    cd /projects/techzone-demo/sandbox/$project_name
    git sparse-checkout set $demo_name
  fi
else 
  github_url=https://github.com/IBM/ibmtechzone-demo-artifacts
  echo "This is a public demo. Lets retrieve the demo files from the public github repo"
  git clone --single-branch --branch $branch --sparse $github_url 
  cd /projects/techzone-demo/sandbox/$project_name
  git sparse-checkout set $demo_name
fi
if [ -d "$demo_name" ]; then
  echo "$demo_name DemoName Found!"
  cp -a /projects/techzone-demo/sandbox/$project_name/$demo_name/. /projects/techzone-demo/sandbox/
  rm -rf /projects/techzone-demo/sandbox/$project_name
  echo "Demo loaded successfully!"
  echo "success"
  exit 2
fi
echo "DemoName Not Found!"
echo "File loading failed!"
rm -rf /projects/techzone-demo/sandbox/$project_name
