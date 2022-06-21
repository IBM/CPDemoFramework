#!/bin/bash  
demo_name=$1
meta_data=$2
sandbox_username=$3
desc=$4
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
project_name=ibmtechzone-demo-artifacts 
username=IBM
git_token=Z2hwX2pMUG5UYTNjd1pLc3NoajNWN09ZN2lCVFV4RWY0NjNqVXJiYg==
# Logic
cd /projects/techzone-demo/sandbox
rm -rf $project_name
if [ ! -d "$project_name" ]; then
  git clone --single-branch --branch $branch --sparse  $github_url 
fi
# TODO
# Update the actual url
cd /projects/techzone-demo/sandbox/$project_name
# git checkout -b $sandbox_username-$demo_name
git sparse-checkout set $sandbox_username-$demo_name
if [ -d "$sandbox_username-$demo_name" ]; then
  # Control will enter here if $DIRECTORY doesn't exist.
  echo "DemoName Already Exists, Choose another name!"
  exit 2
fi
gtd=`echo $git_token | base64 -d`
mkdir $sandbox_username-$demo_name
git sparse-checkout set $sandbox_username-$demo_name 
# TODO
# Add the meta_data and files to demo_name variable
# ......
echo $meta_data > $sandbox_username-$demo_name/readme.json
# # add the required files
cp /projects/techzone-demo/sandbox/governance_artifacts.zip $sandbox_username-$demo_name/
cp /projects/techzone-demo/sandbox/users.csv $sandbox_username-$demo_name/
cp /projects/techzone-demo/sandbox/data_protection_rules.json $sandbox_username-$demo_name/
cp /projects/techzone-demo/sandbox/project_assets.zip $sandbox_username-$demo_name/
# Now
cp ../demo_users.csv $sandbox_username-$demo_name/


git add .
git commit -am "sandbox demo commit by '$sandbox_username'"
git push https://user_name:$gtd@github.com/$username/$project_name.git 

# curl \
#   -X POST \
#   -H 'Authorization: token '${gtd}'' \
#   https://api.github.com/repos/${username}/${project_name}/pulls \
#   -d '{"title":"Sandbox Demo by '$sandbox_username'","body":"","head":"'$sandbox_username-$demo_name'","base":"'$branch'"}'

cd /projects/techzone-demo/sandbox
rm -rf $project_name
echo "Demo Files Uploaded!"   

