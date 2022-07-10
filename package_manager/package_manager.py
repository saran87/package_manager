"""Package Manager module."""
import pickle
from pathlib import Path




def loadAvailablePackagesFromFile():
    data = {}
    myfile = Path('package.pickle')
    myfile.touch(exist_ok=True)
    try:
        with open('package.pickle', 'rb') as f:
            data = pickle.load(f)
    except:
        print("Available Package File Not Found")
    return data

def loadInstalledPackagesFromFile():
    data = {}
    myfile = Path('installed.pickle')
    myfile.touch(exist_ok=True)
    try:
        with open('installed.pickle', 'rb') as f:
            data = pickle.load(f)
    except:
        print("Installed Package File Not Found")

    return data

def writeAvailablePackagesToFile(availablePackages={}):
    with open('package.pickle', 'wb') as f:
        pickle.dump(availablePackages, f, pickle.HIGHEST_PROTOCOL)

def writeInstalledPackagesToFile(installedPakages={}):
    with open('installed.pickle', 'wb') as f:
        pickle.dump(installedPakages, f, pickle.HIGHEST_PROTOCOL)


class PackageManager:

    availablePackages = {}
    installedPackages = {}

    def __init__(self):
        self.availablePackages = loadAvailablePackagesFromFile()
        self.installedPackages = loadInstalledPackagesFromFile()


    def addDependecy(self,package, dependencies):
        if package not in self.availablePackages:
            self.availablePackages[package] = dependencies
            writeAvailablePackagesToFile(self.availablePackages)
            return self.availablePackages[package]
        else:
            return "Package already exists"

    def installPackage(self,package):
        if package not in self.availablePackages:
            return "Package not avialable"
        if package not in self.installedPackages:
            self.installedPackages[package] = True
            for dependentPackage in self.availablePackages[package]:
                 self.installedPackages[dependentPackage] = True
            writeInstalledPackagesToFile(self.installedPackages)
            return package
        else:
            return "Package already installed"

    def removePackage(self,package):
        removedPackages = []
        if package in self.installedPackages:
            for dependentPackage in self.availablePackages[package]:
                del self.installedPackages[dependentPackage]
                removedPackages.append(dependentPackage)
            del self.installedPackages[package]
            removedPackages.append(package)
            writeInstalledPackagesToFile(self.installedPackages)
            return removedPackages
        else:
            return "Package is not installed"


    def listInstalledPackages(self):
        return self.installedPackages.keys()




