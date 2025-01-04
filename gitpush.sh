git add .

echo 'Enter the commit message:'
read commitMessage

git commit -m "$commitMessage"

git push --set-upstream origin master

