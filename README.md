# splice-sample-fixer
A Python utility script for flattening sample libraries into an organized folder based on the sample type encoded in the sample name

## Set up

This script assumes that you have 2 preexisting folders:

a) A folder full of samples from Splice nested very deep within packs
b) A new folder to hold your organized samples


You'll need to update the following variables at the bottom of the file:

```
mess_folder = "/Users/kevindenny/Splice/sounds/packs/"

new_parent_folder = '/Users/kevindenny/hdmi fx Dropbox/Kevin Denny/drums/'
```

If the correct category of the sample can't be determined from the title, it will be routed to a separate sample triage folder:

```
triage_folder = '/Users/kevindenny/hdmi fx Dropbox/Kevin Denny/drums/sample triage/'
```
