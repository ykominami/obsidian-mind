remote.origin.url=git@github.com:ykominami/bmx.git

git filter-repo --path config/settings2.json --invert-paths

git push --force --all
git push --force --tags
