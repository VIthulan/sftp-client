import pip


def install_package_without_dependencies(package):
    try:
        pip.main(['install', '-U', package, '--no-deps'])
    except Exception, e:
        print (e)


def install_package_specific_version(package, version):
    try:
        pip.main(['install', package + '==' + version])
    except Exception, e:
        print (e)
