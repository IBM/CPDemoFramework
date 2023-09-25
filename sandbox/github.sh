#!/bin/bash  
demo_name=$1
meta_data=$2
sandbox_username=$3
desc=$4
git_token=$5
private_github_url=$6
private_git_token=$7

isPrivate="false"
branch="main"
github_url=https://github.com/IBM/ibmtechzone-demo-artifacts
project_name=ibmtechzone-demo-artifacts 
username=IBM

if [[ $PLAYGROUND_ENVIRONMENT == *"development"* ]]; then
      branch="development" 
fi
if [[ $PLAYGROUND_ENVIRONMENT == *"staging"* ]]; then
      branch="staging" 
fi
if [[ $PLAYGROUND_ENVIRONMENT == *"techzone"* ]]; then
      branch="techzone" 
fi

if [ "$6" ]; then
    isPrivate="true"
fi


gtd=$git_token  #`echo $git_token | base64 -d`


if [ $isPrivate == "true" ]; then
  echo "Pushing demo artifacts to Private repository"
  #Lets push the demo artifacts to the private git repo. 
  #add the git token to the git url
  private_github_url="${private_github_url:0:8}$private_git_token@${private_github_url:8}"
  echo $private_github_url
  cd /projects/techzone-demo/sandbox/
  git clone  --sparse  $private_github_url  $project_name
  
  if [ $? != 0 ]; then
    echo "Something went wrong in cloning Private Repository: ${private_github_url}"
    exit 1
  fi 

  cd /projects/techzone-demo/sandbox/$project_name

  if [ -d "$sandbox_username-$demo_name" ]; then
    # Control will enter here if $DIRECTORY doesn't exist.
    echo "DemoName Already Exists in private repo, Choose another name!"
    exit 2
  fi
  mkdir $sandbox_username-$demo_name
  git sparse-checkout set $sandbox_username-$demo_name 

  # Add the meta_data and files to demo_name variable
  echo $meta_data > $sandbox_username-$demo_name/readme.json

  # # add the required files
  cp /projects/techzone-demo/sandbox/governance_artifacts.zip $sandbox_username-$demo_name/
  cp /projects/techzone-demo/sandbox/users.json $sandbox_username-$demo_name/
  cp /projects/techzone-demo/sandbox/data_protection_rules.json $sandbox_username-$demo_name/
  cp /projects/techzone-demo/sandbox/project_assets.zip $sandbox_username-$demo_name/
  cp /projects/techzone-demo/sandbox/demo_users.csv $sandbox_username-$demo_name/
  cp /projects/techzone-demo/sandbox/groups.json $sandbox_username-$demo_name/
  cp /projects/techzone-demo/sandbox/roles.json $sandbox_username-$demo_name/

  git add .
  git commit -am "private demo commit by '$sandbox_username'"
  git push --set-upstream origin

  status_check=$?
  
  if [ $status_check != 0 ]; then
    echo "Something went wrong with pushing artifacts to Private Repository" 
    exit 1
  fi

fi


cd /projects/techzone-demo/sandbox
rm -rf $project_name
if [ ! -d "$project_name" ]; then
    git clone --single-branch --branch $branch --sparse  $github_url 
fi

cd /projects/techzone-demo/sandbox/$project_name
git checkout -b $sandbox_username-$demo_name
git sparse-checkout set $sandbox_username-$demo_name

if [ -d "$sandbox_username-$demo_name" ]; then
  # Control will enter here if $DIRECTORY doesn't exist.
  echo "DemoName Already Exists, Choose another name!"
  exit 2
fi

mkdir $sandbox_username-$demo_name
git sparse-checkout set $sandbox_username-$demo_name 

# Add the meta_data to demo_name variable
echo $meta_data > $sandbox_username-$demo_name/readme.json


if [ $isPrivate == "true" ]; then
  # Push metadata to public repo
  if [ $status_check == 0 ]; then
    echo "Successfully pushed Artifacts to Private Repository"
    git add .
    git commit -am "private demo commit by '$sandbox_username'"
    git push https://user_name:$gtd@github.com/$username/$project_name.git     
  fi

fi 


if [ $isPrivate == "false" ]; then
  echo "Pushing demo artifacts to Public repository"
  # # add the required files
  cp /projects/techzone-demo/sandbox/governance_artifacts.zip $sandbox_username-$demo_name/
  cp /projects/techzone-demo/sandbox/users.json $sandbox_username-$demo_name/
  cp /projects/techzone-demo/sandbox/data_protection_rules.json $sandbox_username-$demo_name/
  cp /projects/techzone-demo/sandbox/project_assets.zip $sandbox_username-$demo_name/
  cp /projects/techzone-demo/sandbox/demo_users.csv $sandbox_username-$demo_name/
  cp /projects/techzone-demo/sandbox/groups.json $sandbox_username-$demo_name/
  cp /projects/techzone-demo/sandbox/roles.json $sandbox_username-$demo_name/

  git add .
  git commit -am "public demo commit by '$sandbox_username'"
  git push https://user_name:$gtd@github.com/$username/$project_name.git 

  if [ $? == 0 ]; then 
    echo "Successfully pushed Artifacts to Public Repository"
  fi

  if [ $? != 0 ]; then
    echo "Something went wrong with pushing artifacts to Public Repository"
  fi

fi


# Pushing to artifacts repo
result="$(curl \
  -X POST \
  -H 'Authorization: token '${gtd}'' \
  https://api.github.com/repos/${username}/${project_name}/pulls \
  -d '{"title":"Sandbox Demo by '$sandbox_username'","body":"","head":"'$sandbox_username-$demo_name'","base":"'$branch'"}')"

requestNumber=$(echo "${result}" | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["number"])')

re='^[0-9]+$'
if ! [[ $requestNumber =~ $re ]] ; then
   echo "Something went wrong while creating the pull request" >&2; exit 1
fi

echo "Pull Request created successfully and the Number is : $requestNumber"
echo "Auto merging the PR" 


merge_status="$(curl --location --request PUT "https://api.github.com/repos/${username}/${project_name}/pulls/$requestNumber/merge" \
--header "Authorization: Bearer ${gtd}" -w 'HTTP_CODE:%{http_code}')"

status=$(echo "${merge_status}" | grep -o 'HTTP_CODE:[1-4][0-9][0-9]' | sed 's/HTTP_CODE://')

if [ $status == "200" ]; then
  echo "Successfully merged the pull request"
fi
if [ $status != "200" ]; then
  echo "Something went wrong while merging the pull request" 
  exit 1
fi

cd /projects/techzone-demo/sandbox
rm -rf $project_name
echo "success"
