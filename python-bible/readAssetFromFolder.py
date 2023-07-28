#
# Read a root folder like code and search for each directory and sub directories, 
# to assess if this is a git hub repo
#

import os,sys
from git import Repo

def parseArgument():
    print(len(sys.argv))
    if (len(sys.argv) > 1):
        return str(sys.argv[1])
    return "."

def buildAsset(path):
    folders = path.split('/') 
    name= folders[len(folders)-1]
    return {'name': name, 'path': path}

def searchAssets(rootFolder):
    print("Search asset from dir " + rootFolder)
    assets = []
    for path,dirs,files in os.walk(rootFolder,topdown=True):
        if (path.endswith(".git")):
            asset = buildAsset(path[:-5])
            gitRepo = Repo(path)
            asset["git_url"] = gitRepo.remotes.origin.url
            assets.append(asset)
        else:
            if path.endswith("src") and path.find("node_modules") == -1 and path.find("docs") == -1:
                assets.append(buildAsset(path))
    return assets

if __name__ == "__main__":
    rootFolder = parseArgument()
    assets=searchAssets(rootFolder)
    print(assets) 
  