git pull

echo '```' > README.md
tree -L 10 -I 'command.sh|README.md|.idea' >> README.md
echo '```' >> README.md

git add .
git commit -m "auto commit"
git push
