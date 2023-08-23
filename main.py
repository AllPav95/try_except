import cosmo

if __name__ == '__main__':
    database = cosmo.readObj()
    cosmo.addJsonObj(database)
    cosmo.saveJsonObj(database)

    print("  Cometa not faund")