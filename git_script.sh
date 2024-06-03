#!/bin/bash

git config user.email "Joshua.Cox@atlasschool.com"
git config user.name "JCox924"

read -p "Enter commit message: " message

git add *
git commit -m "$message"
git push
