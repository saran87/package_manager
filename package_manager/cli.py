"""Console script for package_manager."""
import sys
import click
from .package_manager import PackageManager

@click.group()
def main(args=None):
    """Console script for package_manager."""
    return 0

@click.command()
@click.argument('package')
@click.argument('dependencies', nargs=-1, required=True)
def depend(package, dependencies):
    """ Add packages and its dependencies to the package manager """
    pm = PackageManager()
    pm.addDependecy(package, dependencies)
    print("DEPEND", package, " ".join(dependencies))
    return 0

@click.command()
def list(args=None):
    """ List all the install pacakages and dependencies """
    pm = PackageManager()
    print(" ".join(pm.listInstalledPackages()))
    return 0

@click.command()
@click.argument('package')
def install(package):
    """ Install a package and its dependencies """
    pm = PackageManager()
    print("Install",   pm.installPackage(package))
    return 0

@click.command()
@click.argument('package')
def remove(package):
    """ remove the installed pacakge and its dependencies """
    pm = PackageManager()
    print("Remove", pm.removePackage(package))
    return 0

main.add_command(depend)
main.add_command(list)
main.add_command(install)
main.add_command(remove)
if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
